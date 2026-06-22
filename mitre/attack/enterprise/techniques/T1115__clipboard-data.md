---
attack_id: T1115
name: Clipboard Data
type: technique
parent: null
tactics: [Collection]
platforms: [Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1115
tags: [mitre-attack, technique, T1115]
---

# T1115 - Clipboard Data

**Tactic(s):** Collection  ·  **Platforms:** Linux, macOS, Windows  ·  **ATT&CK:** [T1115](https://attack.mitre.org/techniques/T1115)

## Summary
Adversaries may collect data stored in the clipboard from users copying information within or between applications. 

For example, on Windows adversaries can access clipboard data by using <code>clip.exe</code> or <code>Get-Clipboard</code>.(Citation: MSDN Clipboard)(Citation: clip_win_server)(Citation: CISA_AA21_200B) Additionally, adversaries may monitor then replace users’ clipboard with their data (e.g., [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1565/002)).(Citation: mining_ruby_reversinglabs)

macOS and Linux also have commands, such as <code>pbpaste</code>, to grab clipboard contents.(Citation: Operating with EmPyre)

## Role in the attack flow
Used to achieve the **Collection** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1115
