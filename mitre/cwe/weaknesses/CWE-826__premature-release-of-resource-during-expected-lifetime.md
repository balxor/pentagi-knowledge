---
cwe_id: CWE-826
name: Premature Release of Resource During Expected Lifetime
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/826.html
tags: [mitre-cwe, weakness, CWE-826]
---

# CWE-826 - Premature Release of Resource During Expected Lifetime

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-826](https://cwe.mitre.org/data/definitions/826.html)

## Description
The product releases a resource that is still intended to be used by itself or another actor.

## Extended description
This weakness focuses on errors in which the product should not release a resource, but performs the release anyway. This is different than a weakness in which the product releases a resource at the appropriate time, but it maintains a reference to the resource, which it later accesses. For this weakness, the resource should still be valid upon the subsequent access. When a product releases a resource that is still being used, it is possible that operations will still be taken on this resource, which may have been repurposed in the meantime, leading to issues similar to CWE-825. Consequences may include denial of service, information exposure, or code execution.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data, Read Memory
- **Availability**: DoS: Crash, Exit, or Restart
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands, Modify Application Data, Modify Memory

## Related weaknesses
- CWE-666 (ChildOf)
- CWE-672 (CanPrecede)

## Observed examples (CVE)
- **CVE-2009-3547**: Chain: race condition (CWE-362) might allow resource to be released before operating on it, leading to NULL dereference (CWE-476)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/826.html
