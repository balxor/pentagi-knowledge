---
cwe_id: CWE-197
name: Numeric Truncation Error
type: weakness
abstraction: Base
status: Incomplete
languages: [C, C++, Java, C#]
related_capec: []
url: https://cwe.mitre.org/data/definitions/197.html
tags: [mitre-cwe, weakness, CWE-197]
---

# CWE-197 - Numeric Truncation Error

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-197](https://cwe.mitre.org/data/definitions/197.html)

## Description
Truncation errors occur when a primitive is cast to a primitive of a smaller size and data is lost in the conversion.

## Extended description
When a primitive is cast to a smaller primitive, the high order bits of the large value are lost in the conversion, potentially resulting in an unexpected value that is not equal to the original value. This value may be required as an index into a buffer, a loop iterator, or simply necessary state data. In any case, the value cannot be trusted and the system will be in an undefined state. While this method may be employed viably to isolate the low bits of a value, this usage is rare, and truncation usually implies that an implementation error has occurred.

## Applicable platforms / languages
C, C++, Java, C#

## Common consequences
- **Integrity**: Modify Memory

## Potential mitigations
- **Implementation**: Ensure that no casts, implicit or explicit, take place that move from a larger size primitive or a smaller size primitive.

## Related weaknesses
- CWE-681 (ChildOf)
- CWE-681 (ChildOf)
- CWE-681 (ChildOf)
- CWE-195 (CanAlsoBe)
- CWE-196 (CanAlsoBe)
- CWE-192 (CanAlsoBe)
- CWE-194 (CanAlsoBe)

## Observed examples (CVE)
- **CVE-2020-17087**: Chain: integer truncation (CWE-197) causes small buffer allocation (CWE-131) leading to out-of-bounds write (CWE-787) in kernel pool, as exploited in the wild per CISA KEV.
- **CVE-2009-0231**: Integer truncation of length value leads to heap-based buffer overflow.
- **CVE-2008-3282**: Size of a particular type changes for 64-bit platforms, leading to an integer truncation in document processor causes incorrect index to be generated.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/197.html
