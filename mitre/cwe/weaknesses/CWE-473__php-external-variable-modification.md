---
cwe_id: CWE-473
name: PHP External Variable Modification
type: weakness
abstraction: Variant
status: Draft
languages: [PHP]
related_capec: [CAPEC-77]
url: https://cwe.mitre.org/data/definitions/473.html
tags: [mitre-cwe, weakness, CWE-473]
---

# CWE-473 - PHP External Variable Modification

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-473](https://cwe.mitre.org/data/definitions/473.html)

## Description
A PHP application does not properly protect against the modification of variables from external sources, such as query parameters or cookies. This can expose the application to numerous weaknesses that would not exist otherwise.

## Applicable platforms / languages
PHP

## Common consequences
- **Integrity**: Modify Application Data

## Potential mitigations
- **Requirements, Implementation**: Carefully identify which variables can be controlled or influenced by an external user, and consider adopting a naming convention to emphasize when externally modifiable variables are being used. An application should be reluctant to trust variables that have been initialized outside of its trust boundary. Ensure adequate checking is performed when relying on input from outside a trust boundary. Do not allow your application to run with register_globals enabled. If you implement a register_globals emulator, be extremely careful of variable extraction, dynamic evaluation, and similar issues, since weaknesses in your emulation could allow external variable modification to take place even without register_globals.

## Related attack patterns (CAPEC)
- [CAPEC-77](https://capec.mitre.org/data/definitions/77.html)

## Related weaknesses
- CWE-471 (ChildOf)
- CWE-98 (CanPrecede)

## Observed examples (CVE)
- **CVE-2000-0860**: File upload allows arbitrary file read by setting hidden form variables to match internal variable names.
- **CVE-2001-0854**: Mistakenly trusts $PHP_SELF variable to determine if include script was called by its parent.
- **CVE-2002-0764**: PHP remote file inclusion by modified assumed-immutable variable.
- **CVE-2001-1025**: Modify key variable when calling scripts that don't load a library that initializes it.
- **CVE-2003-0754**: Authentication bypass by modifying array used for authentication.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/473.html
