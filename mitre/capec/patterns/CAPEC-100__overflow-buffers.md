---
capec_id: CAPEC-100
name: Overflow Buffers
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Very High
related_cwe: [CWE-120, CWE-119, CWE-131, CWE-129, CWE-805, CWE-680]
related_attack: []
url: https://capec.mitre.org/data/definitions/100.html
tags: [mitre-capec, attack-pattern, CAPEC-100]
---

# CAPEC-100 - Overflow Buffers

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-100](https://capec.mitre.org/data/definitions/100.html)

## Description
Buffer Overflow attacks target improper or missing bounds checking on buffer operations, typically triggered by input injected by an adversary. As a consequence, an adversary is able to write past the boundaries of allocated buffer regions in memory, causing a program crash or potentially redirection of execution as per the adversaries' choice.

## Prerequisites
- Targeted software performs buffer operations.
- Targeted software inadequately performs bounds-checking on buffer operations.
- Adversary has the capability to influence the input to buffer operations.

## Skills required
- **High**: In cases of directed overflows, where the motive is to divert the flow of the program or application as per the adversaries' bidding, high level skills are required. This may involve detailed knowledge of the target system architecture and kernel.
- **Low**: In most cases, overflowing a buffer does not require advanced skills beyond the ability to notice an overflow and stuff an input variable with content.

## Resources required
- None: No specialized resources are required to execute this type of attack. Detecting and exploiting a buffer overflow does not require any resources beyond knowledge of and access to the target system.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Unreliable Execution, Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Identify target application: The adversary identifies a target application or program to perform the buffer overflow on. Adversaries often look for applications that accept user input and that perform manual memory management. Experiment Find injection vector: The adversary identifies an injection vector to deliver the excessive content to the targeted application's buffer. Techniques Provide large input to a program or application and observe the behavior. If there is a crash, this means that a buffer overflow attack is possible. Craft overflow content: The adversary crafts the content to be injected. If the intent is to simply cause the software to crash, the content need only consist of an excessive quantity of random data. If the intent is to leverage the overflow for execution of arbitrary code, the adversary crafts the payload in such a way that the overwritten return address is replaced with one of the adversary's choosing. Techniques Create malicious shellcode that will execute when the program execution is returned to it. Use a NOP-sled in the overflow content to more easily "slide" into the malicious code. This is done so that the exact return address need not be correct, only in the range of all of the NOPs Exploit Overflow the buffer: Using the injection vector, the adversary injects the crafted overflow content into the buffer.

## Mitigations
- Use a language or compiler that performs automatic bounds checking.
- Use secure functions not vulnerable to buffer overflow.
- If you have to use dangerous functions, make sure that you do boundary checking.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Use OS-level preventative functionality. Not a complete solution.
- Utilize static source code analysis tools to identify potential buffer overflow weaknesses in the software.

## Related weaknesses (CWE)
- [CWE-120](https://cwe.mitre.org/data/definitions/120.html)
- [CWE-119](https://cwe.mitre.org/data/definitions/119.html)
- [CWE-131](https://cwe.mitre.org/data/definitions/131.html)
- [CWE-129](https://cwe.mitre.org/data/definitions/129.html)
- [CWE-805](https://cwe.mitre.org/data/definitions/805.html)
- [CWE-680](https://cwe.mitre.org/data/definitions/680.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/100.html
