---
cwe_id: CWE-1125
name: Excessive Attack Surface
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1125.html
tags: [mitre-cwe, weakness, CWE-1125]
---

# CWE-1125 - Excessive Attack Surface

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1125](https://cwe.mitre.org/data/definitions/1125.html)

## Description
The product has an attack surface whose quantitative measurement exceeds a desirable maximum.

## Extended description
Originating from software security, an "attack surface" measure typically reflects the number of input points and output points that can be utilized by an untrusted party, i.e. a potential attacker. A larger attack surface provides more places to attack, and more opportunities for developers to introduce weaknesses. In some cases, this measure may reflect other aspects of quality besides security; e.g., a product with many inputs and outputs may require a large number of tests in order to improve code coverage.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Varies by Context

## Related weaknesses
- CWE-1120 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1125.html
