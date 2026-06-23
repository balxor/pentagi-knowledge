---
capec_id: CAPEC-47
name: Buffer Overflow via Parameter Expansion
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-120, CWE-119, CWE-118, CWE-130, CWE-131, CWE-74, CWE-20, CWE-680, CWE-697]
related_attack: []
url: https://capec.mitre.org/data/definitions/47.html
tags: [mitre-capec, attack-pattern, CAPEC-47]
---

# CAPEC-47 - Buffer Overflow via Parameter Expansion

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-47](https://capec.mitre.org/data/definitions/47.html)

## Description
In this attack, the target software is given input that the adversary knows will be modified and expanded in size during processing. This attack relies on the target software failing to anticipate that the expanded data may exceed some internal limit, thereby creating a buffer overflow.

## Prerequisites
- The program expands one of the parameters passed to a function with input controlled by the user, but a later function making use of the expanded parameter erroneously considers the original, not the expanded size of the parameter.
- The expanded parameter is used in the context where buffer overflow may become possible due to the incorrect understanding of the parameter size (i.e. thinking that it is smaller than it really is).

## Skills required
- **High**: Finding this particular buffer overflow may not be trivial. Also, stack and especially heap based buffer overflows require a lot of knowledge if the intended goal is arbitrary code execution. Not only that the adversary needs to write the shell code to accomplish their goals, but the adversary also needs to find a way to get the program execution to jump to the planted shell code. There also needs to be sufficient room for the payload. So not every buffer overflow will be exploitable, even by a skilled adversary.

## Resources required
- Access to the program source or binary. If the program is only available in binary then a disassembler and other reverse engineering tools will be helpful.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Unreliable Execution, Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Gain Privileges, Execute Unauthorized Commands (Run Arbitrary Code), Read Data
- **Integrity**: Modify Data, Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Identify target application: The adversary identifies a target application or program to perform the buffer overflow on. Adversaries often look for applications that accept user input and that perform manual memory management. Experiment Find injection vector: The adversary identifies an injection vector to deliver the excessive content to the targeted application's buffer. Techniques In this attack, the normal method of providing large user input does not work. The program performs bounds checking on the user input, but not the expanded user input. The adversary needs to provide input that they believe will be expanded by the program to overflow a buffer. To identify where this is possible, an adversary either needs to have knowledge of the inner workings of the program or use a disassembler and other reverse engineering tools to guide the search. Craft overflow content: The adversary crafts the input to be given to the program. If the intent is to simply cause the software to crash, the input needs only to expand to an excessive quantity of random data. If the intent is to leverage the overflow for execution of arbitrary code, the adversary will craft input that expands in a way that not only overflows the targeted buffer but does so in such a way that the overwritten return address is replaced with one of the adversaries' choosing which points to code injected by the adversary. Techniques Create specific files and directories on the system and then give input using path traversal shortcuts to those directories that could expand past an input buffer. Exploit Overflow the buffer: Using the injection vector, the adversary gives the crafted input to the program, overflowing the buffer.

## Mitigations
- Ensure that when parameter expansion happens in the code that the assumptions used to determine the resulting size of the parameter are accurate and that the new size of the parameter is visible to the whole system

## Related weaknesses (CWE)
- [CWE-120](https://cwe.mitre.org/data/definitions/120.html)
- [CWE-119](https://cwe.mitre.org/data/definitions/119.html)
- [CWE-118](https://cwe.mitre.org/data/definitions/118.html)
- [CWE-130](https://cwe.mitre.org/data/definitions/130.html)
- [CWE-131](https://cwe.mitre.org/data/definitions/131.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-680](https://cwe.mitre.org/data/definitions/680.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/47.html
