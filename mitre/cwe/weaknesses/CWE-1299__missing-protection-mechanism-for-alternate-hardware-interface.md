---
cwe_id: CWE-1299
name: Missing Protection Mechanism for Alternate Hardware Interface
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Microcontroller Hardware, Processor Hardware, Bus/Interface Hardware, Not Technology-Specific]
related_capec: [CAPEC-457, CAPEC-554]
url: https://cwe.mitre.org/data/definitions/1299.html
tags: [mitre-cwe, weakness, CWE-1299]
---

# CWE-1299 - Missing Protection Mechanism for Alternate Hardware Interface

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1299](https://cwe.mitre.org/data/definitions/1299.html)

## Description
The lack of protections on alternate paths to access control-protected assets (such as unprotected shadow registers and other external facing unguarded interfaces) allows an attacker to bypass existing protections to the asset that are only performed against the primary path.

## Extended description
An asset inside a chip might have access-control protections through one interface. However, if all paths to the asset are not protected, an attacker might compromise the asset through alternate paths. These alternate paths could be through shadow or mirror registers inside the IP core, or could be paths from other external-facing interfaces to the IP core or SoC. Consider an SoC with various interfaces such as UART, SMBUS, PCIe, USB, etc. If access control is implemented for SoC internal registers only over the PCIe interface, then an attacker could still modify the SoC internal registers through alternate paths by coming through interfaces such as UART, SMBUS, USB, etc. Alternatively, attackers might be able to bypass existing protections by exploiting unprotected, shadow registers. Shadow registers and mirror registers typically refer to registers that can be accessed from multiple addresses. Writing to or reading from the aliased/mirrored address has the same effect as writing to the address of the main register. They are typically implemented within an IP core or SoC to temporarily hold certain data. These data will later be updated to the main register, and both registers will be in synch. If the shadow registers are not access-protected, attackers could simply initiate transactions to the shadow registers and compromise system security.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Microcontroller Hardware, Processor Hardware, Bus/Interface Hardware, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control**: Modify Memory, Read Memory, DoS: Resource Consumption (Other), Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity, Alter Execution Logic, Bypass Protection Mechanism, Quality Degradation

## Potential mitigations
- **Requirements**: Protect assets from accesses against all potential interfaces and alternate paths.
- **Architecture and Design**: Protect assets from accesses against all potential interfaces and alternate paths.
- **Implementation**: Protect assets from accesses against all potential interfaces and alternate paths.

## Related attack patterns (CAPEC)
- [CAPEC-457](https://capec.mitre.org/data/definitions/457.html)
- [CAPEC-554](https://capec.mitre.org/data/definitions/554.html)

## Related weaknesses
- CWE-1191 (PeerOf)
- CWE-420 (ChildOf)
- CWE-288 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-38399**: Missing protection mechanism on serial connection allows for arbitrary OS command execution.
- **CVE-2020-9285**: Mini-PCI Express slot does not restrict direct memory access.
- **CVE-2020-8004**: When the internal flash is protected by blocking access on the Data Bus (DBUS), it can still be indirectly accessed through the Instruction Bus (IBUS).
- **CVE-2017-18293**: When GPIO is protected by blocking access to corresponding GPIO resource registers, protection can be bypassed by writing to the corresponding banked GPIO registers instead.
- **CVE-2020-15483**: monitor device allows access to physical UART debug port without authentication

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1299.html
