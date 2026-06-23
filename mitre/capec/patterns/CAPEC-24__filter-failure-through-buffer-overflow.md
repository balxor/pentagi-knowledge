---
capec_id: CAPEC-24
name: Filter Failure through Buffer Overflow
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-120, CWE-119, CWE-118, CWE-74, CWE-20, CWE-680, CWE-733, CWE-697]
related_attack: []
url: https://capec.mitre.org/data/definitions/24.html
tags: [mitre-capec, attack-pattern, CAPEC-24]
---

# CAPEC-24 - Filter Failure through Buffer Overflow

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-24](https://capec.mitre.org/data/definitions/24.html)

## Description
In this attack, the idea is to cause an active filter to fail by causing an oversized transaction. An attacker may try to feed overly long input strings to the program in an attempt to overwhelm the filter (by causing a buffer overflow) and hoping that the filter does not fail securely (i.e. the user input is let into the system unfiltered).

## Prerequisites
- Ability to control the length of data passed to an active filter.

## Skills required
- **High**: Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap can require a higher skill level.
- **Low**: An attacker can simply overflow a buffer by inserting a long string into an attacker-modifiable injection vector. The result can be a DoS.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Authorization**: Bypass Protection Mechanism
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code), Unreliable Execution
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Bypass Protection Mechanism
- **Integrity**: Modify Data, Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Survey: The attacker surveys the target application, possibly as a valid and authenticated user Techniques Spidering web sites for inputs that involve potential filtering Brute force guessing of filtered inputs Experiment Attempt injections: Try to feed overly long data to the system. This can be done manually or a dynamic tool (black box) can be used to automate this. An attacker can also use a custom script for that purpose. Techniques Brute force attack through black box penetration test tool. Fuzzing of communications protocols Manual testing of possible inputs with attack data. Monitor responses: Watch for any indication of failure occurring. Carefully watch to see what happened when filter failure occurred. Did the data get in? Techniques Boron tagging. Choose clear attack inputs that are easy to notice in output. In binary this is often 0xa5a5a5a5 (alternating 1s and 0s). Another obvious tag value is all zeroes, but it is not always obvious what goes wrong if the null values get into the data. Check Log files. An attacker with access to log files can look at the outcome of bad input. Exploit Abuse the system through filter failure: An attacker writes a script to consistently induce the filter failure. Techniques DoS through filter failure. The attacker causes the system to crash or stay down because of its failure to filter properly. Malicious code execution. An attacker introduces a malicious payload and executes arbitrary code on the target system. An attacker can use the filter failure to introduce malicious data into the system and leverage a subsequent SQL injection, Cross Site Scripting, Command Injection or similar weakness if it exists.

## Mitigations
- Make sure that ANY failure occurring in the filtering or input validation routine is properly handled and that offending input is NOT allowed to go through. Basically make sure that the vault is closed when failure occurs.
- Pre-design: Use a language or compiler that performs automatic bounds checking.
- Pre-design through Build: Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Operational: Use OS-level preventative functionality. Not a complete solution.
- Design: Use an abstraction library to abstract away risky APIs. Not a complete solution.

## Related weaknesses (CWE)
- [CWE-120](https://cwe.mitre.org/data/definitions/120.html)
- [CWE-119](https://cwe.mitre.org/data/definitions/119.html)
- [CWE-118](https://cwe.mitre.org/data/definitions/118.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-680](https://cwe.mitre.org/data/definitions/680.html)
- [CWE-733](https://cwe.mitre.org/data/definitions/733.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/24.html
