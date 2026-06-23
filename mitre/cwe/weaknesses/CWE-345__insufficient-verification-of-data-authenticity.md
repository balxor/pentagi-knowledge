---
cwe_id: CWE-345
name: Insufficient Verification of Data Authenticity
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, ICS/OT]
related_capec: [CAPEC-111, CAPEC-141, CAPEC-142, CAPEC-148, CAPEC-218, CAPEC-384, CAPEC-385, CAPEC-386, CAPEC-387, CAPEC-388, CAPEC-665, CAPEC-701]
url: https://cwe.mitre.org/data/definitions/345.html
tags: [mitre-cwe, weakness, CWE-345]
---

# CWE-345 - Insufficient Verification of Data Authenticity

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-345](https://cwe.mitre.org/data/definitions/345.html)

## Description
The product does not sufficiently verify the origin or authenticity of data, in a way that causes it to accept invalid data.

## Applicable platforms / languages
Not Language-Specific, ICS/OT

## Common consequences
- **Integrity, Other**: Varies by Context, Unexpected State

## Related attack patterns (CAPEC)
- [CAPEC-111](https://capec.mitre.org/data/definitions/111.html)
- [CAPEC-141](https://capec.mitre.org/data/definitions/141.html)
- [CAPEC-142](https://capec.mitre.org/data/definitions/142.html)
- [CAPEC-148](https://capec.mitre.org/data/definitions/148.html)
- [CAPEC-218](https://capec.mitre.org/data/definitions/218.html)
- [CAPEC-384](https://capec.mitre.org/data/definitions/384.html)
- [CAPEC-385](https://capec.mitre.org/data/definitions/385.html)
- [CAPEC-386](https://capec.mitre.org/data/definitions/386.html)
- [CAPEC-387](https://capec.mitre.org/data/definitions/387.html)
- [CAPEC-388](https://capec.mitre.org/data/definitions/388.html)
- [CAPEC-665](https://capec.mitre.org/data/definitions/665.html)
- [CAPEC-701](https://capec.mitre.org/data/definitions/701.html)

## Related weaknesses
- CWE-693 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-30260**: Distributed Control System (DCS) does not sign firmware images and only relies on insecure checksums for integrity checks
- **CVE-2022-30267**: Distributed Control System (DCS) does not sign firmware images and only relies on insecure checksums for integrity checks
- **CVE-2022-30272**: Remote Terminal Unit (RTU) does not use signatures for firmware images and relies on insecure checksums

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/345.html
