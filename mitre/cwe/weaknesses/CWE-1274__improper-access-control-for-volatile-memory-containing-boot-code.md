---
cwe_id: CWE-1274
name: Improper Access Control for Volatile Memory Containing Boot Code
type: weakness
abstraction: Base
status: Stable
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-456, CAPEC-679]
url: https://cwe.mitre.org/data/definitions/1274.html
tags: [mitre-cwe, weakness, CWE-1274]
---

# CWE-1274 - Improper Access Control for Volatile Memory Containing Boot Code

**Abstraction:** Base  -  **Status:** Stable  -  **CWE:** [CWE-1274](https://cwe.mitre.org/data/definitions/1274.html)

## Description
The product conducts a secure-boot process that transfers bootloader code from Non-Volatile Memory (NVM) into Volatile Memory (VM), but it does not have sufficient access control or other protections for the Volatile Memory.

## Extended description
Adversaries could bypass the secure-boot process and execute their own untrusted, malicious boot code. As a part of a secure-boot process, the read-only-memory (ROM) code for a System-on-Chip (SoC) or other system fetches bootloader code from Non-Volatile Memory (NVM) and stores the code in Volatile Memory (VM), such as dynamic, random-access memory (DRAM) or static, random-access memory (SRAM). The NVM is usually external to the SoC, while the VM is internal to the SoC. As the code is transferred from NVM to VM, it is authenticated by the SoC's ROM code.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Access Control, Integrity**: Modify Memory, Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Ensure that the design of volatile-memory protections is enough to prevent modification from an adversary or untrusted code.
- **Testing**: Test the volatile-memory protections to ensure they are safe from modification or untrusted code.

## Related attack patterns (CAPEC)
- [CAPEC-456](https://capec.mitre.org/data/definitions/456.html)
- [CAPEC-679](https://capec.mitre.org/data/definitions/679.html)

## Related weaknesses
- CWE-284 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-2267**: Locked memory regions may be modified through other interfaces in a secure-boot-loader image due to improper access control.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1274.html
