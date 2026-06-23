---
capec_id: CAPEC-667
name: Bluetooth Impersonation AttackS (BIAS)
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-290]
related_attack: []
url: https://capec.mitre.org/data/definitions/667.html
tags: [mitre-capec, attack-pattern, CAPEC-667]
---

# CAPEC-667 - Bluetooth Impersonation AttackS (BIAS)

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-667](https://capec.mitre.org/data/definitions/667.html)

## Description
An adversary disguises the MAC address of their Bluetooth enabled device to one for which there exists an active and trusted connection and authenticates successfully. The adversary can then perform malicious actions on the target Bluetooth device depending on the target’s capabilities.

## Prerequisites
- Knowledge of a target device's list of trusted connections.

## Skills required
- **Low**: Adversaries must be in close proximity to Bluetooth devices.

## Consequences
- **Confidentiality**: 
- **Integrity**: 

## Execution flow
Execution Flow Explore Find disguise and target: The adversary starts the Bluetooth service on the attacking device and searches for nearby listening devices. Techniques Knowledge of a trusted MAC address. Scanning for devices other than the target that may be trusted. Experiment Disguise: Using the MAC address of the device the adversary wants to impersonate, they may use a tool such as spooftooth or macchanger to spoof their Bluetooth address and attempt to authenticate with the target. Exploit Use device capabilities to accomplish goal: Finally, if authenticated successfully the adversary can perform tasks/information gathering dependent on the target's capabilities and connections.

## Mitigations
- Disable Bluetooth in public places.
- Verify incoming Bluetooth connections; do not automatically trust.
- Change default PIN passwords and always use one when connecting.

## Related weaknesses (CWE)
- [CWE-290](https://cwe.mitre.org/data/definitions/290.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/667.html
