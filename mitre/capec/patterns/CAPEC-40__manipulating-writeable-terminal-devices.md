---
capec_id: CAPEC-40
name: Manipulating Writeable Terminal Devices
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Very High
related_cwe: [CWE-77]
related_attack: []
url: https://capec.mitre.org/data/definitions/40.html
tags: [mitre-capec, attack-pattern, CAPEC-40]
---

# CAPEC-40 - Manipulating Writeable Terminal Devices

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-40](https://capec.mitre.org/data/definitions/40.html)

## Description
This attack exploits terminal devices that allow themselves to be written to by other users. The attacker sends command strings to the target terminal device hoping that the target user will hit enter and thereby execute the malicious command with their privileges. The attacker can send the results (such as copying /etc/passwd) to a known directory and collect once the attack has succeeded.

## Prerequisites
- User terminals must have a permissive access control such as world writeable that allows normal users to control data on other user's terminals.

## Skills required
- **Low**: Ability to discover permissions on terminal devices. Of course, brute force can also be used.

## Resources required
- Access to a terminal on the target network

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Gain Privileges, Read Data, Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Identify attacker-writable terminals: Determine if users TTYs are writable by the attacker. Techniques Determine the permissions for the TTYs found on the system. Any that allow user write to the TTY may be vulnerable. Attempt to write to other user TTYs. This approach could leave a trail or alert a user. Exploit Execute malicious commands: Using one or more vulnerable TTY, execute commands to achieve various impacts. Techniques Commands that allow reading or writing end user files can be executed.

## Mitigations
- Design: Ensure that terminals are only writeable by named owner user and/or administrator
- Design: Enforce principle of least privilege

## Related weaknesses (CWE)
- [CWE-77](https://cwe.mitre.org/data/definitions/77.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/40.html
