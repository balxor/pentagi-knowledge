---
cwe_id: CWE-115
name: Misinterpretation of Input
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/115.html
tags: [mitre-cwe, weakness, CWE-115]
---

# CWE-115 - Misinterpretation of Input

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-115](https://cwe.mitre.org/data/definitions/115.html)

## Description
The product misinterprets an input, whether from an attacker or another product, in a security-relevant fashion.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Unexpected State

## Related weaknesses
- CWE-436 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-2225**: Product sees dangerous file extension in free text of a group discussion, disconnects all users.
- **CVE-2001-0003**: Product does not correctly import and process security settings from another product.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/115.html
