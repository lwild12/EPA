# Key management plan template (aligned to NIST SP 800-57 and NCSC cryptography guidance)

**System:** <name>  **Owner:** <role>  **Version/date:** <>

## 1. Scope and inventory
| Key / secret | Purpose | Algorithm and size | Where stored | Owner | Created | Rotation | Expiry |
|---|---|---|---|---|---|---|---|
| TLS server key | HTTPS for web app | ECDSA P-256 or RSA 3072 | Server HSM/vault, file mode 600 | Platform | | 12 months | 13 months |
| Database encryption key | Data at rest | AES-256-GCM | KMS / vault | DBA | | 12 months | |
| SSH host/user keys | Admin access | Ed25519 | Hardware token (users), vault (hosts) | SecOps | | 12 months | |
| Code-signing key | Release signing | RSA 3072 / Ed25519 | HSM, offline backup | Release mgr | | 24 months | |
| API secrets | Service-to-service | 256-bit random | Secrets manager | App owner | | 90 days | |

## 2. Lifecycle controls
1. **Generate** with a vetted CSPRNG / HSM, never from passwords or `random`. Record who generated it and when.
2. **Distribute** over authenticated, encrypted channels; never by email or chat. Split knowledge for root/CA keys (M-of-N).
3. **Store** in HSM/KMS/vault; separate keys from the data they protect; no keys in source control or images.
4. **Use** each key for one purpose only; least privilege access; log every use.
5. **Rotate** on schedule and on suspected compromise. Support overlapping validity so rotation causes no outage.
6. **Back up** encrypted, in a separate location, tested restore. Backup of keys is itself protected like the key.
7. **Revoke** (CRL/OCSP for certificates, disable in KMS) and **destroy** (cryptographic erase, overwrite, certificate of destruction) at end of life.
8. **Recover** documented process if a key is lost (escrow with dual control) and if it is compromised (below).

## 3. Roles and separation of duties
Key custodians (two people for root keys), security officer approves, auditors review logs. No single person can both create and approve a root key.

## 4. Compromise response
Revoke -> issue new key -> re-encrypt/re-sign -> rotate dependent secrets -> review access logs for misuse -> notify per incident plan -> root-cause fix.

## 5. Algorithm policy
Approved: AES-256-GCM, ChaCha20-Poly1305, SHA-256/384, RSA >= 3000 bits, ECDSA/Ed25519, TLS 1.2+ (prefer 1.3). Banned: MD5, SHA-1 for signatures, DES/3DES, RC4, RSA < 2048. Review annually and plan for post-quantum migration (NCSC guidance on PQC timelines).

## 6. Audit and evidence
Quarterly inventory reconciliation, access review, rotation test, restore test. Keep records for <period>.
