---
cwe_id: CWE-248
name: Uncaught Exception
type: weakness
abstraction: Base
status: Draft
languages: [C++, Java, C#]
related_capec: []
url: https://cwe.mitre.org/data/definitions/248.html
tags: [mitre-cwe, weakness, CWE-248]
---

# CWE-248 - Uncaught Exception

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-248](https://cwe.mitre.org/data/definitions/248.html)

## Description
An exception is thrown from a function, but it is not caught.

## Extended description
When an exception is not caught, it may cause the program to crash or expose sensitive information.

## Applicable platforms / languages
C++, Java, C#

## Common consequences
- **Availability, Confidentiality**: DoS: Crash, Exit, or Restart, Read Application Data

## Related weaknesses
- CWE-705 (ChildOf)
- CWE-755 (ChildOf)
- CWE-703 (ChildOf)
- CWE-703 (ChildOf)

## Observed examples (CVE)
- **CVE-2023-41151**: SDK for OPC Unified Architecture (OPC UA) server has uncaught exception when a socket is blocked for writing but the server tries to send an error
- **CVE-2023-21087**: Java code in a smartphone OS can encounter a "boot loop" due to an uncaught exception

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/248.html
