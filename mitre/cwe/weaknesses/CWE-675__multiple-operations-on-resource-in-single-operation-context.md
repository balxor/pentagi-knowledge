---
cwe_id: CWE-675
name: Multiple Operations on Resource in Single-Operation Context
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/675.html
tags: [mitre-cwe, weakness, CWE-675]
---

# CWE-675 - Multiple Operations on Resource in Single-Operation Context

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-675](https://cwe.mitre.org/data/definitions/675.html)

## Description
The product performs the same operation on a resource two or more times, when the operation should only be applied once.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Other

## Related weaknesses
- CWE-573 (ChildOf)
- CWE-586 (PeerOf)
- CWE-102 (PeerOf)

## Observed examples (CVE)
- **CVE-2009-0935**: Attacker provides invalid address to a memory-reading function, causing a mutex to be unlocked twice
- **CVE-2019-13351**: file descriptor double close can cause the wrong file to be associated with a file descriptor.
- **CVE-2004-1939**: XSS protection mechanism attempts to remove "/" that could be used to close tags, but it can be bypassed using double encoded slashes (%252F)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/675.html
