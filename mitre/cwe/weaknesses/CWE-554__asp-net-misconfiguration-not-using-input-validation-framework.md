---
cwe_id: CWE-554
name: ASP.NET Misconfiguration: Not Using Input Validation Framework
type: weakness
abstraction: Variant
status: Draft
languages: [ASP.NET]
related_capec: []
url: https://cwe.mitre.org/data/definitions/554.html
tags: [mitre-cwe, weakness, CWE-554]
---

# CWE-554 - ASP.NET Misconfiguration: Not Using Input Validation Framework

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-554](https://cwe.mitre.org/data/definitions/554.html)

## Description
The ASP.NET application does not use an input validation framework.

## Applicable platforms / languages
ASP.NET

## Common consequences
- **Integrity**: Unexpected State

## Potential mitigations
- **Architecture and Design**: Use the ASP.NET validation framework to check all program input before it is processed by the application. Example uses of the validation framework include checking to ensure that: Phone number fields contain only valid characters in phone numbers Boolean values are only "T" or "F" Free-form strings are of a reasonable length and composition

## Related weaknesses
- CWE-1173 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/554.html
