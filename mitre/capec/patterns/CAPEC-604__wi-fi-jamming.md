---
capec_id: CAPEC-604
name: Wi-Fi Jamming
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/604.html
tags: [mitre-capec, attack-pattern, CAPEC-604]
---

# CAPEC-604 - Wi-Fi Jamming

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-604](https://capec.mitre.org/data/definitions/604.html)

## Description
In this attack scenario, the attacker actively transmits on the Wi-Fi channel to prevent users from transmitting or receiving data from the targeted Wi-Fi network. There are several known techniques to perform this attack – for example: the attacker may flood the Wi-Fi access point (e.g. the retransmission device) with deauthentication frames. Another method is to transmit high levels of noise on the RF band used by the Wi-Fi network.

## Prerequisites
- Lack of anti-jam features in 802.11
- Lack of authentication on deauthentication/disassociation packets on 802.11-based networks

## Skills required
- **Low**: This attack can be performed by low capability attackers with freely available tools. Commercial tools are also available that can target select networks or all WiFi networks within a range of several miles.

## Consequences
- **Availability**: Other (A successful attack will deny the availability of the Wi-fi network to authorized users.), Resource Consumption (The attacker's goal is to prevent users from accessing the wireless network. Denying connectivity to the wireless network prevents the user from being able to transmit or receive any data, which also prevents VOIP calls, however this attack poses no threat to data confidentiality.)

## Mitigations
- Countermeasures have been proposed for both disassociation flooding and RF jamming, however these countermeasures are not standardized and would need to be supported on both the retransmission device and the handset in order to be effective. Commercial products are not currently available that support jamming countermeasures for Wi-Fi.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/604.html
