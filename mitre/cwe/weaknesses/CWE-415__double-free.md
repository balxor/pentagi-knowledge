---
cwe_id: CWE-415
name: Double Free
type: weakness
abstraction: Variant
status: Draft
languages: [Memory-Unsafe, C, C++]
related_capec: []
url: https://cwe.mitre.org/data/definitions/415.html
tags: [mitre-cwe, weakness, CWE-415]
---

# CWE-415 - Double Free

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-415](https://cwe.mitre.org/data/definitions/415.html)

## Description
The product calls free() twice on the same memory address.

## Applicable platforms / languages
Memory-Unsafe, C, C++

## Common consequences
- **Integrity, Confidentiality, Availability**: Modify Memory, Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design**: Choose a language that provides automatic memory management.
- **Implementation**: Ensure that each allocation is freed only once. After freeing a chunk, set the pointer to NULL to ensure the pointer cannot be freed again. In complicated error conditions, be sure that clean-up routines respect the state of allocation properly. If the language is object oriented, ensure that object destructors delete each chunk of memory only once.
- **Implementation**: Use a static analysis tool to find double free instances.

## Related weaknesses
- CWE-825 (ChildOf)
- CWE-1341 (ChildOf)
- CWE-672 (ChildOf)
- CWE-672 (ChildOf)
- CWE-672 (ChildOf)
- CWE-666 (ChildOf)
- CWE-416 (PeerOf)
- CWE-123 (PeerOf)

## Observed examples (CVE)
- **CVE-2006-5051**: Chain: Signal handler contains too much functionality (CWE-828), introducing a race condition (CWE-362) that leads to a double free (CWE-415).
- **CVE-2004-0642**: Double free resultant from certain error conditions.
- **CVE-2004-0772**: Double free resultant from certain error conditions.
- **CVE-2005-1689**: Double free resultant from certain error conditions.
- **CVE-2003-0545**: Double free from invalid ASN.1 encoding.
- **CVE-2003-1048**: Double free from malformed GIF.
- **CVE-2005-0891**: Double free from malformed GIF.
- **CVE-2002-0059**: Double free from malformed compressed data.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/415.html
