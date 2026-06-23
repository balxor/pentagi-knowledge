---
cwe_id: CWE-839
name: Numeric Range Comparison Without Minimum Check
type: weakness
abstraction: Base
status: Incomplete
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/839.html
tags: [mitre-cwe, weakness, CWE-839]
---

# CWE-839 - Numeric Range Comparison Without Minimum Check

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-839](https://cwe.mitre.org/data/definitions/839.html)

## Description
The product checks a value to ensure that it is less than or equal to a maximum, but it does not also verify that the value is greater than or equal to the minimum.

## Extended description
Some products use signed integers or floats even when their values are only expected to be positive or 0. An input validation check might assume that the value is positive, and only check for the maximum value. If the value is negative, but the code assumes that the value is positive, this can produce an error. The error may have security consequences if the negative value is used for memory allocation, array access, buffer access, etc. Ultimately, the error could lead to a buffer overflow or other type of memory corruption. The use of a negative number in a positive-only context could have security implications for other types of resources. For example, a shopping cart might check that the user is not requesting more than 10 items, but a request for -3 items could cause the application to calculate a negative price and credit the attacker's account.

## Applicable platforms / languages
C, C++

## Common consequences
- **Integrity, Confidentiality, Availability**: Modify Application Data, Execute Unauthorized Code or Commands
- **Availability**: DoS: Resource Consumption (Other)
- **Confidentiality, Integrity**: Modify Memory, Read Memory

## Potential mitigations
- **Implementation**: If the number to be used is always expected to be positive, change the variable type from signed to unsigned or size_t.
- **Implementation**: If the number to be used could have a negative value based on the specification (thus requiring a signed value), but the number should only be positive to preserve code correctness, then include a check to ensure that the value is positive.

## Related weaknesses
- CWE-1023 (ChildOf)
- CWE-195 (CanPrecede)
- CWE-682 (CanPrecede)
- CWE-119 (CanPrecede)
- CWE-124 (CanPrecede)

## Observed examples (CVE)
- **CVE-2010-1866**: Chain: integer overflow (CWE-190) causes a negative signed value, which later bypasses a maximum-only check (CWE-839), leading to heap-based buffer overflow (CWE-122).
- **CVE-2009-1099**: Chain: 16-bit counter can be interpreted as a negative value, compared to a 32-bit maximum value, leading to buffer under-write.
- **CVE-2011-0521**: Chain: kernel's lack of a check for a negative value leads to memory corruption.
- **CVE-2010-3704**: Chain: parser uses atoi() but does not check for a negative value, which can happen on some platforms, leading to buffer under-write.
- **CVE-2010-2530**: Chain: Negative value stored in an int bypasses a size check and causes allocation of large amounts of memory.
- **CVE-2009-3080**: Chain: negative offset value to IOCTL bypasses check for maximum index, then used as an array index for buffer under-read.
- **CVE-2008-6393**: chain: file transfer client performs signed comparison, leading to integer overflow and heap-based buffer overflow.
- **CVE-2008-4558**: chain: negative ID in media player bypasses check for maximum index, then used as an array index for buffer under-read.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/839.html
