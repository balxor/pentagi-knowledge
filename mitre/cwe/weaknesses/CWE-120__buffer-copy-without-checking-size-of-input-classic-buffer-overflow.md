---
cwe_id: CWE-120
name: Buffer Copy without Checking Size of Input ('Classic Buffer Overflow')
type: weakness
abstraction: Base
status: Incomplete
languages: [Memory-Unsafe, C, C++, Assembly]
related_capec: [CAPEC-10, CAPEC-100, CAPEC-14, CAPEC-24, CAPEC-42, CAPEC-44, CAPEC-45, CAPEC-46, CAPEC-47, CAPEC-67, CAPEC-8, CAPEC-9, CAPEC-92]
url: https://cwe.mitre.org/data/definitions/120.html
tags: [mitre-cwe, weakness, CWE-120]
---

# CWE-120 - Buffer Copy without Checking Size of Input ('Classic Buffer Overflow')

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-120](https://cwe.mitre.org/data/definitions/120.html)

## Description
The product copies an input buffer to an output buffer without verifying that the size of the input buffer is less than the size of the output buffer.

## Applicable platforms / languages
Memory-Unsafe, C, C++, Assembly

## Common consequences
- **Integrity, Confidentiality, Availability**: Modify Memory, Execute Unauthorized Code or Commands
- **Availability**: Modify Memory, DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU)

## Potential mitigations
- **Requirements**: Use a language that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, many languages that perform their own memory management, such as Java and Perl, are not subject to buffer overflows. Other languages, such as Ada and C#, typically provide overflow protection, but the protection can be disabled by the programmer. Be wary that a language's interface to native code may still be subject to overflows, even if the language itself is theoretically safe.
- **Architecture and Design**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. Examples include the Safe C String Library (SafeStr) by Messier and Viega [REF-57], and the Strsafe.h library from Microsoft [REF-56]. These libraries provide safer versions of overflow-prone string-handling functions.
- **Operation, Build and Compilation**: Use automatic buffer overflow detection mechanisms that are offered by certain compilers or compiler extensions. Examples include: the Microsoft Visual Studio /GS flag, Fedora/Red Hat FORTIFY_SOURCE GCC flag, StackGuard, and ProPolice, which provide various mechanisms including canary-based detection and range/index checking. D3-SFCV (Stack Frame Canary Validation) from D3FEND [REF-1334] discusses canary-based detection in detail.
- **Implementation**: Consider adhering to the following rules when allocating and managing an application's memory: Double check that your buffer is as large as you specify. When using functions that accept a number of bytes to copy, such as strncpy(), be aware that if the destination buffer size is equal to the source buffer size, it may not NULL-terminate the string. Check buffer boundaries if accessing the buffer in a loop and make sure there is no danger of writing past the allocated space. If necessary, truncate all input strings to a reasonable length before passing them to the copy and concatenation functions.
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright.
- **Architecture and Design**: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server.
- **Operation, Build and Compilation**: Run or compile the software using features or extensions that randomly arrange the positions of a program's executable and libraries in memory. Because this makes the addresses unpredictable, it can prevent an attacker from reliably jumping to exploitable code. Examples include Address Space Layout Randomization (ASLR) [REF-58] [REF-60] and Position-Independent Executables (PIE) [REF-64]. Imported modules may be similarly realigned if their default memory addresses conflict with other modules, in a process known as "rebasing" (for Windows) and "prelinking" (for Linux) [REF-1332] using randomly generated addresses. ASLR for libraries cannot be used in conjunction with prelink since it would require relocating the libraries at run-time, defeating the whole purpose of prelinking. For more information on these techniques see D3-SAOR (Segment Address Offset Randomization) from D3FEND [REF-1335].
- **Operation**: Use a CPU and operating system that offers Data Execution Protection (using hardware NX or XD bits) or the equivalent techniques that simulate this feature in software, such as PaX [REF-60] [REF-61]. These techniques ensure that any instruction executed is exclusively at a memory address that is part of the code segment. For more information on these techniques see D3-PSEP (Process Segment Execution Prevention) from D3FEND [REF-1336].
- **Build and Compilation, Operation**: Most mitigating technologies at the compiler or OS level to date address only a subset of buffer overflow problems and rarely provide complete protection against even that subset. It is good practice to implement strategies to increase the workload of an attacker, such as leaving the attacker to guess an unknown value that changes every program execution.
- **Implementation**: Replace unbounded copy functions with analogous functions that support length arguments, such as strcpy with strncpy. Create these if they are not available.
- **Architecture and Design**: When the set of acceptable objects, such as filenames or URLs, is limited or known, create a mapping from a set of fixed input values (such as numeric IDs) to the actual filenames or URLs, and reject all other inputs.
- **Architecture and Design, Operation**: Run your code using the lowest privileges that are required to accomplish the necessary tasks [REF-76]. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations.
- **Architecture and Design, Operation**: Run the code in a "jail" or similar sandbox environment that enforces strict boundaries between the process and the operating system. This may effectively restrict which files can be accessed in a particular directory or which commands can be executed by the software. OS-level examples include the Unix chroot jail, AppArmor, and SELinux. In general, managed code may provide some protection. For example, java.io.FilePermission in the Java SecurityManager allows the software to specify restrictions on file operations. This may not be a feasible solution, and it only limits the impact to the operating system; the rest of the application may still be subject to compromise. Be careful to avoid CWE-243 and other weaknesses related to jails.

## Related attack patterns (CAPEC)
- [CAPEC-10](https://capec.mitre.org/data/definitions/10.html)
- [CAPEC-100](https://capec.mitre.org/data/definitions/100.html)
- [CAPEC-14](https://capec.mitre.org/data/definitions/14.html)
- [CAPEC-24](https://capec.mitre.org/data/definitions/24.html)
- [CAPEC-42](https://capec.mitre.org/data/definitions/42.html)
- [CAPEC-44](https://capec.mitre.org/data/definitions/44.html)
- [CAPEC-45](https://capec.mitre.org/data/definitions/45.html)
- [CAPEC-46](https://capec.mitre.org/data/definitions/46.html)
- [CAPEC-47](https://capec.mitre.org/data/definitions/47.html)
- [CAPEC-67](https://capec.mitre.org/data/definitions/67.html)
- [CAPEC-8](https://capec.mitre.org/data/definitions/8.html)
- [CAPEC-9](https://capec.mitre.org/data/definitions/9.html)
- [CAPEC-92](https://capec.mitre.org/data/definitions/92.html)

## Related weaknesses
- CWE-787 (ChildOf)
- CWE-119 (ChildOf)
- CWE-787 (ChildOf)
- CWE-787 (ChildOf)
- CWE-123 (CanPrecede)
- CWE-20 (ChildOf)

## Observed examples (CVE)
- **CVE-2000-1094**: buffer overflow using command with long argument
- **CVE-1999-0046**: buffer overflow in local program using long environment variable
- **CVE-2002-1337**: buffer overflow in comment characters, when product increments a counter for a ">" but does not decrement for "<"
- **CVE-2003-0595**: By replacing a valid cookie value with an extremely long string of characters, an attacker may overflow the application's buffers.
- **CVE-2001-0191**: By replacing a valid cookie value with an extremely long string of characters, an attacker may overflow the application's buffers.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/120.html
