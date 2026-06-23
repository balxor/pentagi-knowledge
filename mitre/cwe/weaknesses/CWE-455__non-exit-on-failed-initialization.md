---
cwe_id: CWE-455
name: Non-exit on Failed Initialization
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/455.html
tags: [mitre-cwe, weakness, CWE-455]
---

# CWE-455 - Non-exit on Failed Initialization

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-455](https://cwe.mitre.org/data/definitions/455.html)

## Description
The product does not exit or otherwise modify its operation when security-relevant errors occur during initialization, such as when a configuration file has a format error or a hardware security module (HSM) cannot be activated, which can cause the product to execute in a less secure fashion than intended by the administrator.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Other**: Modify Application Data, Alter Execution Logic

## Potential mitigations
- **Implementation**: Follow the principle of failing securely when an error occurs. The system should enter a state where it is not vulnerable and will not display sensitive error messages to a potential attacker.

## Related weaknesses
- CWE-665 (ChildOf)
- CWE-705 (ChildOf)
- CWE-636 (ChildOf)

## Observed examples (CVE)
- **CVE-2005-1345**: Product does not trigger a fatal error if missing or invalid ACLs are in a configuration file.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/455.html
