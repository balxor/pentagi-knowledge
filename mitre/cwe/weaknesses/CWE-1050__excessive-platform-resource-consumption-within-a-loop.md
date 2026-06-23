---
cwe_id: CWE-1050
name: Excessive Platform Resource Consumption within a Loop
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1050.html
tags: [mitre-cwe, weakness, CWE-1050]
---

# CWE-1050 - Excessive Platform Resource Consumption within a Loop

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1050](https://cwe.mitre.org/data/definitions/1050.html)

## Description
The product has a loop body or loop condition that contains a control element that directly or indirectly consumes platform resources, e.g. messaging, sessions, locks, or file descriptors.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Resource Consumption (Other), Reduce Performance

## Related weaknesses
- CWE-405 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1050.html
