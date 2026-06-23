---
capec_id: CAPEC-668
name: Key Negotiation of Bluetooth Attack (KNOB)
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: High
related_cwe: [CWE-425, CWE-285, CWE-693]
related_attack: [T1565.002]
url: https://capec.mitre.org/data/definitions/668.html
tags: [mitre-capec, attack-pattern, CAPEC-668]
---

# CAPEC-668 - Key Negotiation of Bluetooth Attack (KNOB)

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-668](https://capec.mitre.org/data/definitions/668.html)

## Description
An adversary can exploit a flaw in Bluetooth key negotiation allowing them to decrypt information sent between two devices communicating via Bluetooth. The adversary uses an Adversary in the Middle setup to modify packets sent between the two devices during the authentication process, specifically the entropy bits. Knowledge of the number of entropy bits will allow the attacker to easily decrypt information passing over the line of communication.

## Prerequisites
- Person in the Middle network setup.

## Skills required
- **Medium**: Ability to modify packets.

## Resources required
- Bluetooth adapter, packet capturing capabilities.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Authorization**: Bypass Protection Mechanism
- **Confidentiality**: Read Data, Bypass Protection Mechanism
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Discovery: Using an established Person in the Middle setup, search for Bluetooth devices beginning the authentication process. Techniques Use packet capture tools. Experiment Change the entropy bits: Upon recieving the initial key negotiation packet from the master, the adversary modifies the entropy bits requested to 1 to allow for easy decryption before it is forwarded. Exploit Capture and decrypt data: Once the entropy of encryption is known, the adversary can capture data and then decrypt on their device.

## Mitigations
- Newer Bluetooth firmwares ensure that the KNOB is not negotaited in plaintext. Update your device.

## Related weaknesses (CWE)
- [CWE-425](https://cwe.mitre.org/data/definitions/425.html)
- [CWE-285](https://cwe.mitre.org/data/definitions/285.html)
- [CWE-693](https://cwe.mitre.org/data/definitions/693.html)

## Related ATT&CK techniques
- T1565.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/668.html
