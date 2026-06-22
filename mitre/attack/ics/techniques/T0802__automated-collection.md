---
attack_id: T0802
name: Automated Collection
type: technique
parent: null
tactics: [Collection]
platforms: [None]
url: https://attack.mitre.org/techniques/T0802
tags: [mitre-attack, technique, T0802]
---

# T0802 - Automated Collection

**Tactic(s):** Collection  -  **Platforms:** None  -  **ATT&CK:** [T0802](https://attack.mitre.org/techniques/T0802)

## Summary
Adversaries may automate collection of industrial environment information using tools or scripts. This automated collection may leverage native control protocols and tools available in the control systems environment. For example, the OPC protocol may be used to enumerate and gather information. Access to a system or interface with these native protocols may allow collection and enumeration of other attached, communicating servers and devices.

## Role in the attack flow
Used to achieve the **Collection** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0807 Network Allowlists** - Network allowlists can be implemented through either host-based files or system hosts files to specify what connections (e.g., IP address, MAC address, port, protocol) can be made from a device. Allowlist techniques that operate at the  application layer (e.g., DNP3, Modbus, HTTP) are addressed in [Filter Network Traffic](https://attack.mitre.org/mitigations/M0937) mitigation.
- **M0930 Network Segmentation** - Architect sections of the network to isolate critical systems, functions, or resources. Use physical and logical segmentation to prevent access to potentially sensitive systems and information. Use a DMZ to contain any internet-facing services that should not be exposed from the internal network.  Restrict network access to only required systems and services. In addition, prevent systems from other networks or business functions (e.g., enterprise) from accessing critical process control systems. For example, in IEC 62443, systems within the same secure level should be grouped into a zone, and access to that zone is restricted by a conduit, or mechanism to restrict data flows between zones by segmenting the network. (Citation: IEC February 2019) (Citation: IEC August 2013)

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0802
