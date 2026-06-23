---
cwe_id: CWE-316
name: Cleartext Storage of Sensitive Information in Memory
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/316.html
tags: [mitre-cwe, weakness, CWE-316]
---

# CWE-316 - Cleartext Storage of Sensitive Information in Memory

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-316](https://cwe.mitre.org/data/definitions/316.html)

## Description
The product stores sensitive information in cleartext in memory.

## Extended description
The sensitive memory might be saved to disk, stored in a core dump, or remain uncleared if the product crashes, or if the programmer does not properly clear the memory before freeing it. It could be argued that such problems are usually only exploitable by those with administrator privileges. However, swapping could cause the memory to be written to disk and leave it accessible to physical attack afterwards. Core dump files might have insecure permissions or be stored in archive files that are accessible to untrusted people. Or, uncleared sensitive memory might be inadvertently exposed to attackers due to another weakness.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Memory

## Related weaknesses
- CWE-312 (ChildOf)

## Observed examples (CVE)
- **CVE-2025-24870**: GUI for a desktop client stores credentials in program memory, allowing privilege escalation
- **CVE-2001-1517**: Sensitive authentication information in cleartext in memory.
- **CVE-2001-0984**: Password protector leaves passwords in memory when window is minimized, even when "clear password when minimized" is set.
- **CVE-2003-0291**: SSH client does not clear credentials from memory.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/316.html
