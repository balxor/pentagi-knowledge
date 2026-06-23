---
cwe_id: CWE-49
name: Path Equivalence: 'filename/' (Trailing Slash)
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, Web Based]
related_capec: []
url: https://cwe.mitre.org/data/definitions/49.html
tags: [mitre-cwe, weakness, CWE-49]
---

# CWE-49 - Path Equivalence: 'filename/' (Trailing Slash)

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-49](https://cwe.mitre.org/data/definitions/49.html)

## Description
The product accepts path input in the form of trailing slash ('filedir/') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Related weaknesses
- CWE-41 (ChildOf)
- CWE-162 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-0253**: Overlaps infoleak
- **CVE-2001-0446**: Application server allows remote attackers to read source code for .jsp files by appending a / to the requested URL.
- **CVE-2004-0334**: Bypass Basic Authentication for files using trailing "/"
- **CVE-2001-0893**: Read sensitive files with trailing "/"
- **CVE-2001-0892**: Web server allows remote attackers to view sensitive files under the document root (such as .htpasswd) via a GET request with a trailing /.
- **CVE-2004-1814**: Directory traversal vulnerability in server allows remote attackers to read protected files via .. (dot dot) sequences in an HTTP request.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/49.html
