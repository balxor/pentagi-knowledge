---
cwe_id: CWE-1193
name: Power-On of Untrusted Execution Core Before Enabling Fabric Access Control
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, System on Chip]
related_capec: [CAPEC-1, CAPEC-180]
url: https://cwe.mitre.org/data/definitions/1193.html
tags: [mitre-cwe, weakness, CWE-1193]
---

# CWE-1193 - Power-On of Untrusted Execution Core Before Enabling Fabric Access Control

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1193](https://cwe.mitre.org/data/definitions/1193.html)

## Description
The product enables components that contain untrusted firmware before memory and fabric access controls have been enabled.

## Extended description
After initial reset, System-on-Chip (SoC) fabric access controls and other security features need to be programmed by trusted firmware as part of the boot sequence. If untrusted IPs or peripheral microcontrollers are enabled first, then the untrusted component can master transactions on the hardware bus and target memory or other assets to compromise the SoC boot firmware.

## Applicable platforms / languages
Not Language-Specific, System on Chip

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: The boot sequence should enable fabric access controls and memory protections before enabling third-party hardware IPs and peripheral microcontrollers that use untrusted firmware.

## Related attack patterns (CAPEC)
- [CAPEC-1](https://capec.mitre.org/data/definitions/1.html)
- [CAPEC-180](https://capec.mitre.org/data/definitions/180.html)

## Related weaknesses
- CWE-696 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1193.html
