---
cwe_id: CWE-488
name: Exposure of Data Element to Wrong Session
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-59, CAPEC-60]
url: https://cwe.mitre.org/data/definitions/488.html
tags: [mitre-cwe, weakness, CWE-488]
---

# CWE-488 - Exposure of Data Element to Wrong Session

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-488](https://cwe.mitre.org/data/definitions/488.html)

## Description
The product does not sufficiently enforce boundaries between the states of different sessions, causing data to be provided to, or used by, the wrong session.

## Extended description
Data can "bleed" from one session to another through member variables of singleton objects, such as Servlets, and objects from a shared pool. In the case of Servlets, developers sometimes do not understand that, unless a Servlet implements the SingleThreadModel interface, the Servlet is a singleton; there is only one instance of the Servlet, and that single instance is used and re-used to handle multiple requests that are processed simultaneously by different threads. A common result is that developers use Servlet member fields in such a way that one user may inadvertently see another user's data. In other words, storing user data in Servlet member fields introduces a data access race condition.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design**: Protect the application's sessions from information leakage. Make sure that a session's data is not used or visible by other sessions.
- **Testing**: Use a static analysis tool to scan the code for information leakage vulnerabilities (e.g. Singleton Member Field).
- **Architecture and Design**: In a multithreading environment, storing user data in Servlet member fields introduces a data access race condition. Do not use member fields to store information in the Servlet.

## Related attack patterns (CAPEC)
- [CAPEC-59](https://capec.mitre.org/data/definitions/59.html)
- [CAPEC-60](https://capec.mitre.org/data/definitions/60.html)

## Related weaknesses
- CWE-668 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/488.html
