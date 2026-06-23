---
cwe_id: CWE-307
name: Improper Restriction of Excessive Authentication Attempts
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-16, CAPEC-49, CAPEC-560, CAPEC-565, CAPEC-600, CAPEC-652, CAPEC-653]
url: https://cwe.mitre.org/data/definitions/307.html
tags: [mitre-cwe, weakness, CWE-307]
---

# CWE-307 - Improper Restriction of Excessive Authentication Attempts

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-307](https://cwe.mitre.org/data/definitions/307.html)

## Description
The product does not implement sufficient measures to prevent multiple failed authentication attempts within a short time frame.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Common protection mechanisms include: Disconnecting the user after a small number of failed attempts Implementing a timeout Locking out a targeted account Requiring a computational task on the user's part.
- **Architecture and Design**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid [REF-1482]. Consider using libraries with authentication capabilities such as OpenSSL or the ESAPI Authenticator. [REF-45]

## Related attack patterns (CAPEC)
- [CAPEC-16](https://capec.mitre.org/data/definitions/16.html)
- [CAPEC-49](https://capec.mitre.org/data/definitions/49.html)
- [CAPEC-560](https://capec.mitre.org/data/definitions/560.html)
- [CAPEC-565](https://capec.mitre.org/data/definitions/565.html)
- [CAPEC-600](https://capec.mitre.org/data/definitions/600.html)
- [CAPEC-652](https://capec.mitre.org/data/definitions/652.html)
- [CAPEC-653](https://capec.mitre.org/data/definitions/653.html)

## Related weaknesses
- CWE-1390 (ChildOf)
- CWE-287 (ChildOf)
- CWE-799 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-0039**: the REST API for a network OS has a high limit for number of connections, allowing brute force password guessing
- **CVE-1999-1152**: Product does not disconnect or timeout after multiple failed logins.
- **CVE-2001-1291**: Product does not disconnect or timeout after multiple failed logins.
- **CVE-2001-0395**: Product does not disconnect or timeout after multiple failed logins.
- **CVE-2001-1339**: Product does not disconnect or timeout after multiple failed logins.
- **CVE-2002-0628**: Product does not disconnect or timeout after multiple failed logins.
- **CVE-1999-1324**: User accounts not disabled when they exceed a threshold; possibly a resultant problem.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/307.html
