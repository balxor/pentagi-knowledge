---
cwe_id: CWE-1431
name: Driving Intermediate Cryptographic State/Results to Hardware Module Outputs
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not Architecture-Specific, System on Chip]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1431.html
tags: [mitre-cwe, weakness, CWE-1431]
---

# CWE-1431 - Driving Intermediate Cryptographic State/Results to Hardware Module Outputs

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1431](https://cwe.mitre.org/data/definitions/1431.html)

## Description
The product uses a hardware module implementing a cryptographic algorithm that writes sensitive information about the intermediate state or results of its cryptographic operations via one of its output wires (typically the output port containing the final result).

## Applicable platforms / languages
Not Language-Specific, Not Architecture-Specific, System on Chip

## Common consequences
- **Confidentiality**: Read Memory, Read Application Data

## Potential mitigations
- **Architecture and Design**: Designers/developers should add or modify existing control flow logic along any data flow paths that connect "sources" (signals with intermediate cryptographic state/results) with "sinks" (hardware module outputs and other signals outside of trusted cryptographic zone). The control flow logic should only allow cryptographic results to be driven to "sinks" when appropriate conditions are satisfied (typically when the final result for a cryptographic operation has been generated). When the appropriate conditions are not satisfied (i.e., before or during a cryptographic operation), the control flow logic should drive a safe default value to "sinks".
- **Implementation**: Designers/developers should add or modify existing control flow logic along any data flow paths that connect "sources" (signals with intermediate cryptographic state/results) with "sinks" (hardware module outputs and other signals outside of trusted cryptographic zone). The control flow logic should only allow cryptographic results to be driven to "sinks" when appropriate conditions are satisfied (typically when the final result for a cryptographic operation has been generated). When the appropriate conditions are not satisfied (i.e., before or during a cryptographic operation), the control flow logic should drive a safe default value to "sinks".

## Related weaknesses
- CWE-200 (ChildOf)
- CWE-497 (PeerOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1431.html
