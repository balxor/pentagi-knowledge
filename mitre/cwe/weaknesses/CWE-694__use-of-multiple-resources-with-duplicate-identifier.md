---
cwe_id: CWE-694
name: Use of Multiple Resources with Duplicate Identifier
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/694.html
tags: [mitre-cwe, weakness, CWE-694]
---

# CWE-694 - Use of Multiple Resources with Duplicate Identifier

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-694](https://cwe.mitre.org/data/definitions/694.html)

## Description
The product uses multiple resources that can have the same identifier, in a context in which unique identifiers are required.

## Extended description
If the product assumes that each resource has a unique identifier, the product could operate on the wrong resource if attackers can cause multiple resources to be associated with the same identifier.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism
- **Other**: Quality Degradation

## Potential mitigations
- **Architecture and Design**: Where possible, use unique identifiers. If non-unique identifiers are detected, then do not operate any resource with a non-unique identifier and report the error appropriately.

## Related weaknesses
- CWE-99 (ChildOf)
- CWE-573 (ChildOf)

## Observed examples (CVE)
- **CVE-2013-4787**: chain: mobile OS verifies cryptographic signature of file in an archive, but then installs a different file with the same name that is also listed in the archive.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/694.html
