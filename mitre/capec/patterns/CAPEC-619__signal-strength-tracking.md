---
capec_id: CAPEC-619
name: Signal Strength Tracking
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-201]
related_attack: []
url: https://capec.mitre.org/data/definitions/619.html
tags: [mitre-capec, attack-pattern, CAPEC-619]
---

# CAPEC-619 - Signal Strength Tracking

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-619](https://capec.mitre.org/data/definitions/619.html)

## Description
In this attack scenario, the attacker passively monitors the signal strength of the target’s cellular RF signal or WiFi RF signal and uses the strength of the signal (with directional antennas and/or from multiple listening points at once) to identify the source location of the signal. Obtaining the signal of the target can be accomplished through multiple techniques such as through Cellular Broadcast Message Request or through the use of IMSI Tracking or WiFi MAC Address Tracking.

## Skills required
- **Low**: Commercial tools are available.

## Related weaknesses (CWE)
- [CWE-201](https://cwe.mitre.org/data/definitions/201.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/619.html
