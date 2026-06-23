---
cwe_id: CWE-192
name: Integer Coercion Error
type: weakness
abstraction: Variant
status: Incomplete
languages: [C, C++, Java, C#]
related_capec: []
url: https://cwe.mitre.org/data/definitions/192.html
tags: [mitre-cwe, weakness, CWE-192]
---

# CWE-192 - Integer Coercion Error

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-192](https://cwe.mitre.org/data/definitions/192.html)

## Description
Integer coercion refers to a set of flaws pertaining to the type casting, extension, or truncation of primitive data types.

## Extended description
Several flaws fall under the category of integer coercion errors. For the most part, these errors in and of themselves result only in availability and data integrity issues. However, in some circumstances, they may result in other, more complicated security related flaws, such as buffer overflow conditions.

## Applicable platforms / languages
C, C++, Java, C#

## Common consequences
- **Availability**: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Crash, Exit, or Restart
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands
- **Integrity, Other**: Other

## Potential mitigations
- **Requirements**: A language which throws exceptions on ambiguous data casts might be chosen.
- **Architecture and Design**: Design objects and program flow such that multiple or complex casts are unnecessary
- **Implementation**: Ensure that any data type casting that you must used is entirely understood in order to reduce the plausibility of error in use.

## Related weaknesses
- CWE-681 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-2639**: Chain: integer coercion error (CWE-192) prevents a return value from indicating an error, leading to out-of-bounds write (CWE-787)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/192.html
