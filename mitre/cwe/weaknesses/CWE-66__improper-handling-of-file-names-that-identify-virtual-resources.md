---
cwe_id: CWE-66
name: Improper Handling of File Names that Identify Virtual Resources
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/66.html
tags: [mitre-cwe, weakness, CWE-66]
---

# CWE-66 - Improper Handling of File Names that Identify Virtual Resources

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-66](https://cwe.mitre.org/data/definitions/66.html)

## Description
The product does not handle or incorrectly handles a file name that identifies a "virtual" resource that is not directly specified within the directory that is associated with the file name, causing the product to perform file-based operations on a resource that is not a file.

## Extended description
Virtual file names are represented like normal file names, but they are effectively aliases for other resources that do not behave like normal files. Depending on their functionality, they could be alternate entities. They are not necessarily listed in directories.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Other

## Related weaknesses
- CWE-706 (ChildOf)

## Observed examples (CVE)
- **CVE-1999-0278**: In IIS, remote attackers can obtain source code for ASP files by appending "::$DATA" to the URL.
- **CVE-2004-1084**: Server allows remote attackers to read files and resource fork content via HTTP requests to certain special file names related to multiple data streams in HFS+.
- **CVE-2002-0106**: Server allows remote attackers to cause a denial of service via a series of requests to .JSP files that contain an MS-DOS device name.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/66.html
