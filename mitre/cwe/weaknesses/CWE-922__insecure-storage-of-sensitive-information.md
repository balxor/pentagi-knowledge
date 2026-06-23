---
cwe_id: CWE-922
name: Insecure Storage of Sensitive Information
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/922.html
tags: [mitre-cwe, weakness, CWE-922]
---

# CWE-922 - Insecure Storage of Sensitive Information

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-922](https://cwe.mitre.org/data/definitions/922.html)

## Description
The product stores sensitive information without properly limiting read or write access by unauthorized actors.

## Extended description
If read access is not properly restricted, then attackers can steal the sensitive information. If write access is not properly restricted, then attackers can modify and possibly delete the data, causing incorrect results and possibly a denial of service.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data, Read Files or Directories
- **Integrity**: Modify Application Data, Modify Files or Directories

## Related weaknesses
- CWE-664 (ChildOf)

## Observed examples (CVE)
- **CVE-2009-2272**: password and username stored in cleartext in a cookie

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/922.html
