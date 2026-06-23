---
cwe_id: CWE-401
name: Missing Release of Memory after Effective Lifetime
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific, C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/401.html
tags: [mitre-cwe, weakness, CWE-401]
---

# CWE-401 - Missing Release of Memory after Effective Lifetime

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-401](https://cwe.mitre.org/data/definitions/401.html)

## Description
The product does not sufficiently track and release allocated memory after it has been used, making the memory unavailable for reallocation and reuse.

## Applicable platforms / languages
Not Language-Specific, C, C++

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart, DoS: Instability, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory)
- **Other**: Reduce Performance

## Potential mitigations
- **Implementation**: Choose a language or tool that provides automatic memory management, or makes manual memory management less error-prone. For example, glibc in Linux provides protection against free of invalid pointers. When using Xcode to target OS X or iOS, enable automatic reference counting (ARC) [REF-391]. To help correctly and consistently manage memory when programming in C++, consider using a smart pointer class such as std::auto_ptr (defined by ISO/IEC ISO/IEC 14882:2003), std::shared_ptr and std::unique_ptr (specified by an upcoming revision of the C++ standard, informally referred to as C++ 1x), or equivalent solutions such as Boost.
- **Architecture and Design**: Use an abstraction library to abstract away risky APIs. Not a complete solution.
- **Architecture and Design, Build and Compilation**: Consider using the Boehm-Demers-Weiser garbage collector (bdwgc), which can help avoid leaks.

## Related weaknesses
- CWE-772 (ChildOf)
- CWE-404 (ChildOf)
- CWE-404 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-3119**: Memory leak because function does not free() an element of a data structure.
- **CVE-2004-0427**: Memory leak when counter variable is not decremented.
- **CVE-2002-0574**: chain: reference count is not decremented, leading to memory leak in OS by sending ICMP packets.
- **CVE-2005-3181**: Kernel uses wrong function to release a data structure, preventing data from being properly tracked by other code.
- **CVE-2004-0222**: Memory leak via unknown manipulations as part of protocol test suite.
- **CVE-2001-0136**: Memory leak via a series of the same command.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/401.html
