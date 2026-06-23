---
capec_id: CAPEC-622
name: Electromagnetic Side-Channel Attack
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-201]
related_attack: []
url: https://capec.mitre.org/data/definitions/622.html
tags: [mitre-capec, attack-pattern, CAPEC-622]
---

# CAPEC-622 - Electromagnetic Side-Channel Attack

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-622](https://capec.mitre.org/data/definitions/622.html)

## Description
In this attack scenario, the attacker passively monitors electromagnetic emanations that are produced by the targeted electronic device as an unintentional side-effect of its processing. From these emanations, the attacker derives information about the data that is being processed (e.g. the attacker can recover cryptographic keys by monitoring emanations associated with cryptographic processing). This style of attack requires proximal access to the device, however attacks have been demonstrated at public conferences that work at distances of up to 10-15 feet. There have not been any significant studies to determine the maximum practical distance for such attacks. Since the attack is passive, it is nearly impossible to detect and the targeted device will continue to operate as normal after a successful attack.

## Prerequisites
- Proximal access to the device.

## Skills required
- **Medium**: Sophisticated attack, but detailed techniques published in the open literature.

## Consequences
- **Confidentiality**: Read Data (Derive sensitive information about encrypted data. For mobile devices, depending on which keys are compromised, the attacker may be able to decrypt VOIP communications, impersonate the targeted caller, or access the enterprise VPN server.)

## Mitigations
- Utilize side-channel resistant implementations of all crypto algorithms.
- Strong physical security of all devices that contain secret key information. (even when devices are not in use)

## Related weaknesses (CWE)
- [CWE-201](https://cwe.mitre.org/data/definitions/201.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/622.html
