---
cwe_id: CWE-792
name: Incomplete Filtering of One or More Instances of Special Elements
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/792.html
tags: [mitre-cwe, weakness, CWE-792]
---

# CWE-792 - Incomplete Filtering of One or More Instances of Special Elements

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-792](https://cwe.mitre.org/data/definitions/792.html)

## Description
The product receives data from an upstream component, but does not completely filter one or more instances of special elements before sending it to a downstream component.

## Extended description
Incomplete filtering of this nature involves either: only filtering a single instance of a special element when more exist, or not filtering all instances or all elements where multiple special elements exist.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity**: Unexpected State

## Related weaknesses
- CWE-791 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/792.html
