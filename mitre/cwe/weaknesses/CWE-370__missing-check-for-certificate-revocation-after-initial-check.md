---
cwe_id: CWE-370
name: Missing Check for Certificate Revocation after Initial Check
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-26, CAPEC-29]
url: https://cwe.mitre.org/data/definitions/370.html
tags: [mitre-cwe, weakness, CWE-370]
---

# CWE-370 - Missing Check for Certificate Revocation after Initial Check

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-370](https://cwe.mitre.org/data/definitions/370.html)

## Description
The product does not check the revocation status of a certificate after its initial revocation check, which can cause the product to perform privileged actions even after the certificate is revoked at a later time.

## Extended description
If the revocation status of a certificate is not checked before each action that requires privileges, the system may be subject to a race condition. If a certificate is revoked after the initial check, all subsequent actions taken with the owner of the revoked certificate will lose all benefits guaranteed by the certificate. In fact, it is almost certain that the use of a revoked certificate indicates malicious activity.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity
- **Integrity**: Modify Application Data
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design**: Ensure that certificates are checked for revoked status before each use of a protected resource. If the certificate is checked before each access of a protected resource, the delay subject to a possible race condition becomes almost negligible and significantly reduces the risk associated with this issue.

## Related attack patterns (CAPEC)
- [CAPEC-26](https://capec.mitre.org/data/definitions/26.html)
- [CAPEC-29](https://capec.mitre.org/data/definitions/29.html)

## Related weaknesses
- CWE-299 (ChildOf)
- CWE-296 (PeerOf)
- CWE-297 (PeerOf)
- CWE-298 (PeerOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/370.html
