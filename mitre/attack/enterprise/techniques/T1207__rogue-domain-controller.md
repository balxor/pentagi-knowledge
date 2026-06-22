---
attack_id: T1207
name: Rogue Domain Controller
type: technique
parent: null
tactics: [Defense Impairment]
platforms: [Windows]
url: https://attack.mitre.org/techniques/T1207
tags: [mitre-attack, technique, T1207]
---

# T1207 - Rogue Domain Controller

**Tactic(s):** Defense Impairment  ·  **Platforms:** Windows  ·  **ATT&CK:** [T1207](https://attack.mitre.org/techniques/T1207)

## Summary
Adversaries may register a rogue Domain Controller to enable manipulation of Active Directory data. DCShadow may be used to create a rogue Domain Controller (DC). DCShadow is a method of manipulating Active Directory (AD) data, including objects and schemas, by registering (or reusing an inactive registration) and simulating the behavior of a DC. (Citation: DCShadow Blog) Once registered, a rogue DC may be able to inject and replicate changes into AD infrastructure for any domain object, including credentials and keys.

Registering a rogue DC involves creating a new server and nTDSDSA objects in the Configuration partition of the AD schema, which requires Administrator privileges (either Domain or local to the DC) or the KRBTGT hash. (Citation: Adsecurity Mimikatz Guide)

This technique may bypass system logging and security monitors such as security information and event management (SIEM) products (since actions taken on a rogue DC may not be reported to these sensors). (Citation: DCShadow Blog) The technique may also be used to alter and delete replication and other associated metadata to obstruct forensic analysis. Adversaries may also utilize this technique to perform [SID-History Injection](https://attack.mitre.org/techniques/T1134/005) and/or manipulate AD objects (such as accounts, access control lists, schemas) to establish backdoors for Persistence. (Citation: DCShadow Blog)

## Role in the attack flow
Used to achieve the **Defense Impairment** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1207
