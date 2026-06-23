---
cwe_id: CWE-530
name: Exposure of Backup File to an Unauthorized Control Sphere
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/530.html
tags: [mitre-cwe, weakness, CWE-530]
---

# CWE-530 - Exposure of Backup File to an Unauthorized Control Sphere

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-530](https://cwe.mitre.org/data/definitions/530.html)

## Description
A backup file is stored in a directory or archive that is made accessible to unauthorized actors.

## Extended description
Often, older backup files are renamed with an extension such as .~bk to distinguish them from production files. The source code for old files that have been renamed in this manner and left in the webroot can often be retrieved. This renaming may have been performed automatically by the web server, or manually by the administrator.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Server

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Policy**: Recommendations include implementing a security policy within your organization that prohibits backing up web application source code in the webroot.

## Related weaknesses
- CWE-552 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-7315**: Chain: WordPress plugin does not use sufficient randomness when generating the filename for a backup (CWE-340), allowing attackers to obtain backup files (CWE-530)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/530.html
