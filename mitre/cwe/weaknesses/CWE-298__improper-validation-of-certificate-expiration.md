---
cwe_id: CWE-298
name: Improper Validation of Certificate Expiration
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/298.html
tags: [mitre-cwe, weakness, CWE-298]
---

# CWE-298 - Improper Validation of Certificate Expiration

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-298](https://cwe.mitre.org/data/definitions/298.html)

## Description
A certificate expiration is not validated or is incorrectly validated.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Other**: Other
- **Authentication, Other**: Other

## Potential mitigations
- **Architecture and Design**: Check for expired certificates and provide the user with adequate information about the nature of the problem and how to proceed.
- **Implementation**: If certificate pinning is being used, ensure that all relevant properties of the certificate are fully validated before the certificate is pinned, including the expiration.

## Related weaknesses
- CWE-295 (ChildOf)
- CWE-672 (ChildOf)

## Observed examples (CVE)
- **CVE-2025-4384**: product does not verify that a certificate has expired
- **CVE-2007-3564**: web library product does not verify that a certificate has expired
- **CVE-2007-6746**: IRC product does not check the expiration date of the X.509 certificate
- **CVE-2007-6746**: library for SSL and TLS does not check the activation or expiration dates of CA certificates

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/298.html
