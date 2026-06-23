---
cwe_id: CWE-97
name: Improper Neutralization of Server-Side Includes (SSI) Within a Web Page
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: [CAPEC-101, CAPEC-35]
url: https://cwe.mitre.org/data/definitions/97.html
tags: [mitre-cwe, weakness, CWE-97]
---

# CWE-97 - Improper Neutralization of Server-Side Includes (SSI) Within a Web Page

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-97](https://cwe.mitre.org/data/definitions/97.html)

## Description
The product generates a web page, but does not neutralize or incorrectly neutralizes user-controllable input that could be interpreted as a server-side include (SSI) directive.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Confidentiality, Integrity, Availability**: Execute Unauthorized Code or Commands

## Related attack patterns (CAPEC)
- [CAPEC-101](https://capec.mitre.org/data/definitions/101.html)
- [CAPEC-35](https://capec.mitre.org/data/definitions/35.html)

## Related weaknesses
- CWE-96 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/97.html
