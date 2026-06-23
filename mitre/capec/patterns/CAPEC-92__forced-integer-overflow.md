---
capec_id: CAPEC-92
name: Forced Integer Overflow
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-190, CWE-128, CWE-120, CWE-122, CWE-196, CWE-680, CWE-697]
related_attack: []
url: https://capec.mitre.org/data/definitions/92.html
tags: [mitre-capec, attack-pattern, CAPEC-92]
---

# CAPEC-92 - Forced Integer Overflow

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-92](https://capec.mitre.org/data/definitions/92.html)

## Description
This attack forces an integer variable to go out of range. The integer variable is often used as an offset such as size of memory allocation or similarly. The attacker would typically control the value of such variable and try to get it out of range. For instance the integer in question is incremented past the maximum possible value, it may wrap to become a very small, or negative number, therefore providing a very incorrect value which can lead to unexpected behavior. At worst the attacker can execute arbitrary code.

## Prerequisites
- The attacker can manipulate the value of an integer variable utilized by the target host.
- The target host does not do proper range checking on the variable before utilizing it.
- When the integer variable is incremented or decremented to an out of range value, it gets a very different value (e.g. very small or negative number)

## Skills required
- **High**: Exploiting a buffer overflow by injecting malicious code into the stack of a software system or even the heap can require a higher skill level.
- **Low**: An attacker can simply overflow an integer by inserting an out of range value.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code), Unreliable Execution
- **Confidentiality**: Gain Privileges, Execute Unauthorized Commands (Run Arbitrary Code), Read Data
- **Integrity**: Modify Data, Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore The first step is exploratory meaning the attacker looks for an integer variable that they can control. Experiment The attacker finds an integer variable that they can write into or manipulate and try to get the value of the integer out of the possible range. Exploit The integer variable is forced to have a value out of range which set its final value to an unexpected value. The target host acts on the data and unexpected behavior may happen.

## Mitigations
- Use a language or compiler that performs automatic bounds checking.
- Carefully review the service's implementation before making it available to user. For instance you can use manual or automated code review to uncover vulnerabilities such as integer overflow.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Always do bound checking before consuming user input data.

## Related weaknesses (CWE)
- [CWE-190](https://cwe.mitre.org/data/definitions/190.html)
- [CWE-128](https://cwe.mitre.org/data/definitions/128.html)
- [CWE-120](https://cwe.mitre.org/data/definitions/120.html)
- [CWE-122](https://cwe.mitre.org/data/definitions/122.html)
- [CWE-196](https://cwe.mitre.org/data/definitions/196.html)
- [CWE-680](https://cwe.mitre.org/data/definitions/680.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/92.html
