---
capec_id: CAPEC-58
name: Restful Privilege Elevation
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-267, CWE-269]
related_attack: []
url: https://capec.mitre.org/data/definitions/58.html
tags: [mitre-capec, attack-pattern, CAPEC-58]
---

# CAPEC-58 - Restful Privilege Elevation

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-58](https://capec.mitre.org/data/definitions/58.html)

## Description
An adversary identifies a Rest HTTP (Get, Put, Delete) style permission method allowing them to perform various malicious actions upon server data due to lack of access control mechanisms implemented within the application service accepting HTTP messages.

## Extended description
Rest uses standard HTTP (Get, Put, Delete) style permissions methods, but these are not necessarily correlated generally with back end programs. Strict interpretation of HTTP get methods means that these HTTP Get services should not be used to delete information on the server, but there is no access control mechanism to back up this logic. This means that unless the services are properly ACL'd and the application's service implementation are following these guidelines then an HTTP request can easily execute a delete or update on the server side. The attacker identifies a HTTP Get URL such as http://victimsite/updateOrder, which calls out to a program to update orders on a database or other resource. The URL is not idempotent so the request can be submitted multiple times by the attacker, additionally, the attacker may be able to exploit the URL published as a Get method that actually performs updates (instead of merely retrieving data). This may result in malicious or inadvertent altering of data on the server.

## Prerequisites
- The attacker needs to be able to identify HTTP Get URLs. The Get methods must be set to call applications that perform operations other than get such as update and delete.

## Skills required
- **Low**: It is relatively straightforward to identify an HTTP Get method that changes state on the server side and executes against an over-privileged system interface

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges
- **Integrity**: Modify Data

## Mitigations
- Design: Enforce principle of least privilege
- Implementation: Ensure that HTTP Get methods only retrieve state and do not alter state on the server side
- Implementation: Ensure that HTTP methods have proper ACLs based on what the functionality they expose

## Related weaknesses (CWE)
- [CWE-267](https://cwe.mitre.org/data/definitions/267.html)
- [CWE-269](https://cwe.mitre.org/data/definitions/269.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/58.html
