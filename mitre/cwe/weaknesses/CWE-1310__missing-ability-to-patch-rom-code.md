---
cwe_id: CWE-1310
name: Missing Ability to Patch ROM Code
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip]
related_capec: [CAPEC-682]
url: https://cwe.mitre.org/data/definitions/1310.html
tags: [mitre-cwe, weakness, CWE-1310]
---

# CWE-1310 - Missing Ability to Patch ROM Code

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1310](https://cwe.mitre.org/data/definitions/1310.html)

## Description
Missing an ability to patch ROM code may leave a System or System-on-Chip (SoC) in a vulnerable state.

## Extended description
A System or System-on-Chip (SoC) that implements a boot process utilizing security mechanisms such as Root-of-Trust (RoT) typically starts by executing code from a Read-only-Memory (ROM) component. The code in ROM is immutable, hence any security vulnerabilities discovered in the ROM code can never be fixed for the systems that are already in use. A common weakness is that the ROM does not have the ability to patch if security vulnerabilities are uncovered after the system gets shipped. This leaves the system in a vulnerable state where an adversary can compromise the SoC.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip

## Common consequences
- **Other**: Varies by Context, Reduce Maintainability

## Potential mitigations
- **Architecture and Design, Implementation**: Secure patch support to allow ROM code to be patched on the next boot.
- **Architecture and Design, Implementation**: Support patches that can be programmed in-field or during manufacturing through hardware fuses. This feature can be used for limited patching of devices after shipping, or for the next batch of silicon devices manufactured, without changing the full device ROM.

## Related attack patterns (CAPEC)
- [CAPEC-682](https://capec.mitre.org/data/definitions/682.html)

## Related weaknesses
- CWE-1329 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1310.html
