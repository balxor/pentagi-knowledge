---
capec_id: CAPEC-8
name: Buffer Overflow in an API Call
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-120, CWE-119, CWE-118, CWE-74, CWE-20, CWE-680, CWE-733, CWE-697]
related_attack: []
url: https://capec.mitre.org/data/definitions/8.html
tags: [mitre-capec, attack-pattern, CAPEC-8]
---

# CAPEC-8 - Buffer Overflow in an API Call

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-8](https://capec.mitre.org/data/definitions/8.html)

## Description
This attack targets libraries or shared code modules which are vulnerable to buffer overflow attacks. An adversary who has knowledge of known vulnerable libraries or shared code can easily target software that makes use of these libraries. All clients that make use of the code library thus become vulnerable by association. This has a very broad effect on security across a system, usually affecting more than one software process.

## Prerequisites
- The target host exposes an API to the user.
- One or more API functions exposed by the target host has a buffer overflow vulnerability.

## Skills required
- **High**: Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.
- **Low**: An adversary can simply overflow a buffer by inserting a long string into an adversary-modifiable injection vector. The result can be a DoS.

## Consequences
- **Availability**: Unreliable Execution, Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Read Data
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code), Modify Data

## Execution flow
Execution Flow Explore Identify target application: The adversary, with knowledge of vulnerable libraries or shared code modules, identifies a target application or program that makes use of these. Experiment Find injection vector: The adversary attempts to use the API, and if they can they send a large amount of data to see if the buffer overflow attack really does work. Techniques Provide large input to a program or application and observe the behavior. If there is a crash, this means that a buffer overflow attack is possible. Craft overflow content: The adversary crafts the content to be injected based on their knowledge of the vulnerability and their desired outcome. If the intent is to simply cause the software to crash, the content need only consist of an excessive quantity of random data. If the intent is to leverage the overflow for execution of arbitrary code, the adversary will craft a set of content that not only overflows the targeted buffer but does so in such a way that the overwritten return address is replaced with one of the adversaries' choosing which points to code injected by the adversary. Techniques Create malicious shellcode that will execute when the program execution is returned to it. Use a NOP-sled in the overflow content to more easily "slide" into the malicious code. This is done so that the exact return address need not be correct, only in the range of all of the NOPs Exploit Overflow the buffer: Using the API as the injection vector, the adversary injects the crafted overflow content into the buffer.

## Mitigations
- Use a language or compiler that performs automatic bounds checking.
- Use secure functions not vulnerable to buffer overflow.
- If you have to use dangerous functions, make sure that you do boundary checking.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Use OS-level preventative functionality. Not a complete solution.

## Related weaknesses (CWE)
- [CWE-120](https://cwe.mitre.org/data/definitions/120.html)
- [CWE-119](https://cwe.mitre.org/data/definitions/119.html)
- [CWE-118](https://cwe.mitre.org/data/definitions/118.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-680](https://cwe.mitre.org/data/definitions/680.html)
- [CWE-733](https://cwe.mitre.org/data/definitions/733.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/8.html
