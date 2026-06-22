---
attack_id: T1516
name: Input Injection
type: technique
parent: null
tactics: [Defense Evasion, Impact]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1516
tags: [mitre-attack, technique, T1516]
---

# T1516 - Input Injection

**Tactic(s):** Defense Evasion, Impact  -  **Platforms:** Android  -  **ATT&CK:** [T1516](https://attack.mitre.org/techniques/T1516)

## Summary
A malicious application can inject input to the user interface to mimic user interaction through the abuse of Android's accessibility APIs.

[Input Injection](https://attack.mitre.org/techniques/T1516) can be achieved using any of the following methods:

* Mimicking user clicks on the screen, for example to steal money from a user's PayPal account.(Citation: android-trojan-steals-paypal-2fa)
* Injecting global actions, such as `GLOBAL_ACTION_BACK` (programatically mimicking a physical back button press), to trigger actions on behalf of the user.(Citation: Talos Gustuff Apr 2019)
* Inserting input into text fields on behalf of the user. This method is used legitimately to auto-fill text fields by applications such as password managers.(Citation: bitwarden autofill logins)

## Role in the attack flow
Used to achieve the **Defense Evasion, Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

## Mitigations
- **M1011 User Guidance** - Describes any guidance or training given to users to set particular configuration settings or avoid specific potentially risky behaviors.
- **M1012 Enterprise Policy** - An enterprise mobility management (EMM), also known as mobile device management (MDM), system can be used to provision policies to mobile devices to control aspects of their allowed behavior.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1516
