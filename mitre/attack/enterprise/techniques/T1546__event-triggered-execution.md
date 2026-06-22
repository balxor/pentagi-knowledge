---
attack_id: T1546
name: Event Triggered Execution
type: technique
parent: null
tactics: [Privilege Escalation, Persistence]
platforms: [Linux, macOS, Windows, SaaS, IaaS, Office Suite]
url: https://attack.mitre.org/techniques/T1546
tags: [mitre-attack, technique, T1546]
---

# T1546 - Event Triggered Execution

**Tactic(s):** Privilege Escalation, Persistence  ·  **Platforms:** Linux, macOS, Windows, SaaS, IaaS, Office Suite  ·  **ATT&CK:** [T1546](https://attack.mitre.org/techniques/T1546)

## Summary
Adversaries may establish persistence and/or elevate privileges using system mechanisms that trigger execution based on specific events. Various operating systems have means to monitor and subscribe to events such as logons or other user activity such as running specific applications/binaries. Cloud environments may also support various functions and services that monitor and can be invoked in response to specific cloud events.(Citation: Backdooring an AWS account)(Citation: Varonis Power Automate Data Exfiltration)(Citation: Microsoft DART Case Report 001)

Adversaries may abuse these mechanisms as a means of maintaining persistent access to a victim via repeatedly executing malicious code. After gaining access to a victim system, adversaries may create/modify event triggers to point to malicious content that will be executed whenever the event trigger is invoked.(Citation: FireEye WMI 2015)(Citation: Malware Persistence on OS X)(Citation: amnesia malware)

Since the execution can be proxied by an account with higher permissions, such as SYSTEM or service accounts, an adversary may be able to abuse these triggered execution mechanisms to escalate their privileges.

## Role in the attack flow
Used to achieve the **Privilege Escalation, Persistence** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows, SaaS, IaaS, Office Suite.

## Mitigations
- **M1026 Privileged Account Management** - Privileged Account Management focuses on implementing policies, controls, and tools to securely manage privileged accounts (e.g., SYSTEM, root, or administrative accounts). This includes restricting access, limiting the scope of permissions, monitoring privileged account usage, and ensuring accountability through logging and auditing.This mitigation can be implemented through the following measures:
- **M1051 Update Software** - Software updates ensure systems are protected against known vulnerabilities by applying patches and upgrades provided by vendors. Regular updates reduce the attack surface and prevent adversaries from exploiting known security gaps. This includes patching operating systems, applications, drivers, and firmware. This mitigation can be implemented through the following measures:

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1546
