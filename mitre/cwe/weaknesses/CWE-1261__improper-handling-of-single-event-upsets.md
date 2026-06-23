---
cwe_id: CWE-1261
name: Improper Handling of Single Event Upsets
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1261.html
tags: [mitre-cwe, weakness, CWE-1261]
---

# CWE-1261 - Improper Handling of Single Event Upsets

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1261](https://cwe.mitre.org/data/definitions/1261.html)

## Description
The hardware logic does not effectively handle when single-event upsets (SEUs) occur.

## Extended description
Technology trends such as CMOS-transistor down-sizing, use of new materials, and system-on-chip architectures continue to increase the sensitivity of systems to soft errors. These errors are random, and their causes might be internal (e.g., interconnect coupling) or external (e.g., cosmic radiation). These soft errors are not permanent in nature and cause temporary bit flips known as single-event upsets (SEUs). SEUs are induced errors in circuits caused when charged particles lose energy by ionizing the medium through which they pass, leaving behind a wake of electron-hole pairs that cause temporary failures. If these failures occur in security-sensitive modules in a chip, it might compromise the security guarantees of the chip. For instance, these temporary failures could be bit flips that change the privilege of a regular user to root.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Availability, Access Control**: DoS: Crash, Exit, or Restart, DoS: Instability, Gain Privileges or Assume Identity, Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Implement triple-modular redundancy around security-sensitive modules.
- **Architecture and Design**: SEUs mostly affect SRAMs. For SRAMs storing security-critical data, implement Error-Correcting-Codes (ECC) and Address Interleaving.

## Related weaknesses
- CWE-1384 (ChildOf)
- CWE-1254 (PeerOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1261.html
