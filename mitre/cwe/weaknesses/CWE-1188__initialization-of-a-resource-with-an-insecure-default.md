---
cwe_id: CWE-1188
name: Initialization of a Resource with an Insecure Default
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-665]
url: https://cwe.mitre.org/data/definitions/1188.html
tags: [mitre-cwe, weakness, CWE-1188]
---

# CWE-1188 - Initialization of a Resource with an Insecure Default

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1188](https://cwe.mitre.org/data/definitions/1188.html)

## Description
The product initializes or sets a resource with a default that is intended to be changed by the product's installer, administrator, or maintainer, but the default is not secure.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Other**: Varies by Context

## Related attack patterns (CAPEC)
- [CAPEC-665](https://capec.mitre.org/data/definitions/665.html)

## Related weaknesses
- CWE-1419 (ChildOf)
- CWE-344 (ChildOf)
- CWE-665 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-36349**: insecure default variable initialization in BIOS firmware for a hardware board allows DoS
- **CVE-2022-42467**: A generic database browser interface has a default mode that exposes a web server to the network, allowing queries to the database.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1188.html
