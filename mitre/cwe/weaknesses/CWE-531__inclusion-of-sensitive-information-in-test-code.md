---
cwe_id: CWE-531
name: Inclusion of Sensitive Information in Test Code
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/531.html
tags: [mitre-cwe, weakness, CWE-531]
---

# CWE-531 - Inclusion of Sensitive Information in Test Code

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-531](https://cwe.mitre.org/data/definitions/531.html)

## Description
Accessible test applications can pose a variety of security risks. Since developers or administrators rarely consider that someone besides themselves would even know about the existence of these applications, it is common for them to contain sensitive information or functions.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Distribution, Installation**: Remove test code before deploying the application into production.

## Related weaknesses
- CWE-540 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/531.html
