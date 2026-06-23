---
cwe_id: CWE-129
name: Improper Validation of Array Index
type: weakness
abstraction: Variant
status: Draft
languages: [C, C++, Not Language-Specific]
related_capec: [CAPEC-100]
url: https://cwe.mitre.org/data/definitions/129.html
tags: [mitre-cwe, weakness, CWE-129]
---

# CWE-129 - Improper Validation of Array Index

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-129](https://cwe.mitre.org/data/definitions/129.html)

## Description
The product uses untrusted input when calculating or using an array index, but the product does not validate or incorrectly validates the index to ensure the index references a valid position within the array.

## Applicable platforms / languages
C, C++, Not Language-Specific

## Common consequences
- **Integrity, Availability**: DoS: Crash, Exit, or Restart
- **Integrity**: Modify Memory
- **Confidentiality, Integrity**: Modify Memory, Read Memory
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands
- **Integrity, Availability, Confidentiality**: DoS: Crash, Exit, or Restart, Execute Unauthorized Code or Commands, Read Memory, Modify Memory

## Potential mitigations
- **Architecture and Design**: Use an input validation framework such as Struts or the OWASP ESAPI Validation API. Note that using a framework does not automatically address all input validation problems; be mindful of weaknesses that could arise from misusing the framework itself (CWE-1173).
- **Architecture and Design**: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side, in order to avoid CWE-602. Attackers can bypass the client-side checks by modifying values after the checks have been performed, or by changing the client to remove the client-side checks entirely. Then, these modified values would be submitted to the server. Even though client-side checks provide minimal benefits with respect to server-side security, they are still useful. First, they can support intrusion detection. If the server receives input that should have been rejected by the client, then it may be an indication of an attack. Second, client-side error-checking can provide helpful feedback to the user about the expectations for valid input. Third, there may be a reduction in server-side processing time for accidental input errors, although this is typically a small savings.
- **Requirements**: Use a language that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, Ada allows the programmer to constrain the values of a variable and languages such as Java and Ruby will allow the programmer to handle exceptions when an out-of-bounds index is accessed.
- **Operation, Build and Compilation**: Run or compile the software using features or extensions that randomly arrange the positions of a program's executable and libraries in memory. Because this makes the addresses unpredictable, it can prevent an attacker from reliably jumping to exploitable code. Examples include Address Space Layout Randomization (ASLR) [REF-58] [REF-60] and Position-Independent Executables (PIE) [REF-64]. Imported modules may be similarly realigned if their default memory addresses conflict with other modules, in a process known as "rebasing" (for Windows) and "prelinking" (for Linux) [REF-1332] using randomly generated addresses. ASLR for libraries cannot be used in conjunction with prelink since it would require relocating the libraries at run-time, defeating the whole purpose of prelinking. For more information on these techniques see D3-SAOR (Segment Address Offset Randomization) from D3FEND [REF-1335].
- **Operation**: Use a CPU and operating system that offers Data Execution Protection (using hardware NX or XD bits) or the equivalent techniques that simulate this feature in software, such as PaX [REF-60] [REF-61]. These techniques ensure that any instruction executed is exclusively at a memory address that is part of the code segment. For more information on these techniques see D3-PSEP (Process Segment Execution Prevention) from D3FEND [REF-1336].
- **Implementation**: Assume all input is malicious. Use an "accept known good" input validation strategy, i.e., use a list of acceptable inputs that strictly conform to specifications. Reject any input that does not strictly conform to specifications, or transform it into something that does. When performing input validation, consider all potentially relevant properties, including length, type of input, the full range of acceptable values, missing or extra inputs, syntax, consistency across related fields, and conformance to business rules. As an example of business rule logic, "boat" may be syntactically valid because it only contains alphanumeric characters, but it is not valid if the input is only expected to contain colors such as "red" or "blue." Do not rely exclusively on looking for malicious or malformed inputs. This is likely to miss at least one undesirable input, especially if the code's environment changes. This can give attackers enough room to bypass the intended validation. However, denylists can be useful for detecting potential attacks or determining which inputs are so malformed that they should be rejected outright. When accessing a user-controlled array index, use a stringent range of values that are within the target array. Make sure that you do not allow negative values to be used. That is, verify the minimum as well as the maximum of the range of acceptable values.
- **Implementation**: Be especially careful to validate all input when invoking code that crosses language boundaries, such as from an interpreted language to native code. This could create an unexpected interaction between the language boundaries. Ensure that you are not violating any of the expectations of the language with which you are interfacing. For example, even though Java may not be susceptible to buffer overflows, providing a large argument in a call to native code might trigger an overflow.
- **Architecture and Design, Operation**: Run your code using the lowest privileges that are required to accomplish the necessary tasks [REF-76]. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations.
- **Architecture and Design, Operation**: Run the code in a "jail" or similar sandbox environment that enforces strict boundaries between the process and the operating system. This may effectively restrict which files can be accessed in a particular directory or which commands can be executed by the software. OS-level examples include the Unix chroot jail, AppArmor, and SELinux. In general, managed code may provide some protection. For example, java.io.FilePermission in the Java SecurityManager allows the software to specify restrictions on file operations. This may not be a feasible solution, and it only limits the impact to the operating system; the rest of the application may still be subject to compromise. Be careful to avoid CWE-243 and other weaknesses related to jails.

## Related attack patterns (CAPEC)
- [CAPEC-100](https://capec.mitre.org/data/definitions/100.html)

## Related weaknesses
- CWE-1285 (ChildOf)
- CWE-20 (ChildOf)
- CWE-119 (CanPrecede)
- CWE-823 (CanPrecede)
- CWE-789 (CanPrecede)

## Observed examples (CVE)
- **CVE-2005-0369**: large ID in packet used as array index
- **CVE-2001-1009**: negative array index as argument to POP LIST command
- **CVE-2003-0721**: Integer signedness error leads to negative array index
- **CVE-2004-1189**: product does not properly track a count and a maximum number, which can lead to resultant array index overflow.
- **CVE-2007-5756**: Chain: device driver for packet-capturing software allows access to an unintended IOCTL with resultant array index error.
- **CVE-2005-2456**: Chain: array index error (CWE-129) leads to deadlock (CWE-833)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/129.html
