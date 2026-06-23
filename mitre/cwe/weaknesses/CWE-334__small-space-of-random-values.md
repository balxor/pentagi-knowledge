---
cwe_id: CWE-334
name: Small Space of Random Values
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/334.html
tags: [mitre-cwe, weakness, CWE-334]
---

# CWE-334 - Small Space of Random Values

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-334](https://cwe.mitre.org/data/definitions/334.html)

## Description
The number of possible random values is smaller than needed by the product, making it more susceptible to brute force attacks.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Access Control, Other**: Bypass Protection Mechanism, Other

## Potential mitigations
- **Architecture and Design, Requirements**: Use products or modules that conform to FIPS 140-2 [REF-267] to avoid obvious entropy problems. Consult FIPS 140-2 Annex C ("Approved Random Number Generators").

## Related weaknesses
- CWE-330 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-0583**: Product uses 5 alphanumeric characters for filenames of expense claim reports, stored under web root.
- **CVE-2002-0903**: Product uses small number of random numbers for a code to approve an action, and also uses predictable new user IDs, allowing attackers to hijack new accounts.
- **CVE-2003-1230**: SYN cookies implementation only uses 32-bit keys, making it easier to brute force ISN.
- **CVE-2004-0230**: Complex predictability / randomness (reduced space).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/334.html
