---
cwe_id: CWE-219
name: Storage of File with Sensitive Data Under Web Root
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/219.html
tags: [mitre-cwe, weakness, CWE-219]
---

# CWE-219 - Storage of File with Sensitive Data Under Web Root

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-219](https://cwe.mitre.org/data/definitions/219.html)

## Description
The product stores sensitive data under the web document root with insufficient access control, which might make it accessible to untrusted parties.

## Extended description
Besides public-facing web pages and code, products may store sensitive data, code that is not directly invoked, or other files under the web document root of the web server. If the server is not configured or otherwise used to prevent direct access to those files, then attackers may obtain this sensitive data.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation, System Configuration**: Avoid storing information under the web root directory.
- **System Configuration**: Access control permissions should be set to prevent reading/writing of sensitive files inside/outside of the web directory.

## Related weaknesses
- CWE-552 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-1835**: Data file under web root.
- **CVE-2005-2217**: Data file under web root.
- **CVE-2002-1449**: Username/password in data file under web root.
- **CVE-2002-0943**: Database file under web root.
- **CVE-2005-1645**: database file under web root.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/219.html
