---
attack_id: T0881
name: Service Stop
type: technique
parent: null
tactics: [Inhibit Response Function]
platforms: [None]
url: https://attack.mitre.org/techniques/T0881
tags: [mitre-attack, technique, T0881]
---

# T0881 - Service Stop

**Tactic(s):** Inhibit Response Function  -  **Platforms:** None  -  **ATT&CK:** [T0881](https://attack.mitre.org/techniques/T0881)

## Summary
Adversaries may stop or disable services on a system to render those services unavailable to legitimate users. Stopping critical services can inhibit or stop response to an incident or aid in the adversary's overall objectives to cause damage to the environment. (Citation: Enterprise ATT&CK)  Services may not allow for modification of their data stores while running. Adversaries may stop services in order to conduct Data Destruction. (Citation: Enterprise ATT&CK)

## Role in the attack flow
Used to achieve the **Inhibit Response Function** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0918 User Account Management** - Manage the creation, modification, use, and permissions associated to user accounts.
- **M0924 Restrict Registry Permissions** - Restrict the ability to modify certain hives or keys in the Windows Registry.
- **M0922 Restrict File and Directory Permissions** - Restrict access by setting directory and file permissions that are not specific to users or privileged accounts.
- **M0930 Network Segmentation** - Architect sections of the network to isolate critical systems, functions, or resources. Use physical and logical segmentation to prevent access to potentially sensitive systems and information. Use a DMZ to contain any internet-facing services that should not be exposed from the internal network.  Restrict network access to only required systems and services. In addition, prevent systems from other networks or business functions (e.g., enterprise) from accessing critical process control systems. For example, in IEC 62443, systems within the same secure level should be grouped into a zone, and access to that zone is restricted by a conduit, or mechanism to restrict data flows between zones by segmenting the network. (Citation: IEC February 2019) (Citation: IEC August 2013)

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0881
