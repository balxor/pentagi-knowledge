---
attack_id: T1464
name: Network Denial of Service
type: technique
parent: null
tactics: [Impact]
platforms: [Android, iOS]
url: https://attack.mitre.org/techniques/T1464
tags: [mitre-attack, technique, T1464]
---

# T1464 - Network Denial of Service

**Tactic(s):** Impact  -  **Platforms:** Android, iOS  -  **ATT&CK:** [T1464](https://attack.mitre.org/techniques/T1464)

## Summary
Adversaries may perform Network Denial of Service (DoS) attacks to degrade or block the availability of targeted resources to users. Network DoS can be performed by exhausting the network bandwidth that services rely on, or by jamming the signal going to or coming from devices. 

A Network DoS will occur when an adversary is able to jam radio signals (e.g. Wi-Fi, cellular, GPS) around a device to prevent it from communicating. For example, to jam cellular signal, an adversary may use a handheld signal jammer, which jam devices within the jammer’s operational range.(Citation: NIST-SP800187) 

Usage of cellular jamming has been documented in several arrests reported in the news.(Citation: CNET-Celljammer)(Citation: NYTimes-Celljam)(Citation: Digitaltrends-Celljam)(Citation: Arstechnica-Celljam)

## Role in the attack flow
Used to achieve the **Impact** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Android, iOS.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1464
