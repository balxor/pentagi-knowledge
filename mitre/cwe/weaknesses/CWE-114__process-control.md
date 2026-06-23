---
cwe_id: CWE-114
name: Process Control
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-108, CAPEC-640]
url: https://cwe.mitre.org/data/definitions/114.html
tags: [mitre-cwe, weakness, CWE-114]
---

# CWE-114 - Process Control

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-114](https://cwe.mitre.org/data/definitions/114.html)

## Description
Executing commands or loading libraries from an untrusted source or in an untrusted environment can cause an application to execute malicious commands (and payloads) on behalf of an attacker.

## Extended description
Process control vulnerabilities take two forms: An attacker can change the command that the program executes: the attacker explicitly controls what the command is. An attacker can change the environment in which the command executes: the attacker implicitly controls what the command means. Process control vulnerabilities of the first type occur when either data enters the application from an untrusted source and the data is used as part of a string representing a command that is executed by the application. By executing the command, the application gives an attacker a privilege or capability that the attacker would not otherwise have.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Integrity, Availability**: Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design**: Libraries that are loaded should be well understood and come from a trusted source. The application can execute code contained in the native libraries, which often contain calls that are susceptible to other security problems, such as buffer overflows or command injection. All native libraries should be validated to determine if the application requires the use of the library. It is very difficult to determine what these native libraries actually do, and the potential for malicious code is high. In addition, the potential for an inadvertent mistake in these native libraries is also high, as many are written in C or C++ and may be susceptible to buffer overflow or race condition problems. To help prevent buffer overflow attacks, validate all input to native calls for content and length. If the native library does not come from a trusted source, review the source code of the library. The library should be built from the reviewed source before using it.

## Related attack patterns (CAPEC)
- [CAPEC-108](https://capec.mitre.org/data/definitions/108.html)
- [CAPEC-640](https://capec.mitre.org/data/definitions/640.html)

## Related weaknesses
- CWE-73 (ChildOf)
- CWE-20 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/114.html
