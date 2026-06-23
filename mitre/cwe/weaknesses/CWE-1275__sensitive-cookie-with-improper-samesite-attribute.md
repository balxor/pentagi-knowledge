---
cwe_id: CWE-1275
name: Sensitive Cookie with Improper SameSite Attribute
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Web Based, Web Server]
related_capec: [CAPEC-62]
url: https://cwe.mitre.org/data/definitions/1275.html
tags: [mitre-cwe, weakness, CWE-1275]
---

# CWE-1275 - Sensitive Cookie with Improper SameSite Attribute

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-1275](https://cwe.mitre.org/data/definitions/1275.html)

## Description
The SameSite attribute for sensitive cookies is not set, or an insecure value is used.

## Extended description
The SameSite attribute controls how cookies are sent for cross-domain requests. This attribute may have three values: 'Lax', 'Strict', or 'None'. If the 'None' value is used, a website may create a cross-domain POST HTTP request to another website, and the browser automatically adds cookies to this request. This may lead to Cross-Site-Request-Forgery (CSRF) attacks if there are no additional protections in place (such as Anti-CSRF tokens).

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Web Based, Web Server

## Common consequences
- **Confidentiality, Integrity, Non-Repudiation, Access Control**: Modify Application Data

## Potential mitigations
- **Implementation**: Set the SameSite attribute of a sensitive cookie to 'Lax' or 'Strict'. This instructs the browser to apply this cookie only to same-domain requests, which provides a good Defense in Depth against CSRF attacks. When the 'Lax' value is in use, cookies are also sent for top-level cross-domain navigation via HTTP GET, HEAD, OPTIONS, and TRACE methods, but not for other HTTP methods that are more like to cause side-effects of state mutation.

## Related attack patterns (CAPEC)
- [CAPEC-62](https://capec.mitre.org/data/definitions/62.html)

## Related weaknesses
- CWE-923 (ChildOf)
- CWE-352 (CanPrecede)

## Observed examples (CVE)
- **CVE-2022-24045**: Web application for a room automation system has client-side JavaScript that sets a sensitive cookie without the SameSite security attribute, allowing the cookie to be sniffed

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1275.html
