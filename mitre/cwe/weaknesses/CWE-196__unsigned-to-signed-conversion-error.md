---
cwe_id: CWE-196
name: Unsigned to Signed Conversion Error
type: weakness
abstraction: Variant
status: Draft
languages: [C, C++]
related_capec: [CAPEC-92]
url: https://cwe.mitre.org/data/definitions/196.html
tags: [mitre-cwe, weakness, CWE-196]
---

# CWE-196 - Unsigned to Signed Conversion Error

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-196](https://cwe.mitre.org/data/definitions/196.html)

## Description
The product uses an unsigned primitive and performs a cast to a signed primitive, which can produce an unexpected value if the value of the unsigned primitive can not be represented using a signed primitive.

## Extended description
Although less frequent an issue than signed-to-unsigned conversion, unsigned-to-signed conversion can be the perfect precursor to dangerous buffer underwrite conditions that allow attackers to move down the stack where they otherwise might not have access in a normal buffer overflow condition. Buffer underwrites occur frequently when large unsigned values are cast to signed values, and then used as indexes into a buffer or for pointer arithmetic.

## Applicable platforms / languages
C, C++

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart
- **Integrity**: Modify Memory
- **Integrity, Confidentiality, Availability, Access Control**: Execute Unauthorized Code or Commands, Bypass Protection Mechanism

## Potential mitigations
- **Requirements**: Choose a language which is not subject to these casting flaws.
- **Architecture and Design**: Design object accessor functions to implicitly check values for valid sizes. Ensure that all functions which will be used as a size are checked previous to use as a size. If the language permits, throw exceptions rather than using in-band errors.
- **Implementation**: Error check the return values of all functions. Be aware of implicit casts made, and use unsigned variables for sizes if at all possible.

## Related attack patterns (CAPEC)
- [CAPEC-92](https://capec.mitre.org/data/definitions/92.html)

## Related weaknesses
- CWE-681 (ChildOf)
- CWE-681 (ChildOf)
- CWE-681 (ChildOf)
- CWE-124 (CanAlsoBe)
- CWE-120 (CanAlsoBe)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/196.html
