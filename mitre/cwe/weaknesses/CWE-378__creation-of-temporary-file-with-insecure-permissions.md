---
cwe_id: CWE-378
name: Creation of Temporary File With Insecure Permissions
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/378.html
tags: [mitre-cwe, weakness, CWE-378]
---

# CWE-378 - Creation of Temporary File With Insecure Permissions

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-378](https://cwe.mitre.org/data/definitions/378.html)

## Description
Opening temporary files without appropriate measures or controls can leave the file, its contents and any function that it impacts vulnerable to attack.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data
- **Authorization, Other**: Other
- **Integrity, Other**: Other

## Potential mitigations
- **Requirements**: Many contemporary languages have functions which properly handle this condition. Older C temp file functions are especially susceptible.
- **Implementation**: Ensure that you use proper file permissions. This can be achieved by using a safe temp file function. Temporary files should be writable and readable only by the process that owns the file.
- **Implementation**: Randomize temporary file names. This can also be achieved by using a safe temp-file function. This will ensure that temporary files will not be created in predictable places.

## Related weaknesses
- CWE-377 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-24823**: A network application framework uses the Java function createTempFile(), which will create a file that is readable by other local users of the system

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/378.html
