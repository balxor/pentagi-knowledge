---
cwe_id: CWE-1315
name: Improper Setting of Bus Controlling Capability in Fabric End-point
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-1, CAPEC-180]
url: https://cwe.mitre.org/data/definitions/1315.html
tags: [mitre-cwe, weakness, CWE-1315]
---

# CWE-1315 - Improper Setting of Bus Controlling Capability in Fabric End-point

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1315](https://cwe.mitre.org/data/definitions/1315.html)

## Description
The bus controller enables bits in the fabric end-point to allow responder devices to control transactions on the fabric.

## Extended description
To support reusability, certain fabric interfaces and end points provide a configurable register bit that allows IP blocks connected to the controller to access other peripherals connected to the fabric. This allows the end point to be used with devices that function as a controller or responder. If this bit is set by default in hardware, or if firmware incorrectly sets it later, a device intended to be a responder on a fabric is now capable of controlling transactions to other devices and might compromise system security.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Access Control**: Modify Memory, Read Memory, Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: For responder devices, the register bit in the fabric end-point that enables the bus controlling capability must be set to 0 by default. This bit should not be set during secure-boot flows. Also, writes to this register must be access-protected to prevent malicious modifications to obtain bus-controlling capability.
- **Implementation**: For responder devices, the register bit in the fabric end-point that enables the bus controlling capability must be set to 0 by default. This bit should not be set during secure-boot flows. Also, writes to this register must be access-protected to prevent malicious modifications to obtain bus-controlling capability.
- **System Configuration**: For responder devices, the register bit in the fabric end-point that enables the bus controlling capability must be set to 0 by default. This bit should not be set during secure-boot flows. Also, writes to this register must be access-protected to prevent malicious modifications to obtain bus-controlling capability.

## Related attack patterns (CAPEC)
- [CAPEC-1](https://capec.mitre.org/data/definitions/1.html)
- [CAPEC-180](https://capec.mitre.org/data/definitions/180.html)

## Related weaknesses
- CWE-284 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1315.html
