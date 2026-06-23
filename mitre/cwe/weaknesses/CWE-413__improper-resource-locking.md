---
cwe_id: CWE-413
name: Improper Resource Locking
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/413.html
tags: [mitre-cwe, weakness, CWE-413]
---

# CWE-413 - Improper Resource Locking

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-413](https://cwe.mitre.org/data/definitions/413.html)

## Description
The product does not lock or does not correctly lock a resource when the product must have exclusive access to the resource.

## Extended description
When a resource is not properly locked, an attacker could modify the resource while it is being operated on by the product. This might violate the product's assumption that the resource will not change, potentially leading to unexpected behaviors.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Availability**: Modify Application Data, DoS: Instability, DoS: Crash, Exit, or Restart

## Potential mitigations
- **Architecture and Design**: Use a non-conflicting privilege scheme.
- **Architecture and Design, Implementation**: Use synchronization when locking a resource.

## Related weaknesses
- CWE-667 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-20141**: Chain: an operating system kernel has insufficent resource locking (CWE-413) leading to a use after free (CWE-416).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/413.html
