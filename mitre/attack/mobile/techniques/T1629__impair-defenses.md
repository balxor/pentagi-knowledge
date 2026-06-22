---
attack_id: T1629
name: Impair Defenses
type: technique
parent: null
tactics: [Defense Evasion]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1629
tags: [mitre-attack, technique, T1629]
---

# T1629 - Impair Defenses

**Tactic(s):** Defense Evasion  -  **Platforms:** Android  -  **ATT&CK:** [T1629](https://attack.mitre.org/techniques/T1629)

## Summary
Adversaries may maliciously modify components of a victim environment in order to hinder or disable defensive mechanisms. This not only involves impairing preventative defenses, such as anti-virus, but also detection capabilities that defenders can use to audit activity and identify malicious behavior. This may span both native defenses as well as supplemental capabilities installed by users or mobile endpoint administrators.

## Role in the attack flow
Used to achieve the **Defense Evasion** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

## Mitigations
- **M1010 Deploy Compromised Device Detection Method** - A variety of methods exist that can be used to enable enterprises to identify compromised (e.g. rooted/jailbroken) devices, whether using security mechanisms built directly into the device, third-party mobile security applications, enterprise mobility management (EMM)/mobile device management (MDM) capabilities, or other methods. Some methods may be trivial to evade while others may be more sophisticated.
- **M1001 Security Updates** - Install security updates in response to discovered vulnerabilities.
- **M1011 User Guidance** - Describes any guidance or training given to users to set particular configuration settings or avoid specific potentially risky behaviors.
- **M1004 System Partition Integrity** - Ensure that Android devices being used include and enable the Verified Boot capability, which cryptographically ensures the integrity of the system partition.
- **M1012 Enterprise Policy** - An enterprise mobility management (EMM), also known as mobile device management (MDM), system can be used to provision policies to mobile devices to control aspects of their allowed behavior.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1629
