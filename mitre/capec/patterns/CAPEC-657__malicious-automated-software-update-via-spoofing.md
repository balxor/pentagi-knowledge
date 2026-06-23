---
capec_id: CAPEC-657
name: Malicious Automated Software Update via Spoofing
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-494]
related_attack: [T1072]
url: https://capec.mitre.org/data/definitions/657.html
tags: [mitre-capec, attack-pattern, CAPEC-657]
---

# CAPEC-657 - Malicious Automated Software Update via Spoofing

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-657](https://capec.mitre.org/data/definitions/657.html)

## Description
An attackers uses identify or content spoofing to trick a client into performing an automated software update from a malicious source. A malicious automated software update that leverages spoofing can include content or identity spoofing as well as protocol spoofing. Content or identity spoofing attacks can trigger updates in software by embedding scripted mechanisms within a malicious web page, which masquerades as a legitimate update source. Scripting mechanisms communicate with software components and trigger updates from locations specified by the attackers' server. The result is the client believing there is a legitimate software update available but instead downloading a malicious update from the attacker.

## Consequences
- **Access_Control**: Execute Unauthorized Commands
- **Availability**: Execute Unauthorized Commands
- **Confidentiality**: Execute Unauthorized Commands

## Related weaknesses (CWE)
- [CWE-494](https://cwe.mitre.org/data/definitions/494.html)

## Related ATT&CK techniques
- T1072

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/657.html
