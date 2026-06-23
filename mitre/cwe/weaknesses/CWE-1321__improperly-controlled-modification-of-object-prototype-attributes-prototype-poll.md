---
cwe_id: CWE-1321
name: Improperly Controlled Modification of Object Prototype Attributes ('Prototype Pollution')
type: weakness
abstraction: Variant
status: Incomplete
languages: [JavaScript]
related_capec: [CAPEC-1, CAPEC-180, CAPEC-77]
url: https://cwe.mitre.org/data/definitions/1321.html
tags: [mitre-cwe, weakness, CWE-1321]
---

# CWE-1321 - Improperly Controlled Modification of Object Prototype Attributes ('Prototype Pollution')

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-1321](https://cwe.mitre.org/data/definitions/1321.html)

## Description
The product receives input from an upstream component that specifies attributes that are to be initialized or updated in an object, but it does not properly control modifications of attributes of the object prototype.

## Applicable platforms / languages
JavaScript

## Common consequences
- **Confidentiality, Integrity, Availability**: Read Application Data, Modify Application Data
- **Availability**: DoS: Crash, Exit, or Restart

## Potential mitigations
- **Implementation**: By freezing the object prototype first (for example, Object.freeze(Object.prototype)), modification of the prototype becomes impossible.
- **Architecture and Design**: By blocking modifications of attributes that resolve to object prototype, such as proto or prototype, this weakness can be mitigated.
- **Implementation**: When handling untrusted objects, validating using a schema can be used.
- **Implementation**: By using an object without prototypes (via Object.create(null) ), adding object prototype attributes by accessing the prototype via the special attributes becomes impossible, mitigating this weakness.
- **Implementation**: Map can be used instead of objects in most cases. If Map methods are used instead of object attributes, it is not possible to access the object prototype or modify it.

## Related attack patterns (CAPEC)
- [CAPEC-1](https://capec.mitre.org/data/definitions/1.html)
- [CAPEC-180](https://capec.mitre.org/data/definitions/180.html)
- [CAPEC-77](https://capec.mitre.org/data/definitions/77.html)

## Related weaknesses
- CWE-915 (ChildOf)
- CWE-913 (ChildOf)
- CWE-471 (CanPrecede)

## Observed examples (CVE)
- **CVE-2018-3721**: Prototype pollution by merging objects.
- **CVE-2019-10744**: Prototype pollution by setting default values to object attributes recursively.
- **CVE-2019-11358**: Prototype pollution by merging objects recursively.
- **CVE-2020-8203**: Prototype pollution by setting object attributes based on dot-separated path.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1321.html
