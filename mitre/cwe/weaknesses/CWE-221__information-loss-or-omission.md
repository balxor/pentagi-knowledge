---
cwe_id: CWE-221
name: Information Loss or Omission
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-81]
url: https://cwe.mitre.org/data/definitions/221.html
tags: [mitre-cwe, weakness, CWE-221]
---

# CWE-221 - Information Loss or Omission

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-221](https://cwe.mitre.org/data/definitions/221.html)

## Description
The product does not record, or improperly records, security-relevant information that leads to an incorrect decision or hampers later analysis.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Non-Repudiation**: Hide Activities

## Related attack patterns (CAPEC)
- [CAPEC-81](https://capec.mitre.org/data/definitions/81.html)

## Related weaknesses
- CWE-664 (ChildOf)

## Observed examples (CVE)
- **CVE-2004-2227**: Web browser's filename selection dialog only shows the beginning portion of long filenames, which can trick users into launching executables with dangerous extensions.
- **CVE-2003-0412**: application server does not log complete URI of a long request (truncation).
- **CVE-1999-1029**: Login attempts are not recorded if the user disconnects before the maximum number of tries.
- **CVE-2002-0725**: Attacker performs malicious actions on a hard link to a file, obscuring the real target file.
- **CVE-1999-1055**: Product does not warn user when document contains certain dangerous functions or macros.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/221.html
