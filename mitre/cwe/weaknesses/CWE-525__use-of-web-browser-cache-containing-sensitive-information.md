---
cwe_id: CWE-525
name: Use of Web Browser Cache Containing Sensitive Information
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: [CAPEC-37]
url: https://cwe.mitre.org/data/definitions/525.html
tags: [mitre-cwe, weakness, CWE-525]
---

# CWE-525 - Use of Web Browser Cache Containing Sensitive Information

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-525](https://cwe.mitre.org/data/definitions/525.html)

## Description
The web application does not use an appropriate caching policy that specifies the extent to which each web page and associated form fields should be cached.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design**: Protect information stored in cache.
- **Implementation**: Use a restrictive caching policy for forms and web pages that potentially contain sensitive information, such as "no-cache" in the Cache-Control header.
- **Architecture and Design**: Do not store unnecessarily sensitive information in the cache.
- **Architecture and Design**: Consider using encryption in the cache.

## Related attack patterns (CAPEC)
- [CAPEC-37](https://capec.mitre.org/data/definitions/37.html)

## Related weaknesses
- CWE-524 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-30127**: Product does not set the "no-cache" option in the HTTP Cache-Control, allowing sensitive information to be cached
- **CVE-2024-45314**: Login form for an application development framework does not set "no-cache" and other options in the HTTP Cache-Control header, allowing sensitive information to be cached

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/525.html
