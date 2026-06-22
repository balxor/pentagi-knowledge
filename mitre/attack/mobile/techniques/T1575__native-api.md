---
attack_id: T1575
name: Native API
type: technique
parent: null
tactics: [Defense Evasion, Execution]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1575
tags: [mitre-attack, technique, T1575]
---

# T1575 - Native API

**Tactic(s):** Defense Evasion, Execution  -  **Platforms:** Android  -  **ATT&CK:** [T1575](https://attack.mitre.org/techniques/T1575)

## Summary
Adversaries may use Android’s Native Development Kit (NDK) to write native functions that can achieve execution of binaries or functions. Like system calls on a traditional desktop operating system, native code achieves execution on a lower level than normal Android SDK calls.

The NDK allows developers to write native code in C or C++ that is compiled directly to machine code, avoiding all intermediate languages and steps in compilation that higher level languages, like Java, typically have. The Java Native Interface (JNI) is the component that allows Java functions in the Android app to call functions in a native library.(Citation: Google NDK Getting Started)

Adversaries may also choose to use native functions to execute malicious code since native actions are typically much more difficult to analyze than standard, non-native behaviors.(Citation: MITRE App Vetting Effectiveness)

## Role in the attack flow
Used to achieve the **Defense Evasion, Execution** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1575
