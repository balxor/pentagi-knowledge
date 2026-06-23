---
cwe_id: CWE-1283
name: Mutable Attestation or Measurement Reporting Data
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-680]
url: https://cwe.mitre.org/data/definitions/1283.html
tags: [mitre-cwe, weakness, CWE-1283]
---

# CWE-1283 - Mutable Attestation or Measurement Reporting Data

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1283](https://cwe.mitre.org/data/definitions/1283.html)

## Description
The register contents used for attestation or measurement reporting data to verify boot flow are modifiable by an adversary.

## Extended description
A System-on-Chip (SoC) implements secure boot or verified boot. During this boot flow, the SoC often measures the code that it authenticates. The measurement is usually done by calculating the one-way hash of the code binary and extending it to the previous hash. The hashing algorithm should be a Secure One-Way hash function. The final hash, i.e., the value obtained after the completion of the boot flow, serves as the measurement data used in reporting or in attestation. The calculated hash is often stored in registers that can later be read by the party of interest to determine tampering of the boot flow. A common weakness is that the contents in these registers are modifiable by an adversary, thus spoofing the measurement.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Memory, Read Application Data

## Potential mitigations
- **Architecture and Design**: Measurement data should be stored in registers that are read-only or otherwise have access controls that prevent modification by an untrusted agent.

## Related attack patterns (CAPEC)
- [CAPEC-680](https://capec.mitre.org/data/definitions/680.html)

## Related weaknesses
- CWE-284 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1283.html
