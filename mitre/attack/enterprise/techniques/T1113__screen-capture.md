---
attack_id: T1113
name: Screen Capture
type: technique
parent: null
tactics: [Collection]
platforms: [Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1113
tags: [mitre-attack, technique, T1113]
---

# T1113 - Screen Capture

**Tactic(s):** Collection  -  **Platforms:** Linux, macOS, Windows  -  **ATT&CK:** [T1113](https://attack.mitre.org/techniques/T1113)

## Summary
Adversaries may attempt to take screen captures of the desktop to gather information over the course of an operation. Screen capturing functionality may be included as a feature of a remote access tool used in post-compromise operations. Taking a screenshot is also typically possible through native utilities or API calls, such as <code>CopyFromScreen</code>, <code>xwd</code>, or <code>screencapture</code>.(Citation: CopyFromScreen .NET)(Citation: Antiquated Mac Malware)

## Role in the attack flow
Used to achieve the **Collection** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1113
