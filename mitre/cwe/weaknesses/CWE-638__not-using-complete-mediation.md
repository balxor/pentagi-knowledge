---
cwe_id: CWE-638
name: Not Using Complete Mediation
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-104]
url: https://cwe.mitre.org/data/definitions/638.html
tags: [mitre-cwe, weakness, CWE-638]
---

# CWE-638 - Not Using Complete Mediation

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-638](https://cwe.mitre.org/data/definitions/638.html)

## Description
The product does not perform access checks on a resource every time the resource is accessed by an entity, which can create resultant weaknesses if that entity's rights or privileges change over time.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Confidentiality, Availability, Access Control, Other**: Gain Privileges or Assume Identity, Execute Unauthorized Code or Commands, Bypass Protection Mechanism, Read Application Data, Other

## Potential mitigations
- **Architecture and Design**: Invalidate cached privileges, file handles or descriptors, or other access credentials whenever identities, processes, policies, roles, capabilities or permissions change. Perform complete authentication checks before accepting, caching and reusing data, dynamic content and code (scripts). Avoid caching access control decisions as much as possible.
- **Architecture and Design**: Identify all possible code paths that might access sensitive resources. If possible, create and use a single interface that performs the access checks, and develop code standards that require use of this interface.

## Related attack patterns (CAPEC)
- [CAPEC-104](https://capec.mitre.org/data/definitions/104.html)

## Related weaknesses
- CWE-657 (ChildOf)
- CWE-862 (ChildOf)

## Observed examples (CVE)
- **CVE-2007-0408**: Server does not properly validate client certificates when reusing cached connections.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/638.html
