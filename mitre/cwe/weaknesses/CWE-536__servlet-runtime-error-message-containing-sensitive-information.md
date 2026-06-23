---
cwe_id: CWE-536
name: Servlet Runtime Error Message Containing Sensitive Information
type: weakness
abstraction: Variant
status: Incomplete
languages: [Java, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/536.html
tags: [mitre-cwe, weakness, CWE-536]
---

# CWE-536 - Servlet Runtime Error Message Containing Sensitive Information

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-536](https://cwe.mitre.org/data/definitions/536.html)

## Description
A servlet error message indicates that there exists an unhandled exception in the web application code and may provide useful information to an attacker.

## Applicable platforms / languages
Java, Web Based, Web Server

## Common consequences
- **Confidentiality**: Read Application Data

## Related weaknesses
- CWE-211 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/536.html
