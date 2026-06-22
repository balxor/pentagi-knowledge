---
attack_id: T1123
name: Audio Capture
type: technique
parent: null
tactics: [Collection]
platforms: [Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1123
tags: [mitre-attack, technique, T1123]
---

# T1123 - Audio Capture

**Tactic(s):** Collection  -  **Platforms:** Linux, macOS, Windows  -  **ATT&CK:** [T1123](https://attack.mitre.org/techniques/T1123)

## Summary
An adversary can leverage a computer's peripheral devices (e.g., microphones and webcams) or applications (e.g., voice and video call services) to capture audio recordings for the purpose of listening into sensitive conversations to gather information.(Citation: ESET Attor Oct 2019)

Malware or scripts may be used to interact with the devices through an available API provided by the operating system or an application to capture audio. Audio files may be written to disk and exfiltrated later.

## Role in the attack flow
Used to achieve the **Collection** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1123
