---
cwe_id: CWE-1316
name: Fabric-Address Map Allows Programming of Unwarranted Overlaps of Protected and Unprotected Ranges
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Bus/Interface Hardware, Not Technology-Specific]
related_capec: [CAPEC-456, CAPEC-679]
url: https://cwe.mitre.org/data/definitions/1316.html
tags: [mitre-cwe, weakness, CWE-1316]
---

# CWE-1316 - Fabric-Address Map Allows Programming of Unwarranted Overlaps of Protected and Unprotected Ranges

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1316](https://cwe.mitre.org/data/definitions/1316.html)

## Description
The address map of the on-chip fabric has protected and unprotected regions overlapping, allowing an attacker to bypass access control to the overlapping portion of the protected region.

## Extended description
Various ranges can be defined in the system-address map, either in the memory or in Memory-Mapped-IO (MMIO) space. These ranges are usually defined using special range registers that contain information, such as base address and size. Address decoding is the process of determining for which range the incoming transaction is destined. To ensure isolation, ranges containing secret data are access-control protected. Occasionally, these ranges could overlap. The overlap could either be intentional (e.g. due to a limited number of range registers or limited choice in choosing size of the range) or unintentional (e.g. introduced by errors). Some hardware designs allow dynamic remapping of address ranges assigned to peripheral MMIO ranges. In such designs, intentional address overlaps can be created through misconfiguration by malicious software. When protected and unprotected ranges overlap, an attacker could send a transaction and potentially compromise the protections in place, violating the principle of least privilege.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Bus/Interface Hardware, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Access Control, Authorization**: Bypass Protection Mechanism, Read Memory, Modify Memory

## Potential mitigations
- **Architecture and Design**: When architecting the address map of the chip, ensure that protected and unprotected ranges are isolated and do not overlap. When designing, ensure that ranges hardcoded in Register-Transfer Level (RTL) do not overlap.
- **Implementation**: Ranges configured by firmware should not overlap. If overlaps are mandatory because of constraints such as a limited number of registers, then ensure that no assets are present in the overlapped portion.
- **Testing**: Validate mitigation actions with robust testing.

## Related attack patterns (CAPEC)
- [CAPEC-456](https://capec.mitre.org/data/definitions/456.html)
- [CAPEC-679](https://capec.mitre.org/data/definitions/679.html)

## Related weaknesses
- CWE-284 (ChildOf)

## Observed examples (CVE)
- **CVE-2009-4419**: Attacker can modify MCHBAR register to overlap with an attacker-controlled region, which modification prevents the SENTER instruction from properly applying VT-d protection while a Measured Launch Environment is being launched.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1316.html
