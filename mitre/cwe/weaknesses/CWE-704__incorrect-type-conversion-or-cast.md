---
cwe_id: CWE-704
name: Incorrect Type Conversion or Cast
type: weakness
abstraction: Class
status: Incomplete
languages: [C, C++, Not Language-Specific, Memory-Unsafe, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/704.html
tags: [mitre-cwe, weakness, CWE-704]
---

# CWE-704 - Incorrect Type Conversion or Cast

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-704](https://cwe.mitre.org/data/definitions/704.html)

## Description
The product does not correctly convert an object, resource, or structure from one type to a different type.

## Applicable platforms / languages
C, C++, Not Language-Specific, Memory-Unsafe, Not Technology-Specific

## Common consequences
- **Other**: Other

## Related weaknesses
- CWE-664 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-43537**: Chain: in a web browser, an unsigned 64-bit integer is forcibly cast to a 32-bit integer (CWE-681) and potentially leading to an integer overflow (CWE-190). If an integer overflow occurs, this can cause heap memory corruption (CWE-122)
- **CVE-2022-3979**: Chain: data visualization program written in PHP uses the "!=" operator instead of the type-strict "!==" operator (CWE-480) when validating hash values, potentially leading to an incorrect type conversion (CWE-704)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/704.html
