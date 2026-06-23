---
cwe_id: CWE-524
name: Use of Cache Containing Sensitive Information
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-204]
url: https://cwe.mitre.org/data/definitions/524.html
tags: [mitre-cwe, weakness, CWE-524]
---

# CWE-524 - Use of Cache Containing Sensitive Information

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-524](https://cwe.mitre.org/data/definitions/524.html)

## Description
The code uses a cache that contains sensitive information, but the cache can be read by an actor outside of the intended control sphere.

## Extended description
Applications may use caches to improve efficiency when communicating with remote entities or performing intensive calculations. A cache maintains a pool of objects, threads, connections, pages, financial data, passwords, or other resources to minimize the time it takes to initialize and access these resources. If the cache is accessible to unauthorized actors, attackers can read the cache and obtain this sensitive information.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design**: Protect information stored in cache.
- **Architecture and Design**: Do not store unnecessarily sensitive information in the cache.
- **Architecture and Design**: Consider using encryption in the cache.

## Related attack patterns (CAPEC)
- [CAPEC-204](https://capec.mitre.org/data/definitions/204.html)

## Related weaknesses
- CWE-668 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-30127**: Product does not set the "no-cache" option in the HTTP Cache-Control header, allowing sensitive information to be cached

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/524.html
