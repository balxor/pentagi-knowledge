---
cwe_id: CWE-202
name: Exposure of Sensitive Information Through Data Queries
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/202.html
tags: [mitre-cwe, weakness, CWE-202]
---

# CWE-202 - Exposure of Sensitive Information Through Data Queries

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-202](https://cwe.mitre.org/data/definitions/202.html)

## Description
When trying to keep information confidential, an attacker can often infer some of the information by using statistics.

## Extended description
In situations where data should not be tied to individual users, but a large number of users should be able to make queries that "scrub" the identity of users, it may be possible to get information about a user -- e.g., by specifying search terms that are known to be unique to that user.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Files or Directories, Read Application Data

## Potential mitigations
- **Architecture and Design**: This is a complex topic. See the [REF-1492] for a good discussion of best practices.

## Related weaknesses
- CWE-1230 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-41935**: Wiki product allows an adversary to discover filenames via a series of queries starting with one letter and then iteratively extending the match.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/202.html
