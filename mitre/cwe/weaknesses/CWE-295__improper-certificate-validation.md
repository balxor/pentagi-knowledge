---
cwe_id: CWE-295
name: Improper Certificate Validation
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, Web Based, Mobile]
related_capec: [CAPEC-459, CAPEC-475]
url: https://cwe.mitre.org/data/definitions/295.html
tags: [mitre-cwe, weakness, CWE-295]
---

# CWE-295 - Improper Certificate Validation

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-295](https://cwe.mitre.org/data/definitions/295.html)

## Description
The product does not validate, or incorrectly validates, a certificate.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based, Mobile

## Common consequences
- **Integrity, Authentication**: Bypass Protection Mechanism, Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design, Implementation**: Certificates should be carefully managed and checked to assure that data are encrypted with the intended owner's public key.
- **Implementation**: If certificate pinning is being used, ensure that all relevant properties of the certificate are fully validated before the certificate is pinned, including the hostname.

## Related attack patterns (CAPEC)
- [CAPEC-459](https://capec.mitre.org/data/definitions/459.html)
- [CAPEC-475](https://capec.mitre.org/data/definitions/475.html)

## Related weaknesses
- CWE-287 (ChildOf)
- CWE-287 (ChildOf)
- CWE-322 (PeerOf)

## Observed examples (CVE)
- **CVE-2019-12496**: A Go framework for robotics, drones, and IoT devices skips verification of root CA certificates by default.
- **CVE-2014-1266**: Chain: incorrect "goto" in Apple SSL product bypasses certificate validation, allowing Adversary-in-the-Middle (AITM) attack (Apple "goto fail" bug). CWE-705 (Incorrect Control Flow Scoping) -> CWE-561 (Dead Code) -> CWE-295 (Improper Certificate Validation) -> CWE-393 (Return of Wrong Status Code) -> CWE-300 (Channel Accessible by Non-Endpoint). The code's whitespace indentation did not reflect the actual control flow (CWE-1114) and did not explicitly delimit the block (CWE-483), which could have made it more difficult for human code auditors to detect the vulnerability.
- **CVE-2021-22909**: Chain: router's firmware update procedure uses curl with "-k" (insecure) option that disables certificate validation (CWE-295), allowing adversary-in-the-middle (AITM) compromise with a malicious firmware image (CWE-494).
- **CVE-2008-4989**: Verification function trusts certificate chains in which the last certificate is self-signed.
- **CVE-2012-5821**: Web browser uses a TLS-related function incorrectly, preventing it from verifying that a server's certificate is signed by a trusted certification authority (CA)
- **CVE-2009-3046**: Web browser does not check if any intermediate certificates are revoked.
- **CVE-2011-0199**: Operating system does not check Certificate Revocation List (CRL) in some cases, allowing spoofing using a revoked certificate.
- **CVE-2012-5810**: Mobile banking application does not verify hostname, leading to financial loss.
- **CVE-2012-3446**: Cloud-support library written in Python uses incorrect regular expression when matching hostname.
- **CVE-2009-2408**: Web browser does not correctly handle '\0' character (NUL) in Common Name, allowing spoofing of https sites.
- **CVE-2012-2993**: Smartphone device does not verify hostname, allowing spoofing of mail services.
- **CVE-2012-5822**: Application uses third-party library that does not validate hostname.
- **CVE-2012-5819**: Cloud storage management application does not validate hostname.
- **CVE-2012-5817**: Java library uses JSSE SSLSocket and SSLEngine classes, which do not verify the hostname.
- **CVE-2010-1378**: Chain: incorrect calculation (CWE-682) allows attackers to bypass certificate checks (CWE-295)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/295.html
