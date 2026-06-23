---
cwe_id: CWE-321
name: Use of Hard-coded Cryptographic Key
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific, ICS/OT]
related_capec: []
url: https://cwe.mitre.org/data/definitions/321.html
tags: [mitre-cwe, weakness, CWE-321]
---

# CWE-321 - Use of Hard-coded Cryptographic Key

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-321](https://cwe.mitre.org/data/definitions/321.html)

## Description
The product uses a hard-coded, unchangeable cryptographic key.

## Applicable platforms / languages
Not Language-Specific, ICS/OT

## Common consequences
- **Access Control**: Bypass Protection Mechanism, Gain Privileges or Assume Identity, Read Application Data

## Potential mitigations
- **Architecture and Design**: Prevention schemes mirror that of hard-coded password storage.

## Related weaknesses
- CWE-798 (ChildOf)
- CWE-798 (ChildOf)
- CWE-798 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-29960**: Engineering Workstation uses hard-coded cryptographic keys that could allow for unathorized filesystem access and privilege escalation
- **CVE-2022-30271**: Remote Terminal Unit (RTU) uses a hard-coded SSH private key that is likely to be used by default.
- **CVE-2020-10884**: WiFi router service has a hard-coded encryption key, allowing root access
- **CVE-2014-2198**: Communications / collaboration product has a hardcoded SSH private key, allowing access to root account

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/321.html
