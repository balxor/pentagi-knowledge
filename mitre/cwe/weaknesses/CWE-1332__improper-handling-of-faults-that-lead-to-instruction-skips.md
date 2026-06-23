---
cwe_id: CWE-1332
name: Improper Handling of Faults that Lead to Instruction Skips
type: weakness
abstraction: Base
status: Stable
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip]
related_capec: [CAPEC-624, CAPEC-625]
url: https://cwe.mitre.org/data/definitions/1332.html
tags: [mitre-cwe, weakness, CWE-1332]
---

# CWE-1332 - Improper Handling of Faults that Lead to Instruction Skips

**Abstraction:** Base  -  **Status:** Stable  -  **CWE:** [CWE-1332](https://cwe.mitre.org/data/definitions/1332.html)

## Description
The device is missing or incorrectly implements circuitry or sensors that detect and mitigate the skipping of security-critical CPU instructions when they occur.

## Extended description
The operating conditions of hardware may change in ways that cause unexpected behavior to occur, including the skipping of security-critical CPU instructions. Generally, this can occur due to electrical disturbances or when the device operates outside of its expected conditions. In practice, application code may contain conditional branches that are security-sensitive (e.g., accepting or rejecting a user-provided password). These conditional branches are typically implemented by a single conditional branch instruction in the program binary which, if skipped, may lead to effectively flipping the branch condition - i.e., causing the wrong security-sensitive branch to be taken. This affects processes such as firmware authentication, password verification, and other security-sensitive decision points. Attackers can use fault injection techniques to alter the operating conditions of hardware so that security-critical instructions are skipped more frequently or more reliably than they would in a "natural" setting.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip

## Common consequences
- **Confidentiality, Integrity, Authentication**: Bypass Protection Mechanism, Alter Execution Logic, Unexpected State

## Potential mitigations
- **Architecture and Design**: Design strategies for ensuring safe failure if inputs, such as Vcc, are modified out of acceptable ranges.
- **Architecture and Design**: Design strategies for ensuring safe behavior if instructions attempt to be skipped.
- **Architecture and Design**: Identify mission critical secrets that should be wiped if faulting is detected, and design a mechanism to do the deletion.
- **Implementation**: Add redundancy by performing an operation multiple times, either in space or time, and perform majority voting. Additionally, make conditional instruction timing unpredictable.
- **Implementation**: Use redundant operations or canaries to detect and respond to faults.
- **Implementation**: Ensure that fault mitigations are strong enough in practice. For example, a low power detection mechanism that takes 50 clock cycles to trigger at lower voltages may be an insufficient security mechanism if the instruction counter has already progressed with no other CPU activity occurring.

## Related attack patterns (CAPEC)
- [CAPEC-624](https://capec.mitre.org/data/definitions/624.html)
- [CAPEC-625](https://capec.mitre.org/data/definitions/625.html)

## Related weaknesses
- CWE-1384 (ChildOf)
- CWE-1247 (PeerOf)

## Observed examples (CVE)
- **CVE-2019-15894**: fault injection attack bypasses the verification mode, potentially allowing arbitrary code execution.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1332.html
