---
attack_id: T1104
name: Multi-Stage Channels
type: technique
parent: null
tactics: [Command and Control]
platforms: [Linux, macOS, Windows, ESXi]
url: https://attack.mitre.org/techniques/T1104
tags: [mitre-attack, technique, T1104]
---

# T1104 - Multi-Stage Channels

**Tactic(s):** Command and Control  ·  **Platforms:** Linux, macOS, Windows, ESXi  ·  **ATT&CK:** [T1104](https://attack.mitre.org/techniques/T1104)

## Summary
Adversaries may create multiple stages for command and control that are employed under different conditions or for certain functions. Use of multiple stages may obfuscate the command and control channel to make detection more difficult.

Remote access tools will call back to the first-stage command and control server for instructions. The first stage may have automated capabilities to collect basic host information, update tools, and upload additional files. A second remote access tool (RAT) could be uploaded at that point to redirect the host to the second-stage command and control server. The second stage will likely be more fully featured and allow the adversary to interact with the system through a reverse shell and additional RAT features.

The different stages will likely be hosted separately with no overlapping infrastructure. The loader may also have backup first-stage callbacks or [Fallback Channels](https://attack.mitre.org/techniques/T1008) in case the original first-stage communication path is discovered and blocked.

## Role in the attack flow
Used to achieve the **Command and Control** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows, ESXi.

## Mitigations
- **M1031 Network Intrusion Prevention** - Use intrusion detection signatures to block traffic at network boundaries.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1104
