---
attack_id: T1593
name: Search Open Websites/Domains
type: technique
parent: null
tactics: [Reconnaissance]
platforms: [PRE]
url: https://attack.mitre.org/techniques/T1593
tags: [mitre-attack, technique, T1593]
---

# T1593 - Search Open Websites/Domains

**Tactic(s):** Reconnaissance  -  **Platforms:** PRE  -  **ATT&CK:** [T1593](https://attack.mitre.org/techniques/T1593)

## Summary
Adversaries may search freely available websites and/or domains for information about victims that can be used during targeting. Information about victims may be available in various online sites, such as social media, new sites, or those hosting information about business operations such as hiring or requested/rewarded contracts.(Citation: Cyware Social Media)(Citation: SecurityTrails Google Hacking)(Citation: ExploitDB GoogleHacking)

Adversaries may search in different online sites depending on what information they seek to gather. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)), establishing operational resources (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Phishing](https://attack.mitre.org/techniques/T1566)).

## Role in the attack flow
Used to achieve the **Reconnaissance** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: PRE.

## Mitigations
- **M1047 Audit** - Auditing is the process of recording activity and systematically reviewing and analyzing the activity and system configurations. The primary purpose of auditing is to detect anomalies and identify potential threats or weaknesses in the environment. Proper auditing configurations can also help to meet compliance requirements. The process of auditing encompasses regular analysis of user behaviors and system logs in support of proactive security measures.
- **M1013 Application Developer Guidance** - Application Developer Guidance focuses on providing developers with the knowledge, tools, and best practices needed to write secure code, reduce vulnerabilities, and implement secure design principles. By integrating security throughout the software development lifecycle (SDLC), this mitigation aims to prevent the introduction of exploitable weaknesses in applications, systems, and APIs. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1593
