---
cwe_id: CWE-1243
name: Sensitive Non-Volatile Information Not Protected During Debug
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-116, CAPEC-545]
url: https://cwe.mitre.org/data/definitions/1243.html
tags: [mitre-cwe, weakness, CWE-1243]
---

# CWE-1243 - Sensitive Non-Volatile Information Not Protected During Debug

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1243](https://cwe.mitre.org/data/definitions/1243.html)

## Description
Access to security-sensitive information stored in fuses is not limited during debug.

## Extended description
Several security-sensitive values are programmed into fuses to be used during early-boot flows or later at runtime. Examples of these security-sensitive values include root keys, encryption keys, manufacturing-specific information, chip-manufacturer-specific information, and original-equipment-manufacturer (OEM) data. After the chip is powered on, these values are sensed from fuses and stored in temporary locations such as registers and local memories. These locations are typically access-control protected from untrusted agents capable of accessing them. Even to trusted agents, only read-access is provided.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Access Control**: Modify Memory, Read Memory, Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design, Implementation**: Disable access to security-sensitive information stored in fuses directly and also reflected from temporary storage locations when in debug mode.

## Related attack patterns (CAPEC)
- [CAPEC-116](https://capec.mitre.org/data/definitions/116.html)
- [CAPEC-545](https://capec.mitre.org/data/definitions/545.html)

## Related weaknesses
- CWE-1263 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1243.html
