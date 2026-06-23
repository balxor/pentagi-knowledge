---
cwe_id: CWE-195
name: Signed to Unsigned Conversion Error
type: weakness
abstraction: Variant
status: Draft
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/195.html
tags: [mitre-cwe, weakness, CWE-195]
---

# CWE-195 - Signed to Unsigned Conversion Error

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-195](https://cwe.mitre.org/data/definitions/195.html)

## Description
The product uses a signed primitive and performs a cast to an unsigned primitive, which can produce an unexpected value if the value of the signed primitive can not be represented using an unsigned primitive.

## Extended description
It is dangerous to rely on implicit casts between signed and unsigned numbers because the result can take on an unexpected value and violate assumptions made by the program. Often, functions will return negative values to indicate a failure. When the result of a function is to be used as a size parameter, using these negative return values can have unexpected results. For example, if negative size values are passed to the standard memory copy or allocation functions they will be implicitly cast to a large unsigned value. This may lead to an exploitable buffer overflow or underflow condition.

## Applicable platforms / languages
C, C++

## Common consequences
- **Integrity**: Unexpected State

## Related weaknesses
- CWE-681 (ChildOf)
- CWE-681 (ChildOf)
- CWE-681 (ChildOf)
- CWE-119 (CanPrecede)

## Observed examples (CVE)
- **CVE-2025-27363**: Font rendering library does not properly handle assigning a signed short value to an unsigned long (CWE-195), leading to an integer wraparound (CWE-190), causing too small of a buffer (CWE-131), leading to an out-of-bounds write (CWE-787).
- **CVE-2007-4268**: Chain: integer signedness error (CWE-195) passes signed comparison, leading to heap overflow (CWE-122)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/195.html
