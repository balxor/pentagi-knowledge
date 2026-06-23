---
cwe_id: CWE-302
name: Authentication Bypass by Assumed-Immutable Data
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, Web Based]
related_capec: [CAPEC-10, CAPEC-13, CAPEC-21, CAPEC-274, CAPEC-31, CAPEC-39, CAPEC-45, CAPEC-77]
url: https://cwe.mitre.org/data/definitions/302.html
tags: [mitre-cwe, weakness, CWE-302]
---

# CWE-302 - Authentication Bypass by Assumed-Immutable Data

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-302](https://cwe.mitre.org/data/definitions/302.html)

## Description
The authentication scheme or implementation uses key data elements that are assumed to be immutable, but can be controlled or modified by the attacker.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design, Operation, Implementation**: Implement proper protection for immutable data (e.g. environment variable, hidden form fields, etc.)

## Related attack patterns (CAPEC)
- [CAPEC-10](https://capec.mitre.org/data/definitions/10.html)
- [CAPEC-13](https://capec.mitre.org/data/definitions/13.html)
- [CAPEC-21](https://capec.mitre.org/data/definitions/21.html)
- [CAPEC-274](https://capec.mitre.org/data/definitions/274.html)
- [CAPEC-31](https://capec.mitre.org/data/definitions/31.html)
- [CAPEC-39](https://capec.mitre.org/data/definitions/39.html)
- [CAPEC-45](https://capec.mitre.org/data/definitions/45.html)
- [CAPEC-77](https://capec.mitre.org/data/definitions/77.html)

## Related weaknesses
- CWE-1390 (ChildOf)
- CWE-807 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-0367**: DebPloit
- **CVE-2004-0261**: Web auth
- **CVE-2002-1730**: Authentication bypass by setting certain cookies to "true".
- **CVE-2002-1734**: Authentication bypass by setting certain cookies to "true".
- **CVE-2002-2064**: Admin access by setting a cookie.
- **CVE-2002-2054**: Gain privileges by setting cookie.
- **CVE-2004-1611**: Product trusts authentication information in cookie.
- **CVE-2005-1708**: Authentication bypass by setting admin-testing variable to true.
- **CVE-2005-1787**: Bypass auth and gain privileges by setting a variable.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/302.html
