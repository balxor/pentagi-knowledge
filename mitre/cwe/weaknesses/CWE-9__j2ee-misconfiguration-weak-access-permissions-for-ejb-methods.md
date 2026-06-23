---
cwe_id: CWE-9
name: J2EE Misconfiguration: Weak Access Permissions for EJB Methods
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/9.html
tags: [mitre-cwe, weakness, CWE-9]
---

# CWE-9 - J2EE Misconfiguration: Weak Access Permissions for EJB Methods

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-9](https://cwe.mitre.org/data/definitions/9.html)

## Description
If elevated access rights are assigned to EJB methods, then an attacker can take advantage of the permissions to exploit the product.

## Extended description
If the EJB deployment descriptor contains one or more method permissions that grant access to the special ANYONE role, it indicates that access control for the application has not been fully thought through or that the application is structured in such a way that reasonable access control restrictions are impossible.

## Applicable platforms / languages
Java

## Common consequences
- **Other**: Other

## Potential mitigations
- **Architecture and Design, System Configuration**: Follow the principle of least privilege when assigning access rights to EJB methods. Permission to invoke EJB methods should not be granted to the ANYONE role.

## Related weaknesses
- CWE-266 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/9.html
