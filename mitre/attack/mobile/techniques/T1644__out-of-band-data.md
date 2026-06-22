---
attack_id: T1644
name: Out of Band Data
type: technique
parent: null
tactics: [Command and Control]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1644
tags: [mitre-attack, technique, T1644]
---

# T1644 - Out of Band Data

**Tactic(s):** Command and Control  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1644](https://attack.mitre.org/techniques/T1644)

## Summary
Adversaries may communicate with compromised devices using out of band data streams. This could be done for a variety of reasons, including evading network traffic monitoring, as a backup method of command and control, or for data exfiltration if the device is not connected to any Internet-providing networks (i.e. cellular or Wi-Fi). Several out of band data streams exist, such as SMS messages, NFC, and Bluetooth. 

 

On Android, applications can read push notifications to capture content from SMS messages, or other out of band data streams. This requires that the user manually grant notification access to the application via the settings menu. However, the application could launch an Intent to take the user directly there. 

 

On iOS, there is no way to programmatically read push notifications.

## Role in the attack flow
Used to achieve the **Command and Control** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

## Mitigations
- **M1011 User Guidance** - Describes any guidance or training given to users to set particular configuration settings or avoid specific potentially risky behaviors.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1644
