---
cwe_id: CWE-419
name: Unprotected Primary Channel
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-383]
url: https://cwe.mitre.org/data/definitions/419.html
tags: [mitre-cwe, weakness, CWE-419]
---

# CWE-419 - Unprotected Primary Channel

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-419](https://cwe.mitre.org/data/definitions/419.html)

## Description
The product uses a primary channel for administration or restricted functionality, but it does not properly protect the channel.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity, Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Do not expose administrative functionnality on the user UI.
- **Architecture and Design**: Protect the administrative/restricted functionality with a strong authentication mechanism.

## Related attack patterns (CAPEC)
- [CAPEC-383](https://capec.mitre.org/data/definitions/383.html)

## Related weaknesses
- CWE-923 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/419.html
