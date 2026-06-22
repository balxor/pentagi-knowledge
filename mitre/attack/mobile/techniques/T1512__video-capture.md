---
attack_id: T1512
name: Video Capture
type: technique
parent: null
tactics: [Collection]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1512
tags: [mitre-attack, technique, T1512]
---

# T1512 - Video Capture

**Tactic(s):** Collection  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1512](https://attack.mitre.org/techniques/T1512)

## Summary
An adversary can leverage a device’s cameras to gather information by capturing video recordings. Images may also be captured, potentially in specified intervals, in lieu of video files.  

 

Malware or scripts may interact with the device cameras through an available API provided by the operating system. Video or image files may be written to disk and exfiltrated later. This technique differs from [Screen Capture](https://attack.mitre.org/techniques/T1513) due to use of the device’s cameras for video recording rather than capturing the victim’s screen. 

 

In Android, an application must hold the `android.permission.CAMERA` permission to access the cameras. In iOS, applications must include the `NSCameraUsageDescription` key in the `Info.plist` file. In both cases, the user must grant permission to the requesting application to use the camera. If the device has been rooted or jailbroken, an adversary may be able to access the camera without knowledge of the user.

## Role in the attack flow
Used to achieve the **Collection** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

## Mitigations
- **M1006 Use Recent OS Version** - New mobile operating system versions bring not only patches against discovered vulnerabilities but also often bring security architecture improvements that provide resilience against potential vulnerabilities or weaknesses that have not yet been discovered. They may also bring improvements that block use of observed adversary techniques.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1512
