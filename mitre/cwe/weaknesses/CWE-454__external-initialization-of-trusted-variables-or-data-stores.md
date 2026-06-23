---
cwe_id: CWE-454
name: External Initialization of Trusted Variables or Data Stores
type: weakness
abstraction: Base
status: Draft
languages: [PHP, Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/454.html
tags: [mitre-cwe, weakness, CWE-454]
---

# CWE-454 - External Initialization of Trusted Variables or Data Stores

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-454](https://cwe.mitre.org/data/definitions/454.html)

## Description
The product initializes critical internal variables or data stores using inputs that can be modified by untrusted actors.

## Extended description
A product system should be reluctant to trust variables that have been initialized outside of its trust boundary, especially if they are initialized by users. The variables may have been initialized incorrectly. If an attacker can initialize the variable, then they can influence what the vulnerable system will do.

## Applicable platforms / languages
PHP, Not Language-Specific

## Common consequences
- **Integrity**: Modify Application Data

## Potential mitigations
- **Implementation**: A product system should be reluctant to trust variables that have been initialized outside of its trust boundary. Ensure adequate checking (e.g. input validation) is performed when relying on input from outside a trust boundary.
- **Architecture and Design**: Avoid any external control of variables. If necessary, restrict the variables that can be modified using an allowlist, and use a different namespace or naming convention if possible.

## Related weaknesses
- CWE-1419 (ChildOf)
- CWE-456 (CanAlsoBe)

## Observed examples (CVE)
- **CVE-2022-43468**: WordPress module sets internal variables based on external inputs, allowing false reporting of the number of views
- **CVE-2000-0959**: Does not clear dangerous environment variables, enabling symlink attack.
- **CVE-2001-0033**: Specify alternate configuration directory in environment variable, enabling untrusted path.
- **CVE-2001-0872**: Dangerous environment variable not cleansed.
- **CVE-2001-0084**: Specify arbitrary modules using environment variable.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/454.html
