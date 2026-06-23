---
cwe_id: CWE-437
name: Incomplete Model of Endpoint Features
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/437.html
tags: [mitre-cwe, weakness, CWE-437]
---

# CWE-437 - Incomplete Model of Endpoint Features

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-437](https://cwe.mitre.org/data/definitions/437.html)

## Description
A product acts as an intermediary or monitor between two or more endpoints, but it does not have a complete model of an endpoint's features, behaviors, or state, potentially causing the product to perform incorrect actions based on this incomplete model.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Other**: Unexpected State, Varies by Context

## Related weaknesses
- CWE-436 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-55629**: network-based IDS does not model how TCP endpoints handle TCP urgent data, allowing attackers to bypass detection

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/437.html
