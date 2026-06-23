---
cwe_id: CWE-614
name: Sensitive Cookie in HTTPS Session Without 'Secure' Attribute
type: weakness
abstraction: Variant
status: Draft
languages: [Web Based]
related_capec: [CAPEC-102]
url: https://cwe.mitre.org/data/definitions/614.html
tags: [mitre-cwe, weakness, CWE-614]
---

# CWE-614 - Sensitive Cookie in HTTPS Session Without 'Secure' Attribute

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-614](https://cwe.mitre.org/data/definitions/614.html)

## Description
The Secure attribute for sensitive cookies in HTTPS sessions is not set.

## Applicable platforms / languages
Web Based

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation**: Always set the secure attribute when the cookie should be sent via HTTPS only.

## Related attack patterns (CAPEC)
- [CAPEC-102](https://capec.mitre.org/data/definitions/102.html)

## Related weaknesses
- CWE-319 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-47833**: python library for ML and data science does not use the Secure flag for session cookies
- **CVE-2004-0462**: A product does not set the Secure attribute for sensitive cookies in HTTPS sessions, which could cause the user agent to send those cookies in plaintext over an HTTP session with the product.
- **CVE-2008-3663**: A product does not set the secure flag for the session cookie in an https session, which can cause the cookie to be sent in http requests and make it easier for remote attackers to capture this cookie.
- **CVE-2008-3662**: A product does not set the secure flag for the session cookie in an https session, which can cause the cookie to be sent in http requests and make it easier for remote attackers to capture this cookie.
- **CVE-2008-0128**: A product does not set the secure flag for a cookie in an https session, which can cause the cookie to be sent in http requests and make it easier for remote attackers to capture this cookie.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/614.html
