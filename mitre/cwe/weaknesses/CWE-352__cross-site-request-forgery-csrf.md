---
cwe_id: CWE-352
name: Cross-Site Request Forgery (CSRF)
type: weakness
abstraction: Compound
status: Stable
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: [CAPEC-111, CAPEC-462, CAPEC-467, CAPEC-62]
url: https://cwe.mitre.org/data/definitions/352.html
tags: [mitre-cwe, weakness, CWE-352]
---

# CWE-352 - Cross-Site Request Forgery (CSRF)

**Abstraction:** Compound  -  **Status:** Stable  -  **CWE:** [CWE-352](https://cwe.mitre.org/data/definitions/352.html)

## Description
The web application does not, or cannot, sufficiently verify whether a request was intentionally provided by the user who sent the request, which could have originated from an unauthorized actor.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Confidentiality, Integrity, Availability, Non-Repudiation, Access Control**: Gain Privileges or Assume Identity, Bypass Protection Mechanism, Read Application Data, Modify Application Data, DoS: Crash, Exit, or Restart

## Potential mitigations
- **Architecture and Design**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid [REF-1482]. For example, use anti-CSRF packages such as the OWASP CSRFGuard. [REF-330] Another example is the ESAPI Session Management control, which includes a component for CSRF. [REF-45]
- **Implementation**: Ensure that the application is free of cross-site scripting issues (CWE-79), because most CSRF defenses can be bypassed using attacker-controlled script.
- **Architecture and Design**: Generate a unique nonce for each form, place the nonce into the form, and verify the nonce upon receipt of the form. Be sure that the nonce is not predictable (CWE-330). [REF-332]
- **Architecture and Design**: Identify especially dangerous operations. When the user performs a dangerous operation, send a separate confirmation request to ensure that the user intended to perform that operation.
- **Architecture and Design**: Use the "double-submitted cookie" method as described by Felten and Zeller: When a user visits a site, the site should generate a pseudorandom value and set it as a cookie on the user's machine. The site should require every form submission to include this value as a form value and also as a cookie value. When a POST request is sent to the site, the request should only be considered valid if the form value and the cookie value are the same. Because of the same-origin policy, an attacker cannot read or modify the value stored in the cookie. To successfully submit a form on behalf of the user, the attacker would have to correctly guess the pseudorandom value. If the pseudorandom value is cryptographically strong, this will be prohibitively difficult. This technique requires Javascript, so it may not work for browsers that have Javascript disabled. [REF-331]
- **Architecture and Design**: Do not use the GET method for any request that triggers a state change.
- **Implementation**: Check the HTTP Referer header to see if the request originated from an expected page. This could break legitimate functionality, because users or proxies may have disabled sending the Referer for privacy reasons.

## Related attack patterns (CAPEC)
- [CAPEC-111](https://capec.mitre.org/data/definitions/111.html)
- [CAPEC-462](https://capec.mitre.org/data/definitions/462.html)
- [CAPEC-467](https://capec.mitre.org/data/definitions/467.html)
- [CAPEC-62](https://capec.mitre.org/data/definitions/62.html)

## Related weaknesses
- CWE-345 (ChildOf)
- CWE-345 (ChildOf)
- CWE-346 (Requires)
- CWE-441 (Requires)
- CWE-642 (Requires)
- CWE-613 (Requires)

## Observed examples (CVE)
- **CVE-2004-1703**: Add user accounts via a URL in an img tag
- **CVE-2004-1995**: Add user accounts via a URL in an img tag
- **CVE-2004-1967**: Arbitrary code execution by specifying the code in a crafted img tag or URL
- **CVE-2004-1842**: Gain administrative privileges via a URL in an img tag
- **CVE-2005-1947**: Delete a victim's information via a URL or an img tag
- **CVE-2005-2059**: Change another user's settings via a URL or an img tag
- **CVE-2005-1674**: Perform actions as administrator via a URL or an img tag
- **CVE-2009-3520**: modify password for the administrator
- **CVE-2009-3022**: CMS allows modification of configuration via CSRF attack against the administrator
- **CVE-2009-3759**: web interface allows password changes or stopping a virtual machine via CSRF

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/352.html
