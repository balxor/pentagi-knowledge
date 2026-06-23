---
cwe_id: CWE-832
name: Unlock of a Resource that is not Locked
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/832.html
tags: [mitre-cwe, weakness, CWE-832]
---

# CWE-832 - Unlock of a Resource that is not Locked

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-832](https://cwe.mitre.org/data/definitions/832.html)

## Description
The product attempts to unlock a resource that is not locked.

## Extended description
Depending on the locking functionality, an unlock of a non-locked resource might cause memory corruption or other modification to the resource (or its associated metadata that is used for tracking locks).

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Confidentiality, Availability, Other**: DoS: Crash, Exit, or Restart, Execute Unauthorized Code or Commands, Modify Memory, Other

## Related weaknesses
- CWE-667 (ChildOf)

## Observed examples (CVE)
- **CVE-2010-4210**: function in OS kernel unlocks a mutex that was not previously locked, causing a panic or overwrite of arbitrary memory.
- **CVE-2008-4302**: Chain: OS kernel does not properly handle a failure of a function call (CWE-755), leading to an unlock of a resource that was not locked (CWE-832), with resultant crash.
- **CVE-2009-1243**: OS kernel performs an unlock in some incorrect circumstances, leading to panic.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/832.html
