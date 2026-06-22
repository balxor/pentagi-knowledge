---
attack_id: T0888
name: Remote System Information Discovery
type: technique
parent: null
tactics: [Discovery]
platforms: [None]
url: https://attack.mitre.org/techniques/T0888
tags: [mitre-attack, technique, T0888]
---

# T0888 - Remote System Information Discovery

**Tactic(s):** Discovery  -  **Platforms:** None  -  **ATT&CK:** [T0888](https://attack.mitre.org/techniques/T0888)

## Summary
An adversary may attempt to get detailed information about remote systems and their peripherals, such as make/model, role, and configuration. Adversaries may use information from Remote System Information Discovery to aid in targeting and shaping follow-on behaviors. For example, the system's operational role and model information can dictate whether it is a relevant target for the adversary's operational objectives. In addition, the system's configuration may be used to scope subsequent technique usage. 

Requests for system information are typically implemented using automation and management protocols and are often automatically requested by vendor software during normal operation. This information may be used to tailor management actions, such as program download and system or module firmware. An adversary may leverage this same information by issuing calls directly to the system's API.

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0814 Static Network Configuration** - Configure hosts and devices to use static network configurations when possible, protocols that require dynamic discovery/addressing (e.g., ARP, DHCP, DNS) can be used to manipulate network message forwarding and enable various AiTM attacks. This mitigation may not always be usable due to limited device features or challenges introduced with different network configurations.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0888
