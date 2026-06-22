---
attack_id: T0893
name: Data from Local System
type: technique
parent: null
tactics: [Collection]
platforms: [None]
url: https://attack.mitre.org/techniques/T0893
tags: [mitre-attack, technique, T0893]
---

# T0893 - Data from Local System

**Tactic(s):** Collection  -  **Platforms:** None  -  **ATT&CK:** [T0893](https://attack.mitre.org/techniques/T0893)

## Summary
Adversaries may target and collect data from local system sources, such as file systems, configuration files, or local databases. This can include sensitive data such as specifications, schematics, or diagrams of control system layouts, devices, and processes.

Adversaries may do this using [Command-Line Interface](https://attack.mitre.org/techniques/T0807) or [Scripting](https://attack.mitre.org/techniques/T0853) techniques to interact with the file system to gather information. Adversaries may also use [Automated Collection](https://attack.mitre.org/techniques/T0802) on the local system.

## Role in the attack flow
Used to achieve the **Collection** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0941 Encrypt Sensitive Information** - Protect sensitive data-at-rest with strong encryption.
- **M0803 Data Loss Prevention** - Data Loss Prevention (DLP) technologies can be used to help identify adversarial attempts to exfiltrate operational information, such as engineering plans, trade secrets, recipes, intellectual property, or process telemetry. DLP functionality may be built into other security products such as firewalls or standalone suites running on the network and host-based agents. DLP may be configured to prevent the transfer of information through corporate resources such as email, web, and physical media such as USB for host-based solutions.
- **M0922 Restrict File and Directory Permissions** - Restrict access by setting directory and file permissions that are not specific to users or privileged accounts.
- **M0917 User Training** - Train users to be aware of access or manipulation attempts by an adversary to reduce the risk of successful spearphishing, social engineering, and other techniques that involve user interaction.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0893
