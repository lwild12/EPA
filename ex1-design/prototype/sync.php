<?php
declare(strict_types=1);
/**
 * Visit-note sync endpoint, version 1 (topics 2 and 4).
 * Spec: POST JSON {client_id, staff_id, patient_ref, note_text, created_at}
 *       with header  Authorization: Bearer <token>
 * Returns: 201 created, 200 duplicate, 400 invalid, 401 not authenticated,
 *          403 not authorised, 405 wrong method, 413 too large.
 * Safe to repeat: client_id is unique, a repeat returns 200 and stores nothing new.
 */
require __DIR__ . '/db.php';

const MAX_BODY = 65536;        // 64 KB
const REQUIRE_HTTPS = false;   // switch to true in topic 5 once TLS is set up, then retest

ini_set('display_errors', '0');   // no stack traces to the client
header('Content-Type: application/json');
header('X-Content-Type-Options: nosniff');

function respond(int $code, array $body = []): never {
    http_response_code($code);
    echo json_encode($body ?: ['status' => $code]);
    exit;
}

set_exception_handler(function (Throwable $t) {
    error_log('sync.php error: ' . get_class($t));   // class only: no SQL, no note text
    respond(500, ['error' => 'server error']);
});

if (REQUIRE_HTTPS && empty($_SERVER['HTTPS'])) { respond(403, ['error' => 'https required']); }

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Allow: POST');
    respond(405, ['error' => 'method not allowed']);
}

// --- authenticate ---
$auth = $_SERVER['HTTP_AUTHORIZATION'] ?? '';
if (!preg_match('/^Bearer ([A-Za-z0-9._~+\/-]{16,200})$/', $auth, $m)) {
    respond(401, ['error' => 'authentication required']);
}
$pdo = db();
$st = $pdo->prepare('SELECT scope, expires_at, revoked FROM api_tokens WHERE token_hash = ?');
$st->execute([hash('sha256', $m[1])]);
$tok = $st->fetch();
if (!$tok || (int)$tok['revoked'] === 1 || ($tok['expires_at'] !== null && strtotime($tok['expires_at']) < time())) {
    respond(401, ['error' => 'authentication required']);
}

// --- authorise ---
if ($tok['scope'] !== 'write') { respond(403, ['error' => 'not permitted']); }

// --- validate ---
$raw = file_get_contents('php://input', false, null, 0, MAX_BODY + 1);
if ($raw === false || strlen($raw) > MAX_BODY) { respond(413, ['error' => 'body too large']); }
$d = json_decode($raw, true);
if (!is_array($d)) { respond(400, ['error' => 'invalid json']); }

$lim = ['client_id' => 64, 'staff_id' => 64, 'patient_ref' => 64, 'note_text' => 20000];
foreach ($lim as $f => $max) {
    if (!isset($d[$f]) || !is_string($d[$f]) || trim($d[$f]) === '' || mb_strlen($d[$f]) > $max) {
        respond(400, ['error' => "invalid field: $f"]);
    }
}
$ts = isset($d['created_at']) && is_string($d['created_at']) ? strtotime($d['created_at']) : false;
if ($ts === false) { respond(400, ['error' => 'invalid field: created_at']); }

// --- store once, acknowledge ---
try {
    $pdo->prepare('INSERT INTO notes (client_id, staff_id, patient_ref, note_text, created_at) VALUES (?, ?, ?, ?, ?)')
        ->execute([$d['client_id'], $d['staff_id'], $d['patient_ref'], $d['note_text'], date('Y-m-d H:i:s', $ts)]);
} catch (PDOException $e) {
    if ($e->getCode() === '23000') {   // unique client_id: already stored
        respond(200, ['status' => 'duplicate', 'client_id' => $d['client_id']]);
    }
    throw $e;
}
respond(201, ['status' => 'created', 'client_id' => $d['client_id']]);
