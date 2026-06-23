---
cwe_id: CWE-351
name: Insufficient Type Distinction
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/351.html
tags: [mitre-cwe, weakness, CWE-351]
---

# CWE-351 - Insufficient Type Distinction

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-351](https://cwe.mitre.org/data/definitions/351.html)

## Description
The product does not properly distinguish between different types of elements in a way that leads to insecure behavior.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Other

## Related weaknesses
- CWE-345 (ChildOf)
- CWE-436 (PeerOf)

## Observed examples (CVE)
- **CVE-2005-2260**: Browser user interface does not distinguish between user-initiated and synthetic events.
- **CVE-2005-2801**: Product does not compare all required data in two separate elements, causing it to think they are the same, leading to loss of ACLs. Similar to Same Name error.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/351.html
