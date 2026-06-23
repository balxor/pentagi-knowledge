---
cwe_id: CWE-532
name: Insertion of Sensitive Information into Log File
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-215]
url: https://cwe.mitre.org/data/definitions/532.html
tags: [mitre-cwe, weakness, CWE-532]
---

# CWE-532 - Insertion of Sensitive Information into Log File

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-532](https://cwe.mitre.org/data/definitions/532.html)

## Description
The product writes sensitive information to a log file.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design, Implementation**: Consider seriously the sensitivity of the information written into log files. Do not write secrets into the log files.
- **Distribution**: Remove debug log files before deploying the application into production.
- **Operation**: Protect log files against unauthorized read/write.
- **Implementation**: Adjust configurations appropriately when software is transitioned from a debug state to production.

## Related attack patterns (CAPEC)
- [CAPEC-215](https://capec.mitre.org/data/definitions/215.html)

## Related weaknesses
- CWE-538 (ChildOf)
- CWE-200 (ChildOf)

## Observed examples (CVE)
- **CVE-2017-9615**: verbose logging stores admin credentials in a world-readable log file
- **CVE-2018-1999036**: SSH password for private key stored in build log

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/532.html
