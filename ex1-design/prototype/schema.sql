-- MySQL / MariaDB (XAMPP). Run in phpMyAdmin or: mysql -u root < schema.sql
CREATE DATABASE IF NOT EXISTS company_db CHARACTER SET utf8mb4;
USE company_db;

CREATE TABLE IF NOT EXISTS notes (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  client_id   VARCHAR(64)  NOT NULL,
  staff_id    VARCHAR(64)  NOT NULL,
  patient_ref VARCHAR(64)  NOT NULL,
  note_text   TEXT         NOT NULL,
  created_at  DATETIME     NOT NULL,
  received_at TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY uq_client_id (client_id)      -- makes sync safe to repeat
);

CREATE TABLE IF NOT EXISTS api_tokens (
  id         INT AUTO_INCREMENT PRIMARY KEY,
  token_hash CHAR(64)    NOT NULL UNIQUE,  -- SHA-256 of the token; the token itself is never stored
  label      VARCHAR(64) NOT NULL,
  scope      VARCHAR(32) NOT NULL,         -- 'write' or 'read'
  expires_at DATETIME    NULL,
  revoked    TINYINT(1)  NOT NULL DEFAULT 0
);
