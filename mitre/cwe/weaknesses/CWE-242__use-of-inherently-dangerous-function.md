---
cwe_id: CWE-242
name: Use of Inherently Dangerous Function
type: weakness
abstraction: Base
status: Draft
languages: [C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/242.html
tags: [mitre-cwe, weakness, CWE-242]
---

# CWE-242 - Use of Inherently Dangerous Function

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-242](https://cwe.mitre.org/data/definitions/242.html)

## Description
The product calls a function that can never be guaranteed to work safely.

## Extended description
Certain functions behave in dangerous ways regardless of how they are used. Functions in this category were often implemented without taking security concerns into account. The gets() function is unsafe because it does not perform bounds checking on the size of its input. An attacker can easily send arbitrarily-sized input to gets() and overflow the destination buffer. Similarly, the >> operator is unsafe to use when reading into a statically-allocated character array because it does not perform bounds checking on the size of its input. An attacker can easily send arbitrarily-sized input to the >> operator and overflow the destination buffer.

## Applicable platforms / languages
C, C++

## Common consequences
- **Other**: Varies by Context

## Potential mitigations
- **Build and Compilation, Implementation**: Identify a list of prohibited API functions and prohibit developers from using these functions, providing safer alternatives. In some cases, automatic code analysis tools or the compiler can be instructed to spot use of prohibited functions, such as the "banned.h" include file from Microsoft's SDL. [REF-554] [REF-1009] [REF-7]
- **Testing**: Use grep or static analysis tools to spot usage of dangerous functions.

## Related weaknesses
- CWE-1177 (ChildOf)

## Observed examples (CVE)
- **CVE-2007-4004**: FTP client uses inherently insecure gets() function and is setuid root on some systems, allowing buffer overflow

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/242.html
