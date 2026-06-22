---
attack_id: T1027
name: Obfuscated Files or Information
type: technique
parent: null
tactics: [Stealth]
platforms: [ESXi, Linux, macOS, Network Devices, Windows]
url: https://attack.mitre.org/techniques/T1027
tags: [mitre-attack, technique, T1027]
---

# T1027 - Obfuscated Files or Information

**Tactic(s):** Stealth  -  **Platforms:** ESXi, Linux, macOS, Network Devices, Windows  -  **ATT&CK:** [T1027](https://attack.mitre.org/techniques/T1027)

## Summary
Adversaries may attempt to make an executable or file difficult to discover or analyze by encrypting, encoding, or otherwise obfuscating its contents on the system or in transit. This is common behavior that can be used across different platforms and the network to evade defenses. 

Payloads may be compressed, archived, or encrypted in order to avoid detection. These payloads may be used during Initial Access or later to mitigate detection. Sometimes a user's action may be required to open and [Deobfuscate/Decode Files or Information](https://attack.mitre.org/techniques/T1140) for [User Execution](https://attack.mitre.org/techniques/T1204). The user may also be required to input a password to open a password protected compressed/encrypted file that was provided by the adversary.(Citation: Volexity PowerDuke November 2016) Adversaries may also use compressed or archived scripts, such as JavaScript. 

Portions of files can also be encoded to hide the plain-text strings that would otherwise help defenders with discovery.(Citation: Linux/Cdorked.A We Live Security Analysis) Payloads may also be split into separate, seemingly benign files that only reveal malicious functionality when reassembled.(Citation: Carbon Black Obfuscation Sept 2016)

Adversaries may also abuse [Command Obfuscation](https://attack.mitre.org/techniques/T1027/010) to obscure commands executed from payloads or directly via [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059). Environment variables, aliases, characters, and other platform/language specific semantics can be used to evade signature based detections and application control mechanisms.(Citation: FireEye Obfuscation June 2017)(Citation: FireEye Revoke-Obfuscation July 2017)(Citation: PaloAlto EncodedCommand March 2017)

## Role in the attack flow
Used to achieve the **Stealth** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: ESXi, Linux, macOS, Network Devices, Windows.

## Mitigations
- **M1047 Audit** - Auditing is the process of recording activity and systematically reviewing and analyzing the activity and system configurations. The primary purpose of auditing is to detect anomalies and identify potential threats or weaknesses in the environment. Proper auditing configurations can also help to meet compliance requirements. The process of auditing encompasses regular analysis of user behaviors and system logs in support of proactive security measures.
- **M1040 Behavior Prevention on Endpoint** - Behavior Prevention on Endpoint refers to the use of technologies and strategies to detect and block potentially malicious activities by analyzing the behavior of processes, files, API calls, and other endpoint events. Rather than relying solely on known signatures, this approach leverages heuristics, machine learning, and real-time monitoring to identify anomalous patterns indicative of an attack. This mitigation can be implemented through the following measures:
- **M1017 User Training** - User Training involves educating employees and contractors on recognizing, reporting, and preventing cyber threats that rely on human interaction, such as phishing, social engineering, and other manipulative techniques. Comprehensive training programs create a human firewall by empowering users to be an active component of the organization's cybersecurity defenses. This mitigation can be implemented through the following measures:
- **M1049 Antivirus/Antimalware** - Antivirus/Antimalware solutions utilize signatures, heuristics, and behavioral analysis to detect, block, and remediate malicious software, including viruses, trojans, ransomware, and spyware. These solutions continuously monitor endpoints and systems for known malicious patterns and suspicious behaviors that indicate compromise. Antivirus/Antimalware software should be deployed across all devices, with automated updates to ensure protection against the latest threats. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1027
