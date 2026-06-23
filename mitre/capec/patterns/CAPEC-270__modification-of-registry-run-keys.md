---
capec_id: CAPEC-270
name: Modification of Registry Run Keys
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Medium
related_cwe: [CWE-15]
related_attack: [T1547.001, T1547.014]
url: https://capec.mitre.org/data/definitions/270.html
tags: [mitre-capec, attack-pattern, CAPEC-270]
---

# CAPEC-270 - Modification of Registry Run Keys

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-270](https://capec.mitre.org/data/definitions/270.html)

## Description
An adversary adds a new entry to the "run keys" in the Windows registry so that an application of their choosing is executed when a user logs in. In this way, the adversary can get their executable to operate and run on the target system with the authorized user's level of permissions. This attack is a good way for an adversary to run persistent spyware on a user's machine, such as a keylogger.

## Prerequisites
- The adversary must have gained access to the target system via physical or logical means in order to carry out this attack.

## Consequences
- **Integrity**: Modify Data, Gain Privileges

## Execution flow
Execution Flow Explore Determine target system: The adversary must first determine the system they wish to target. This attack only works on Windows. Experiment Gain access to the system: The adversary needs to gain access to the system in some way so that they can modify the Windows registry. Techniques Gain physical access to a system either through shoulder surfing a password or accessing a system that is left unlocked. Gain remote access to a system through a variety of means. Exploit Modify Windows registry: The adversary will modify the Windows registry by adding a new entry to the "run keys" referencing a desired program. This program will be run whenever the user logs in.

## Mitigations
- Identify programs that may be used to acquire process information and block them by using a software restriction policy or tools that restrict program execution by using a process allowlist.

## Related weaknesses (CWE)
- [CWE-15](https://cwe.mitre.org/data/definitions/15.html)

## Related ATT&CK techniques
- T1547.001
- T1547.014

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/270.html
