---
capec_id: CAPEC-173
name: Action Spoofing
type: attack-pattern
abstraction: Meta
likelihood: High
severity: Very High
related_cwe: [CWE-451]
related_attack: []
url: https://capec.mitre.org/data/definitions/173.html
tags: [mitre-capec, attack-pattern, CAPEC-173]
---

# CAPEC-173 - Action Spoofing

**Abstraction:** Meta  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-173](https://capec.mitre.org/data/definitions/173.html)

## Description
An adversary is able to disguise one action for another and therefore trick a user into initiating one type of action when they intend to initiate a different action. For example, a user might be led to believe that clicking a button will submit a query, but in fact it downloads software. Adversaries may perform this attack through social means, such as by simply convincing a victim to perform the action or relying on a user's natural inclination to do so, or through technical means, such as a clickjacking attack where a user sees one interface but is actually interacting with a second, invisible, interface.

## Prerequisites
- The adversary must convince the victim into performing the decoy action.
- The adversary must have the means to control a user's interface to present them with a decoy action as well as the actual malicious action. Simple versions of this attack can be performed using web pages requiring only that the adversary be able to host (or control) content that the user visits.

## Consequences
- **Availability**: Other (Action spoofing can result in a wide variety of consequences and negatively affect all three elements of the security triad.)
- **Confidentiality**: Other (Action spoofing can result in a wide variety of consequences and negatively affect all three elements of the security triad.)
- **Integrity**: Other (Action spoofing can result in a wide variety of consequences and negatively affect all three elements of the security triad.)

## Mitigations
- Avoid interacting with suspicious sites or clicking suspicious links.
- An organization should provide regular, robust cybersecurity training to its employees.

## Related weaknesses (CWE)
- [CWE-451](https://cwe.mitre.org/data/definitions/451.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/173.html
