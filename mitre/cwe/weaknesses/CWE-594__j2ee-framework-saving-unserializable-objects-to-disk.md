---
cwe_id: CWE-594
name: J2EE Framework: Saving Unserializable Objects to Disk
type: weakness
abstraction: Variant
status: Incomplete
languages: [Java, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/594.html
tags: [mitre-cwe, weakness, CWE-594]
---

# CWE-594 - J2EE Framework: Saving Unserializable Objects to Disk

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-594](https://cwe.mitre.org/data/definitions/594.html)

## Description
When the J2EE container attempts to write unserializable objects to disk there is no guarantee that the process will complete successfully.

## Extended description
In heavy load conditions, most J2EE application frameworks flush objects to disk to manage memory requirements of incoming requests. For example, session scoped objects, and even application scoped objects, are written to disk when required. While these application frameworks do the real work of writing objects to disk, they do not enforce that those objects be serializable, thus leaving the web application vulnerable to crashes induced by serialization failure. An attacker may be able to mount a denial of service attack by sending enough requests to the server to force the web application to save objects to disk.

## Applicable platforms / languages
Java, Web Based, Web Server

## Common consequences
- **Integrity**: Modify Application Data
- **Availability**: DoS: Crash, Exit, or Restart

## Potential mitigations
- **Architecture and Design, Implementation**: All objects that become part of session and application scope must implement the java.io.Serializable interface to ensure serializability of containing objects.

## Related weaknesses
- CWE-1076 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/594.html
