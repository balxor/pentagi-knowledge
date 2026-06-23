---
cwe_id: CWE-108
name: Struts: Unvalidated Action Form
type: weakness
abstraction: Variant
status: Incomplete
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/108.html
tags: [mitre-cwe, weakness, CWE-108]
---

# CWE-108 - Struts: Unvalidated Action Form

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-108](https://cwe.mitre.org/data/definitions/108.html)

## Description
Every Action Form must have a corresponding validation form.

## Extended description
If a Struts Action Form Mapping specifies a form, it must have a validation form defined under the Struts Validator.

## Applicable platforms / languages
Java

## Common consequences
- **Other**: Other
- **Confidentiality, Integrity, Availability, Other**: Other

## Potential mitigations
- **Implementation**: Map every Action Form to a corresponding validation form. An action or a form may perform validation in other ways, but the Struts Validator provides an excellent way to verify that all input receives at least a basic level of validation. Without this approach, it is difficult, and often impossible, to establish with a high level of confidence that all input is validated.

## Related weaknesses
- CWE-1173 (ChildOf)
- CWE-20 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/108.html
