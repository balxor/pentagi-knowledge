---
cwe_id: CWE-340
name: Generation of Predictable Numbers or Identifiers
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/340.html
tags: [mitre-cwe, weakness, CWE-340]
---

# CWE-340 - Generation of Predictable Numbers or Identifiers

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-340](https://cwe.mitre.org/data/definitions/340.html)

## Description
The product uses a scheme that generates numbers or identifiers that are more predictable than required.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Varies by Context

## Related weaknesses
- CWE-330 (ChildOf)
- CWE-384 (CanPrecede)

## Observed examples (CVE)
- **CVE-2022-29330**: Product for administering PBX systems uses predictable identifiers and timestamps for filenames (CWE-340) which allows attackers to access files via direct request (CWE-425).
- **CVE-2001-1141**: PRNG allows attackers to use the output of small PRNG requests to determine the internal state information, which could be used by attackers to predict future pseudo-random numbers.
- **CVE-1999-0074**: Listening TCP ports are sequentially allocated, allowing spoofing attacks.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/340.html
