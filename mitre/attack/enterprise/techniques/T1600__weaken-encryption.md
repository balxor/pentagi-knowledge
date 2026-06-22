---
attack_id: T1600
name: Weaken Encryption
type: technique
parent: null
tactics: [Defense Impairment]
platforms: [Network Devices]
url: https://attack.mitre.org/techniques/T1600
tags: [mitre-attack, technique, T1600]
---

# T1600 - Weaken Encryption

**Tactic(s):** Defense Impairment  -  **Platforms:** Network Devices  -  **ATT&CK:** [T1600](https://attack.mitre.org/techniques/T1600)

## Summary
Adversaries may compromise a network device’s encryption capability in order to bypass encryption that would otherwise protect data communications.(Citation: Cisco Synful Knock Evolution)

Encryption can be used to protect transmitted network traffic to maintain its confidentiality (protect against unauthorized disclosure) and integrity (protect against unauthorized changes). Encryption ciphers are used to convert a plaintext message to ciphertext and can be computationally intensive to decipher without the associated decryption key. Typically, longer keys increase the cost of cryptanalysis, or decryption without the key.

Adversaries can compromise and manipulate devices that perform encryption of network traffic. For example, through behaviors such as [Modify System Image](https://attack.mitre.org/techniques/T1601), [Reduce Key Space](https://attack.mitre.org/techniques/T1600/001), and [Disable Crypto Hardware](https://attack.mitre.org/techniques/T1600/002), an adversary can negatively effect and/or eliminate a device’s ability to securely encrypt network traffic. This poses a greater risk of unauthorized disclosure and may help facilitate data manipulation, Credential Access, or Collection efforts.(Citation: Cisco Blog Legacy Device Attacks)

## Role in the attack flow
Used to achieve the **Defense Impairment** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Network Devices.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1600
