---
cwe_id: CWE-583
name: finalize() Method Declared Public
type: weakness
abstraction: Variant
status: Incomplete
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/583.html
tags: [mitre-cwe, weakness, CWE-583]
---

# CWE-583 - finalize() Method Declared Public

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-583](https://cwe.mitre.org/data/definitions/583.html)

## Description
The product violates secure coding principles for mobile code by declaring a finalize() method public.

## Extended description
A product should never call finalize explicitly, except to call super.finalize() inside an implementation of finalize(). In mobile code situations, the otherwise error prone practice of manual garbage collection can become a security threat if an attacker can maliciously invoke a finalize() method because it is declared with public access.

## Applicable platforms / languages
Java

## Common consequences
- **Confidentiality, Integrity, Availability**: Alter Execution Logic, Execute Unauthorized Code or Commands, Modify Application Data

## Potential mitigations
- **Implementation**: If you are using finalize() as it was designed, there is no reason to declare finalize() with anything other than protected access.

## Related weaknesses
- CWE-668 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/583.html
