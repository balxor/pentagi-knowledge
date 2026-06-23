---
cwe_id: CWE-1328
name: Security Version Number Mutable to Older Versions
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Security Hardware, Not Technology-Specific]
related_capec: [CAPEC-176]
url: https://cwe.mitre.org/data/definitions/1328.html
tags: [mitre-cwe, weakness, CWE-1328]
---

# CWE-1328 - Security Version Number Mutable to Older Versions

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1328](https://cwe.mitre.org/data/definitions/1328.html)

## Description
Security-version number in hardware is mutable, resulting in the ability to downgrade (roll-back) the boot firmware to vulnerable code versions.

## Extended description
A System-on-Chip (SoC) implements secure boot or verified boot. It might support a security version number, which prevents downgrading the current firmware to a vulnerable version. Once downgraded to a previous version, an adversary can launch exploits on the SoC and thus compromise the security of the SoC. These downgrade attacks are also referred to as roll-back attacks. The security version number must be stored securely and persistently across power-on resets. A common weakness is that the security version number is modifiable by an adversary, allowing roll-back or downgrade attacks or, under certain circumstances, preventing upgrades (i.e. Denial-of-Service on upgrades). In both cases, the SoC is in a vulnerable state.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Security Hardware, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Authentication, Authorization**: Other

## Potential mitigations
- **Architecture and Design**: When architecting the system, security version data should be designated for storage in registers that are either read-only or have access controls that prevent modification by an untrusted agent.
- **Implementation**: During implementation and test, security version data should be demonstrated to be read-only and access controls should be validated.

## Related attack patterns (CAPEC)
- [CAPEC-176](https://capec.mitre.org/data/definitions/176.html)

## Related weaknesses
- CWE-285 (ChildOf)
- CWE-757 (PeerOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1328.html
