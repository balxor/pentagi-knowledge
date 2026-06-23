---
cwe_id: CWE-408
name: Incorrect Behavior Order: Early Amplification
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/408.html
tags: [mitre-cwe, weakness, CWE-408]
---

# CWE-408 - Incorrect Behavior Order: Early Amplification

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-408](https://cwe.mitre.org/data/definitions/408.html)

## Description
The product allows an entity to perform a legitimate but expensive operation before authentication or authorization has taken place.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: DoS: Amplification, DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory)

## Related weaknesses
- CWE-405 (ChildOf)
- CWE-696 (ChildOf)

## Observed examples (CVE)
- **CVE-2004-2458**: Tool creates directories before authenticating user.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/408.html
