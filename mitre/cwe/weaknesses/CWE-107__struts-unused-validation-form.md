---
cwe_id: CWE-107
name: Struts: Unused Validation Form
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/107.html
tags: [mitre-cwe, weakness, CWE-107]
---

# CWE-107 - Struts: Unused Validation Form

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-107](https://cwe.mitre.org/data/definitions/107.html)

## Description
An unused validation form indicates that validation logic is not up-to-date.

## Applicable platforms / languages
Java

## Common consequences
- **Other**: Quality Degradation

## Potential mitigations
- **Implementation**: Remove the unused Validation Form from the validation.xml file.

## Related weaknesses
- CWE-1164 (ChildOf)
- CWE-20 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/107.html
