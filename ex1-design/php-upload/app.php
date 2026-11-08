<?php
declare(strict_types=1);

/**
 * Secure login + file upload demo (EPA Exercise 1).
 * Run:  php -S 127.0.0.1:8080 app.php   (development only)
 *
 * Security controls (name these in your write-up):
 *  - Passwords hashed with password_hash (bcrypt/argon), verified with password_verify
 *  - PDO prepared statements (SQL injection)
 *  - CSRF token on every state-changing form
 *  - Session fixation defence (session_regenerate_id) + HttpOnly/SameSite cookies
 *  - Login throttling (brute force)
 *  - Upload: size limit, extension allow-list, real MIME check (finfo), random server-side name,
 *    stored OUTSIDE the web root, served only through an authenticated download handler
 *  - Output escaping with htmlspecialchars (XSS)
 *  - Security headers (CSP, X-Content-Type-Options, X-Frame-Options, Referrer-Policy)
 */

const MAX_BYTES = 2 * 1024 * 1024;
const ALLOWED = ['pdf' => 'application/pdf', 'png' => 'image/png', 'jpg' => 'image/jpeg', 'txt' => 'text/plain'];
const MAX_FAILS = 5;
const LOCK_SECS = 300;

$base = __DIR__;
$uploadDir = $base . '/private_uploads';   // keep outside web root in real deployments
$dbFile = $base . '/app.sqlite';
if (!is_dir($uploadDir)) {
    mkdir($uploadDir, 0700, true);
}

session_set_cookie_params(['httponly' => true, 'samesite' => 'Strict', 'secure' => false /* true behind HTTPS */]);
session_start();

header("Content-Security-Policy: default-src 'self'; style-src 'self' 'unsafe-inline'; frame-ancestors 'none'");
header('X-Content-Type-Options: nosniff');
header('X-Frame-Options: DENY');
header('Referrer-Policy: no-referrer');

$pdo = new PDO('sqlite:' . $dbFile, null, null, [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
]);
$pdo->exec('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, pw TEXT NOT NULL, fails INTEGER DEFAULT 0, locked_until INTEGER DEFAULT 0)');
$pdo->exec('CREATE TABLE IF NOT EXISTS files (id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, stored TEXT NOT NULL, original TEXT NOT NULL, mime TEXT NOT NULL, size INTEGER NOT NULL, created INTEGER NOT NULL)');

function e(string $s): string { return htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'); }
function csrf(): string {
    if (empty($_SESSION['csrf'])) { $_SESSION['csrf'] = bin2hex(random_bytes(32)); }
    return $_SESSION['csrf'];
}
function check_csrf(): void {
    $t = $_POST['csrf'] ?? '';
    if (!is_string($t) || !hash_equals($_SESSION['csrf'] ?? '', $t)) {
        http_response_code(403);
        exit('Bad CSRF token');
    }
}
function page(string $body): void {
    echo '<!doctype html><meta charset="utf-8"><title>Secure upload</title><body style="font-family:sans-serif;max-width:40rem;margin:2rem auto">' . $body;
    exit;
}

$action = $_GET['a'] ?? 'home';

if ($action === 'register' && $_SERVER['REQUEST_METHOD'] === 'POST') {
    check_csrf();
    $u = trim((string)($_POST['username'] ?? ''));
    $p = (string)($_POST['password'] ?? '');
    if (!preg_match('/^[A-Za-z0-9_]{3,32}$/', $u) || strlen($p) < 12) {
        page('<p>Username 3-32 chars (letters, digits, _) and password at least 12 characters.</p><a href="?">Back</a>');
    }
    try {
        $pdo->prepare('INSERT INTO users (username, pw) VALUES (?, ?)')->execute([$u, password_hash($p, PASSWORD_DEFAULT)]);
    } catch (PDOException $ex) {
        page('<p>Could not register.</p><a href="?">Back</a>');   // do not leak which part failed
    }
    header('Location: ?');
    exit;
}

if ($action === 'login' && $_SERVER['REQUEST_METHOD'] === 'POST') {
    check_csrf();
    $stmt = $pdo->prepare('SELECT * FROM users WHERE username = ?');
    $stmt->execute([(string)($_POST['username'] ?? '')]);
    $user = $stmt->fetch();
    $ok = false;
    if ($user && $user['locked_until'] > time()) {
        page('<p>Account temporarily locked. Try later.</p><a href="?">Back</a>');
    }
    // verify against a dummy hash when user is missing to keep timing similar
    $hash = $user['pw'] ?? '$2y$10$usesomesillystringforsalt$';
    if (password_verify((string)($_POST['password'] ?? ''), $hash) && $user) {
        $ok = true;
    }
    if ($ok) {
        session_regenerate_id(true);
        $_SESSION['uid'] = (int)$user['id'];
        $pdo->prepare('UPDATE users SET fails = 0, locked_until = 0 WHERE id = ?')->execute([$user['id']]);
        header('Location: ?');
        exit;
    }
    if ($user) {
        $fails = (int)$user['fails'] + 1;
        $lock = $fails >= MAX_FAILS ? time() + LOCK_SECS : 0;
        $pdo->prepare('UPDATE users SET fails = ?, locked_until = ? WHERE id = ?')->execute([$lock ? 0 : $fails, $lock, $user['id']]);
    }
    error_log('failed login for ' . preg_replace('/[^A-Za-z0-9_]/', '?', (string)($_POST['username'] ?? '')));
    page('<p>Invalid credentials.</p><a href="?">Back</a>');
}

if ($action === 'logout') {
    $_SESSION = [];
    session_destroy();
    header('Location: ?');
    exit;
}

$uid = $_SESSION['uid'] ?? null;

if ($action === 'upload' && $_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!$uid) { http_response_code(401); exit('Login required'); }
    check_csrf();
    $f = $_FILES['file'] ?? null;
    if (!$f || $f['error'] !== UPLOAD_ERR_OK || !is_uploaded_file($f['tmp_name'])) {
        page('<p>Upload failed.</p><a href="?">Back</a>');
    }
    if ($f['size'] > MAX_BYTES) { page('<p>File too large (2 MB max).</p><a href="?">Back</a>'); }
    $ext = strtolower(pathinfo($f['name'], PATHINFO_EXTENSION));
    if (!array_key_exists($ext, ALLOWED)) { page('<p>File type not allowed.</p><a href="?">Back</a>'); }
    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $mime = $finfo->file($f['tmp_name']);
    if ($mime !== ALLOWED[$ext]) { page('<p>File content does not match its extension.</p><a href="?">Back</a>'); }
    $stored = bin2hex(random_bytes(16));            // never trust the client-supplied name
    if (!move_uploaded_file($f['tmp_name'], "$uploadDir/$stored")) { page('<p>Could not store file.</p><a href="?">Back</a>'); }
    chmod("$uploadDir/$stored", 0600);
    $orig = preg_replace('/[^A-Za-z0-9._ -]/', '_', basename($f['name']));
    $pdo->prepare('INSERT INTO files (user_id, stored, original, mime, size, created) VALUES (?,?,?,?,?,?)')
        ->execute([$uid, $stored, $orig, $mime, (int)$f['size'], time()]);
    header('Location: ?');
    exit;
}

if ($action === 'download') {
    if (!$uid) { http_response_code(401); exit('Login required'); }
    $stmt = $pdo->prepare('SELECT * FROM files WHERE id = ? AND user_id = ?');   // object-level authorisation
    $stmt->execute([(int)($_GET['id'] ?? 0), $uid]);
    $row = $stmt->fetch();
    if (!$row) { http_response_code(404); exit('Not found'); }
    header('Content-Type: ' . $row['mime']);
    header('Content-Disposition: attachment; filename="' . $row['original'] . '"');
    header('Content-Length: ' . $row['size']);
    readfile("$uploadDir/" . $row['stored']);
    exit;
}

// ---- Home page ----
if (!$uid) {
    $t = e(csrf());
    page(<<<HTML
<h1>Secure upload demo</h1>
<h2>Log in</h2>
<form method="post" action="?a=login">
<input type="hidden" name="csrf" value="$t">
<p><input name="username" placeholder="username" autocomplete="username" required></p>
<p><input name="password" type="password" placeholder="password" autocomplete="current-password" required></p>
<button>Log in</button></form>
<h2>Register</h2>
<form method="post" action="?a=register">
<input type="hidden" name="csrf" value="$t">
<p><input name="username" placeholder="username" required></p>
<p><input name="password" type="password" placeholder="12+ character password" autocomplete="new-password" required></p>
<button>Register</button></form>
HTML);
}

$stmt = $pdo->prepare('SELECT id, original, size FROM files WHERE user_id = ? ORDER BY id DESC');
$stmt->execute([$uid]);
$list = '';
foreach ($stmt as $r) {
    $list .= '<li><a href="?a=download&id=' . (int)$r['id'] . '">' . e($r['original']) . '</a> (' . (int)$r['size'] . ' bytes)</li>';
}
$t = e(csrf());
page(<<<HTML
<h1>Your files</h1>
<ul>$list</ul>
<form method="post" action="?a=upload" enctype="multipart/form-data">
<input type="hidden" name="csrf" value="$t">
<input type="file" name="file" required> <button>Upload</button></form>
<p><a href="?a=logout">Log out</a></p>
HTML);
