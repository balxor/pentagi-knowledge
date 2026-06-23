---
cwe_id: CWE-122
name: Heap-based Buffer Overflow
type: weakness
abstraction: Variant
status: Draft
languages: [Memory-Unsafe, C, C++, Not Technology-Specific]
related_capec: [CAPEC-92]
url: https://cwe.mitre.org/data/definitions/122.html
tags: [mitre-cwe, weakness, CWE-122]
---

# CWE-122 - Heap-based Buffer Overflow

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-122](https://cwe.mitre.org/data/definitions/122.html)

## Description
A heap overflow condition is a buffer overflow, where the buffer that can be overwritten is allocated in the heap portion of memory, generally meaning that the buffer was allocated using a routine such as malloc().

## Applicable platforms / languages
Memory-Unsafe, C, C++, Not Technology-Specific

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory)
- **Integrity, Confidentiality, Availability, Access Control**: Execute Unauthorized Code or Commands, Bypass Protection Mechanism, Modify Memory
- **Integrity, Confidentiality, Availability, Access Control, Other**: Execute Unauthorized Code or Commands, Bypass Protection Mechanism, Other

## Potential mitigations
- **general**: Pre-design: Use a language or compiler that performs automatic bounds checking.
- **Architecture and Design**: Use an abstraction library to abstract away risky APIs. Not a complete solution.
- **Operation, Build and Compilation**: Use automatic buffer overflow detection mechanisms that are offered by certain compilers or compiler extensions. Examples include: the Microsoft Visual Studio /GS flag, Fedora/Red Hat FORTIFY_SOURCE GCC flag, StackGuard, and ProPolice, which provide various mechanisms including canary-based detection and range/index checking. D3-SFCV (Stack Frame Canary Validation) from D3FEND [REF-1334] discusses canary-based detection in detail.
- **Operation, Build and Compilation**: Run or compile the software using features or extensions that randomly arrange the positions of a program's executable and libraries in memory. Because this makes the addresses unpredictable, it can prevent an attacker from reliably jumping to exploitable code. Examples include Address Space Layout Randomization (ASLR) [REF-58] [REF-60] and Position-Independent Executables (PIE) [REF-64]. Imported modules may be similarly realigned if their default memory addresses conflict with other modules, in a process known as "rebasing" (for Windows) and "prelinking" (for Linux) [REF-1332] using randomly generated addresses. ASLR for libraries cannot be used in conjunction with prelink since it would require relocating the libraries at run-time, defeating the whole purpose of prelinking. For more information on these techniques see D3-SAOR (Segment Address Offset Randomization) from D3FEND [REF-1335].
- **Implementation**: Implement and perform bounds checking on input.
- **Implementation**: Do not use dangerous functions such as gets. Look for their safe equivalent, which checks for the boundary.
- **Operation**: Use OS-level preventative functionality. This is not a complete solution, but it provides some defense in depth.

## Related attack patterns (CAPEC)
- [CAPEC-92](https://capec.mitre.org/data/definitions/92.html)

## Related weaknesses
- CWE-788 (ChildOf)
- CWE-787 (ChildOf)

## Observed examples (CVE)
- **CVE-2025-46687**: Chain: Javascript engine code does not perform a length check (CWE-1284) leading to integer overflow (CWE-190) causing allocation of smaller buffer than expected (CWE-131) resulting in a heap-based buffer overflow (CWE-122)
- **CVE-2021-43537**: Chain: in a web browser, an unsigned 64-bit integer is forcibly cast to a 32-bit integer (CWE-681) and potentially leading to an integer overflow (CWE-190). If an integer overflow occurs, this can cause heap memory corruption (CWE-122)
- **CVE-2007-4268**: Chain: integer signedness error (CWE-195) passes signed comparison, leading to heap overflow (CWE-122)
- **CVE-2009-2523**: Chain: product does not handle when an input string is not NULL terminated (CWE-170), leading to buffer over-read (CWE-125) or heap-based buffer overflow (CWE-122).
- **CVE-2021-29529**: Chain: machine-learning product can have a heap-based buffer overflow (CWE-122) when some integer-oriented bounds are calculated by using ceiling() and floor() on floating point values (CWE-1339)
- **CVE-2010-1866**: Chain: integer overflow (CWE-190) causes a negative signed value, which later bypasses a maximum-only check (CWE-839), leading to heap-based buffer overflow (CWE-122).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/122.html
