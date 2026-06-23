---
cwe_id: CWE-767
name: Access to Critical Private Variable via Public Method
type: weakness
abstraction: Base
status: Incomplete
languages: [C++, C#, Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/767.html
tags: [mitre-cwe, weakness, CWE-767]
---

# CWE-767 - Access to Critical Private Variable via Public Method

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-767](https://cwe.mitre.org/data/definitions/767.html)

## Description
The product defines a public method that reads or modifies a private variable.

## Extended description
If an attacker modifies the variable to contain unexpected values, this could violate assumptions from other parts of the code. Additionally, if an attacker can read the private variable, it may expose sensitive information or make it easier to launch further attacks.

## Applicable platforms / languages
C++, C#, Java

## Common consequences
- **Integrity, Other**: Modify Application Data, Other

## Potential mitigations
- **Implementation**: Use class accessor and mutator methods appropriately. Perform validation when accepting data from a public method that is intended to modify a critical private variable. Also be sure that appropriate access controls are being applied when a public method interfaces with critical data.

## Related weaknesses
- CWE-668 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/767.html
