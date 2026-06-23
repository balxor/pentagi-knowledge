---
cwe_id: CWE-296
name: Improper Following of a Certificate's Chain of Trust
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, Web Based]
related_capec: []
url: https://cwe.mitre.org/data/definitions/296.html
tags: [mitre-cwe, weakness, CWE-296]
---

# CWE-296 - Improper Following of a Certificate's Chain of Trust

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-296](https://cwe.mitre.org/data/definitions/296.html)

## Description
The product does not follow, or incorrectly follows, the chain of trust for a certificate back to a trusted root certificate.

## Extended description
There are several ways in which the chain of trust might be broken, including but not limited to: Any certificate in the chain is self-signed, unless it is the root. Not every intermediate certificate is checked, starting from the original certificate all the way up to the root certificate. An intermediate, CA-signed certificate does not have the expected Basic Constraints or other important extensions. The root certificate has been compromised or authorized to the wrong party.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based

## Common consequences
- **Non-Repudiation**: Hide Activities
- **Integrity, Confidentiality, Availability, Access Control**: Gain Privileges or Assume Identity, Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design**: Ensure that proper certificate checking is included in the system design.
- **Implementation**: Understand, and properly implement all checks necessary to ensure the integrity of certificate trust integrity.
- **Implementation**: If certificate pinning is being used, ensure that all relevant properties of the certificate are fully validated before the certificate is pinned, including the full chain of trust.

## Related weaknesses
- CWE-295 (ChildOf)
- CWE-573 (ChildOf)

## Observed examples (CVE)
- **CVE-2016-2402**: Server allows bypass of certificate pinning by sending a chain of trust that includes a trusted CA that is not pinned.
- **CVE-2008-4989**: Verification function trusts certificate chains in which the last certificate is self-signed.
- **CVE-2012-5821**: Chain: Web browser uses a TLS-related function incorrectly, preventing it from verifying that a server's certificate is signed by a trusted certification authority (CA).
- **CVE-2009-3046**: Web browser does not check if any intermediate certificates are revoked.
- **CVE-2009-0265**: chain: DNS server does not correctly check return value from the OpenSSL EVP_VerifyFinal function allows bypass of validation of the certificate chain.
- **CVE-2009-0124**: chain: incorrect check of return value from the OpenSSL EVP_VerifyFinal function allows bypass of validation of the certificate chain.
- **CVE-2002-0970**: File-transfer software does not validate Basic Constraints of an intermediate CA-signed certificate.
- **CVE-2002-0862**: Cryptographic API, as used in web browsers, mail clients, and other software, does not properly validate Basic Constraints.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/296.html
