---
capec_id: CAPEC-613
name: WiFi SSID Tracking
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-201, CWE-300]
related_attack: []
url: https://capec.mitre.org/data/definitions/613.html
tags: [mitre-capec, attack-pattern, CAPEC-613]
---

# CAPEC-613 - WiFi SSID Tracking

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-613](https://capec.mitre.org/data/definitions/613.html)

## Description
In this attack scenario, the attacker passively listens for WiFi management frame messages containing the Service Set Identifier (SSID) for the WiFi network. These messages are frequently transmitted by WiFi access points (e.g., the retransmission device) as well as by clients that are accessing the network (e.g., the handset/mobile device). Once the attacker is able to associate an SSID with a particular user or set of users (for example, when attending a public event), the attacker can then scan for this SSID to track that user in the future.

## Prerequisites
- None

## Skills required
- **Low**: Open source and commercial software tools are available and open databases of known WiFi SSID addresses are available online.

## Mitigations
- Do not enable the feature of "Hidden SSIDs" (also known as "Network Cloaking") – this option disables the usual broadcasting of the SSID by the access point, but forces the mobile handset to send requests on all supported radio channels which contains the SSID. The result is that tracking of the mobile device becomes easier since it is transmitting the SSID more frequently.
- Frequently change the SSID to new and unrelated values

## Related weaknesses (CWE)
- [CWE-201](https://cwe.mitre.org/data/definitions/201.html)
- [CWE-300](https://cwe.mitre.org/data/definitions/300.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/613.html
