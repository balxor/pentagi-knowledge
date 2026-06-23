---
cwe_id: CWE-1301
name: Insufficient or Incomplete Data Removal within Hardware Component
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-37]
url: https://cwe.mitre.org/data/definitions/1301.html
tags: [mitre-cwe, weakness, CWE-1301]
---

# CWE-1301 - Insufficient or Incomplete Data Removal within Hardware Component

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1301](https://cwe.mitre.org/data/definitions/1301.html)

## Description
The product's data removal process does not completely delete all data and potentially sensitive information within hardware components.

## Extended description
Physical properties of hardware devices, such as remanence of magnetic media, residual charge of ROMs/RAMs, or screen burn-in may still retain sensitive data after a data removal process has taken place and power is removed. Recovering data after erasure or overwriting is possible due to a phenomenon called data remanence. For example, if the same value is written repeatedly to a memory location, the corresponding memory cells can become physically altered to a degree such that even after the original data is erased that data can still be recovered through physical characterization of the memory cells.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Memory, Read Application Data

## Potential mitigations
- **Architecture and Design**: Apply blinding or masking techniques to implementations of cryptographic algorithms.
- **Implementation**: Alter the method of erasure, add protection of media, or destroy the media to protect the data.

## Related attack patterns (CAPEC)
- [CAPEC-37](https://capec.mitre.org/data/definitions/37.html)

## Related weaknesses
- CWE-226 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-8575**: Firmware Data Deletion Vulnerability in which a base station factory reset might not delete all user information. The impact of this enables a new owner of a used device that has been "factory-default reset" with a vulnerable firmware version can still retrieve, at least, the previous owner's wireless network name, and the previous owner's wireless security (such as WPA2) key. This issue was addressed with improved, data deletion.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1301.html
