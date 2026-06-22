---
attack_id: TA0005
name: Stealth
type: tactic
shortname: stealth
killchain_order: 7
url: https://attack.mitre.org/tactics/TA0005
tags: [mitre-attack, tactic, stealth]
---

# TA0005 - Stealth (Tactic)

> The adversary is trying to hide and conceal their actions, appearing as normal behavior.

## Goal
The adversary is trying to hide and conceal their actions, appearing as normal behavior.

Stealth consists of techniques that reduce the likelihood of detection by blending in with legitimate activity or minimizing observable signals. These techniques are characterized by concealment behaviors, such as avoiding, obfuscating, or mimicking normal operations, without modifying security controls or compromising collection and monitoring feeds. The goal is to remain indistinguishable from benign activity while leaving defensive systems intact.

## Position in the attack flow
Phase 7 of the ATT&CK kill chain. An autonomous agent selects techniques from this tactic when its current sub-goal matches the objective above.

## Techniques in this tactic (30)
- [T1006](https://attack.mitre.org/techniques/T1006) Direct Volume Access
- [T1014](https://attack.mitre.org/techniques/T1014) Rootkit
- [T1027](https://attack.mitre.org/techniques/T1027) Obfuscated Files or Information
- [T1036](https://attack.mitre.org/techniques/T1036) Masquerading
- [T1055](https://attack.mitre.org/techniques/T1055) Process Injection
- [T1070](https://attack.mitre.org/techniques/T1070) Indicator Removal
- [T1078](https://attack.mitre.org/techniques/T1078) Valid Accounts
- [T1127](https://attack.mitre.org/techniques/T1127) Trusted Developer Utilities Proxy Execution
- [T1134](https://attack.mitre.org/techniques/T1134) Access Token Manipulation
- [T1140](https://attack.mitre.org/techniques/T1140) Deobfuscate/Decode Files or Information
- [T1197](https://attack.mitre.org/techniques/T1197) BITS Jobs
- [T1202](https://attack.mitre.org/techniques/T1202) Indirect Command Execution
- [T1205](https://attack.mitre.org/techniques/T1205) Traffic Signaling
- [T1211](https://attack.mitre.org/techniques/T1211) Exploitation for Stealth
- [T1216](https://attack.mitre.org/techniques/T1216) System Script Proxy Execution
- [T1218](https://attack.mitre.org/techniques/T1218) System Binary Proxy Execution
- [T1220](https://attack.mitre.org/techniques/T1220) XSL Script Processing
- [T1221](https://attack.mitre.org/techniques/T1221) Template Injection
- [T1480](https://attack.mitre.org/techniques/T1480) Execution Guardrails
- [T1497](https://attack.mitre.org/techniques/T1497) Virtualization/Sandbox Evasion
- [T1535](https://attack.mitre.org/techniques/T1535) Unused/Unsupported Cloud Regions
- [T1542](https://attack.mitre.org/techniques/T1542) Pre-OS Boot
- [T1564](https://attack.mitre.org/techniques/T1564) Hide Artifacts
- [T1574](https://attack.mitre.org/techniques/T1574) Hijack Execution Flow
- [T1612](https://attack.mitre.org/techniques/T1612) Build Image on Host
- [T1620](https://attack.mitre.org/techniques/T1620) Reflective Code Loading
- [T1622](https://attack.mitre.org/techniques/T1622) Debugger Evasion
- [T1678](https://attack.mitre.org/techniques/T1678) Delay Execution
- [T1679](https://attack.mitre.org/techniques/T1679) Selective Exclusion
- [T1684](https://attack.mitre.org/techniques/T1684) Social Engineering

Source: MITRE ATT&CK - https://attack.mitre.org/tactics/TA0005
