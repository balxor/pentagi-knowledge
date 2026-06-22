---
attack_id: T1547
name: Boot or Logon Autostart Execution
type: technique
parent: null
tactics: [Persistence, Privilege Escalation]
platforms: [Linux, macOS, Windows, Network Devices]
url: https://attack.mitre.org/techniques/T1547
tags: [mitre-attack, technique, T1547]
---

# T1547 - Boot or Logon Autostart Execution

**Tactic(s):** Persistence, Privilege Escalation  -  **Platforms:** Linux, macOS, Windows, Network Devices  -  **ATT&CK:** [T1547](https://attack.mitre.org/techniques/T1547)

## Summary
Adversaries may configure system settings to automatically execute a program during system boot or logon to maintain persistence or gain higher-level privileges on compromised systems. Operating systems may have mechanisms for automatically running a program on system boot or account logon.(Citation: Microsoft Run Key)(Citation: MSDN Authentication Packages)(Citation: Microsoft TimeProvider)(Citation: Cylance Reg Persistence Sept 2013)(Citation: Linux Kernel Programming) These mechanisms may include automatically executing programs that are placed in specially designated directories or are referenced by repositories that store configuration information, such as the Windows Registry. An adversary may achieve the same goal by modifying or extending features of the kernel.

Since some boot or logon autostart programs run with higher privileges, an adversary may leverage these to elevate privileges.

## Role in the attack flow
Used to achieve the **Persistence, Privilege Escalation** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows, Network Devices.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1547
