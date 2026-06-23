---
cwe_id: CWE-436
name: Interpretation Conflict
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-105, CAPEC-273, CAPEC-34]
url: https://cwe.mitre.org/data/definitions/436.html
tags: [mitre-cwe, weakness, CWE-436]
---

# CWE-436 - Interpretation Conflict

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-436](https://cwe.mitre.org/data/definitions/436.html)

## Description
Product A handles inputs or steps differently than Product B, which causes A to perform incorrect actions based on its perception of B's state.

## Extended description
This is generally found in proxies, firewalls, anti-virus software, and other intermediary devices that monitor, allow, deny, or modify traffic based on how the client or server is expected to behave.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Integrity, Other**: Unexpected State, Varies by Context

## Related attack patterns (CAPEC)
- [CAPEC-105](https://capec.mitre.org/data/definitions/105.html)
- [CAPEC-273](https://capec.mitre.org/data/definitions/273.html)
- [CAPEC-34](https://capec.mitre.org/data/definitions/34.html)

## Related weaknesses
- CWE-435 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-1215**: Bypass filters or poison web cache using requests with multiple Content-Length headers, a non-standard behavior.
- **CVE-2002-0485**: Anti-virus product allows bypass via Content-Type and Content-Disposition headers that are mixed case, which are still processed by some clients.
- **CVE-2002-1978**: FTP clients sending a command with "PASV" in the argument can cause firewalls to misinterpret the server's error as a valid response, allowing filter bypass.
- **CVE-2002-1979**: FTP clients sending a command with "PASV" in the argument can cause firewalls to misinterpret the server's error as a valid response, allowing filter bypass.
- **CVE-2002-0637**: Virus product bypass with spaces between MIME header fields and the ":" separator, a non-standard message that is accepted by some clients.
- **CVE-2002-1777**: AV product detection bypass using inconsistency manipulation (file extension in MIME Content-Type vs. Content-Disposition field).
- **CVE-2005-3310**: CMS system allows uploads of files with GIF/JPG extensions, but if they contain HTML, Internet Explorer renders them as HTML instead of images.
- **CVE-2005-4260**: Interpretation conflict allows XSS via invalid "<" when a ">" is expected, which is treated as ">" by many web browsers.
- **CVE-2005-4080**: Interpretation conflict (non-standard behavior) enables XSS because browser ignores invalid characters in the middle of tags.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/436.html
