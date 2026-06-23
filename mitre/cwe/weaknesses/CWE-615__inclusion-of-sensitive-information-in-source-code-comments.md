---
cwe_id: CWE-615
name: Inclusion of Sensitive Information in Source Code Comments
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/615.html
tags: [mitre-cwe, weakness, CWE-615]
---

# CWE-615 - Inclusion of Sensitive Information in Source Code Comments

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-615](https://cwe.mitre.org/data/definitions/615.html)

## Description
While adding general comments is very useful, some programmers tend to leave important data, such as: filenames related to the web application, old links or links which were not meant to be browsed by users, old code fragments, etc.

## Extended description
An attacker who finds these comments can map the application's structure and files, expose hidden parts of the site, and study the fragments of code to reverse engineer the application, which may help develop further attacks against the site.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Distribution**: Remove comments which have sensitive information about the design/implementation of the application. Some of the comments may be exposed to the user and affect the security posture of the application.

## Related weaknesses
- CWE-540 (ChildOf)
- CWE-546 (PeerOf)

## Observed examples (CVE)
- **CVE-2007-6197**: Version numbers and internal hostnames leaked in HTML comments.
- **CVE-2007-4072**: CMS places full pathname of server in HTML comment.
- **CVE-2009-2431**: blog software leaks real username in HTML comment.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/615.html
