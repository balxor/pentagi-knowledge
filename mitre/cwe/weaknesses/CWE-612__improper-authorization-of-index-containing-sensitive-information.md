---
cwe_id: CWE-612
name: Improper Authorization of Index Containing Sensitive Information
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/612.html
tags: [mitre-cwe, weakness, CWE-612]
---

# CWE-612 - Improper Authorization of Index Containing Sensitive Information

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-612](https://cwe.mitre.org/data/definitions/612.html)

## Description
The product creates a search index of private or sensitive documents, but it does not properly limit index access to actors who are authorized to see the original information.

## Extended description
Web sites and other document repositories may apply an indexing routine against a group of private documents to facilitate search. If the index's results are available to parties who do not have access to the documents being indexed, then attackers could obtain portions of the documents by conducting targeted searches and reading the results. The risk is especially dangerous if search results include surrounding text that was not part of the search query. This issue can appear in search engines that are not configured (or implemented) to ignore critical files that should remain hidden; even without permissions to download these files directly, the remote user could read them.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based, Web Server

## Common consequences
- **Confidentiality**: Read Application Data

## Related weaknesses
- CWE-1230 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-41918**: A search application's access control rules are not properly applied to indices for data streams, allowing for the viewing of sensitive information.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/612.html
