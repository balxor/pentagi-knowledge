---
attack_id: T1030
name: Data Transfer Size Limits
type: technique
parent: null
tactics: [Exfiltration]
platforms: [Linux, macOS, Windows, ESXi]
url: https://attack.mitre.org/techniques/T1030
tags: [mitre-attack, technique, T1030]
---

# T1030 - Data Transfer Size Limits

**Tactic(s):** Exfiltration  ·  **Platforms:** Linux, macOS, Windows, ESXi  ·  **ATT&CK:** [T1030](https://attack.mitre.org/techniques/T1030)

## Summary
An adversary may exfiltrate data in fixed size chunks instead of whole files or limit packet sizes below certain thresholds. This approach may be used to avoid triggering network data transfer threshold alerts.

## Role in the attack flow
Used to achieve the **Exfiltration** objective. An autonomous agent invokes this when its current sub-goal matches that tactic and the target platform is one of: Linux, macOS, Windows, ESXi.

## Mitigations
- **M1031 Network Intrusion Prevention** - Use intrusion detection signatures to block traffic at network boundaries.

Source: MITRE ATT&CK - https://attack.mitre.org/techniques/T1030
