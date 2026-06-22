---
attack_id: T0865
name: Spearphishing Attachment
type: technique
parent: null
tactics: [Initial Access]
platforms: [None]
url: https://attack.mitre.org/techniques/T0865
tags: [mitre-attack, technique, T0865]
---

# T0865 - Spearphishing Attachment

**Tactic(s):** Initial Access  -  **Platforms:** None  -  **ATT&CK:** [T0865](https://attack.mitre.org/techniques/T0865)

## Summary
Adversaries may use a spearphishing attachment, a variant of spearphishing, as a form of a social engineering attack against specific targets. Spearphishing attachments are different from other forms of spearphishing in that they employ malware attached to an email. All forms of spearphishing are electronically delivered and target a specific individual, company, or industry. In this scenario, adversaries attach a file to the spearphishing email and usually rely upon [User Execution](https://attack.mitre.org/techniques/T0863) to gain execution and access. (Citation: Enterprise ATT&CK October 2019) 

A Chinese spearphishing campaign running from December 9, 2011 through February 29, 2012, targeted ONG organizations and their employees. The emails were constructed with a high level of sophistication to convince employees to open the malicious file attachments. (Citation: CISA AA21-201A Pipeline Intrusion July 2021)

## Role in the attack flow
Used to achieve the **Initial Access** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0917 User Training** - Train users to be aware of access or manipulation attempts by an adversary to reduce the risk of successful spearphishing, social engineering, and other techniques that involve user interaction.
- **M0931 Network Intrusion Prevention** - Use intrusion detection signatures to block traffic at network boundaries.  In industrial control environments, network intrusion prevention should be configured so it will not disrupt protocols and communications responsible for real-time functions related to control or safety.
- **M0949 Antivirus/Antimalware** - Use signatures or heuristics to detect malicious software.  Within industrial control environments, antivirus/antimalware installations should be limited to assets that are not involved in critical or real-time operations. To minimize the impact to system availability, all products should first be validated within a representative test environment before deployment to production systems. (Citation: NCCIC August 2018)
- **M0921 Restrict Web-Based Content** - Restrict use of certain websites, block downloads/attachments, block Javascript, restrict browser extensions, etc.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0865
