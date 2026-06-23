---
cwe_id: CWE-703
name: Improper Check or Handling of Exceptional Conditions
type: weakness
abstraction: Pillar
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/703.html
tags: [mitre-cwe, weakness, CWE-703]
---

# CWE-703 - Improper Check or Handling of Exceptional Conditions

**Abstraction:** Pillar  -  **Status:** Incomplete  -  **CWE:** [CWE-703](https://cwe.mitre.org/data/definitions/703.html)

## Description
The product does not properly anticipate or handle exceptional conditions that rarely occur during normal operation of the product.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Availability, Integrity**: Read Application Data, DoS: Crash, Exit, or Restart, Unexpected State

## Observed examples (CVE)
- **[REF-1374]**: Chain: JavaScript-based cryptocurrency library can fall back to the insecure Math.random() function instead of reporting a failure (CWE-392), thus reducing the entropy (CWE-332) and leading to generation of non-unique cryptographic keys for Bitcoin wallets (CWE-1391)
- **CVE-2022-22224**: Chain: an operating system does not properly process malformed Open Shortest Path First (OSPF) Type/Length/Value Identifiers (TLV) (CWE-703), which can cause the process to enter an infinite loop (CWE-835)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/703.html
