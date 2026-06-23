---
capec_id: CAPEC-10
name: Buffer Overflow via Environment Variables
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-120, CWE-302, CWE-118, CWE-119, CWE-74, CWE-99, CWE-20, CWE-680, CWE-733, CWE-697]
related_attack: []
url: https://capec.mitre.org/data/definitions/10.html
tags: [mitre-capec, attack-pattern, CAPEC-10]
---

# CAPEC-10 - Buffer Overflow via Environment Variables

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-10](https://capec.mitre.org/data/definitions/10.html)

## Description
This attack pattern involves causing a buffer overflow through manipulation of environment variables. Once the adversary finds that they can modify an environment variable, they may try to overflow associated buffers. This attack leverages implicit trust often placed in environment variables.

## Extended description
Although the focus of this attack is putting excessive content into an environment variable that is loaded into a buffer, environment variables can be used to assist a classic buffer overflow attack as well. In the case where the buffer used in a traditional buffer overflow attack is not large enough to store the adversary's shell code, they will store the shell code in an environment variable and attempt to return to its address, rather than back into the data they wrote to the buffer.

## Prerequisites
- The application uses environment variables.
- An environment variable exposed to the user is vulnerable to a buffer overflow.
- The vulnerable environment variable uses untrusted data.
- Tainted data used in the environment variables is not properly validated. For instance boundary checking is not done before copying the input data to a buffer.

## Skills required
- **High**: Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.
- **Low**: An attacker can simply overflow a buffer by inserting a long string into an attacker-modifiable injection vector. The result can be a DoS.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Unreliable Execution, Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Read Data, Gain Privileges
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code), Modify Data

## Execution flow
Execution Flow Explore Identify target application: The adversary identifies a target application or program to perform the buffer overflow on. In this attack the adversary looks for an application that loads the content of an environment variable into a buffer. Experiment Find injection vector: The adversary identifies an injection vector to deliver the excessive content to the targeted application's buffer. Techniques Change the values of environment variables thought to be used by the application to contain excessive data. If the program is loading the value of the environment variable into a buffer, this could cause a crash and an attack vector will be found. Craft overflow content: The adversary crafts the content to be injected. If the intent is to simply cause the software to crash, the content need only consist of an excessive quantity of random data. If the intent is to leverage the overflow for execution of arbitrary code, the adversary crafts the payload in such a way that the overwritten return address is replaced with one of the adversary's choosing. Techniques Create malicious shellcode that will execute when the program execution is returned to it. Use a NOP-sled in the overflow content to more easily "slide" into the malicious code. This is done so that the exact return address need not be correct, only in the range of all of the NOPs Exploit Overflow the buffer: Using the injection vector, the adversary injects the crafted overflow content into the buffer.

## Mitigations
- Do not expose environment variable to the user.
- Do not use untrusted data in your environment variables.
- Use a language or compiler that performs automatic bounds checking
- There are tools such as Sharefuzz [REF-2] which is an environment variable fuzzer for Unix that support loading a shared library. You can use Sharefuzz to determine if you are exposing an environment variable vulnerable to buffer overflow.

## Related weaknesses (CWE)
- [CWE-120](https://cwe.mitre.org/data/definitions/120.html)
- [CWE-302](https://cwe.mitre.org/data/definitions/302.html)
- [CWE-118](https://cwe.mitre.org/data/definitions/118.html)
- [CWE-119](https://cwe.mitre.org/data/definitions/119.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-99](https://cwe.mitre.org/data/definitions/99.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-680](https://cwe.mitre.org/data/definitions/680.html)
- [CWE-733](https://cwe.mitre.org/data/definitions/733.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/10.html
