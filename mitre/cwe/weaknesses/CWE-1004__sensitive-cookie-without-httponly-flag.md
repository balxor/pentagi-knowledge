---
cwe_id: CWE-1004
name: Sensitive Cookie Without 'HttpOnly' Flag
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1004.html
tags: [mitre-cwe, weakness, CWE-1004]
---

# CWE-1004 - Sensitive Cookie Without 'HttpOnly' Flag

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-1004](https://cwe.mitre.org/data/definitions/1004.html)

## Description
The product uses a cookie to store sensitive information, but the cookie is not marked with the HttpOnly flag.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Confidentiality**: Read Application Data
- **Integrity**: Gain Privileges or Assume Identity

## Potential mitigations
- **Implementation**: Leverage the HttpOnly flag when setting a sensitive cookie in a response.

## Related weaknesses
- CWE-732 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-47833**: python library for ML and data science does not use the HTTPOnly security attribute for session cookies
- **CVE-2022-24045**: Web application for a room automation system has client-side Javascript that sets a sensitive cookie without the HTTPOnly security attribute, allowing the cookie to be accessed.
- **CVE-2014-3852**: CMS written in Python does not include the HTTPOnly flag in a Set-Cookie header, allowing remote attackers to obtain potentially sensitive information via script access to this cookie.
- **CVE-2015-4138**: Appliance for managing encrypted communications does not use HttpOnly flag.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1004.html
