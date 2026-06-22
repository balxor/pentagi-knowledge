---
attack_id: T0814
name: Denial of Service
type: technique
parent: null
tactics: [Inhibit Response Function]
platforms: [None]
url: https://attack.mitre.org/techniques/T0814
tags: [mitre-attack, technique, T0814]
---

# T0814 - Denial of Service

**Tactic(s):** Inhibit Response Function  -  **Platforms:** None  -  **ATT&CK:** [T0814](https://attack.mitre.org/techniques/T0814)

## Summary
Adversaries may perform Denial-of-Service (DoS) attacks to disrupt expected device functionality. Examples of DoS attacks include overwhelming the target device with a high volume of requests in a short time period and sending the target device a request it does not know how to handle. Disrupting device state may temporarily render it unresponsive, possibly lasting until a reboot can occur. When placed in this state, devices may be unable to send and receive requests, and may not perform expected response functions in reaction to other events in the environment. 

Some ICS devices are particularly sensitive to DoS events, and may become unresponsive in reaction to even a simple ping sweep. Adversaries may also attempt to execute a Permanent Denial-of-Service (PDoS) against certain devices, such as in the case of the BrickerBot malware. (Citation: ICS-CERT April 2017) 

Adversaries may exploit a software vulnerability to cause a denial of service by taking advantage of a programming error in a program, service, or within the operating system software or kernel itself to execute adversary-controlled code. Vulnerabilities may exist in software that can be used to cause a denial of service condition. 

Adversaries may have prior knowledge about industrial protocols or control devices used in the environment through [Remote System Information Discovery](https://attack.mitre.org/techniques/T0888). There are examples of adversaries remotely causing a [Device Restart/Shutdown](https://attack.mitre.org/techniques/T0816) by exploiting a vulnerability that induces uncontrolled resource consumption. (Citation: ICS-CERT August 2018) (Citation: Common Weakness Enumeration January 2019) (Citation: MITRE March 2018)

## Role in the attack flow
Used to achieve the **Inhibit Response Function** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: None.

## Mitigations
- **M0815 Watchdog Timers** - Utilize watchdog timers to ensure devices can quickly detect whether a system is unresponsive.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T0814
