---
cwe_id: CWE-821
name: Incorrect Synchronization
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/821.html
tags: [mitre-cwe, weakness, CWE-821]
---

# CWE-821 - Incorrect Synchronization

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-821](https://cwe.mitre.org/data/definitions/821.html)

## Description
The product utilizes a shared resource in a concurrent manner, but it does not correctly synchronize access to the resource.

## Extended description
If access to a shared resource is not correctly synchronized, then the resource may not be in a state that is expected by the product. This might lead to unexpected or insecure behaviors, especially if an attacker can influence the shared resource.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Confidentiality, Other**: Modify Application Data, Read Application Data, Alter Execution Logic

## Related weaknesses
- CWE-662 (ChildOf)
- CWE-662 (ChildOf)
- CWE-662 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/821.html
