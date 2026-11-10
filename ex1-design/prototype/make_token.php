<?php
// Creates an API token. Prints it ONCE; only its hash goes in the database.
// Usage: php make_token.php <label> <write|read>
require __DIR__ . '/db.php';
[$self, $label, $scope] = $argv + [null, 'test', 'write'];
if (!in_array($scope, ['write', 'read'], true)) { fwrite(STDERR, "scope must be write or read\n"); exit(1); }
$token = bin2hex(random_bytes(24));
$pdo = db();
$pdo->prepare('INSERT INTO api_tokens (token_hash, label, scope, expires_at) VALUES (?, ?, ?, ?)')
    ->execute([hash('sha256', $token), $label, $scope, date('Y-m-d H:i:s', time() + 86400 * 30)]);
echo $token, "\n";
