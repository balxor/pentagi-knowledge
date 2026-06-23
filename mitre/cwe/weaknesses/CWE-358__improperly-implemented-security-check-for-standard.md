---
cwe_id: CWE-358
name: Improperly Implemented Security Check for Standard
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/358.html
tags: [mitre-cwe, weakness, CWE-358]
---

# CWE-358 - Improperly Implemented Security Check for Standard

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-358](https://cwe.mitre.org/data/definitions/358.html)

## Description
The product does not implement or incorrectly implements one or more security-relevant checks as specified by the design of a standardized algorithm, protocol, or technique.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Related weaknesses
- CWE-573 (ChildOf)
- CWE-693 (ChildOf)
- CWE-345 (CanAlsoBe)
- CWE-290 (CanAlsoBe)

## Observed examples (CVE)
- **CVE-2002-0862**: Browser does not verify Basic Constraints of a certificate, even though it is required, allowing spoofing of trusted certificates.
- **CVE-2002-0970**: Browser does not verify Basic Constraints of a certificate, even though it is required, allowing spoofing of trusted certificates.
- **CVE-2002-1407**: Browser does not verify Basic Constraints of a certificate, even though it is required, allowing spoofing of trusted certificates.
- **CVE-2005-0198**: Logic error prevents some required conditions from being enforced during Challenge-Response Authentication Mechanism with MD5 (CRAM-MD5).
- **CVE-2004-2163**: Shared secret not verified in a RADIUS response packet, allowing authentication bypass by spoofing server replies.
- **CVE-2005-2181**: Insufficient verification in VoIP implementation, in violation of standard, allows spoofed messages.
- **CVE-2005-2182**: Insufficient verification in VoIP implementation, in violation of standard, allows spoofed messages.
- **CVE-2005-2298**: Security check not applied to all components, allowing bypass.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/358.html
