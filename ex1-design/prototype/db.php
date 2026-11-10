<?php
// Connection settings. Override with environment variables if needed.
function db(): PDO {
    $dsn  = getenv('DB_DSN')  ?: 'mysql:host=127.0.0.1;dbname=company_db;charset=utf8mb4';
    $user = getenv('DB_USER') !== false ? getenv('DB_USER') : 'root';   // XAMPP default (lab only)
    $pass = getenv('DB_PASS') !== false ? getenv('DB_PASS') : '';
    return new PDO($dsn, $user, $pass, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES => false,
    ]);
}
