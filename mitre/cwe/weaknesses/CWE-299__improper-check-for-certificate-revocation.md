---
cwe_id: CWE-299
name: Improper Check for Certificate Revocation
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, Web Based]
related_capec: []
url: https://cwe.mitre.org/data/definitions/299.html
tags: [mitre-cwe, weakness, CWE-299]
---

# CWE-299 - Improper Check for Certificate Revocation

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-299](https://cwe.mitre.org/data/definitions/299.html)

## Description
The product does not check or incorrectly checks the revocation status of a certificate, which may cause it to use a certificate that has been compromised.

## Extended description
An improper check for certificate revocation is a far more serious flaw than related certificate failures. This is because the use of any revoked certificate is almost certainly malicious. The most common reason for certificate revocation is compromise of the system in question, with the result that no legitimate servers will be using a revoked certificate, unless they are sorely out of sync.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity
- **Integrity, Other**: Other
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design**: Ensure that certificates are checked for revoked status.
- **Implementation**: If certificate pinning is being used, ensure that all relevant properties of the certificate are fully validated before the certificate is pinned, including the revoked status.

## Related weaknesses
- CWE-295 (ChildOf)
- CWE-404 (ChildOf)

## Observed examples (CVE)
- **CVE-2011-2014**: LDAP-over-SSL implementation does not check Certificate Revocation List (CRL), allowing spoofing using a revoked certificate.
- **CVE-2011-0199**: Operating system does not check Certificate Revocation List (CRL) in some cases, allowing spoofing using a revoked certificate.
- **CVE-2010-5185**: Antivirus product does not check whether certificates from signed executables have been revoked.
- **CVE-2009-3046**: Web browser does not check if any intermediate certificates are revoked.
- **CVE-2009-0161**: chain: Ruby module for OCSP misinterprets a response, preventing detection of a revoked certificate.
- **CVE-2011-2701**: chain: incorrect parsing of replies from OCSP responders allows bypass using a revoked certificate.
- **CVE-2011-0935**: Router can permanently cache certain public keys, which would allow bypass if the certificate is later revoked.
- **CVE-2009-1358**: chain: OS package manager does not properly check the return value, allowing bypass using a revoked certificate.
- **CVE-2009-0642**: chain: language interpreter does not properly check the return value from an OSCP function, allowing bypass using a revoked certificate.
- **CVE-2008-4679**: chain: web service component does not call the expected method, which prevents a check for revoked certificates.
- **CVE-2006-4410**: Certificate revocation list not searched for certain certificates.
- **CVE-2006-4409**: Product cannot access certificate revocation list when an HTTP proxy is being used.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/299.html
