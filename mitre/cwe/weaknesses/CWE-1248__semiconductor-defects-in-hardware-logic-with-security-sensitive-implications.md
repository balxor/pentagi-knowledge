---
cwe_id: CWE-1248
name: Semiconductor Defects in Hardware Logic with Security-Sensitive Implications
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-624, CAPEC-625]
url: https://cwe.mitre.org/data/definitions/1248.html
tags: [mitre-cwe, weakness, CWE-1248]
---

# CWE-1248 - Semiconductor Defects in Hardware Logic with Security-Sensitive Implications

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1248](https://cwe.mitre.org/data/definitions/1248.html)

## Description
The security-sensitive hardware module contains semiconductor defects.

## Extended description
A semiconductor device can fail for various reasons. While some are manufacturing and packaging defects, the rest are due to prolonged use or usage under extreme conditions. Some mechanisms that lead to semiconductor defects include encapsulation failure, die-attach failure, wire-bond failure, bulk-silicon defects, oxide-layer faults, aluminum-metal faults (including electromigration, corrosion of aluminum, etc.), and thermal/electrical stress. These defects manifest as faults on chip-internal signals or registers, have the effect of inputs, outputs, or intermediate signals being always 0 or always 1, and do not switch as expected.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Availability, Access Control**: DoS: Instability

## Potential mitigations
- **Testing**: While semiconductor-manufacturing companies implement several mechanisms to continuously improve the semiconductor manufacturing process to ensure reduction of defects, some defects can only be fixed after manufacturing. Post-manufacturing testing of silicon die is critical. Fault models such as stuck-at-0 or stuck-at-1 must be used to develop post-manufacturing test cases and achieve good coverage. Once the silicon packaging is done, extensive post-silicon testing must be performed to ensure that hardware logic implementing security functionalities is defect-free.
- **Operation**: Operating the hardware outside device specification, such as at extremely high temperatures, voltage, etc., accelerates semiconductor degradation and results in defects. When these defects manifest as faults in security-critical, hardware modules, it results in compromise of security guarantees. Thus, operating the device within the specification is important.

## Related attack patterns (CAPEC)
- [CAPEC-624](https://capec.mitre.org/data/definitions/624.html)
- [CAPEC-625](https://capec.mitre.org/data/definitions/625.html)

## Related weaknesses
- CWE-693 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1248.html
