---
attack_id: T1643
name: Generate Traffic from Victim
type: technique
parent: null
tactics: [Impact]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1643
tags: [mitre-attack, technique, T1643]
---

# T1643 - Generate Traffic from Victim

**Tactic(s):** Impact  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1643](https://attack.mitre.org/techniques/T1643)

## Summary
Adversaries may generate outbound traffic from devices. This is typically performed to manipulate external outcomes, such as to achieve carrier billing fraud or to manipulate app store rankings or ratings. Outbound traffic is typically generated as SMS messages or general web traffic, but may take other forms as well.

If done via SMS messages, Android apps must hold the `SEND_SMS` permission. Additionally, sending an SMS message requires user consent if the recipient is a premium number. Applications cannot send SMS messages on iOS

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

## Mitigations
- **M1011 User Guidance** - Describes any guidance or training given to users to set particular configuration settings or avoid specific potentially risky behaviors.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1643
