---
cwe_id: CWE-69
name: Improper Handling of Windows ::DATA Alternate Data Stream
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Windows]
related_capec: [CAPEC-168]
url: https://cwe.mitre.org/data/definitions/69.html
tags: [mitre-cwe, weakness, CWE-69]
---

# CWE-69 - Improper Handling of Windows ::DATA Alternate Data Stream

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-69](https://cwe.mitre.org/data/definitions/69.html)

## Description
The product does not properly prevent access to, or detect usage of, alternate data streams (ADS).

## Extended description
An attacker can use an ADS to hide information about a file (e.g. size, the name of the process) from a system or file browser tools such as Windows Explorer and 'dir' at the command line utility. Alternately, the attacker might be able to bypass intended access restrictions for the associated data fork.

## Applicable platforms / languages
Not Language-Specific, Windows

## Common consequences
- **Access Control, Non-Repudiation, Other**: Bypass Protection Mechanism, Hide Activities, Other

## Potential mitigations
- **Implementation**: Ensure that the source code correctly parses the filename to read or write to the correct stream.

## Related attack patterns (CAPEC)
- [CAPEC-168](https://capec.mitre.org/data/definitions/168.html)

## Related weaknesses
- CWE-66 (ChildOf)

## Observed examples (CVE)
- **CVE-1999-0278**: In IIS, remote attackers can obtain source code for ASP files by appending "::$DATA" to the URL.
- **CVE-2000-0927**: Product does not properly record file sizes if they are stored in alternative data streams, which allows users to bypass quota restrictions.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/69.html
