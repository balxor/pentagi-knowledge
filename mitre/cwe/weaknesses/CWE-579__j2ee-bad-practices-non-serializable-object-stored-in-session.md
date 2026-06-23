---
cwe_id: CWE-579
name: J2EE Bad Practices: Non-serializable Object Stored in Session
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/579.html
tags: [mitre-cwe, weakness, CWE-579]
---

# CWE-579 - J2EE Bad Practices: Non-serializable Object Stored in Session

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-579](https://cwe.mitre.org/data/definitions/579.html)

## Description
The product stores a non-serializable object as an HttpSession attribute, which can hurt reliability.

## Extended description
A J2EE application can make use of multiple JVMs in order to improve application reliability and performance. In order to make the multiple JVMs appear as a single application to the end user, the J2EE container can replicate an HttpSession object across multiple JVMs so that if one JVM becomes unavailable another can step in and take its place without disrupting the flow of the application. This is only possible if all session data is serializable, allowing the session to be duplicated between the JVMs.

## Applicable platforms / languages
Java

## Common consequences
- **Other**: Quality Degradation

## Potential mitigations
- **Implementation**: In order for session replication to work, the values the product stores as attributes in the session must implement the Serializable interface.

## Related weaknesses
- CWE-573 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/579.html
