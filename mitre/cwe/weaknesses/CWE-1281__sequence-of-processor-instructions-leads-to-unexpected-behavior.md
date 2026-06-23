---
cwe_id: CWE-1281
name: Sequence of Processor Instructions Leads to Unexpected Behavior
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific, Processor Hardware]
related_capec: [CAPEC-212]
url: https://cwe.mitre.org/data/definitions/1281.html
tags: [mitre-cwe, weakness, CWE-1281]
---

# CWE-1281 - Sequence of Processor Instructions Leads to Unexpected Behavior

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1281](https://cwe.mitre.org/data/definitions/1281.html)

## Description
Specific combinations of processor instructions lead to undesirable behavior such as locking the processor until a hard reset performed.

## Extended description
If the instruction set architecture (ISA) and processor logic are not designed carefully and tested thoroughly, certain combinations of instructions may lead to locking the processor or other unexpected and undesirable behavior. Upon encountering unimplemented instruction opcodes or illegal instruction operands, the processor should throw an exception and carry on without negatively impacting security. However, specific combinations of legal and illegal instructions may cause unexpected behavior with security implications such as allowing unprivileged programs to completely lock the CPU.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific, Processor Hardware

## Common consequences
- **Integrity, Availability**: Varies by Context

## Potential mitigations
- **Testing**: Implement a rigorous testing strategy that incorporates randomization to explore instruction sequences that are unlikely to appear in normal workloads in order to identify halt and catch fire instruction sequences.
- **Patching and Maintenance**: Patch operating system to avoid running Halt and Catch Fire type sequences or to mitigate the damage caused by unexpected behavior. See [REF-1108].

## Related attack patterns (CAPEC)
- [CAPEC-212](https://capec.mitre.org/data/definitions/212.html)

## Related weaknesses
- CWE-691 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-26339**: A bug in AMD CPU's core logic allows a potential DoS by using a specific x86 instruction sequence to hang the processor
- **CVE-1999-1476**: A bug in some Intel Pentium processors allow DoS (hang) via an invalid "CMPXCHG8B" instruction, causing a deadlock

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1281.html
