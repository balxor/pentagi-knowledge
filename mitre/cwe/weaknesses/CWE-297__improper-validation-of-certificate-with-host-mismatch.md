---
cwe_id: CWE-297
name: Improper Validation of Certificate with Host Mismatch
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, Mobile, Web Based]
related_capec: []
url: https://cwe.mitre.org/data/definitions/297.html
tags: [mitre-cwe, weakness, CWE-297]
---

# CWE-297 - Improper Validation of Certificate with Host Mismatch

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-297](https://cwe.mitre.org/data/definitions/297.html)

## Description
The product communicates with a host that provides a certificate, but the product does not properly ensure that the certificate is actually associated with that host.

## Extended description
Even if a certificate is well-formed, signed, and follows the chain of trust, it may simply be a valid certificate for a different site than the site that the product is interacting with. In order to ensure data integrity, the certificate must be valid, and it must pertain to the site that is being accessed. Even if the product attempts to check the hostname, it is still possible to incorrectly check the hostname. For example, attackers could create a certificate with a name that begins with a trusted name followed by a NUL byte, which could cause some string-based comparisons to only examine the portion that contains the trusted name.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Mobile, Web Based

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity
- **Authentication, Other**: Other
- **Access Control, Other**: Gain Privileges or Assume Identity, Other

## Potential mitigations
- **Architecture and Design**: Fully check the hostname of the certificate and provide the user with adequate information about the nature of the problem and how to proceed.
- **Implementation**: If certificate pinning is being used, ensure that all relevant properties of the certificate are fully validated before the certificate is pinned, including the hostname.

## Related weaknesses
- CWE-923 (ChildOf)
- CWE-295 (ChildOf)

## Observed examples (CVE)
- **CVE-2012-5810**: Mobile banking application does not verify hostname, leading to financial loss.
- **CVE-2012-5811**: Mobile application for printing documents does not verify hostname, allowing attackers to read sensitive documents.
- **CVE-2012-5807**: Software for electronic checking does not verify hostname, leading to financial loss.
- **CVE-2012-3446**: Cloud-support library written in Python uses incorrect regular expression when matching hostname.
- **CVE-2009-2408**: Web browser does not correctly handle '\0' character (NUL) in Common Name, allowing spoofing of https sites.
- **CVE-2012-0867**: Database program truncates the Common Name during hostname verification, allowing spoofing.
- **CVE-2010-2074**: Incorrect handling of '\0' character (NUL) in hostname verification allows spoofing.
- **CVE-2009-4565**: Mail server's incorrect handling of '\0' character (NUL) in hostname verification allows spoofing.
- **CVE-2009-3767**: LDAP server's incorrect handling of '\0' character (NUL) in hostname verification allows spoofing.
- **CVE-2012-5806**: Payment processing module does not verify hostname when connecting to PayPal using PHP fsockopen function.
- **CVE-2012-2993**: Smartphone device does not verify hostname, allowing spoofing of mail services.
- **CVE-2012-5804**: E-commerce module does not verify hostname when connecting to payment site.
- **CVE-2012-5824**: Chat application does not validate hostname, leading to loss of privacy.
- **CVE-2012-5822**: Application uses third-party library that does not validate hostname.
- **CVE-2012-5819**: Cloud storage management application does not validate hostname.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/297.html
