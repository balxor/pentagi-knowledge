---
attack_id: T1634
name: Credentials from Password Store
type: technique
parent: null
tactics: [Credential Access]
platforms: [iOS]
url: https://attack.mitre.org/techniques/T1634
tags: [mitre-attack, technique, T1634]
---

# T1634 - Credentials from Password Store

**Tactic(s):** Credential Access  -  **Platforms:** iOS  -  **ATT&CK:** [T1634](https://attack.mitre.org/techniques/T1634)

## Summary
Adversaries may search common password storage locations to obtain user credentials. Passwords can be stored in several places on a device, depending on the operating system or application holding the credentials. There are also specific applications that store passwords to make it easier for users to manage and maintain. Once credentials are obtained, they can be used to perform lateral movement and access restricted information.

## Role in the attack flow
Used to achieve the **Credential Access** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: iOS.

## Mitigations
- **M1001 Security Updates** - Install security updates in response to discovered vulnerabilities.
- **M1002 Attestation** - Enable remote attestation capabilities when available (such as Android SafetyNet or Samsung Knox TIMA Attestation) and prohibit devices that fail the attestation from accessing enterprise resources.
- **M1010 Deploy Compromised Device Detection Method** - A variety of methods exist that can be used to enable enterprises to identify compromised (e.g. rooted/jailbroken) devices, whether using security mechanisms built directly into the device, third-party mobile security applications, enterprise mobility management (EMM)/mobile device management (MDM) capabilities, or other methods. Some methods may be trivial to evade while others may be more sophisticated.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1634
