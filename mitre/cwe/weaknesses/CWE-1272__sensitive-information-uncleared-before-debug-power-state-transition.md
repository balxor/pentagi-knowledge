---
cwe_id: CWE-1272
name: Sensitive Information Uncleared Before Debug/Power State Transition
type: weakness
abstraction: Base
status: Stable
languages: [VHDL, Verilog, Hardware Description Language, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-150, CAPEC-37, CAPEC-545, CAPEC-546]
url: https://cwe.mitre.org/data/definitions/1272.html
tags: [mitre-cwe, weakness, CWE-1272]
---

# CWE-1272 - Sensitive Information Uncleared Before Debug/Power State Transition

**Abstraction:** Base  -  **Status:** Stable  -  **CWE:** [CWE-1272](https://cwe.mitre.org/data/definitions/1272.html)

## Description
The product performs a power or debug state transition, but it does not clear sensitive information that should no longer be accessible due to changes to information access restrictions.

## Extended description
A device or system frequently employs many power and sleep states during its normal operation (e.g., normal power, additional power, low power, hibernate, deep sleep, etc.). A device also may be operating within a debug condition. State transitions can happen from one power or debug state to another. If there is information available in the previous state which should not be available in the next state and is not properly removed before the transition into the next state, sensitive information may leak from the system.

## Applicable platforms / languages
VHDL, Verilog, Hardware Description Language, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control, Accountability, Authentication, Authorization, Non-Repudiation**: Read Memory, Read Application Data

## Potential mitigations
- **Architecture and Design, Implementation**: During state transitions, information not needed in the next state should be removed before the transition to the next state.

## Related attack patterns (CAPEC)
- [CAPEC-150](https://capec.mitre.org/data/definitions/150.html)
- [CAPEC-37](https://capec.mitre.org/data/definitions/37.html)
- [CAPEC-545](https://capec.mitre.org/data/definitions/545.html)
- [CAPEC-546](https://capec.mitre.org/data/definitions/546.html)

## Related weaknesses
- CWE-226 (ChildOf)
- CWE-200 (CanPrecede)

## Observed examples (CVE)
- **CVE-2020-12926**: Product software does not set a flag as per TPM specifications, thereby preventing a failed authorization attempt from being recorded after a loss of power.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1272.html
