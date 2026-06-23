---
cwe_id: CWE-539
name: Use of Persistent Cookies Containing Sensitive Information
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: [CAPEC-21, CAPEC-31, CAPEC-39, CAPEC-59, CAPEC-60]
url: https://cwe.mitre.org/data/definitions/539.html
tags: [mitre-cwe, weakness, CWE-539]
---

# CWE-539 - Use of Persistent Cookies Containing Sensitive Information

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-539](https://cwe.mitre.org/data/definitions/539.html)

## Description
The web application uses persistent cookies, but the cookies contain sensitive information.

## Extended description
Cookies are small bits of data that are sent by the web application but stored locally in the browser. This lets the application use the cookie to pass information between pages and store variable information. The web application controls what information is stored in a cookie and how it is used. Typical types of information stored in cookies are session identifiers, personalization and customization information, and in rare cases even usernames to enable automated logins. There are two different types of cookies: session cookies and persistent cookies. Session cookies just live in the browser's memory and are not stored anywhere, but persistent cookies are stored on the browser's hard drive. This can cause security and privacy issues depending on the information stored in the cookie and how it is accessed.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design**: Do not store sensitive information in persistent cookies.

## Related attack patterns (CAPEC)
- [CAPEC-21](https://capec.mitre.org/data/definitions/21.html)
- [CAPEC-31](https://capec.mitre.org/data/definitions/31.html)
- [CAPEC-39](https://capec.mitre.org/data/definitions/39.html)
- [CAPEC-59](https://capec.mitre.org/data/definitions/59.html)
- [CAPEC-60](https://capec.mitre.org/data/definitions/60.html)

## Related weaknesses
- CWE-552 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/539.html
