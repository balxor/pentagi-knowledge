---
attack_id: T1217
name: Browser Information Discovery
type: technique
parent: null
tactics: [Discovery]
platforms: [Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1217
tags: [mitre-attack, technique, T1217]
---

# T1217 - Browser Information Discovery

**Tactic(s):** Discovery  ·  **Platforms:** Linux, macOS, Windows  ·  **ATT&CK:** [T1217](https://attack.mitre.org/techniques/T1217)

## Summary
Adversaries may enumerate information about browsers to learn more about compromised environments. Data saved by browsers (such as bookmarks, accounts, and browsing history) may reveal a variety of personal information about users (e.g., banking sites, relationships/interests, social media, etc.) as well as details about internal network resources such as servers, tools/dashboards, or other related infrastructure.(Citation: Kaspersky Autofill)

Browser information may also highlight additional targets after an adversary has access to valid credentials, especially [Credentials In Files](https://attack.mitre.org/techniques/T1552/001) associated with logins cached by a browser.

Specific storage locations vary based on platform and/or application, but browser information is typically stored in local files and databases (e.g., `%APPDATA%/Google/Chrome`).(Citation: Chrome Roaming Profiles)

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1217
