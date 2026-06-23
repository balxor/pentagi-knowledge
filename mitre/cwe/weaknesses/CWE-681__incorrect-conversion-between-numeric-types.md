---
cwe_id: CWE-681
name: Incorrect Conversion between Numeric Types
type: weakness
abstraction: Base
status: Draft
languages: [C, Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/681.html
tags: [mitre-cwe, weakness, CWE-681]
---

# CWE-681 - Incorrect Conversion between Numeric Types

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-681](https://cwe.mitre.org/data/definitions/681.html)

## Description
When converting from one data type to another, such as long to integer, data can be omitted or translated in a way that produces unexpected values. If the resulting values are used in a sensitive context, then dangerous behaviors may occur.

## Applicable platforms / languages
C, Not Language-Specific, Not Technology-Specific

## Common consequences
- **Other, Integrity**: Unexpected State, Quality Degradation

## Potential mitigations
- **Implementation**: Avoid making conversion between numeric types. Always check for the allowed ranges.

## Related weaknesses
- CWE-704 (ChildOf)
- CWE-704 (ChildOf)
- CWE-682 (CanPrecede)

## Observed examples (CVE)
- **CVE-2022-2639**: Chain: integer coercion error (CWE-192) prevents a return value from indicating an error, leading to out-of-bounds write (CWE-787)
- **CVE-2021-43537**: Chain: in a web browser, an unsigned 64-bit integer is forcibly cast to a 32-bit integer (CWE-681) and potentially leading to an integer overflow (CWE-190). If an integer overflow occurs, this can cause heap memory corruption (CWE-122)
- **CVE-2007-4268**: Chain: integer signedness error (CWE-195) passes signed comparison, leading to heap overflow (CWE-122)
- **CVE-2007-4988**: Chain: signed short width value in image processor is sign extended during conversion to unsigned int, which leads to integer overflow and heap-based buffer overflow.
- **CVE-2009-0231**: Integer truncation of length value leads to heap-based buffer overflow.
- **CVE-2008-3282**: Size of a particular type changes for 64-bit platforms, leading to an integer truncation in document processor causes incorrect index to be generated.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/681.html
