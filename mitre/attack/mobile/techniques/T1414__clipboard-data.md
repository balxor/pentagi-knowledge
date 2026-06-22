---
attack_id: T1414
name: Clipboard Data
type: technique
parent: null
tactics: [Collection, Credential Access]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1414
tags: [mitre-attack, technique, T1414]
---

# T1414 - Clipboard Data

**Tactic(s):** Collection, Credential Access  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1414](https://attack.mitre.org/techniques/T1414)

## Summary
Adversaries may abuse clipboard manager APIs to obtain sensitive information copied to the device clipboard. For example, passwords being copied and pasted from a password manager application could be captured by a malicious application installed on the device.(Citation: Fahl-Clipboard) 

 

On Android, applications can use the `ClipboardManager.OnPrimaryClipChangedListener()` API to register as a listener and monitor the clipboard for changes. However, starting in Android 10, this can only be used if the application is in the foreground, or is set as the device’s default input method editor (IME).(Citation: Github Capture Clipboard 2019)(Citation: Android 10 Privacy Changes) 

 

On iOS, this can be accomplished by accessing the `UIPasteboard.general.string` field. However, starting in iOS 14, upon accessing the clipboard, the user will be shown a system notification if the accessed text originated in a different application. For example, if the user copies the text of an iMessage from the Messages application, the notification will read “application_name has pasted from Messages” when the text was pasted in a different application.(Citation: UIPPasteboard)

## Role in the attack flow
Used to achieve the **Collection, Credential Access** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

## Mitigations
- **M1006 Use Recent OS Version** - New mobile operating system versions bring not only patches against discovered vulnerabilities but also often bring security architecture improvements that provide resilience against potential vulnerabilities or weaknesses that have not yet been discovered. They may also bring improvements that block use of observed adversary techniques.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1414
