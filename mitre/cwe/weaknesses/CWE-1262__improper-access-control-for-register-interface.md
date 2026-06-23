---
cwe_id: CWE-1262
name: Improper Access Control for Register Interface
type: weakness
abstraction: Base
status: Stable
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-680]
url: https://cwe.mitre.org/data/definitions/1262.html
tags: [mitre-cwe, weakness, CWE-1262]
---

# CWE-1262 - Improper Access Control for Register Interface

**Abstraction:** Base  -  **Status:** Stable  -  **CWE:** [CWE-1262](https://cwe.mitre.org/data/definitions/1262.html)

## Description
The product uses memory-mapped I/O registers that act as an interface to hardware functionality from software, but there is improper access control to those registers.

## Extended description
Software commonly accesses peripherals in a System-on-Chip (SoC) or other device through a memory-mapped register interface. Malicious software could tamper with any security-critical hardware data that is accessible directly or indirectly through the register interface, which could lead to a loss of confidentiality and integrity.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Memory, Read Application Data, Modify Memory, Modify Application Data, Gain Privileges or Assume Identity, Bypass Protection Mechanism, Unexpected State, Alter Execution Logic

## Potential mitigations
- **Architecture and Design**: Design proper policies for hardware register access from software.
- **Implementation**: Ensure that access control policies for register access are implemented in accordance with the specified design.

## Related attack patterns (CAPEC)
- [CAPEC-680](https://capec.mitre.org/data/definitions/680.html)

## Related weaknesses
- CWE-284 (ChildOf)

## Observed examples (CVE)
- **CVE-2014-2915**: virtualization product does not restrict access to debug and other processor registers in the hardware, allowing a crash of the host or guest OS
- **CVE-2021-3011**: virtual interrupt controller in a virtualization product allows crash of host by writing a certain invalid value to a register, which triggers a fatal error instead of returning an error code
- **CVE-2020-12446**: Driver exposes access to Model Specific Register (MSR) registers, allowing admin privileges.
- **CVE-2015-2150**: Virtualization product does not restrict access to PCI command registers, allowing host crash from the guest.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1262.html
