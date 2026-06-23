---
capec_id: CAPEC-45
name: Buffer Overflow via Symbolic Links
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-120, CWE-285, CWE-302, CWE-118, CWE-119, CWE-74, CWE-20, CWE-680, CWE-697]
related_attack: []
url: https://capec.mitre.org/data/definitions/45.html
tags: [mitre-capec, attack-pattern, CAPEC-45]
---

# CAPEC-45 - Buffer Overflow via Symbolic Links

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-45](https://capec.mitre.org/data/definitions/45.html)

## Description
This type of attack leverages the use of symbolic links to cause buffer overflows. An adversary can try to create or manipulate a symbolic link file such that its contents result in out of bounds data. When the target software processes the symbolic link file, it could potentially overflow internal buffers with insufficient bounds checking.

## Prerequisites
- The adversary can create symbolic link on the target host.
- The target host does not perform correct boundary checking while consuming data from a resources.

## Skills required
- **High**: Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.
- **Low**: An adversary can simply overflow a buffer by inserting a long string into an adversary-modifiable injection vector. The result can be a DoS.

## Consequences
- **Availability**: Unreliable Execution, Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Read Data
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code), Modify Data

## Execution flow
Execution Flow Explore Identify target application: The adversary identifies a target application or program that might load in certain files to memory. Experiment Find injection vector: The adversary identifies an injection vector to deliver the excessive content to the targeted application's buffer. Techniques The adversary creates or modifies a symbolic link pointing to those files which contain an excessive amount of data. If creating a symbolic link to one of those files causes different behavior in the application, then an injection vector has been identified. Craft overflow file content: The adversary crafts the content to be injected. If the intent is to simply cause the software to crash, the content need only consist of an excessive quantity of random data. If the intent is to leverage the overflow for execution of arbitrary code, the adversary crafts the payload in such a way that the overwritten return address is replaced with one of the adversary's choosing. Techniques Create malicious shellcode that will execute when the program execution is returned to it. Use a NOP-sled in the overflow content to more easily "slide" into the malicious code. This is done so that the exact return address need not be correct, only in the range of all of the NOPs Exploit Overflow the buffer: Using the specially crafted file content, the adversary creates a symbolic link from the identified resource to the malicious file, causing a targeted buffer overflow attack.

## Mitigations
- Pay attention to the fact that the resource you read from can be a replaced by a Symbolic link. You can do a Symlink check before reading the file and decide that this is not a legitimate way of accessing the resource.
- Because Symlink can be modified by an adversary, make sure that the ones you read are located in protected directories.
- Pay attention to the resource pointed to by your symlink links (See attack pattern named "Forced Symlink race"), they can be replaced by malicious resources.
- Always check the size of the input data before copying to a buffer.
- Use a language or compiler that performs automatic bounds checking.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Use OS-level preventative functionality. Not a complete solution.

## Related weaknesses (CWE)
- [CWE-120](https://cwe.mitre.org/data/definitions/120.html)
- [CWE-285](https://cwe.mitre.org/data/definitions/285.html)
- [CWE-302](https://cwe.mitre.org/data/definitions/302.html)
- [CWE-118](https://cwe.mitre.org/data/definitions/118.html)
- [CWE-119](https://cwe.mitre.org/data/definitions/119.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-680](https://cwe.mitre.org/data/definitions/680.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/45.html
