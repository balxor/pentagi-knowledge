---
cwe_id: CWE-1280
name: Access Control Check Implemented After Asset is Accessed
type: weakness
abstraction: Base
status: Incomplete
languages: [Verilog, VHDL, Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-180]
url: https://cwe.mitre.org/data/definitions/1280.html
tags: [mitre-cwe, weakness, CWE-1280]
---

# CWE-1280 - Access Control Check Implemented After Asset is Accessed

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1280](https://cwe.mitre.org/data/definitions/1280.html)

## Description
A product's hardware-based access control check occurs after the asset has been accessed.

## Extended description
The product implements a hardware-based access control check. The asset should be accessible only after the check is successful. If, however, this operation is not atomic and the asset is accessed before the check is complete, the security of the system may be compromised.

## Applicable platforms / languages
Verilog, VHDL, Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Access Control, Confidentiality, Integrity**: Modify Memory, Read Memory, Modify Application Data, Read Application Data, Gain Privileges or Assume Identity, Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: Implement the access control check first. Access should only be given to asset if agent is authorized.

## Related attack patterns (CAPEC)
- [CAPEC-180](https://capec.mitre.org/data/definitions/180.html)

## Related weaknesses
- CWE-696 (ChildOf)
- CWE-284 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1280.html
