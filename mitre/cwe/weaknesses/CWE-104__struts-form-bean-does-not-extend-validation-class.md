---
cwe_id: CWE-104
name: Struts: Form Bean Does Not Extend Validation Class
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/104.html
tags: [mitre-cwe, weakness, CWE-104]
---

# CWE-104 - Struts: Form Bean Does Not Extend Validation Class

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-104](https://cwe.mitre.org/data/definitions/104.html)

## Description
If a form bean does not extend an ActionForm subclass of the Validator framework, it can expose the application to other weaknesses related to insufficient input validation.

## Applicable platforms / languages
Java

## Common consequences
- **Other**: Other
- **Confidentiality, Integrity, Availability, Other**: Other

## Potential mitigations
- **Implementation**: Ensure that all forms extend one of the Validation Classes.

## Related weaknesses
- CWE-573 (ChildOf)
- CWE-20 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/104.html
