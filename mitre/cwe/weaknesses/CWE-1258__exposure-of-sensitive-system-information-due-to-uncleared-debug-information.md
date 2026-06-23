---
cwe_id: CWE-1258
name: Exposure of Sensitive System Information Due to Uncleared Debug Information
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-150, CAPEC-204, CAPEC-37, CAPEC-545]
url: https://cwe.mitre.org/data/definitions/1258.html
tags: [mitre-cwe, weakness, CWE-1258]
---

# CWE-1258 - Exposure of Sensitive System Information Due to Uncleared Debug Information

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1258](https://cwe.mitre.org/data/definitions/1258.html)

## Description
The hardware does not fully clear security-sensitive values, such as keys and intermediate values in cryptographic operations, when debug mode is entered.

## Extended description
Security sensitive values, keys, intermediate steps of cryptographic operations, etc. are stored in temporary registers in the hardware. If these values are not cleared when debug mode is entered they may be accessed by a debugger allowing sensitive information to be accessible by untrusted parties.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Memory
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Whenever debug mode is enabled, all registers containing sensitive assets must be cleared.

## Related attack patterns (CAPEC)
- [CAPEC-150](https://capec.mitre.org/data/definitions/150.html)
- [CAPEC-204](https://capec.mitre.org/data/definitions/204.html)
- [CAPEC-37](https://capec.mitre.org/data/definitions/37.html)
- [CAPEC-545](https://capec.mitre.org/data/definitions/545.html)

## Related weaknesses
- CWE-212 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-33080**: Uncleared debug information in memory accelerator for SSD product exposes sensitive system information
- **CVE-2022-31162**: Rust library leaks Oauth client details in application debug logs

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1258.html
