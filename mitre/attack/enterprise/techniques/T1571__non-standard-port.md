---
attack_id: T1571
name: Non-Standard Port
type: technique
parent: null
tactics: [Command and Control]
platforms: [ESXi, Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1571
tags: [mitre-attack, technique, T1571]
---

# T1571 - Non-Standard Port

**Tactic(s):** Command and Control  -  **Platforms:** ESXi, Linux, macOS, Windows  -  **ATT&CK:** [T1571](https://attack.mitre.org/techniques/T1571)

## Summary
Adversaries may communicate using a protocol and port pairing that are typically not associated. For example, HTTPS over port 8088(Citation: Symantec Elfin Mar 2019) or port 587(Citation: Fortinet Agent Tesla April 2018) as opposed to the traditional port 443. Adversaries may make changes to the standard port used by a protocol to bypass filtering or muddle analysis/parsing of network data.

Adversaries may also make changes to victim systems to abuse non-standard ports. For example, Registry keys and other configuration settings can be used to modify protocol and port pairings.(Citation: change_rdp_port_conti)

## Role in the attack flow
Used to achieve the **Command and Control** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: ESXi, Linux, macOS, Windows.

## Mitigations
- **M1030 Network Segmentation** - Network segmentation involves dividing a network into smaller, isolated segments to control and limit the flow of traffic between devices, systems, and applications. By segmenting networks, organizations can reduce the attack surface, restrict lateral movement by adversaries, and protect critical assets from compromise.
- **M1031 Network Intrusion Prevention** - Use intrusion detection signatures to block traffic at network boundaries.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1571
