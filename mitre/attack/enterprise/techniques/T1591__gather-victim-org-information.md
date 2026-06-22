---
attack_id: T1591
name: Gather Victim Org Information
type: technique
parent: null
tactics: [Reconnaissance]
platforms: [PRE]
url: https://attack.mitre.org/techniques/T1591
tags: [mitre-attack, technique, T1591]
---

# T1591 - Gather Victim Org Information

**Tactic(s):** Reconnaissance  -  **Platforms:** PRE  -  **ATT&CK:** [T1591](https://attack.mitre.org/techniques/T1591)

## Summary
Adversaries may gather information about the victim's organization that can be used during targeting. Information about an organization may include a variety of details, including the names of divisions/departments, specifics of business operations, as well as the roles and responsibilities of key employees.

Adversaries may gather this information in various ways, such as direct elicitation via [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about an organization may also be exposed to adversaries via online or other accessible data sets (ex: [Social Media](https://attack.mitre.org/techniques/T1593/001) or [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)).(Citation: ThreatPost Broadvoice Leak)(Citation: SEC EDGAR Search) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Establish Accounts](https://attack.mitre.org/techniques/T1585) or [Compromise Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [Phishing](https://attack.mitre.org/techniques/T1566) or [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).

## Role in the attack flow
Used to achieve the **Reconnaissance** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: PRE.

## Mitigations
- **M1056 Pre-compromise** - Pre-compromise mitigations involve proactive measures and defenses implemented to prevent adversaries from successfully identifying and exploiting weaknesses during the Reconnaissance and Resource Development phases of an attack. These activities focus on reducing an organization's attack surface, identify adversarial preparation efforts, and increase the difficulty for attackers to conduct successful operations. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1591
