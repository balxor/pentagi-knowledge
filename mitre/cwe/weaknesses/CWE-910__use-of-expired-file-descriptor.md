---
cwe_id: CWE-910
name: Use of Expired File Descriptor
type: weakness
abstraction: Base
status: Incomplete
languages: [C, C++, Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/910.html
tags: [mitre-cwe, weakness, CWE-910]
---

# CWE-910 - Use of Expired File Descriptor

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-910](https://cwe.mitre.org/data/definitions/910.html)

## Description
The product uses or accesses a file descriptor after it has been closed.

## Extended description
After a file descriptor for a particular file or device has been released, it can be reused. The code might not write to the original file, since the reused file descriptor might reference a different file or device.

## Applicable platforms / languages
C, C++, Not Language-Specific

## Common consequences
- **Confidentiality**: Read Files or Directories
- **Availability**: DoS: Crash, Exit, or Restart

## Related weaknesses
- CWE-672 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/910.html
