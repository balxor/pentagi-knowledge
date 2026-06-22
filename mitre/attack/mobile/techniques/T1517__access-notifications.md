---
attack_id: T1517
name: Access Notifications
type: technique
parent: null
tactics: [Collection, Credential Access]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1517
tags: [mitre-attack, technique, T1517]
---

# T1517 - Access Notifications

**Tactic(s):** Collection, Credential Access  -  **Platforms:** Android  -  **ATT&CK:** [T1517](https://attack.mitre.org/techniques/T1517)

## Summary
Adversaries may collect data within notifications sent by the operating system or other applications. Notifications may contain sensitive data such as one-time authentication codes sent over SMS, email, or other mediums. In the case of Credential Access, adversaries may attempt to intercept one-time code sent to the device. Adversaries can also dismiss notifications to prevent the user from noticing that the notification has arrived and can trigger action buttons contained within notifications.(Citation: ESET 2FA Bypass)

## Role in the attack flow
Used to achieve the **Collection, Credential Access** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

## Mitigations
- **M1011 User Guidance** - Describes any guidance or training given to users to set particular configuration settings or avoid specific potentially risky behaviors.
- **M1013 Application Developer Guidance** - Application Developer Guidance focuses on providing developers with the knowledge, tools, and best practices needed to write secure code, reduce vulnerabilities, and implement secure design principles. By integrating security throughout the software development lifecycle (SDLC), this mitigation aims to prevent the introduction of exploitable weaknesses in applications, systems, and APIs. This mitigation can be implemented through the following measures:
- **M1012 Enterprise Policy** - An enterprise mobility management (EMM), also known as mobile device management (MDM), system can be used to provision policies to mobile devices to control aspects of their allowed behavior.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1517
