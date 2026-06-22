---
attack_id: T1596
name: Search Open Technical Databases
type: technique
parent: null
tactics: [Reconnaissance]
platforms: [PRE]
url: https://attack.mitre.org/techniques/T1596
tags: [mitre-attack, technique, T1596]
---

# T1596 - Search Open Technical Databases

**Tactic(s):** Reconnaissance  -  **Platforms:** PRE  -  **ATT&CK:** [T1596](https://attack.mitre.org/techniques/T1596)

## Summary
Adversaries may search freely available technical databases for information about victims that can be used during targeting. Information about victims may be available in online databases and repositories, such as registrations of domains/certificates as well as public collections of network data/artifacts gathered from traffic and/or scans.(Citation: WHOIS)(Citation: DNS Dumpster)(Citation: Circl Passive DNS)(Citation: Medium SSL Cert)(Citation: SSLShopper Lookup)(Citation: DigitalShadows CDN)(Citation: Shodan)

Adversaries may search in different open databases depending on what information they seek to gather. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [Phishing for Information](https://attack.mitre.org/techniques/T1598) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133) or [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).

## Role in the attack flow
Used to achieve the **Reconnaissance** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: PRE.

## Mitigations
- **M1056 Pre-compromise** - Pre-compromise mitigations involve proactive measures and defenses implemented to prevent adversaries from successfully identifying and exploiting weaknesses during the Reconnaissance and Resource Development phases of an attack. These activities focus on reducing an organization's attack surface, identify adversarial preparation efforts, and increase the difficulty for attackers to conduct successful operations. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1596
