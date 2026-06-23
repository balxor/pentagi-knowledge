---
cwe_id: CWE-341
name: Predictable from Observable State
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/341.html
tags: [mitre-cwe, weakness, CWE-341]
---

# CWE-341 - Predictable from Observable State

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-341](https://cwe.mitre.org/data/definitions/341.html)

## Description
A number or object is predictable based on observations that the attacker can make about the state of the system or network, such as time, process ID, etc.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Varies by Context

## Potential mitigations
- **Implementation**: Increase the entropy used to seed a PRNG.
- **Architecture and Design, Requirements**: Use products or modules that conform to FIPS 140-2 [REF-267] to avoid obvious entropy problems. Consult FIPS 140-2 Annex C ("Approved Random Number Generators").
- **Implementation**: Use a PRNG that periodically re-seeds itself using input from high-quality sources, such as hardware devices with high entropy. However, do not re-seed too frequently, or else the entropy source might block.

## Related weaknesses
- CWE-340 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-48445**: Chain: e-commerce app relies on an easily-guessable timestamp (CWE-341) in a weak authentication algorithm (CWE-1390)
- **CVE-2002-0389**: Mail server stores private mail messages with predictable filenames in a world-executable directory, which allows local users to read private mailing list archives.
- **CVE-2001-1141**: PRNG allows attackers to use the output of small PRNG requests to determine the internal state information, which could be used by attackers to predict future pseudo-random numbers.
- **CVE-2000-0335**: DNS resolver library uses predictable IDs, which allows a local attacker to spoof DNS query results.
- **CVE-2005-1636**: MFV. predictable filename and insecure permissions allows file modification to execute SQL queries.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/341.html
