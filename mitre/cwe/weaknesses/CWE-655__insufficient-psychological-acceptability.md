---
cwe_id: CWE-655
name: Insufficient Psychological Acceptability
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/655.html
tags: [mitre-cwe, weakness, CWE-655]
---

# CWE-655 - Insufficient Psychological Acceptability

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-655](https://cwe.mitre.org/data/definitions/655.html)

## Description
The product has a protection mechanism that is too difficult or inconvenient to use, encouraging non-malicious users to disable or bypass the mechanism, whether by accident or on purpose.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Testing**: Where possible, perform human factors and usability studies to identify where your product's security mechanisms are difficult to use, and why.
- **Architecture and Design**: Make the security mechanism as seamless as possible, while also providing the user with sufficient details when a security decision produces unexpected results.

## Related weaknesses
- CWE-657 (ChildOf)
- CWE-693 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/655.html
