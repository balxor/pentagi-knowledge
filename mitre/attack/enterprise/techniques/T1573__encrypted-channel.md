---
attack_id: T1573
name: Encrypted Channel
type: technique
parent: null
tactics: [Command and Control]
platforms: [ESXi, Linux, macOS, Network Devices, Windows]
url: https://attack.mitre.org/techniques/T1573
tags: [mitre-attack, technique, T1573]
---

# T1573 - Encrypted Channel

**Tactic(s):** Command and Control  -  **Platforms:** ESXi, Linux, macOS, Network Devices, Windows  -  **ATT&CK:** [T1573](https://attack.mitre.org/techniques/T1573)

## Summary
Adversaries may employ an encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Despite the use of a secure algorithm, these implementations may be vulnerable to reverse engineering if secret keys are encoded and/or generated within malware samples/configuration files.

## Role in the attack flow
Used to achieve the **Command and Control** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: ESXi, Linux, macOS, Network Devices, Windows.

## Mitigations
- **M1031 Network Intrusion Prevention** - Use intrusion detection signatures to block traffic at network boundaries.
- **M1020 SSL/TLS Inspection** - SSL/TLS inspection involves decrypting encrypted network traffic to examine its content for signs of malicious activity. This capability is crucial for detecting threats that use encryption to evade detection, such as phishing, malware, or data exfiltration. After inspection, the traffic is re-encrypted and forwarded to its destination. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1573
