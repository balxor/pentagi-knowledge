---
attack_id: T1614
name: System Location Discovery
type: technique
parent: null
tactics: [Discovery]
platforms: [IaaS, Linux, macOS, Windows]
url: https://attack.mitre.org/techniques/T1614
tags: [mitre-attack, technique, T1614]
---

# T1614 - System Location Discovery

**Tactic(s):** Discovery  ·  **Platforms:** IaaS, Linux, macOS, Windows  ·  **ATT&CK:** [T1614](https://attack.mitre.org/techniques/T1614)

## Summary
Adversaries may gather information in an attempt to calculate the geographical location of a victim host. Adversaries may use the information from [System Location Discovery](https://attack.mitre.org/techniques/T1614) during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Adversaries may attempt to infer the location of a system using various system checks, such as time zone, keyboard layout, and/or language settings.(Citation: FBI Ragnar Locker 2020)(Citation: Sophos Geolocation 2016)(Citation: Bleepingcomputer RAT malware 2020) Windows API functions such as <code>GetLocaleInfoW</code> can also be used to determine the locale of the host.(Citation: FBI Ragnar Locker 2020) In cloud environments, an instance's availability zone may also be discovered by accessing the instance metadata service from the instance.(Citation: AWS Instance Identity Documents)(Citation: Microsoft Azure Instance Metadata 2021)

Adversaries may also attempt to infer the location of a victim host using IP addressing, such as via online geolocation IP-lookup services.(Citation: Securelist Trasparent Tribe 2020)(Citation: Sophos Geolocation 2016)

## Role in the attack flow
Used to achieve the **Discovery** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: IaaS, Linux, macOS, Windows.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1614
