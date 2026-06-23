---
cwe_id: CWE-190
name: Integer Overflow or Wraparound
type: weakness
abstraction: Base
status: Stable
languages: [Not Language-Specific, C, Not Technology-Specific]
related_capec: [CAPEC-92]
url: https://cwe.mitre.org/data/definitions/190.html
tags: [mitre-cwe, weakness, CWE-190]
---

# CWE-190 - Integer Overflow or Wraparound

**Abstraction:** Base  -  **Status:** Stable  -  **CWE:** [CWE-190](https://cwe.mitre.org/data/definitions/190.html)

## Description
The product performs a calculation that can produce an integer overflow or wraparound when the logic assumes that the resulting value will always be larger than the original value. This occurs when an integer value is incremented to a value that is too large to store in the associated representation. When this occurs, the value may become a very small or negative number.

## Applicable platforms / languages
Not Language-Specific, C, Not Technology-Specific

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (Memory), DoS: Instability
- **Integrity**: Modify Memory
- **Confidentiality, Availability, Access Control**: Execute Unauthorized Code or Commands, Bypass Protection Mechanism
- **Availability, Other**: Alter Execution Logic, DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU)
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Requirements**: Ensure that all protocols are strictly defined, such that all out-of-bounds behavior can be identified simply, and require strict conformance to the protocol.
- **Requirements**: Use a language that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. If possible, choose a language or compiler that performs automatic bounds checking.
- **Architecture and Design**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid [REF-1482]. Use libraries or frameworks that make it easier to handle numbers without unexpected consequences. Examples include safe integer handling packages such as SafeInt (C++) or IntegerLib (C or C++). [REF-106]
- **Implementation**: Perform input validation on any numeric input by ensuring that it is within the expected range. Enforce that the input meets both the minimum and maximum requirements for the expected range. Use unsigned integers where possible. This makes it easier to perform validation for integer overflows. When signed integers are required, ensure that the range check includes minimum values as well as maximum values.
- **Implementation**: Understand the programming language's underlying representation and how it interacts with numeric calculation (CWE-681). Pay close attention to byte size discrepancies, precision, signed/unsigned distinctions, truncation, conversion and casting between types, "not-a-number" calculations, and how the language handles numbers that are too large or too small for its underlying representation. [REF-7] Also be careful to account for 32-bit, 64-bit, and other potential differences that may affect the numeric representation.
- **Architecture and Design**: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.
- **Implementation**: Examine compiler warnings closely and eliminate problems with potential security implications, such as signed / unsigned mismatch in memory operations, or use of uninitialized variables. Even if the weakness is rarely exploitable, a single failure may lead to the compromise of the entire system.

## Related attack patterns (CAPEC)
- [CAPEC-92](https://capec.mitre.org/data/definitions/92.html)

## Related weaknesses
- CWE-682 (ChildOf)
- CWE-682 (ChildOf)
- CWE-20 (ChildOf)
- CWE-119 (CanPrecede)

## Observed examples (CVE)
- **CVE-2025-46687**: Chain: Javascript engine code does not perform a length check (CWE-1284) leading to integer overflow (CWE-190) causing allocation of smaller buffer than expected (CWE-131) resulting in a heap-based buffer overflow (CWE-122)
- **CVE-2025-27363**: Font rendering library does not properly handle assigning a signed short value to an unsigned long (CWE-195), leading to an integer wraparound (CWE-190), causing too small of a buffer (CWE-131), leading to an out-of-bounds write (CWE-787).
- **CVE-2021-43537**: Chain: in a web browser, an unsigned 64-bit integer is forcibly cast to a 32-bit integer (CWE-681) and potentially leading to an integer overflow (CWE-190). If an integer overflow occurs, this can cause heap memory corruption (CWE-122)
- **CVE-2019-19911**: Chain: Python library does not limit the resources used to process images that specify a very large number of bands (CWE-1284), leading to excessive memory consumption (CWE-789) or an integer overflow (CWE-190).
- **CVE-2022-0545**: Chain: 3D renderer has an integer overflow (CWE-190) leading to write-what-where condition (CWE-123) using a crafted image.
- **CVE-2021-30860**: Chain: improper input validation (CWE-20) leads to integer overflow (CWE-190) in mobile OS, as exploited in the wild per CISA KEV.
- **CVE-2021-30663**: Chain: improper input validation (CWE-20) leads to integer overflow (CWE-190) in mobile OS, as exploited in the wild per CISA KEV.
- **CVE-2018-10887**: Chain: unexpected sign extension (CWE-194) leads to integer overflow (CWE-190), causing an out-of-bounds read (CWE-125)
- **CVE-2019-1010006**: Chain: compiler optimization (CWE-733) removes or modifies code used to detect integer overflow (CWE-190), allowing out-of-bounds write (CWE-787).
- **CVE-2010-1866**: Chain: integer overflow (CWE-190) causes a negative signed value, which later bypasses a maximum-only check (CWE-839), leading to heap-based buffer overflow (CWE-122).
- **CVE-2010-2753**: Chain: integer overflow leads to use-after-free
- **CVE-2005-1513**: Chain: integer overflow in securely-coded mail program leads to buffer overflow. In 2005, this was regarded as unrealistic to exploit, but in 2020, it was rediscovered to be easier to exploit due to evolutions of the technology.
- **CVE-2002-0391**: Integer overflow via a large number of arguments.
- **CVE-2002-0639**: Integer overflow in OpenSSH as listed in the demonstrative examples.
- **CVE-2005-1141**: Image with large width and height leads to integer overflow.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/190.html
