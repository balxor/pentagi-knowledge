---
cwe_id: CWE-653
name: Improper Isolation or Compartmentalization
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/653.html
tags: [mitre-cwe, weakness, CWE-653]
---

# CWE-653 - Improper Isolation or Compartmentalization

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-653](https://cwe.mitre.org/data/definitions/653.html)

## Description
The product does not properly compartmentalize or isolate functionality, processes, or resources that require different privilege levels, rights, or permissions.

## Extended description
When a weakness occurs in functionality that is accessible by lower-privileged users, then without strong boundaries, an attack might extend the scope of the damage to higher-privileged users.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity, Bypass Protection Mechanism

## Potential mitigations
- **Architecture and Design**: Break up privileges between different modules, objects, or entities. Minimize the interfaces between modules and require strong access control between them.

## Related weaknesses
- CWE-657 (ChildOf)
- CWE-693 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-33096**: Improper isolation of shared resource in a network-on-chip leads to denial of service
- **CVE-2019-6260**: Baseboard Management Controller (BMC) device implements Advanced High-performance Bus (AHB) bridges that do not require authentication for arbitrary read and write access to the BMC's physical address space from the host, and possibly the network [REF-1138].

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/653.html
