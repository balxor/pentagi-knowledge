---
attack_id: T0883
name: Internet Accessible Device
type: technique
parent: null
tactics: [Initial Access]
platforms: [None]
url: https://attack.mitre.org/techniques/T0883
tags: [mitre-attack, technique, T0883]
---

# T0883 - Internet Accessible Device

**Tactic(s):** Initial Access  -  **Platforms:** None  -  **ATT&CK:** [T0883](https://attack.mitre.org/techniques/T0883)

## Summary
Adversaries may gain access into industrial environments through systems exposed directly to the internet for remote access rather than through [External Remote Services](https://attack.mitre.org/techniques/T0822). Internet Accessible Devices are exposed to the internet unintentionally or intentionally without adequate protections. This may allow for adversaries to move directly into the control system network. Access onto these devices is accomplished without the use of exploits, these would be represented within the [Exploit Public-Facing Application](https://attack.mitre.org/techniques/T0819) technique.

Adversaries may leverage built in functions for remote access which may not be protected or utilize minimal legacy protections that may be targeted. (Citation: NCCIC January 2014) These services may be discoverable through the use of online scanning tools. 

In the case of the Bowman dam incident, adversaries leveraged access to the dam control network through a cellular modem. Access to the device was protected by password authentication, although the application was vulnerable to brute forcing. (Citation: NCCIC January 2014) (Citation: Danny Yadron December 2015) (Citation: Mark Thompson March 2016)

In Trend Micros manufacturing deception operations adversaries were detected leveraging direct internet access to an ICS environment through the exposure of operational protocols such as Siemens S7, Omron FINS, and EtherNet/IP, in addition to misconfigured VNC access. (Citation: Stephen Hilt, Federico Maggi, Charles Perine, Lord Remorin, Martin Rsler, and Rainer Vosseler)

## Role in the attack flow
Used to achieve the **Initial Access** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0930 Network Segmentation** - Architect sections of the network to isolate critical systems, functions, or resources. Use physical and logical segmentation to prevent access to potentially sensitive systems and information. Use a DMZ to contain any internet-facing services that should not be exposed from the internal network.  Restrict network access to only required systems and services. In addition, prevent systems from other networks or business functions (e.g., enterprise) from accessing critical process control systems. For example, in IEC 62443, systems within the same secure level should be grouped into a zone, and access to that zone is restricted by a conduit, or mechanism to restrict data flows between zones by segmenting the network. (Citation: IEC February 2019) (Citation: IEC August 2013)

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0883
