---
capec_id: CAPEC-623
name: Compromising Emanations Attack
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-201]
related_attack: []
url: https://capec.mitre.org/data/definitions/623.html
tags: [mitre-capec, attack-pattern, CAPEC-623]
---

# CAPEC-623 - Compromising Emanations Attack

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-623](https://capec.mitre.org/data/definitions/623.html)

## Description
Compromising Emanations (CE) are defined as unintentional signals which an attacker may intercept and analyze to disclose the information processed by the targeted equipment. Commercial mobile devices and retransmission devices have displays, buttons, microchips, and radios that emit mechanical emissions in the form of sound or vibrations. Capturing these emissions can help an adversary understand what the device is doing.

## Prerequisites
- Proximal access to the device.

## Skills required
- **High**: Sophisticated attack.

## Consequences
- **Confidentiality**: Read Data (Capture vibrations/emissions from the handset or retransmission device display screen to recreat display information from a distance.)

## Mitigations
- None are known.

## Related weaknesses (CWE)
- [CWE-201](https://cwe.mitre.org/data/definitions/201.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/623.html
