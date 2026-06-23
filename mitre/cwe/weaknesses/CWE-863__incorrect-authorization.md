---
cwe_id: CWE-863
name: Incorrect Authorization
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Web Server, Database Server, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/863.html
tags: [mitre-cwe, weakness, CWE-863]
---

# CWE-863 - Incorrect Authorization

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-863](https://cwe.mitre.org/data/definitions/863.html)

## Description
The product performs an authorization check when an actor attempts to access a resource or perform an action, but it does not correctly perform the check.

## Applicable platforms / languages
Not Language-Specific, Web Server, Database Server, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Application Data, Read Files or Directories
- **Integrity**: Modify Application Data, Modify Files or Directories
- **Access Control**: Gain Privileges or Assume Identity, Bypass Protection Mechanism
- **Confidentiality, Integrity, Availability**: Execute Unauthorized Code or Commands
- **Availability**: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Resource Consumption (Other)

## Potential mitigations
- **Architecture and Design**: Divide the product into anonymous, normal, privileged, and administrative areas. Reduce the attack surface by carefully mapping roles with data and functionality. Use role-based access control (RBAC) [REF-229] to enforce the roles at the appropriate boundaries. Note that this approach may not protect against horizontal authorization, i.e., it will not protect a user from attacking others with the same role.
- **Architecture and Design**: Ensure that access control checks are performed related to the business logic. These checks may be different than the access control checks that are applied to more generic resources such as files, connections, processes, memory, and database records. For example, a database may restrict access for medical records to a specific database user, but each record might only be intended to be accessible to the patient and the patient's doctor [REF-7].
- **Architecture and Design**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, consider using authorization frameworks such as the JAAS Authorization Framework [REF-233] and the OWASP ESAPI Access Control feature [REF-45].
- **Architecture and Design**: For web applications, make sure that the access control mechanism is enforced correctly at the server side on every page. Users should not be able to access any unauthorized functionality or information by simply requesting direct access to that page. One way to do this is to ensure that all pages containing sensitive information are not cached, and that all such pages restrict access to requests that are accompanied by an active and authenticated session token associated with a user who has the required permissions to access that page.
- **System Configuration, Installation**: Use the access control capabilities of your operating system and server environment and define your access control lists accordingly. Use a "default deny" policy when defining these ACLs.

## Related weaknesses
- CWE-285 (ChildOf)
- CWE-284 (ChildOf)

## Observed examples (CVE)
- **CVE-2025-24839**: collaboration platform allows attacker to access an AI bot by using a plugin to set a critical property
- **CVE-2025-32796**: LLM application development platform allows non-admin users to enable or disable apps using certain API endpoints
- **CVE-2021-39155**: Chain: A microservice integration and management platform compares the hostname in the HTTP Host header in a case-sensitive way (CWE-178, CWE-1289), allowing bypass of the authorization policy (CWE-863) using a hostname with mixed case or other variations.
- **CVE-2019-15900**: Chain: sscanf() call is used to check if a username and group exists, but the return value of sscanf() call is not checked (CWE-252), causing an uninitialized variable to be checked (CWE-457), returning success to allow authorization bypass for executing a privileged (CWE-863).
- **CVE-2009-2213**: Gateway uses default "Allow" configuration for its authorization settings.
- **CVE-2009-0034**: Chain: product does not properly interpret a configuration option for a system group, allowing users to gain privileges.
- **CVE-2008-6123**: Chain: SNMP product does not properly parse a configuration option for which hosts are allowed to connect, allowing unauthorized IP addresses to connect.
- **CVE-2008-7109**: Chain: reliance on client-side security (CWE-602) allows attackers to bypass authorization using a custom client.
- **CVE-2008-3424**: Chain: product does not properly handle wildcards in an authorization policy list, allowing unintended access.
- **CVE-2008-4577**: ACL-based protection mechanism treats negative access rights as if they are positive, allowing bypass of intended restrictions.
- **CVE-2006-6679**: Product relies on the X-Forwarded-For HTTP header for authorization, allowing unintended access by spoofing the header.
- **CVE-2005-2801**: Chain: file-system code performs an incorrect comparison (CWE-697), preventing default ACLs from being properly applied.
- **CVE-2001-1155**: Chain: product does not properly check the result of a reverse DNS lookup because of operator precedence (CWE-783), allowing bypass of DNS-based access restrictions.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/863.html
