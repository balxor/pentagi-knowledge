---
capec_id: CAPEC-478
name: Modification of Windows Service Configuration
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: [CWE-284]
related_attack: [T1574.011, T1543.003]
url: https://capec.mitre.org/data/definitions/478.html
tags: [mitre-capec, attack-pattern, CAPEC-478]
---

# CAPEC-478 - Modification of Windows Service Configuration

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-478](https://capec.mitre.org/data/definitions/478.html)

## Description
An adversary exploits a weakness in access control to modify the execution parameters of a Windows service. The goal of this attack is to execute a malicious binary in place of an existing service.

## Prerequisites
- The adversary must have the capability to write to the Windows Registry on the targeted system.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Integrity**: Execute Unauthorized Commands (By altering specific configuration settings for the service, the adversary could run arbitrary code to be executed.)

## Execution flow
Execution Flow Explore Determine target system: The adversary must first determine the system they wish to modify the registry of. This needs to be a windows machine as this attack only works on the windows registry. Experiment Gain access to the system: The adversary needs to gain access to the system in some way so that they can modify the windows registry. Techniques Gain physical access to a system either through shoulder surfing a password or accessing a system that is left unlocked. Gain remote access to a system through a variety of means. Exploit Modify windows registry: The adversary will modify the windows registry by changing the configuration settings for a service. Specifically, the adversary will change the path settings to define a path to a malicious binary to be executed.

## Mitigations
- Ensure proper permissions are set for Registry hives to prevent users from modifying keys for system components that may lead to privilege escalation.

## Related weaknesses (CWE)
- [CWE-284](https://cwe.mitre.org/data/definitions/284.html)

## Related ATT&CK techniques
- T1574.011
- T1543.003

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/478.html
