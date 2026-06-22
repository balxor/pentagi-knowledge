---
attack_id: T1653
name: Power Settings
type: technique
parent: null
tactics: [Persistence]
platforms: [Windows, Linux, macOS, Network Devices]
url: https://attack.mitre.org/techniques/T1653
tags: [mitre-attack, technique, T1653]
---

# T1653 - Power Settings

**Tactic(s):** Persistence  -  **Platforms:** Windows, Linux, macOS, Network Devices  -  **ATT&CK:** [T1653](https://attack.mitre.org/techniques/T1653)

## Summary
Adversaries may impair a system's ability to hibernate, reboot, or shut down in order to extend access to infected machines. When a computer enters a dormant state, some or all software and hardware may cease to operate which can disrupt malicious activity.(Citation: Sleep, shut down, hibernate)

Adversaries may abuse system utilities and configuration settings to maintain access by preventing machines from entering a state, such as standby, that can terminate malicious activity.(Citation: Microsoft: Powercfg command-line options)(Citation: systemdsleep Linux)

For example, `powercfg` controls all configurable power system settings on a Windows system and can be abused to prevent an infected host from locking or shutting down.(Citation: Two New Monero Malware Attacks Target Windows and Android Users) Adversaries may also extend system lock screen timeout settings.(Citation: BATLOADER: The Evasive Downloader Malware) Other relevant settings, such as disk and hibernate timeout, can be similarly abused to keep the infected machine running even if no user is active.(Citation: CoinLoader: A Sophisticated Malware Loader Campaign)

Aware that some malware cannot survive system reboots, adversaries may entirely delete files used to invoke system shut down or reboot.(Citation: Condi-Botnet-binaries)

## Role in the attack flow
Used to achieve the **Persistence** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Windows, Linux, macOS, Network Devices.

## Mitigations
- **M1047 Audit** - Auditing is the process of recording activity and systematically reviewing and analyzing the activity and system configurations. The primary purpose of auditing is to detect anomalies and identify potential threats or weaknesses in the environment. Proper auditing configurations can also help to meet compliance requirements. The process of auditing encompasses regular analysis of user behaviors and system logs in support of proactive security measures.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1653
