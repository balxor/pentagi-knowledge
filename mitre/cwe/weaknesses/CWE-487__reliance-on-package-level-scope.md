---
cwe_id: CWE-487
name: Reliance on Package-level Scope
type: weakness
abstraction: Base
status: Incomplete
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/487.html
tags: [mitre-cwe, weakness, CWE-487]
---

# CWE-487 - Reliance on Package-level Scope

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-487](https://cwe.mitre.org/data/definitions/487.html)

## Description
Java packages are not inherently closed; therefore, relying on them for code security is not a good practice.

## Extended description
The purpose of package scope is to prevent accidental access by other parts of a program. This is an ease-of-software-development feature but not a security feature.

## Applicable platforms / languages
Java

## Common consequences
- **Confidentiality**: Read Application Data
- **Integrity**: Modify Application Data

## Potential mitigations
- **Architecture and Design, Implementation**: Data should be private static and final whenever possible. This will assure that your code is protected by instantiating early, preventing access and tampering.

## Related weaknesses
- CWE-664 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/487.html
