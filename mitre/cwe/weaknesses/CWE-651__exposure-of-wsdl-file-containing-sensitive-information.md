---
cwe_id: CWE-651
name: Exposure of WSDL File Containing Sensitive Information
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/651.html
tags: [mitre-cwe, weakness, CWE-651]
---

# CWE-651 - Exposure of WSDL File Containing Sensitive Information

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-651](https://cwe.mitre.org/data/definitions/651.html)

## Description
The Web services architecture may require exposing a Web Service Definition Language (WSDL) file that contains information on the publicly accessible services and how callers of these services should interact with them (e.g. what parameters they expect and what types they return).

## Extended description
An information exposure may occur if any of the following apply: The WSDL file is accessible to a wider audience than intended. The WSDL file contains information on the methods/services that should not be publicly accessible or information about deprecated methods. This problem is made more likely due to the WSDL often being automatically generated from the code. Information in the WSDL file helps guess names/locations of methods/resources that should not be publicly accessible.

## Applicable platforms / languages
Not Language-Specific, Web Server

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design**: Limit access to the WSDL file as much as possible. If services are provided only to a limited number of entities, it may be better to provide WSDL privately to each of these entities than to publish WSDL publicly.
- **Architecture and Design**: Make sure that WSDL does not describe methods that should not be publicly accessible. Make sure to protect service methods that should not be publicly accessible with access controls.
- **Architecture and Design**: Do not use method names in WSDL that might help an adversary guess names of private methods/resources used by the service.

## Related weaknesses
- CWE-538 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/651.html
