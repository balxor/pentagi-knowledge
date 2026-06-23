---
cwe_id: CWE-552
name: Files or Directories Accessible to External Parties
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, Cloud Computing]
related_capec: [CAPEC-150, CAPEC-639]
url: https://cwe.mitre.org/data/definitions/552.html
tags: [mitre-cwe, weakness, CWE-552]
---

# CWE-552 - Files or Directories Accessible to External Parties

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-552](https://cwe.mitre.org/data/definitions/552.html)

## Description
The product makes files or directories accessible to unauthorized actors, even though they should not be.

## Extended description
Web servers, FTP servers, and similar servers may store a set of files underneath a "root" directory that is accessible to the server's users. Applications may store sensitive files underneath this root without also using access control to limit which users may request those files, if any. Alternately, an application might package multiple files or directories into an archive file (e.g., ZIP or tar), but the application might not exclude sensitive files that are underneath those directories. In cloud technologies and containers, this weakness might present itself in the form of misconfigured storage accounts that can be read or written by a public or anonymous user.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Cloud Computing

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Potential mitigations
- **Implementation, System Configuration, Operation**: When storing data in the cloud (e.g., S3 buckets, Azure blobs, Google Cloud Storage, etc.), use the provider's controls to disable public access.

## Related attack patterns (CAPEC)
- [CAPEC-150](https://capec.mitre.org/data/definitions/150.html)
- [CAPEC-639](https://capec.mitre.org/data/definitions/639.html)

## Related weaknesses
- CWE-668 (ChildOf)
- CWE-668 (ChildOf)
- CWE-285 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-1835**: Data file under web root.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/552.html
