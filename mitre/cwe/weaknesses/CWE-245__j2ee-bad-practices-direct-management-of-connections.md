---
cwe_id: CWE-245
name: J2EE Bad Practices: Direct Management of Connections
type: weakness
abstraction: Variant
status: Draft
languages: [Java, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/245.html
tags: [mitre-cwe, weakness, CWE-245]
---

# CWE-245 - J2EE Bad Practices: Direct Management of Connections

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-245](https://cwe.mitre.org/data/definitions/245.html)

## Description
The J2EE application directly manages connections, instead of using the container's connection management facilities.

## Extended description
The J2EE standard forbids the direct management of connections. It requires that applications use the container's resource management facilities to obtain connections to resources. Every major web application container provides pooled database connection management as part of its resource management framework. Duplicating this functionality in an application is difficult and error prone, which is part of the reason it is forbidden under the J2EE standard.

## Applicable platforms / languages
Java, Web Based, Web Server

## Common consequences
- **Other**: Quality Degradation

## Related weaknesses
- CWE-695 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/245.html
