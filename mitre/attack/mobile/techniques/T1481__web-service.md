---
attack_id: T1481
name: Web Service
type: technique
parent: null
tactics: [Command and Control]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1481
tags: [mitre-attack, technique, T1481]
---

# T1481 - Web Service

**Tactic(s):** Command and Control  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1481](https://attack.mitre.org/techniques/T1481)

## Summary
Adversaries may use an existing, legitimate external Web service as a means for relaying data to/from a compromised system. Popular websites and social media, acting as a mechanism for C2, may give a significant amount of cover. This is due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection. 

 

Use of Web services may also protect back-end C2 infrastructure from discovery through malware binary analysis, or enable operational resiliency (since this infrastructure may be dynamically changed).

## Role in the attack flow
Used to achieve the **Command and Control** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1481
