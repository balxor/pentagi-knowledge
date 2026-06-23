---
capec_id: CAPEC-508
name: Shoulder Surfing
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-200, CWE-359]
related_attack: []
url: https://capec.mitre.org/data/definitions/508.html
tags: [mitre-capec, attack-pattern, CAPEC-508]
---

# CAPEC-508 - Shoulder Surfing

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-508](https://capec.mitre.org/data/definitions/508.html)

## Description
In a shoulder surfing attack, an adversary observes an unaware individual's keystrokes, screen content, or conversations with the goal of obtaining sensitive information. One motive for this attack is to obtain sensitive information about the target for financial, personal, political, or other gains. From an insider threat perspective, an additional motive could be to obtain system/application credentials or cryptographic keys. Shoulder surfing attacks are accomplished by observing the content "over the victim's shoulder", as implied by the name of this attack.

## Prerequisites
- The adversary typically requires physical proximity to the target's environment, in order to observe their screen or conversation. This may not be the case if the adversary is able to record the target and obtain sensitive information upon review of the recording.

## Skills required
- **Low**: In most cases, an adversary can simply observe and retain the desired information.

## Consequences
- **Confidentiality**: Read Data

## Mitigations
- Be mindful of your surroundings when discussing or viewing sensitive information in public areas.
- Pertaining to insider threats, ensure that sensitive information is not displayed to nor discussed around individuals without need-to-know access to said information.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)
- [CWE-359](https://cwe.mitre.org/data/definitions/359.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/508.html
