---
capec_id: CAPEC-195
name: Principal Spoof
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/195.html
tags: [mitre-capec, attack-pattern, CAPEC-195]
---

# CAPEC-195 - Principal Spoof

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-195](https://capec.mitre.org/data/definitions/195.html)

## Description
A Principal Spoof is a form of Identity Spoofing where an adversary pretends to be some other person in an interaction. This is often accomplished by crafting a message (either written, verbal, or visual) that appears to come from a person other than the adversary. Phishing and Pharming attacks often attempt to do this so that their attempts to gather sensitive information appear to come from a legitimate source. A Principal Spoof does not use stolen or spoofed authentication credentials, instead relying on the appearance and content of the message to reflect identity.

## Extended description
The possible outcomes of a Principal Spoof mirror those of Identity Spoofing. (e.g., escalation of privilege and false attribution of data or activities) Likewise, most techniques for Identity Spoofing (crafting messages or intercepting and replaying or modifying messages) can be used for a Principal Spoof attack. However, because a Principal Spoof is used to impersonate a person, social engineering can be both an attack technique (using social techniques to generate evidence in support of a false identity) as well as a possible outcome (manipulating people's perceptions by making statements or performing actions under a target's name).

## Prerequisites
- The target must associate data or activities with a person's identity and the adversary must be able to modify this identity without detection.

## Resources required
- None: No specialized resources are required to execute this type of attack.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/195.html
