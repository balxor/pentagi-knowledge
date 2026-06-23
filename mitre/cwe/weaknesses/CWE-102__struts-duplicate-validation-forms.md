---
cwe_id: CWE-102
name: Struts: Duplicate Validation Forms
type: weakness
abstraction: Variant
status: Incomplete
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/102.html
tags: [mitre-cwe, weakness, CWE-102]
---

# CWE-102 - Struts: Duplicate Validation Forms

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-102](https://cwe.mitre.org/data/definitions/102.html)

## Description
The product uses multiple validation forms with the same name, which might cause the Struts Validator to validate a form that the programmer does not expect.

## Extended description
If two validation forms have the same name, the Struts Validator arbitrarily chooses one of the forms to use for input validation and discards the other. This decision might not correspond to the programmer's expectations, possibly leading to resultant weaknesses. Moreover, it indicates that the validation logic is not up-to-date, and can indicate that other, more subtle validation errors are present.

## Applicable platforms / languages
Java

## Common consequences
- **Integrity**: Unexpected State

## Potential mitigations
- **Implementation**: The DTD or schema validation will not catch the duplicate occurrence of the same form name. To find the issue in the implementation, manual checks or automated static analysis could be applied to the xml configuration files.

## Related weaknesses
- CWE-694 (ChildOf)
- CWE-1173 (ChildOf)
- CWE-20 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/102.html
