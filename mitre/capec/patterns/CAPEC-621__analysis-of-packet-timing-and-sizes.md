---
capec_id: CAPEC-621
name: Analysis of Packet Timing and Sizes
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-201]
related_attack: []
url: https://capec.mitre.org/data/definitions/621.html
tags: [mitre-capec, attack-pattern, CAPEC-621]
---

# CAPEC-621 - Analysis of Packet Timing and Sizes

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-621](https://capec.mitre.org/data/definitions/621.html)

## Description
An attacker may intercept and log encrypted transmissions for the purpose of analyzing metadata such as packet timing and sizes. Although the actual data may be encrypted, this metadata may reveal valuable information to an attacker. Note that this attack is applicable to VOIP data as well as application data, especially for interactive apps that require precise timing and low-latency (e.g. thin-clients).

## Prerequisites
- Use of untrusted communication paths enables an attacker to intercept and log communications, including metadata such as packet timing and sizes.

## Skills required
- **High**: These attacks generally require sophisticated machine learning techniques and require traffic capture as a prerequisite.

## Consequences
- **Confidentiality**: Read Data (Derive sensitive information about encrypted data.)

## Mitigations
- Distort packet sizes and timing at VPN layer by adding padding to normalize packet sizes and timing delays to reduce information leakage via timing.

## Related weaknesses (CWE)
- [CWE-201](https://cwe.mitre.org/data/definitions/201.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/621.html
