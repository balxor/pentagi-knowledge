---
cwe_id: CWE-363
name: Race Condition Enabling Link Following
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-26]
url: https://cwe.mitre.org/data/definitions/363.html
tags: [mitre-cwe, weakness, CWE-363]
---

# CWE-363 - Race Condition Enabling Link Following

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-363](https://cwe.mitre.org/data/definitions/363.html)

## Description
The product checks the status of a file or directory before accessing it, which produces a race condition in which the file can be replaced with a link before the access is performed, causing the product to access the wrong file.

## Extended description
While developers might expect that there is a very narrow time window between the time of check and time of use, there is still a race condition. An attacker could cause the product to slow down (e.g. with memory consumption), causing the time window to become larger. Alternately, in some situations, the attacker could win the race by performing a large number of attacks.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity**: Read Files or Directories, Modify Files or Directories

## Related attack patterns (CAPEC)
- [CAPEC-26](https://capec.mitre.org/data/definitions/26.html)

## Related weaknesses
- CWE-367 (ChildOf)
- CWE-59 (CanPrecede)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/363.html
