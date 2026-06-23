---
cwe_id: CWE-119
name: Improper Restriction of Operations within the Bounds of a Memory Buffer
type: weakness
abstraction: Class
status: Stable
languages: [Memory-Unsafe, C, C++, Assembly, Not Technology-Specific]
related_capec: [CAPEC-10, CAPEC-100, CAPEC-123, CAPEC-14, CAPEC-24, CAPEC-42, CAPEC-44, CAPEC-45, CAPEC-46, CAPEC-47, CAPEC-8, CAPEC-9]
url: https://cwe.mitre.org/data/definitions/119.html
tags: [mitre-cwe, weakness, CWE-119]
---

# CWE-119 - Improper Restriction of Operations within the Bounds of a Memory Buffer

**Abstraction:** Class  -  **Status:** Stable  -  **CWE:** [CWE-119](https://cwe.mitre.org/data/definitions/119.html)

## Description
The product performs operations on a memory buffer, but it reads from or writes to a memory location outside the buffer's intended boundary. This may result in read or write operations on unexpected memory locations that could be linked to other variables, data structures, or internal program data.

## Applicable platforms / languages
Memory-Unsafe, C, C++, Assembly, Not Technology-Specific

## Common consequences
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands, Modify Memory
- **Availability, Confidentiality**: Read Memory, DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory)
- **Confidentiality**: Read Memory

## Potential mitigations
- **Requirements**: Use a language that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, many languages that perform their own memory management, such as Java and Perl, are not subject to buffer overflows. Other languages, such as Ada and C#, typically provide overflow protection, but the protection can be disabled by the programmer. Be wary that a language's interface to native code may still be subject to overflows, even if the language itself is theoretically safe.
- **Architecture and Design**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. Examples include the Safe C String Library (SafeStr) by Messier and Viega [REF-57], and the Strsafe.h library from Microsoft [REF-56]. These libraries provide safer versions of overflow-prone string-handling functions.
- **Operation, Build and Compilation**: Use automatic buffer overflow detection mechanisms that are offered by certain compilers or compiler extensions. Examples include: the Microsoft Visual Studio /GS flag, Fedora/Red Hat FORTIFY_SOURCE GCC flag, StackGuard, and ProPolice, which provide various mechanisms including canary-based detection and range/index checking. D3-SFCV (Stack Frame Canary Validation) from D3FEND [REF-1334] discusses canary-based detection in detail.
- **Implementation**: Consider adhering to the following rules when allocating and managing an application's memory: Double check that the buffer is as large as specified. When using functions that accept a number of bytes to copy, such as strncpy(), be aware that if the destination buffer size is equal to the source buffer size, it may not NULL-terminate the string. Check buffer boundaries if accessing the buffer in a loop and make sure there is no danger of writing past the allocated space. If necessary, truncate all input strings to a reasonable length before passing them to the copy and concatenation functions.
- **Operation, Build and Compilation**: Run or compile the software using features or extensions that randomly arrange the positions of a program's executable and libraries in memory. Because this makes the addresses unpredictable, it can prevent an attacker from reliably jumping to exploitable code. Examples include Address Space Layout Randomization (ASLR) [REF-58] [REF-60] and Position-Independent Executables (PIE) [REF-64]. Imported modules may be similarly realigned if their default memory addresses conflict with other modules, in a process known as "rebasing" (for Windows) and "prelinking" (for Linux) [REF-1332] using randomly generated addresses. ASLR for libraries cannot be used in conjunction with prelink since it would require relocating the libraries at run-time, defeating the whole purpose of prelinking. For more information on these techniques see D3-SAOR (Segment Address Offset Randomization) from D3FEND [REF-1335].
- **Operation**: Use a CPU and operating system that offers Data Execution Protection (using hardware NX or XD bits) or the equivalent techniques that simulate this feature in software, such as PaX [REF-60] [REF-61]. These techniques ensure that any instruction executed is exclusively at a memory address that is part of the code segment. For more information on these techniques see D3-PSEP (Process Segment Execution Prevention) from D3FEND [REF-1336].
- **Implementation**: Replace unbounded copy functions with analogous functions that support length arguments, such as strcpy with strncpy. Create these if they are not available.

## Related attack patterns (CAPEC)
- [CAPEC-10](https://capec.mitre.org/data/definitions/10.html)
- [CAPEC-100](https://capec.mitre.org/data/definitions/100.html)
- [CAPEC-123](https://capec.mitre.org/data/definitions/123.html)
- [CAPEC-14](https://capec.mitre.org/data/definitions/14.html)
- [CAPEC-24](https://capec.mitre.org/data/definitions/24.html)
- [CAPEC-42](https://capec.mitre.org/data/definitions/42.html)
- [CAPEC-44](https://capec.mitre.org/data/definitions/44.html)
- [CAPEC-45](https://capec.mitre.org/data/definitions/45.html)
- [CAPEC-46](https://capec.mitre.org/data/definitions/46.html)
- [CAPEC-47](https://capec.mitre.org/data/definitions/47.html)
- [CAPEC-8](https://capec.mitre.org/data/definitions/8.html)
- [CAPEC-9](https://capec.mitre.org/data/definitions/9.html)

## Related weaknesses
- CWE-118 (ChildOf)
- CWE-20 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-22991**: Incorrect URI normalization in application traffic product leads to buffer overflow, as exploited in the wild per CISA KEV.
- **CVE-2025-47153**: Chain: build process for JavaScript runtime environment can have inconsistent sizes for off_t (CWE-1102), allowing out-of-bounds access / segmentation fault (CWE-119)
- **CVE-2020-29557**: Buffer overflow in Wi-Fi router web interface, as exploited in the wild per CISA KEV.
- **CVE-2009-2550**: Classic stack-based buffer overflow in media player using a long entry in a playlist
- **CVE-2009-2403**: Heap-based buffer overflow in media player using a long entry in a playlist
- **CVE-2009-0689**: large precision value in a format string triggers overflow
- **CVE-2009-0690**: negative offset value leads to out-of-bounds read
- **CVE-2009-1532**: malformed inputs cause accesses of uninitialized or previously-deleted objects, leading to memory corruption
- **CVE-2009-1528**: chain: lack of synchronization leads to memory corruption
- **CVE-2021-29529**: Chain: machine-learning product can have a heap-based buffer overflow (CWE-122) when some integer-oriented bounds are calculated by using ceiling() and floor() on floating point values (CWE-1339)
- **CVE-2009-0558**: attacker-controlled array index leads to code execution
- **CVE-2009-0269**: chain: -1 value from a function call was intended to indicate an error, but is used as an array index instead.
- **CVE-2009-0566**: chain: incorrect calculations lead to incorrect pointer dereference and memory corruption
- **CVE-2009-1350**: product accepts crafted messages that lead to a dereference of an arbitrary pointer
- **CVE-2009-0191**: chain: malformed input causes dereference of uninitialized memory

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/119.html
