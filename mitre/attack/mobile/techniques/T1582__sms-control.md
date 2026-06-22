---
attack_id: T1582
name: SMS Control
type: technique
parent: null
tactics: [Impact]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1582
tags: [mitre-attack, technique, T1582]
---

# T1582 - SMS Control

**Tactic(s):** Impact  -  **Platforms:** Android  -  **ATT&CK:** [T1582](https://attack.mitre.org/techniques/T1582)

## Summary
Adversaries may delete, alter, or send SMS messages without user authorization. This could be used to hide C2 SMS messages, spread malware, or various external effects.

This can be accomplished by requesting the `RECEIVE_SMS` or `SEND_SMS` permissions depending on what the malware is attempting to do. If the app is set as the default SMS handler on the device, the `SMS_DELIVER` broadcast intent can be registered, which allows the app to write to the SMS content provider. The content provider directly modifies the messaging database on the device, which could allow malicious applications with this ability to insert, modify, or delete arbitrary messages on the device.(Citation: SMS KitKat)(Citation: Android SmsProvider)

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

## Mitigations
- **M1011 User Guidance** - Describes any guidance or training given to users to set particular configuration settings or avoid specific potentially risky behaviors.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1582
