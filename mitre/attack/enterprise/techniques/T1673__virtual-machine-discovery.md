---
attack_id: T1673
name: Virtual Machine Discovery
type: technique
parent: null
tactics: [Discovery]
platforms: [ESXi, Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1673
tags: [mitre-attack, technique, T1673]
---

# T1673 - Virtual Machine Discovery

**Tactic(s):** Discovery  -  **Platforms:** ESXi, Linux, macOS, Windows  -  **ATT&CK:** [T1673](https://attack.mitre.org/techniques/T1673)

## Summary
An adversary may attempt to enumerate running virtual machines (VMs) after gaining access to a host or hypervisor. For example, adversaries may enumerate a list of VMs on an ESXi hypervisor using a [Hypervisor CLI](https://attack.mitre.org/techniques/T1059/012) such as `esxcli` or `vim-cmd` (e.g. `esxcli vm process list or vim-cmd vmsvc/getallvms`).(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)(Citation: TrendMicro Play) Adversaries may also directly leverage a graphical user interface, such as VMware vCenter, in order to view virtual machines on a host. 

Adversaries may use the information from [Virtual Machine Discovery](https://attack.mitre.org/techniques/T1673) during discovery to shape follow-on behaviors. Subsequently discovered VMs may be leveraged for follow-on activities such as [Service Stop](https://attack.mitre.org/techniques/T1489) or [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486).(Citation: Crowdstrike Hypervisor Jackpotting Pt 2 2021)

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: ESXi, Linux, macOS, Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1673
