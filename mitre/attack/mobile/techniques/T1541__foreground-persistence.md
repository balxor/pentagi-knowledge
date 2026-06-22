---
attack_id: T1541
name: Foreground Persistence
type: technique
parent: null
tactics: [Defense Evasion, Persistence]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1541
tags: [mitre-attack, technique, T1541]
---

# T1541 - Foreground Persistence

**Tactic(s):** Defense Evasion, Persistence  -  **Platforms:** Android  -  **ATT&CK:** [T1541](https://attack.mitre.org/techniques/T1541)

## Summary
Adversaries may abuse Android's `startForeground()` API method to maintain continuous sensor access. Beginning in Android 9, idle applications running in the background no longer have access to device sensors, such as the camera, microphone, and gyroscope.(Citation: Android-SensorsOverview) Applications can retain sensor access by running in the foreground, using Android’s `startForeground()` API method. This informs the system that the user is actively interacting with the application, and it should not be killed. The only requirement to start a foreground service is showing a persistent notification to the user.(Citation: Android-ForegroundServices)

Malicious applications may abuse the `startForeground()` API method to continue running in the foreground, while presenting a notification to the user pretending to be a genuine application. This would allow unhindered access to the device’s sensors, assuming permission has been previously granted.(Citation: BlackHat Sutter Android Foreground 2019)

Malicious applications may also abuse the `startForeground()` API to inform the Android system that the user is actively interacting with the application, thus preventing it from being killed by the low memory killer.(Citation: TrendMicro-Yellow Camera)

## Role in the attack flow
Used to achieve the **Defense Evasion, Persistence** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

## Mitigations
- **M1011 User Guidance** - Describes any guidance or training given to users to set particular configuration settings or avoid specific potentially risky behaviors.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1541
