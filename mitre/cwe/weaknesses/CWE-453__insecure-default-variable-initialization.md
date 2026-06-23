---
cwe_id: CWE-453
name: Insecure Default Variable Initialization
type: weakness
abstraction: Variant
status: Draft
languages: [PHP, Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/453.html
tags: [mitre-cwe, weakness, CWE-453]
---

# CWE-453 - Insecure Default Variable Initialization

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-453](https://cwe.mitre.org/data/definitions/453.html)

## Description
The product, by default, initializes an internal variable with an insecure or less secure value than is possible.

## Applicable platforms / languages
PHP, Not Language-Specific

## Common consequences
- **Integrity**: Modify Application Data

## Potential mitigations
- **System Configuration**: Disable or change default settings when they can be used to abuse the system. Since those default settings are shipped with the product they are likely to be known by a potential attacker who is familiar with the product. For instance, default credentials should be changed or the associated accounts should be disabled.

## Related weaknesses
- CWE-1188 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-36349**: insecure default variable initialization in BIOS firmware for a hardware board allows DoS

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/453.html
