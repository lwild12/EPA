# Lookup cheat-sheet

Short how-tos for the enrichment steps. Always write down **what you looked up, where, and when** (source, date accessed). Record what you really saw, not what you expect.

## Hash (VirusTotal and friends)

1. Open virustotal.com and paste the SHA-256 into the search box.
2. Note: detection count, the suggested family or label, and first-seen date.
3. Check MalwareBazaar (bazaar.abuse.ch) and MWDB (mwdb.cert.pl) if your CAPE page showed their tags (Fig 2).
4. Write: "three sources agree on Agent Tesla" only if that is what you saw.

## Domain (WHOIS)

1. Search for a WHOIS lookup (for example lookup.icann.org, or the `whois` command if your PC has it).
2. Enter `checkip.dyndns.org`. For a subdomain you may need the parent domain (`dyndns.org`).
3. Note: registrar or owner, and creation date. Privacy redaction is normal. Write what is shown.
4. Say what the service is for: a public IP-address lookup.

## IP address (ASN or owner)

1. Use a lookup such as bgp.he.net or ipinfo.io.
2. Enter one IP from Fig 8 or your hosts list.
3. Note: the owner or network (ASN), and the country.
4. Use the CNAMEs in your DNS screenshot (`azureedge.net`, `akamaiedge.net`, `letsencrypt`) as supporting evidence.

## External sources (pass needs at least one national cyber authority and OWASP)

1. **NCSC** (ncsc.gov.uk): search for phishing guidance, or device or supply chain security guidance. Pick one page you actually read.
2. **OWASP** (owasp.org): the API Security Top 10 fits your token test. Look at the entries on authentication and on resource consumption. Check the exact wording on the page.
3. For each, write: title, URL, date accessed, and one sentence on what it told you.
4. Optional extras: MITRE ATT&CK (attack.mitre.org) for technique IDs; CISA Known Exploited Vulnerabilities for a vulnerability source.

## ATT&CK ID check

1. Open attack.mitre.org and search the ID (for example T1566).
2. Confirm the name matches what you wrote.
3. Delete any ID you cannot confirm.

## Hash of a file (Windows PowerShell)

`Get-FileHash -Algorithm SHA256 <path-to-file>`

## Word count

1. Select only the justification body text in Word (not headings, tables or figure captions).
2. Review, then Word Count. Check the "selection" count.
3. Target 1,000. Allowed range 900 to 1,100.

## Screenshots

- Snipping Tool: `Win+Shift+S`.
- Paste into one document and check the page count against the 5-page A4 limit.
