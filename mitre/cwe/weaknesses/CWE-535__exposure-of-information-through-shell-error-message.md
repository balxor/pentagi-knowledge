---
cwe_id: CWE-535
name: Exposure of Information Through Shell Error Message
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/535.html
tags: [mitre-cwe, weakness, CWE-535]
---

# CWE-535 - Exposure of Information Through Shell Error Message

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-535](https://cwe.mitre.org/data/definitions/535.html)

## Description
A command shell error message indicates that there exists an unhandled exception in the web application code. In many cases, an attacker can leverage the conditions that cause these errors in order to gain unauthorized access to the system.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Related weaknesses
- CWE-211 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/535.html
