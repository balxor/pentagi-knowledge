---
attack_id: T1001
name: Data Obfuscation
type: technique
parent: null
tactics: [Command and Control]
platforms: [ESXi, Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1001
tags: [mitre-attack, technique, T1001]
---

# T1001 - Data Obfuscation

**Tactic(s):** Command and Control  ·  **Platforms:** ESXi, Linux, macOS, Windows  ·  **ATT&CK:** [T1001](https://attack.mitre.org/techniques/T1001)

## Summary
Adversaries may obfuscate command and control traffic to make it more difficult to detect.(Citation: Bitdefender FunnyDream Campaign November 2020) Command and control (C2) communications are hidden (but not necessarily encrypted) in an attempt to make the content more difficult to discover or decipher and to make the communication less conspicuous and hide commands from being seen. This encompasses many methods, such as adding junk data to protocol traffic, using steganography, or impersonating legitimate protocols.

## Role in the attack flow
Used to achieve the **Command and Control** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: ESXi, Linux, macOS, Windows.

## Mitigations
- **M1031 Network Intrusion Prevention** - Use intrusion detection signatures to block traffic at network boundaries.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1001
