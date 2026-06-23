---
capec_id: CAPEC-407
name: Pretexting
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: Low
related_cwe: []
related_attack: [T1589]
url: https://capec.mitre.org/data/definitions/407.html
tags: [mitre-capec, attack-pattern, CAPEC-407]
---

# CAPEC-407 - Pretexting

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** Low  -  **CAPEC:** [CAPEC-407](https://capec.mitre.org/data/definitions/407.html)

## Description
An adversary engages in pretexting behavior to solicit information from target persons, or manipulate the target into performing some action that serves the adversary's interests. During a pretexting attack, the adversary creates an invented scenario, assuming an identity or role to persuade a targeted victim to release information or perform some action. It is more than just creating a lie; in some cases it can be creating a whole new identity and then using that identity to manipulate the receipt of information.

## Extended description
Pretexting can also be used to impersonate people in certain jobs and roles that they never themselves have done. In simple form, these attacks can be leveraged to learn information about a target. More complicated iterations may seek to solicit a target to perform some action that assists the adversary in exploiting organizational weaknesses or obtaining access to secure facilities or systems. Pretexting is not a one-size fits all solution. Good information gathering techniques can make or break a good pretext. A solid pretext is an essential part of building trust. If an adversary’s alias, story, or identity has holes or lacks credibility or even the perception of credibility the target will most likely catch on.

## Prerequisites
- The adversary must have the means and knowledge of how to communicate with the target in some manner.The adversary must have knowledge of the pretext that would influence the actions of the specific target.

## Skills required
- **Low**: The adversary requires strong inter-personal and communication skills.

## Consequences
- **Confidentiality**: Other (Depending on the adversary's intentions and the specific nature their actions/requests, a successful pretexting attack can result in the compromise to the confidentiality of sensitive information in a variety of contexts.)

## Mitigations
- An organization should provide regular, robust cybersecurity training to its employees to prevent successful social engineering attacks.

## Related ATT&CK techniques
- T1589

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/407.html
