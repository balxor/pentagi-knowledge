---
capec_id: CAPEC-609
name: Cellular Traffic Intercept
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-311]
related_attack: [T1111]
url: https://capec.mitre.org/data/definitions/609.html
tags: [mitre-capec, attack-pattern, CAPEC-609]
---

# CAPEC-609 - Cellular Traffic Intercept

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-609](https://capec.mitre.org/data/definitions/609.html)

## Description
Cellular traffic for voice and data from mobile devices and retransmission devices can be intercepted via numerous methods. Malicious actors can deploy their own cellular tower equipment and intercept cellular traffic surreptitiously. Additionally, government agencies of adversaries and malicious actors can intercept cellular traffic via the telecommunications backbone over which mobile traffic is transmitted.

## Prerequisites
- None

## Skills required
- **Medium**: Adversaries can purchase hardware and software solutions, or create their own solutions, to capture/intercept cellular radio traffic. The cost of a basic Base Transceiver Station (BTS) to broadcast to local mobile cellular radios in mobile devices has dropped to very affordable costs. The ability of commercial cellular providers to monitor for "rogue" BTS stations is poor in many areas and it is assumed that "rogue" BTS stations exist in urban areas.

## Consequences
- **Confidentiality**: Read Data (Capture all cellular and RF traffic from mobile and retransmission devices. Move bulk traffic capture to storage area for cryptanalysis of encrypted traffic, and telemetry analysis of non-encrypted data. (packet headers, cellular power data, signal strength, etc.))

## Mitigations
- Encryption of all data packets emanating from the smartphone to a retransmission device via two encrypted tunnels with Suite B cryptography, all the way to the VPN gateway at the datacenter.

## Related weaknesses (CWE)
- [CWE-311](https://cwe.mitre.org/data/definitions/311.html)

## Related ATT&CK techniques
- T1111

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/609.html
