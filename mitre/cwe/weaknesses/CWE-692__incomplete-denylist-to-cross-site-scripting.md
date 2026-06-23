---
cwe_id: CWE-692
name: Incomplete Denylist to Cross-Site Scripting
type: weakness
abstraction: Compound
status: Draft
languages: [Not Language-Specific, Web Based, Web Server]
related_capec: [CAPEC-120, CAPEC-267, CAPEC-71, CAPEC-80, CAPEC-85]
url: https://cwe.mitre.org/data/definitions/692.html
tags: [mitre-cwe, weakness, CWE-692]
---

# CWE-692 - Incomplete Denylist to Cross-Site Scripting

**Abstraction:** Compound  -  **Status:** Draft  -  **CWE:** [CWE-692](https://cwe.mitre.org/data/definitions/692.html)

## Description
The product uses a denylist-based protection mechanism to defend against XSS attacks, but the denylist is incomplete, allowing XSS variants to succeed.

## Extended description
While XSS might seem simple to prevent, web browsers vary so widely in how they parse web pages, that a denylist cannot keep track of all the variations. The "XSS Cheat Sheet" [REF-714] contains a large number of attacks that are intended to bypass incomplete denylists.

## Applicable platforms / languages
Not Language-Specific, Web Based, Web Server

## Common consequences
- **Confidentiality, Integrity, Availability**: Execute Unauthorized Code or Commands

## Related attack patterns (CAPEC)
- [CAPEC-120](https://capec.mitre.org/data/definitions/120.html)
- [CAPEC-267](https://capec.mitre.org/data/definitions/267.html)
- [CAPEC-71](https://capec.mitre.org/data/definitions/71.html)
- [CAPEC-80](https://capec.mitre.org/data/definitions/80.html)
- [CAPEC-85](https://capec.mitre.org/data/definitions/85.html)

## Related weaknesses
- CWE-184 (StartsWith)
- CWE-184 (ChildOf)

## Observed examples (CVE)
- **CVE-2007-5727**: Denylist only removes <SCRIPT> tag.
- **CVE-2006-3617**: Denylist only removes <SCRIPT> tag.
- **CVE-2006-4308**: Denylist only checks "javascript:" tag

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/692.html
