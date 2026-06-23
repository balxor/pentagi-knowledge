---
cwe_id: CWE-93
name: Improper Neutralization of CRLF Sequences ('CRLF Injection')
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-15, CAPEC-81]
url: https://cwe.mitre.org/data/definitions/93.html
tags: [mitre-cwe, weakness, CWE-93]
---

# CWE-93 - Improper Neutralization of CRLF Sequences ('CRLF Injection')

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-93](https://cwe.mitre.org/data/definitions/93.html)

## Description
The product uses CRLF (carriage return line feeds) as a special element, e.g. to separate lines or records, but it does not neutralize or incorrectly neutralizes CRLF sequences from inputs.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Modify Application Data

## Potential mitigations
- **Implementation**: Avoid using CRLF as a special sequence.
- **Implementation**: Appropriately filter or quote CRLF sequences in user-controlled input.

## Related attack patterns (CAPEC)
- [CAPEC-15](https://capec.mitre.org/data/definitions/15.html)
- [CAPEC-81](https://capec.mitre.org/data/definitions/81.html)

## Related weaknesses
- CWE-74 (ChildOf)
- CWE-117 (CanPrecede)

## Observed examples (CVE)
- **CVE-2002-1771**: CRLF injection enables spam proxy (add mail headers) using email address or name.
- **CVE-2002-1783**: CRLF injection in API function arguments modify headers for outgoing requests.
- **CVE-2004-1513**: Spoofed entries in web server log file via carriage returns
- **CVE-2006-4624**: Chain: inject fake log entries with fake timestamps using CRLF injection
- **CVE-2005-1951**: Chain: Application accepts CRLF in an object ID, allowing HTTP response splitting.
- **CVE-2004-1687**: Chain: HTTP response splitting via CRLF in parameter related to URL.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/93.html
