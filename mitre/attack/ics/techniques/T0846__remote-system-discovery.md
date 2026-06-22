---
attack_id: T0846
name: Remote System Discovery
type: technique
parent: null
tactics: [Discovery]
platforms: [None]
url: https://attack.mitre.org/techniques/T0846
tags: [mitre-attack, technique, T0846]
---

# T0846 - Remote System Discovery

**Tactic(s):** Discovery  -  **Platforms:** None  -  **ATT&CK:** [T0846](https://attack.mitre.org/techniques/T0846)

## Summary
Adversaries may attempt to get a listing of other systems by IP address, hostname, or other logical identifier on a network that may be used for subsequent Lateral Movement or Discovery techniques. Functionality could exist within adversary tools to enable this, but utilities available on the operating system or vendor software could also be used.(Citation: Enterprise ATT&CK January 2018)

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0814 Static Network Configuration** - Configure hosts and devices to use static network configurations when possible, protocols that require dynamic discovery/addressing (e.g., ARP, DHCP, DNS) can be used to manipulate network message forwarding and enable various AiTM attacks. This mitigation may not always be usable due to limited device features or challenges introduced with different network configurations.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0846
