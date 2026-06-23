---
cwe_id: CWE-224
name: Obscured Security-relevant Information by Alternate Name
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/224.html
tags: [mitre-cwe, weakness, CWE-224]
---

# CWE-224 - Obscured Security-relevant Information by Alternate Name

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-224](https://cwe.mitre.org/data/definitions/224.html)

## Description
The product records security-relevant information according to an alternate name of the affected entity, instead of the canonical name.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Non-Repudiation, Access Control**: Hide Activities, Gain Privileges or Assume Identity

## Related weaknesses
- CWE-221 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-0725**: Attacker performs malicious actions on a hard link to a file, obscuring the real target file.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/224.html
