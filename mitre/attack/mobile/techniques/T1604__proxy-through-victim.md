---
attack_id: T1604
name: Proxy Through Victim
type: technique
parent: null
tactics: [Defense Evasion]
platforms: [Android]
url: https://attack.mitre.org/techniques/T1604
tags: [mitre-attack, technique, T1604]
---

# T1604 - Proxy Through Victim

**Tactic(s):** Defense Evasion  -  **Platforms:** Android  -  **ATT&CK:** [T1604](https://attack.mitre.org/techniques/T1604)

## Summary
Adversaries may use a compromised device as a proxy server to the Internet. By utilizing a proxy, adversaries hide the true IP address of their C2 server and associated infrastructure from the destination of the network traffic. This masquerades an adversary’s traffic as legitimate traffic originating from the compromised device, which can evade IP-based restrictions and alerts on certain services, such as bank accounts and social media websites.(Citation: Threat Fabric Exobot)

The most common type of proxy is a SOCKS proxy. It can typically be implemented using standard OS-level APIs and 3rd party libraries with no indication to the user. On Android, adversaries can use the `Proxy` API to programmatically establish a SOCKS proxy connection, or lower-level APIs to interact directly with raw sockets.

## Role in the attack flow
Used to achieve the **Defense Evasion** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1604
