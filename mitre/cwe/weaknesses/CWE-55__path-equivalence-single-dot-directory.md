---
cwe_id: CWE-55
name: Path Equivalence: '/./' (Single Dot Directory)
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/55.html
tags: [mitre-cwe, weakness, CWE-55]
---

# CWE-55 - Path Equivalence: '/./' (Single Dot Directory)

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-55](https://cwe.mitre.org/data/definitions/55.html)

## Description
The product accepts path input in the form of single dot directory exploit ('/./') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Potential mitigations
- **Implementation**: Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.

## Related weaknesses
- CWE-41 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-6091**: Chain: AI agent platform does not restrict pathnames containing internal "/./" sequences (CWE-55), leading to an incomplete denylist (CWE-184) that does not prevent OS command injection (CWE-78)
- **CVE-2000-0004**: Server allows remote attackers to read source code for executable files by inserting a . (dot) into the URL.
- **CVE-2002-0304**: Server allows remote attackers to read password-protected files via a /./ in the HTTP request.
- **CVE-1999-1083**: Possibly (could be a cleansing error)
- **CVE-2004-0815**: "/./////etc" cleansed to ".///etc" then "/etc"
- **CVE-2002-0112**: Server allows remote attackers to view password protected files via /./ in the URL.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/55.html
