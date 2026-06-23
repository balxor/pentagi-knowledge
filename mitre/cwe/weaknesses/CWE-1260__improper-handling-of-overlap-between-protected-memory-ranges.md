---
cwe_id: CWE-1260
name: Improper Handling of Overlap Between Protected Memory Ranges
type: weakness
abstraction: Base
status: Stable
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Memory Hardware, Processor Hardware]
related_capec: [CAPEC-456, CAPEC-679]
url: https://cwe.mitre.org/data/definitions/1260.html
tags: [mitre-cwe, weakness, CWE-1260]
---

# CWE-1260 - Improper Handling of Overlap Between Protected Memory Ranges

**Abstraction:** Base  -  **Status:** Stable  -  **CWE:** [CWE-1260](https://cwe.mitre.org/data/definitions/1260.html)

## Description
The product allows address regions to overlap, which can result in the bypassing of intended memory protection.

## Extended description
Isolated memory regions and access control (read/write) policies are used by hardware to protect privileged software. Software components are often allowed to change or remap memory region definitions in order to enable flexible and dynamically changeable memory management by system software. If a software component running at lower privilege can program a memory address region to overlap with other memory regions used by software running at higher privilege, privilege escalation may be available to attackers. The memory protection unit (MPU) logic can incorrectly handle such an address overlap and allow the lower-privilege software to read or write into the protected memory region, resulting in privilege escalation attack. An address overlap weakness can also be used to launch a denial of service attack on the higher-privilege software memory regions.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Memory Hardware, Processor Hardware

## Common consequences
- **Confidentiality, Integrity, Availability**: Modify Memory, Read Memory, DoS: Instability

## Potential mitigations
- **Architecture and Design**: Ensure that memory regions are isolated as intended and that access control (read/write) policies are used by hardware to protect privileged software.
- **Implementation**: For all of the programmable memory protection regions, the memory protection unit (MPU) design can define a priority scheme. For example: if three memory regions can be programmed (Region_0, Region_1, and Region_2), the design can enforce a priority scheme, such that, if a system address is within multiple regions, then the region with the lowest ID takes priority and the access-control policy of that region will be applied. In some MPU designs, the priority scheme can also be programmed by trusted software. Hardware logic or trusted firmware can also check for region definitions and block programming of memory regions with overlapping addresses. The memory-access-control-check filter can also be designed to apply a policy filter to all of the overlapping ranges, i.e., if an address is within Region_0 and Region_1, then access to this address is only granted if both Region_0 and Region_1 policies allow the access.

## Related attack patterns (CAPEC)
- [CAPEC-456](https://capec.mitre.org/data/definitions/456.html)
- [CAPEC-679](https://capec.mitre.org/data/definitions/679.html)

## Related weaknesses
- CWE-284 (ChildOf)
- CWE-119 (CanPrecede)

## Observed examples (CVE)
- **CVE-2008-7096**: virtualization product allows compromise of hardware product by accessing certain remapping registers.
- **[REF-1100]**: processor design flaw allows ring 0 code to access more privileged rings by causing a register window to overlap a range of protected system RAM [REF-1100]

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1260.html
