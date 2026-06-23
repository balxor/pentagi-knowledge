---
cwe_id: CWE-342
name: Predictable Exact Value from Previous Values
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/342.html
tags: [mitre-cwe, weakness, CWE-342]
---

# CWE-342 - Predictable Exact Value from Previous Values

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-342](https://cwe.mitre.org/data/definitions/342.html)

## Description
An exact value or random number can be precisely predicted by observing previous values.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Varies by Context

## Potential mitigations
- **general**: Increase the entropy used to seed a PRNG.
- **Architecture and Design, Requirements**: Use products or modules that conform to FIPS 140-2 [REF-267] to avoid obvious entropy problems. Consult FIPS 140-2 Annex C ("Approved Random Number Generators").
- **Implementation**: Use a PRNG that periodically re-seeds itself using input from high-quality sources, such as hardware devices with high entropy. However, do not re-seed too frequently, or else the entropy source might block.

## Related weaknesses
- CWE-340 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-1463**: Firewall generates easily predictable initial sequence numbers (ISN), which allows remote attackers to spoof connections.
- **CVE-1999-0074**: Listening TCP ports are sequentially allocated, allowing spoofing attacks.
- **CVE-1999-0077**: Predictable TCP sequence numbers allow spoofing.
- **CVE-2000-0335**: DNS resolver uses predictable IDs, allowing a local user to spoof DNS query results.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/342.html
