---
cwe_id: CWE-1279
name: Cryptographic Operations are run Before Supporting Units are Ready
type: weakness
abstraction: Base
status: Incomplete
languages: [Verilog, VHDL, Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Processor Hardware, Not Technology-Specific]
related_capec: [CAPEC-97]
url: https://cwe.mitre.org/data/definitions/1279.html
tags: [mitre-cwe, weakness, CWE-1279]
---

# CWE-1279 - Cryptographic Operations are run Before Supporting Units are Ready

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1279](https://cwe.mitre.org/data/definitions/1279.html)

## Description
Performing cryptographic operations without ensuring that the supporting inputs are ready to supply valid data may compromise the cryptographic result.

## Extended description
Many cryptographic hardware units depend upon other hardware units to supply information to them to produce a securely encrypted result. For example, a cryptographic unit that depends on an external random-number-generator (RNG) unit for entropy must wait until the RNG unit is producing random numbers. If a cryptographic unit retrieves a private encryption key from a fuse unit, the fuse unit must be up and running before a key may be supplied.

## Applicable platforms / languages
Verilog, VHDL, Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Processor Hardware, Not Technology-Specific

## Common consequences
- **Access Control, Confidentiality, Integrity, Availability, Accountability, Authentication, Authorization, Non-Repudiation**: Varies by Context

## Potential mitigations
- **Architecture and Design**: Best practices should be used to design cryptographic systems.
- **Implementation**: Continuously ensuring that cryptographic inputs are supplying valid information is necessary to ensure that the encrypted output is secure.

## Related attack patterns (CAPEC)
- [CAPEC-97](https://capec.mitre.org/data/definitions/97.html)

## Related weaknesses
- CWE-696 (ChildOf)
- CWE-665 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1279.html
