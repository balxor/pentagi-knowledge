---
cwe_id: CWE-121
name: Stack-based Buffer Overflow
type: weakness
abstraction: Variant
status: Draft
languages: [Memory-Unsafe, C, C++, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/121.html
tags: [mitre-cwe, weakness, CWE-121]
---

# CWE-121 - Stack-based Buffer Overflow

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-121](https://cwe.mitre.org/data/definitions/121.html)

## Description
A stack-based buffer overflow condition is a condition where the buffer being overwritten is allocated on the stack (i.e., is a local variable or, rarely, a parameter to a function).

## Applicable platforms / languages
Memory-Unsafe, C, C++, Not Technology-Specific

## Common consequences
- **Availability**: Modify Memory, DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory)
- **Integrity, Confidentiality, Availability, Access Control**: Modify Memory, Execute Unauthorized Code or Commands, Bypass Protection Mechanism
- **Integrity, Confidentiality, Availability, Access Control, Other**: Modify Memory, Execute Unauthorized Code or Commands, Bypass Protection Mechanism, Other

## Potential mitigations
- **Operation, Build and Compilation**: Use automatic buffer overflow detection mechanisms that are offered by certain compilers or compiler extensions. Examples include: the Microsoft Visual Studio /GS flag, Fedora/Red Hat FORTIFY_SOURCE GCC flag, StackGuard, and ProPolice, which provide various mechanisms including canary-based detection and range/index checking. D3-SFCV (Stack Frame Canary Validation) from D3FEND [REF-1334] discusses canary-based detection in detail.
- **Architecture and Design**: Use an abstraction library to abstract away risky APIs. Not a complete solution.
- **Implementation**: Implement and perform bounds checking on input.
- **Implementation**: Do not use dangerous functions such as gets. Use safer, equivalent functions which check for boundary errors.
- **Operation, Build and Compilation**: Run or compile the software using features or extensions that randomly arrange the positions of a program's executable and libraries in memory. Because this makes the addresses unpredictable, it can prevent an attacker from reliably jumping to exploitable code. Examples include Address Space Layout Randomization (ASLR) [REF-58] [REF-60] and Position-Independent Executables (PIE) [REF-64]. Imported modules may be similarly realigned if their default memory addresses conflict with other modules, in a process known as "rebasing" (for Windows) and "prelinking" (for Linux) [REF-1332] using randomly generated addresses. ASLR for libraries cannot be used in conjunction with prelink since it would require relocating the libraries at run-time, defeating the whole purpose of prelinking. For more information on these techniques see D3-SAOR (Segment Address Offset Randomization) from D3FEND [REF-1335].

## Related weaknesses
- CWE-788 (ChildOf)
- CWE-787 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-35395**: Stack-based buffer overflows in SFK for wifi chipset used for IoT/embedded devices, as exploited in the wild per CISA KEV.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/121.html
