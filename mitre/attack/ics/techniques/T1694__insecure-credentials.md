---
attack_id: T1694
name: Insecure Credentials
type: technique
parent: null
tactics: [Persistence, Lateral Movement]
platforms: []
url: https://attack.mitre.org/techniques/T1694
tags: [mitre-attack, technique, T1694]
---

# T1694 - Insecure Credentials

**Tactic(s):** Persistence, Lateral Movement  -  **Platforms:** n/a  -  **ATT&CK:** [T1694](https://attack.mitre.org/techniques/T1694)

## Summary
Adversaries may target insecure credentials as a means to persist on a system or device or move laterally from one system or device to another. Insecure credentials may appear as default credentials which are pre-configured credentials on a system, device, or software that are well-known in documentation or hard-coded credentials which are built into the system, device, or software that cannot be changed or not easily changed because of the impact on control processes.(Citation: NIST SP 800-82r3)(Citation: ICS-ALERT-13-164-01)(Citation: OT IceFall)
 Adversaries often times use insecure credentials to evade detection as they are typically forgotten about by system and device owners.

## Role in the attack flow
Used to achieve the **Persistence, Lateral Movement** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: any.

## Mitigations
- **M0801 Access Management** - Access Management technologies can be used to enforce authorization polices and decisions, especially when existing field devices do not provide sufficient capabilities to support user identification and authentication. (Citation: McCarthy, J et al. July 2018) These technologies typically utilize an in-line network device or gateway system to prevent access to unauthenticated users, while also integrating with an authentication service to first verify user credentials. (Citation: Centre for the Protection of National Infrastructure November 2010)

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1694
