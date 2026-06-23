---
cwe_id: CWE-820
name: Missing Synchronization
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/820.html
tags: [mitre-cwe, weakness, CWE-820]
---

# CWE-820 - Missing Synchronization

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-820](https://cwe.mitre.org/data/definitions/820.html)

## Description
The product utilizes a shared resource in a concurrent manner but does not attempt to synchronize access to the resource.

## Extended description
If access to a shared resource is not synchronized, then the resource may not be in a state that is expected by the product. This might lead to unexpected or insecure behaviors, especially if an attacker can influence the shared resource.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Confidentiality, Other**: Modify Application Data, Read Application Data, Alter Execution Logic

## Related weaknesses
- CWE-662 (ChildOf)
- CWE-662 (ChildOf)
- CWE-662 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/820.html
