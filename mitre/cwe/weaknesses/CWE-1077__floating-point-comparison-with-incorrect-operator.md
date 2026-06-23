---
cwe_id: CWE-1077
name: Floating Point Comparison with Incorrect Operator
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1077.html
tags: [mitre-cwe, weakness, CWE-1077]
---

# CWE-1077 - Floating Point Comparison with Incorrect Operator

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-1077](https://cwe.mitre.org/data/definitions/1077.html)

## Description
The code performs a comparison such as an equality test between two float (floating point) values, but it uses comparison operators that do not account for the possibility of loss of precision.

## Extended description
Numeric calculation using floating point values can generate imprecise results because of rounding errors. As a result, two different calculations might generate numbers that are mathematically equal, but have slightly different bit representations that do not translate to the same mathematically-equal values. As a result, an equality test or other comparison might produce unexpected results.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Reduce Reliability

## Related weaknesses
- CWE-697 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1077.html
