---
cwe_id: CWE-1278
name: Missing Protection Against Hardware Reverse Engineering Using Integrated Circuit (IC) Imaging Techniques
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-188, CAPEC-37, CAPEC-545]
url: https://cwe.mitre.org/data/definitions/1278.html
tags: [mitre-cwe, weakness, CWE-1278]
---

# CWE-1278 - Missing Protection Against Hardware Reverse Engineering Using Integrated Circuit (IC) Imaging Techniques

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1278](https://cwe.mitre.org/data/definitions/1278.html)

## Description
Information stored in hardware may be recovered by an attacker with the capability to capture and analyze images of the integrated circuit using techniques such as scanning electron microscopy.

## Extended description
The physical structure of a device, viewed at high enough magnification, can reveal the information stored inside. Typical steps in IC reverse engineering involve removing the chip packaging (decapsulation) then using various imaging techniques ranging from high resolution x-ray microscopy to invasive techniques involving removing IC layers and imaging each layer using a scanning electron microscope. The goal of such activities is to recover secret keys, unique device identifiers, and proprietary code and circuit designs embedded in hardware that the attacker has been unsuccessful at accessing through other means. These secrets may be stored in non-volatile memory or in the circuit netlist. Memory technologies such as masked ROM allow easier to extraction of secrets than One-time Programmable (OTP) memory.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality**: Varies by Context

## Potential mitigations
- **Architecture and Design**: The cost of secret extraction via IC reverse engineering should outweigh the potential value of the secrets being extracted. Threat model and value of secrets should be used to choose the technology used to safeguard those secrets. Examples include IC camouflaging and obfuscation, tamper-proof packaging, active shielding, and physical tampering detection information erasure.

## Related attack patterns (CAPEC)
- [CAPEC-188](https://capec.mitre.org/data/definitions/188.html)
- [CAPEC-37](https://capec.mitre.org/data/definitions/37.html)
- [CAPEC-545](https://capec.mitre.org/data/definitions/545.html)

## Related weaknesses
- CWE-693 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1278.html
