---
cwe_id: CWE-194
name: Unexpected Sign Extension
type: weakness
abstraction: Variant
status: Incomplete
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/194.html
tags: [mitre-cwe, weakness, CWE-194]
---

# CWE-194 - Unexpected Sign Extension

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-194](https://cwe.mitre.org/data/definitions/194.html)

## Description
The product performs an operation on a number that causes it to be sign extended when it is transformed into a larger data type. When the original number is negative, this can produce unexpected values that lead to resultant weaknesses.

## Applicable platforms / languages
C, C++

## Common consequences
- **Integrity, Confidentiality, Availability, Other**: Read Memory, Modify Memory, Other

## Potential mitigations
- **Implementation**: Avoid using signed variables if you don't need to represent negative values. When negative values are needed, perform validation after you save those values to larger data types, or before passing them to functions that are expecting unsigned values.

## Related weaknesses
- CWE-681 (ChildOf)
- CWE-681 (ChildOf)
- CWE-681 (ChildOf)

## Observed examples (CVE)
- **CVE-2018-10887**: Chain: unexpected sign extension (CWE-194) leads to integer overflow (CWE-190), causing an out-of-bounds read (CWE-125)
- **CVE-1999-0234**: Sign extension error produces -1 value that is treated as a command separator, enabling OS command injection.
- **CVE-2003-0161**: Product uses "char" type for input character. When char is implemented as a signed type, ASCII value 0xFF (255), a sign extension produces a -1 value that is treated as a program-specific separator value, effectively disabling a length check and leading to a buffer overflow. This is also a multiple interpretation error.
- **CVE-2007-4988**: chain: signed short width value in image processor is sign extended during conversion to unsigned int, which leads to integer overflow and heap-based buffer overflow.
- **CVE-2006-1834**: chain: signedness error allows bypass of a length check; later sign extension makes exploitation easier.
- **CVE-2005-2753**: Sign extension when manipulating Pascal-style strings leads to integer overflow and improper memory copy.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/194.html
