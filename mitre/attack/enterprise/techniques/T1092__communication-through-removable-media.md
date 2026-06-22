---
attack_id: T1092
name: Communication Through Removable Media
type: technique
parent: null
tactics: [Command and Control]
platforms: [Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1092
tags: [mitre-attack, technique, T1092]
---

# T1092 - Communication Through Removable Media

**Tactic(s):** Command and Control  ·  **Platforms:** Linux, macOS, Windows  ·  **ATT&CK:** [T1092](https://attack.mitre.org/techniques/T1092)

## Summary
Adversaries can perform command and control between compromised hosts on potentially disconnected networks using removable media to transfer commands from system to system.(Citation: ESET Sednit USBStealer 2014) Both systems would need to be compromised, with the likelihood that an Internet-connected system was compromised first and the second through lateral movement by [Replication Through Removable Media](https://attack.mitre.org/techniques/T1091). Commands and files would be relayed from the disconnected system to the Internet-connected system to which the adversary has direct access.

## Role in the attack flow
Used to achieve the **Command and Control** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows.

## Mitigations
- **M1042 Disable or Remove Feature or Program** - Disable or remove unnecessary and potentially vulnerable software, features, or services to reduce the attack surface and prevent abuse by adversaries. This involves identifying software or features that are no longer needed or that could be exploited and ensuring they are either removed or properly disabled. This mitigation can be implemented through the following measures: 
- **M1028 Operating System Configuration** - Operating System Configuration involves adjusting system settings and hardening the default configurations of an operating system (OS) to mitigate adversary exploitation and prevent abuse of system functionality. Proper OS configurations address security vulnerabilities, limit attack surfaces, and ensure robust defense against a wide range of techniques. This mitigation can be implemented through the following measures: 

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1092
