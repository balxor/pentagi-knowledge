---
cwe_id: CWE-1335
name: Incorrect Bitwise Shift of Integer
type: weakness
abstraction: Base
status: Draft
languages: [C, C++, C#, Java, JavaScript, Not OS-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1335.html
tags: [mitre-cwe, weakness, CWE-1335]
---

# CWE-1335 - Incorrect Bitwise Shift of Integer

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1335](https://cwe.mitre.org/data/definitions/1335.html)

## Description
An integer value is specified to be shifted by a negative amount or an amount greater than or equal to the number of bits contained in the value causing an unexpected or indeterminate result.

## Extended description
Specifying a value to be shifted by a negative amount is undefined in various languages. Various computer architectures implement this action in different ways. The compilers and interpreters when generating code to accomplish a shift generally do not do a check for this issue. Specifying an over-shift, a shift greater than or equal to the number of bits contained in a value to be shifted, produces a result which varies by architecture and compiler. In some languages, this action is specifically listed as producing an undefined result.

## Applicable platforms / languages
C, C++, C#, Java, JavaScript, Not OS-Specific, Not Technology-Specific

## Common consequences
- **Integrity**: DoS: Crash, Exit, or Restart

## Potential mitigations
- **Implementation**: Implicitly or explicitly add checks and mitigation for negative or over-shift values.

## Related weaknesses
- CWE-682 (ChildOf)

## Observed examples (CVE)
- **CVE-2023-4720**: multimedia product performs a left shift with a negative value, leading to a crash
- **CVE-2009-4307**: An unexpected large value in the ext4 filesystem causes an overshift condition resulting in a divide by zero.
- **CVE-2012-2100**: An unexpected large value in the ext4 filesystem causes an overshift condition resulting in a divide by zero - fix of CVE-2009-4307.
- **CVE-2020-8835**: An overshift in a kernel allowed out of bounds reads and writes resulting in a root takeover.
- **CVE-2015-1607**: Program is not properly handling signed bitwise left-shifts causing an overlapping memcpy memory range error.
- **CVE-2016-9842**: Compression function improperly executes a signed left shift of a negative integer.
- **CVE-2018-18445**: Some kernels improperly handle right shifts of 32 bit numbers in a 64 bit register.
- **CVE-2013-4206**: Putty has an incorrectly sized shift value resulting in an overshift.
- **CVE-2018-20788**: LED driver overshifts under certain conditions resulting in a DoS.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1335.html
