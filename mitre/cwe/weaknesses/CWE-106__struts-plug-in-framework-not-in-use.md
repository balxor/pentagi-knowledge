---
cwe_id: CWE-106
name: Struts: Plug-in Framework not in Use
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/106.html
tags: [mitre-cwe, weakness, CWE-106]
---

# CWE-106 - Struts: Plug-in Framework not in Use

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-106](https://cwe.mitre.org/data/definitions/106.html)

## Description
When an application does not use an input validation framework such as the Struts Validator, there is a greater risk of introducing weaknesses related to insufficient input validation.

## Extended description
Unchecked input is the leading cause of vulnerabilities in J2EE applications. Unchecked input leads to cross-site scripting, process control, and SQL injection vulnerabilities, among others. Although J2EE applications are not generally susceptible to memory corruption attacks, if a J2EE application interfaces with native code that does not perform array bounds checking, an attacker may be able to use an input validation mistake in the J2EE application to launch a buffer overflow attack.

## Applicable platforms / languages
Java

## Common consequences
- **Integrity**: Unexpected State

## Potential mitigations
- **Architecture and Design**: Use an input validation framework such as Struts.
- **Architecture and Design**: Use an input validation framework such as Struts.
- **Implementation**: Use the Struts Validator to validate all program input before it is processed by the application. Ensure that there are no holes in the configuration of the Struts Validator. Example uses of the validator include checking to ensure that: Phone number fields contain only valid characters in phone numbers Boolean values are only "T" or "F" Free-form strings are of a reasonable length and composition
- **Implementation**: Use the Struts Validator to validate all program input before it is processed by the application. Ensure that there are no holes in the configuration of the Struts Validator. Example uses of the validator include checking to ensure that: Phone number fields contain only valid characters in phone numbers Boolean values are only "T" or "F" Free-form strings are of a reasonable length and composition

## Related weaknesses
- CWE-1173 (ChildOf)
- CWE-20 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/106.html
