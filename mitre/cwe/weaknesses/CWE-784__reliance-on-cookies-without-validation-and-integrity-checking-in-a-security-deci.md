---
cwe_id: CWE-784
name: Reliance on Cookies without Validation and Integrity Checking in a Security Decision
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/784.html
tags: [mitre-cwe, weakness, CWE-784]
---

# CWE-784 - Reliance on Cookies without Validation and Integrity Checking in a Security Decision

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-784](https://cwe.mitre.org/data/definitions/784.html)

## Description
The product uses a protection mechanism that relies on the existence or values of a cookie, but it does not properly ensure that the cookie is valid for the associated user.

## Extended description
Attackers can easily modify cookies, within the browser or by implementing the client-side code outside of the browser. Attackers can bypass protection mechanisms such as authorization and authentication by modifying the cookie to contain an expected value.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Access Control**: Bypass Protection Mechanism, Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Avoid using cookie data for a security-related decision.
- **Implementation**: Perform thorough input validation (i.e.: server side validation) on the cookie data if you're going to use it for a security related decision.
- **Architecture and Design**: Add integrity checks to detect tampering.
- **Architecture and Design**: Protect critical cookies from replay attacks, since cross-site scripting or other attacks may allow attackers to steal a strongly-encrypted cookie that also passes integrity checks. This mitigation applies to cookies that should only be valid during a single transaction or session. By enforcing timeouts, you may limit the scope of an attack. As part of your integrity check, use an unpredictable, server-side value that is not exposed to the client.

## Related weaknesses
- CWE-807 (ChildOf)
- CWE-565 (ChildOf)

## Observed examples (CVE)
- **CVE-2009-1549**: Attacker can bypass authentication by setting a cookie to a specific value.
- **CVE-2009-1619**: Attacker can bypass authentication and gain admin privileges by setting an "admin" cookie to 1.
- **CVE-2009-0864**: Content management system allows admin privileges by setting a "login" cookie to "OK."
- **CVE-2008-5784**: e-dating application allows admin privileges by setting the admin cookie to 1.
- **CVE-2008-6291**: Web-based email list manager allows attackers to gain admin privileges by setting a login cookie to "admin."

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/784.html
