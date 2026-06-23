---
cwe_id: CWE-537
name: Java Runtime Error Message Containing Sensitive Information
type: weakness
abstraction: Variant
status: Incomplete
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/537.html
tags: [mitre-cwe, weakness, CWE-537]
---

# CWE-537 - Java Runtime Error Message Containing Sensitive Information

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-537](https://cwe.mitre.org/data/definitions/537.html)

## Description
In many cases, an attacker can leverage the conditions that cause unhandled exception errors in order to gain unauthorized access to the system.

## Applicable platforms / languages
Java

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation**: Do not expose sensitive error information to the user.

## Related weaknesses
- CWE-211 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/537.html
