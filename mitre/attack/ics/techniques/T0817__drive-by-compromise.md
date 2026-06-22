---
attack_id: T0817
name: Drive-by Compromise
type: technique
parent: null
tactics: [Initial Access]
platforms: [None]
url: https://attack.mitre.org/techniques/T0817
tags: [mitre-attack, technique, T0817]
---

# T0817 - Drive-by Compromise

**Tactic(s):** Initial Access  -  **Platforms:** None  -  **ATT&CK:** [T0817](https://attack.mitre.org/techniques/T0817)

## Summary
Adversaries may gain access to a system during a drive-by compromise, when a user visits a website as part of a regular browsing session. With this technique, the user's web browser is targeted and exploited simply by visiting the compromised website. 

The adversary may target a specific community, such as trusted third party suppliers or other industry specific groups, which often visit the target website. This kind of targeted attack relies on a common interest, and is known as a strategic web compromise or watering hole attack. 

The National Cyber Awareness System (NCAS) has issued a Technical Alert (TA) regarding Russian government cyber activity targeting critical infrastructure sectors. (Citation: Cybersecurity & Infrastructure Security Agency March 2018) Analysis by DHS and FBI has noted two distinct categories of victims in the Dragonfly campaign on the Western energy sector: staging and intended targets. The adversary targeted the less secure networks of staging targets, including trusted third-party suppliers and related peripheral organizations. Initial access to the intended targets used watering hole attacks to target process control, ICS, and critical infrastructure related trade publications and informational websites.

## Role in the attack flow
Used to achieve the **Initial Access** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0951 Update Software** - Perform regular software updates to mitigate exploitation risk. Software updates may need to be scheduled around operational down times.
- **M0948 Application Isolation and Sandboxing** - Restrict the execution of code to a virtual environment on or in-transit to an endpoint system.
- **M0950 Exploit Protection** - Use capabilities to detect and block conditions that may lead to or be indicative of a software exploit occurring.
- **M0921 Restrict Web-Based Content** - Restrict use of certain websites, block downloads/attachments, block Javascript, restrict browser extensions, etc.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0817
