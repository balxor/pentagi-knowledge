---
capec_id: CAPEC-614
name: Rooting SIM Cards
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: High
related_cwe: [CWE-327]
related_attack: []
url: https://capec.mitre.org/data/definitions/614.html
tags: [mitre-capec, attack-pattern, CAPEC-614]
---

# CAPEC-614 - Rooting SIM Cards

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** High  -  **CAPEC:** [CAPEC-614](https://capec.mitre.org/data/definitions/614.html)

## Description
SIM cards are the de facto trust anchor of mobile devices worldwide. The cards protect the mobile identity of subscribers, associate devices with phone numbers, and increasingly store payment credentials, for example in NFC-enabled phones with mobile wallets. This attack leverages over-the-air (OTA) updates deployed via cryptographically-secured SMS messages to deliver executable code to the SIM. By cracking the DES key, an attacker can send properly signed binary SMS messages to a device, which are treated as Java applets and are executed on the SIM. These applets are allowed to send SMS, change voicemail numbers, and query the phone location, among many other predefined functions. These capabilities alone provide plenty of potential for abuse.

## Prerequisites
- A SIM card that relies on the DES cipher.

## Skills required
- **Medium**: This is a sophisticated attack, but detailed techniques are published in open literature.

## Consequences
- **Confidentiality**: Execute Unauthorized Commands
- **Integrity**: Execute Unauthorized Commands

## Mitigations
- Upgrade the SIM card to use the state-of-the-art AES or the somewhat outdated 3DES algorithm for OTA.

## Related weaknesses (CWE)
- [CWE-327](https://cwe.mitre.org/data/definitions/327.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/614.html
