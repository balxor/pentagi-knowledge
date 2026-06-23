---
capec_id: CAPEC-647
name: Collect Data from Registries
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Medium
related_cwe: [CWE-285]
related_attack: [T1005, T1012, T1552.002]
url: https://capec.mitre.org/data/definitions/647.html
tags: [mitre-capec, attack-pattern, CAPEC-647]
---

# CAPEC-647 - Collect Data from Registries

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-647](https://capec.mitre.org/data/definitions/647.html)

## Description
An adversary exploits a weakness in authorization to gather system-specific data and sensitive information within a registry (e.g., Windows Registry, Mac plist). These contain information about the system configuration, software, operating system, and security. The adversary can leverage information gathered in order to carry out further attacks.

## Prerequisites
- The adversary must have obtained logical access to the system by some means (e.g., via obtained credentials or planting malware on the system).
- The adversary must have capability to navigate the operating system to peruse the registry.

## Skills required
- **Low**: Once the adversary has logical access (which can potentially require high knowledge and skill level), the adversary needs only the capability and facility to navigate the system through the OS graphical user interface or the command line.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Confidentiality**: Read Data (The adversary is able to read sensitive information about the system in the registry.)

## Execution flow
Execution Flow Explore Gain logical access to system: An adversary must first gain logical access to the system it wants to gather registry information from, Techniques Obtain user account credentials and access the system Plant malware on the system that will give remote logical access to the adversary Experiment Determine if the permissions are correct: Once logical access is gained, an adversary will determine if they have the proper permissions, or are authorized, to view registry information. If they do not, they will need to escalate privileges on the system through other means Peruse registry for information: Once an adversary has access to a registry, they will gather all system-specific data and sensitive information that they deem useful. Exploit Follow-up attack: Use any information or weaknesses found to carry out a follow-up attack

## Mitigations
- Employ a robust and layered defensive posture in order to prevent unauthorized users on your system.
- Employ robust identification and audit/blocking via using an allowlist of applications on your system. Unnecessary applications, utilities, and configurations will have a presence in the system registry that can be leveraged by an adversary through this attack pattern.

## Related weaknesses (CWE)
- [CWE-285](https://cwe.mitre.org/data/definitions/285.html)

## Related ATT&CK techniques
- T1005
- T1012
- T1552.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/647.html
