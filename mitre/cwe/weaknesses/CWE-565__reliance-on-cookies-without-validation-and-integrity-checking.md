---
cwe_id: CWE-565
name: Reliance on Cookies without Validation and Integrity Checking
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-226, CAPEC-31, CAPEC-39]
url: https://cwe.mitre.org/data/definitions/565.html
tags: [mitre-cwe, weakness, CWE-565]
---

# CWE-565 - Reliance on Cookies without Validation and Integrity Checking

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-565](https://cwe.mitre.org/data/definitions/565.html)

## Description
The product relies on the existence or values of cookies when performing security-critical operations, but it does not properly ensure that the setting is valid for the associated user.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity, Availability**: Modify Application Data, Execute Unauthorized Code or Commands
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Avoid using cookie data for a security-related decision.
- **Implementation**: Perform thorough input validation (i.e.: server side validation) on the cookie data if you're going to use it for a security related decision.
- **Architecture and Design**: Add integrity checks to detect tampering.
- **Architecture and Design**: Protect critical cookies from replay attacks, since cross-site scripting or other attacks may allow attackers to steal a strongly-encrypted cookie that also passes integrity checks. This mitigation applies to cookies that should only be valid during a single transaction or session. By enforcing timeouts, you may limit the scope of an attack. As part of your integrity check, use an unpredictable, server-side value that is not exposed to the client.

## Related attack patterns (CAPEC)
- [CAPEC-226](https://capec.mitre.org/data/definitions/226.html)
- [CAPEC-31](https://capec.mitre.org/data/definitions/31.html)
- [CAPEC-39](https://capec.mitre.org/data/definitions/39.html)

## Related weaknesses
- CWE-642 (ChildOf)
- CWE-669 (ChildOf)
- CWE-602 (ChildOf)

## Observed examples (CVE)
- **CVE-2008-5784**: e-dating application allows admin privileges by setting the admin cookie to 1.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/565.html
