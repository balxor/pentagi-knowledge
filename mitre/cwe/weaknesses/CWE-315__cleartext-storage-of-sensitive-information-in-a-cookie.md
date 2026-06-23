---
cwe_id: CWE-315
name: Cleartext Storage of Sensitive Information in a Cookie
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-31, CAPEC-37, CAPEC-39, CAPEC-74]
url: https://cwe.mitre.org/data/definitions/315.html
tags: [mitre-cwe, weakness, CWE-315]
---

# CWE-315 - Cleartext Storage of Sensitive Information in a Cookie

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-315](https://cwe.mitre.org/data/definitions/315.html)

## Description
The product stores sensitive information in cleartext in a cookie.

## Extended description
Attackers can use widely-available tools to view the cookie and read the sensitive information. Even if the information is encoded in a way that is not human-readable, certain techniques could determine which encoding is being used, then decode the information.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Related attack patterns (CAPEC)
- [CAPEC-31](https://capec.mitre.org/data/definitions/31.html)
- [CAPEC-37](https://capec.mitre.org/data/definitions/37.html)
- [CAPEC-39](https://capec.mitre.org/data/definitions/39.html)
- [CAPEC-74](https://capec.mitre.org/data/definitions/74.html)

## Related weaknesses
- CWE-312 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-1800**: Admin password in cleartext in a cookie.
- **CVE-2001-1537**: Default configuration has cleartext usernames/passwords in cookie.
- **CVE-2001-1536**: Usernames/passwords in cleartext in cookies.
- **CVE-2005-2160**: Authentication information stored in cleartext in a cookie.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/315.html
