---
cwe_id: CWE-103
name: Struts: Incomplete validate() Method Definition
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/103.html
tags: [mitre-cwe, weakness, CWE-103]
---

# CWE-103 - Struts: Incomplete validate() Method Definition

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-103](https://cwe.mitre.org/data/definitions/103.html)

## Description
The product has a validator form that either does not define a validate() method, or defines a validate() method but does not call super.validate().

## Applicable platforms / languages
Java

## Common consequences
- **Other**: Unexpected State, Varies by Context
- **Confidentiality, Integrity, Availability, Other**: Other

## Potential mitigations
- **Implementation**: Implement the validate() method and call super.validate() within that method.

## Related weaknesses
- CWE-573 (ChildOf)
- CWE-20 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/103.html
