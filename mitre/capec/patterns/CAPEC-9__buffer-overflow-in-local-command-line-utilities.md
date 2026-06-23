---
capec_id: CAPEC-9
name: Buffer Overflow in Local Command-Line Utilities
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-120, CWE-118, CWE-119, CWE-74, CWE-20, CWE-680, CWE-733, CWE-697]
related_attack: []
url: https://capec.mitre.org/data/definitions/9.html
tags: [mitre-capec, attack-pattern, CAPEC-9]
---

# CAPEC-9 - Buffer Overflow in Local Command-Line Utilities

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-9](https://capec.mitre.org/data/definitions/9.html)

## Description
This attack targets command-line utilities available in a number of shells. An adversary can leverage a vulnerability found in a command-line utility to escalate privilege to root.

## Prerequisites
- The target host exposes a command-line utility to the user.
- The command-line utility exposed by the target host has a buffer overflow vulnerability that can be exploited.

## Skills required
- **High**: Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.
- **Low**: An adversary can simply overflow a buffer by inserting a long string into an adversary-modifiable injection vector. The result can be a DoS.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code), Unreliable Execution
- **Confidentiality**: Gain Privileges, Execute Unauthorized Commands (Run Arbitrary Code), Read Data
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code), Modify Data

## Execution flow
Execution Flow Explore Identify target system: The adversary first finds a target system that they want to gain elevated priveleges on. This could be a system they already have some level of access to or a system that they will gain unauthorized access at a lower privelege using some other means. Find injection vector: The adversary identifies command line utilities exposed by the target host that contain buffer overflow vulnerabilites. The adversary likely knows which utilities have these vulnerabilities and what the effected versions are, so they will also obtain version numbers for these utilities. Experiment Craft overflow command: Once the adversary has found a vulnerable utility, they will use their knownledge of the vulnerabilty to create the command that will exploit the buffer overflow. Exploit Overflow the buffer: Using the injection vector, the adversary executes the crafted command, gaining elevated priveleges on the machine.

## Mitigations
- Carefully review the service's implementation before making it available to user. For instance you can use manual or automated code review to uncover vulnerabilities such as buffer overflow.
- Use a language or compiler that performs automatic bounds checking.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Operational: Use OS-level preventative functionality. Not a complete solution.
- Apply the latest patches to your user exposed services. This may not be a complete solution, especially against a zero day attack.
- Do not unnecessarily expose services.

## Related weaknesses (CWE)
- [CWE-120](https://cwe.mitre.org/data/definitions/120.html)
- [CWE-118](https://cwe.mitre.org/data/definitions/118.html)
- [CWE-119](https://cwe.mitre.org/data/definitions/119.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-680](https://cwe.mitre.org/data/definitions/680.html)
- [CWE-733](https://cwe.mitre.org/data/definitions/733.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/9.html
