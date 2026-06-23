---
cwe_id: CWE-223
name: Omission of Security-relevant Information
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/223.html
tags: [mitre-cwe, weakness, CWE-223]
---

# CWE-223 - Omission of Security-relevant Information

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-223](https://cwe.mitre.org/data/definitions/223.html)

## Description
The product does not record or display information that would be important for identifying the source or nature of an attack, or determining if an action is safe.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Non-Repudiation**: Hide Activities

## Related weaknesses
- CWE-221 (ChildOf)

## Observed examples (CVE)
- **CVE-1999-1029**: Login attempts are not recorded if the user disconnects before the maximum number of tries.
- **CVE-2002-1839**: Sender's IP address not recorded in outgoing e-mail.
- **CVE-2000-0542**: Failed authentication attempts are not recorded if later attempt succeeds.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/223.html
