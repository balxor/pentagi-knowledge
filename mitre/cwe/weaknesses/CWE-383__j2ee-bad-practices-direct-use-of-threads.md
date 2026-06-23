---
cwe_id: CWE-383
name: J2EE Bad Practices: Direct Use of Threads
type: weakness
abstraction: Variant
status: Draft
languages: [Java, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/383.html
tags: [mitre-cwe, weakness, CWE-383]
---

# CWE-383 - J2EE Bad Practices: Direct Use of Threads

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-383](https://cwe.mitre.org/data/definitions/383.html)

## Description
Thread management in a Web application is forbidden in some circumstances and is always highly error prone.

## Extended description
Thread management in a web application is forbidden by the J2EE standard in some circumstances and is always highly error prone. Managing threads is difficult and is likely to interfere in unpredictable ways with the behavior of the application container. Even without interfering with the container, thread management usually leads to bugs that are hard to detect and diagnose like deadlock, race conditions, and other synchronization errors.

## Applicable platforms / languages
Java, Web Based, Web Server

## Common consequences
- **Other**: Quality Degradation

## Potential mitigations
- **Architecture and Design**: For EJB, use framework approaches for parallel execution, instead of using threads.

## Related weaknesses
- CWE-695 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/383.html
