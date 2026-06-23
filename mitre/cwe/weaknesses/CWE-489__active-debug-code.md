---
cwe_id: CWE-489
name: Active Debug Code
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, ICS/OT]
related_capec: [CAPEC-121, CAPEC-661]
url: https://cwe.mitre.org/data/definitions/489.html
tags: [mitre-cwe, weakness, CWE-489]
---

# CWE-489 - Active Debug Code

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-489](https://cwe.mitre.org/data/definitions/489.html)

## Description
The product is released with debugging code still enabled or active.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, ICS/OT

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control, Other**: Bypass Protection Mechanism, Read Application Data, Gain Privileges or Assume Identity, Varies by Context

## Potential mitigations
- **Build and Compilation, Distribution**: Remove debug code before deploying the application.

## Related attack patterns (CAPEC)
- [CAPEC-121](https://capec.mitre.org/data/definitions/121.html)
- [CAPEC-661](https://capec.mitre.org/data/definitions/661.html)

## Related weaknesses
- CWE-710 (ChildOf)
- CWE-215 (CanPrecede)

## Observed examples (CVE)
- **CVE-2024-44092**: smartphone is built for production with debugging code present, allowing local privilege escalation
- **CVE-2024-36475**: network hub contains active debug code, which allows users to execute arbitrary OS commands using a debug function
- **CVE-2024-29075**: Mesh Wi-Fi router has active debug code, allowing attackers to modify device settings

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/489.html
