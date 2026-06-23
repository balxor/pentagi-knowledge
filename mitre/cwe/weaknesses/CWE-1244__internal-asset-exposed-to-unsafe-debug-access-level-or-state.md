---
cwe_id: CWE-1244
name: Internal Asset Exposed to Unsafe Debug Access Level or State
type: weakness
abstraction: Base
status: Stable
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip]
related_capec: [CAPEC-114]
url: https://cwe.mitre.org/data/definitions/1244.html
tags: [mitre-cwe, weakness, CWE-1244]
---

# CWE-1244 - Internal Asset Exposed to Unsafe Debug Access Level or State

**Abstraction:** Base  -  **Status:** Stable  -  **CWE:** [CWE-1244](https://cwe.mitre.org/data/definitions/1244.html)

## Description
The product uses physical debug or test interfaces with support for multiple access levels, but it assigns the wrong debug access level to an internal asset, providing unintended access to the asset from untrusted debug agents.

## Extended description
Debug authorization can have multiple levels of access, defined such that different system internal assets are accessible based on the current authorized debug level. Other than debugger authentication (e.g., using passwords or challenges), the authorization can also be based on the system state or boot stage. For example, full system debug access might only be allowed early in boot after a system reset to ensure that previous session data is not accessible to the authenticated debugger.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, System on Chip

## Common consequences
- **Confidentiality**: Read Memory
- **Integrity**: Modify Memory
- **Authorization, Access Control**: Gain Privileges or Assume Identity, Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design, Implementation**: For security-sensitive assets accessible over debug/test interfaces, only allow trusted agents.
- **Architecture and Design**: Apply blinding [REF-1219] or masking techniques in strategic areas.
- **Implementation**: Add shielding or tamper-resistant protections to the device, which increases the difficulty and cost for accessing debug/test interfaces.

## Related attack patterns (CAPEC)
- [CAPEC-114](https://capec.mitre.org/data/definitions/114.html)

## Related weaknesses
- CWE-863 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-18827**: After ROM code execution, JTAG access is disabled. But before the ROM code is executed, JTAG access is possible, allowing a user full system access. This allows a user to modify the boot flow and successfully bypass the secure-boot process.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1244.html
