---
capec_id: CAPEC-642
name: Replace Binaries
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: High
related_cwe: [CWE-732]
related_attack: [T1505.005, T1554, T1574.005]
url: https://capec.mitre.org/data/definitions/642.html
tags: [mitre-capec, attack-pattern, CAPEC-642]
---

# CAPEC-642 - Replace Binaries

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** High  -  **CAPEC:** [CAPEC-642](https://capec.mitre.org/data/definitions/642.html)

## Description
Adversaries know that certain binaries will be regularly executed as part of normal processing. If these binaries are not protected with the appropriate file system permissions, it could be possible to replace them with malware. This malware might be executed at higher system permission levels. A variation of this pattern is to discover self-extracting installation packages that unpack binaries to directories with weak file permissions which it does not clean up appropriately. These binaries can be replaced by malware, which can then be executed.

## Prerequisites
- The attacker must be able to place the malicious binary on the target machine.

## Mitigations
- Insure that binaries commonly used by the system have the correct file permissions. Set operating system policies that restrict privilege elevation of non-Administrators. Use auditing tools to observe changes to system services.

## Related weaknesses (CWE)
- [CWE-732](https://cwe.mitre.org/data/definitions/732.html)

## Related ATT&CK techniques
- T1505.005
- T1554
- T1574.005

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/642.html
