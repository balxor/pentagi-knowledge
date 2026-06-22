---
attack_id: T1461
name: Lockscreen Bypass
type: technique
parent: null
tactics: [Initial Access]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1461
tags: [mitre-attack, technique, T1461]
---

# T1461 - Lockscreen Bypass

**Tactic(s):** Initial Access  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1461](https://attack.mitre.org/techniques/T1461)

## Summary
An adversary with physical access to a mobile device may seek to bypass the device’s lockscreen. Several methods exist to accomplish this, including:

* Biometric spoofing: If biometric authentication is used, an adversary could attempt to spoof a mobile device’s biometric authentication mechanism. Both iOS and Android partly mitigate this attack by requiring the device’s passcode rather than biometrics to unlock the device after every device restart, and after a set or random amount of time.(Citation: SRLabs-Fingerprint)(Citation: TheSun-FaceID)
* Unlock code bypass: An adversary could attempt to brute-force or otherwise guess the lockscreen passcode (typically a PIN or password), including physically observing (“shoulder surfing”) the device owner’s use of the lockscreen passcode. Mobile OS vendors partly mitigate this by implementing incremental backoff timers after a set number of failed unlock attempts, as well as a configurable full device wipe after several failed unlock attempts.
* Vulnerability exploit: Techniques have been periodically demonstrated that exploit mobile devices to bypass the lockscreen. The vulnerabilities are generally patched by the device or OS vendor once disclosed.(Citation: Wired-AndroidBypass)(Citation: Kaspersky-iOSBypass)

## Role in the attack flow
Used to achieve the **Initial Access** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

## Mitigations
- **M1012 Enterprise Policy** - An enterprise mobility management (EMM), also known as mobile device management (MDM), system can be used to provision policies to mobile devices to control aspects of their allowed behavior.
- **M1001 Security Updates** - Install security updates in response to discovered vulnerabilities.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1461
