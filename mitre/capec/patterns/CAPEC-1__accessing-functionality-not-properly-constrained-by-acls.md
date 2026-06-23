---
capec_id: CAPEC-1
name: Accessing Functionality Not Properly Constrained by ACLs
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-276, CWE-285, CWE-434, CWE-693, CWE-732, CWE-1191, CWE-1193, CWE-1220, CWE-1297, CWE-1311, CWE-1314, CWE-1315, CWE-1318, CWE-1320, CWE-1321, CWE-1327]
related_attack: [T1574.010]
url: https://capec.mitre.org/data/definitions/1.html
tags: [mitre-capec, attack-pattern, CAPEC-1]
---

# CAPEC-1 - Accessing Functionality Not Properly Constrained by ACLs

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-1](https://capec.mitre.org/data/definitions/1.html)

## Description
In applications, particularly web applications, access to functionality is mitigated by an authorization framework. This framework maps Access Control Lists (ACLs) to elements of the application's functionality; particularly URL's for web apps. In the case that the administrator failed to specify an ACL for a particular element, an attacker may be able to access it with impunity. An attacker with the ability to access functionality not properly constrained by ACLs can obtain sensitive information and possibly compromise the entire application. Such an attacker can access resources that must be available only to users at a higher privilege level, can access management sections of the application, or can run queries for data that they otherwise not supposed to.

## Prerequisites
- The application must be navigable in a manner that associates elements (subsections) of the application with ACLs.
- The various resources, or individual URLs, must be somehow discoverable by the attacker
- The administrator must have forgotten to associate an ACL or has associated an inappropriately permissive ACL with a particular navigable resource.

## Skills required
- **Low**: In order to discover unrestricted resources, the attacker does not need special tools or skills. They only have to observe the resources or access mechanisms invoked as each action is performed and then try and access those access mechanisms directly.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges

## Execution flow
Execution Flow Explore Survey: The attacker surveys the target application, possibly as a valid and authenticated user Techniques Spidering web sites for all available links Brute force guessing of resource names Brute force guessing of user names / credentials Brute force guessing of function names / actions Identify Functionality: At each step, the attacker notes the resource or functionality access mechanism invoked upon performing specific actions Techniques Use the web inventory of all forms and inputs and apply attack data to those inputs. Use a packet sniffer to capture and record network traffic Execute the software in a debugger and record API calls into the operating system or important libraries. This might occur in an environment other than a production environment, in order to find weaknesses that can be exploited in a production environment. Experiment Iterate over access capabilities: Possibly as a valid user, the attacker then tries to access each of the noted access mechanisms directly in order to perform functions not constrained by the ACLs. Techniques Fuzzing of API parameters (URL parameters, OS API parameters, protocol parameters)

## Mitigations
- In a J2EE setting, administrators can associate a role that is impossible for the authenticator to grant users, such as "NoAccess", with all Servlets to which access is guarded by a limited number of servlets visible to, and accessible by, the user. Having done so, any direct access to those protected Servlets will be prohibited by the web container. In a more general setting, the administrator must mark every resource besides the ones supposed to be exposed to the user as accessible by a role impossible for the user to assume. The default security setting must be to deny access and then grant access only to those resources intended by business logic.

## Related weaknesses (CWE)
- [CWE-276](https://cwe.mitre.org/data/definitions/276.html)
- [CWE-285](https://cwe.mitre.org/data/definitions/285.html)
- [CWE-434](https://cwe.mitre.org/data/definitions/434.html)
- [CWE-693](https://cwe.mitre.org/data/definitions/693.html)
- [CWE-732](https://cwe.mitre.org/data/definitions/732.html)
- [CWE-1191](https://cwe.mitre.org/data/definitions/1191.html)
- [CWE-1193](https://cwe.mitre.org/data/definitions/1193.html)
- [CWE-1220](https://cwe.mitre.org/data/definitions/1220.html)
- [CWE-1297](https://cwe.mitre.org/data/definitions/1297.html)
- [CWE-1311](https://cwe.mitre.org/data/definitions/1311.html)
- [CWE-1314](https://cwe.mitre.org/data/definitions/1314.html)
- [CWE-1315](https://cwe.mitre.org/data/definitions/1315.html)
- [CWE-1318](https://cwe.mitre.org/data/definitions/1318.html)
- [CWE-1320](https://cwe.mitre.org/data/definitions/1320.html)
- [CWE-1321](https://cwe.mitre.org/data/definitions/1321.html)
- [CWE-1327](https://cwe.mitre.org/data/definitions/1327.html)

## Related ATT&CK techniques
- T1574.010

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/1.html
