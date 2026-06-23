---
cwe_id: CWE-109
name: Struts: Validator Turned Off
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/109.html
tags: [mitre-cwe, weakness, CWE-109]
---

# CWE-109 - Struts: Validator Turned Off

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-109](https://cwe.mitre.org/data/definitions/109.html)

## Description
Automatic filtering via a Struts bean has been turned off, which disables the Struts Validator and custom validation logic. This exposes the application to other weaknesses related to insufficient input validation.

## Applicable platforms / languages
Java

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: Ensure that an action form mapping enables validation. Set the validate field to true.

## Related weaknesses
- CWE-1173 (ChildOf)
- CWE-20 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/109.html
