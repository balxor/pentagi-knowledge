---
attack_id: T1406
name: Obfuscated Files or Information
type: technique
parent: null
tactics: [Defense Evasion]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1406
tags: [mitre-attack, technique, T1406]
---

# T1406 - Obfuscated Files or Information

**Tactic(s):** Defense Evasion  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1406](https://attack.mitre.org/techniques/T1406)

## Summary
Adversaries may attempt to make a payload or file difficult to discover or analyze by encrypting, encoding, or otherwise obfuscating its contents on the device or in transit. This is common behavior that can be used across different platforms and the network to evade defenses. 
 
Payloads may be compressed, archived, or encrypted in order to avoid detection. These payloads may be used during Initial Access or later to mitigate detection. Portions of files can also be encoded to hide the plaintext strings that would otherwise help defenders with discovery. Payloads may also be split into separate, seemingly benign files that only reveal malicious functionality when reassembled.(Citation: Microsoft MalLockerB)

## Role in the attack flow
Used to achieve the **Defense Evasion** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1406
