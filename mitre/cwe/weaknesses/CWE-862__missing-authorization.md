---
cwe_id: CWE-862
name: Missing Authorization
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, AI/ML, Web Server, Database Server, Not Technology-Specific]
related_capec: [CAPEC-665]
url: https://cwe.mitre.org/data/definitions/862.html
tags: [mitre-cwe, weakness, CWE-862]
---

# CWE-862 - Missing Authorization

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-862](https://cwe.mitre.org/data/definitions/862.html)

## Description
The product does not perform an authorization check when an actor attempts to access a resource or perform an action.

## Applicable platforms / languages
Not Language-Specific, AI/ML, Web Server, Database Server, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Application Data, Read Files or Directories
- **Integrity**: Modify Application Data, Modify Files or Directories
- **Access Control**: Gain Privileges or Assume Identity, Bypass Protection Mechanism
- **Availability**: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Resource Consumption (Other)

## Potential mitigations
- **Architecture and Design**: Divide the product into anonymous, normal, privileged, and administrative areas. Reduce the attack surface by carefully mapping roles with data and functionality. Use role-based access control (RBAC) [REF-229] to enforce the roles at the appropriate boundaries. Note that this approach may not protect against horizontal authorization, i.e., it will not protect a user from attacking others with the same role.
- **Architecture and Design**: Ensure that access control checks are performed related to the business logic. These checks may be different than the access control checks that are applied to more generic resources such as files, connections, processes, memory, and database records. For example, a database may restrict access for medical records to a specific database user, but each record might only be intended to be accessible to the patient and the patient's doctor [REF-7].
- **Architecture and Design**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, consider using authorization frameworks such as the JAAS Authorization Framework [REF-233] and the OWASP ESAPI Access Control feature [REF-45].
- **Architecture and Design**: For web applications, make sure that the access control mechanism is enforced correctly at the server side on every page. Users should not be able to access any unauthorized functionality or information by simply requesting direct access to that page. One way to do this is to ensure that all pages containing sensitive information are not cached, and that all such pages restrict access to requests that are accompanied by an active and authenticated session token associated with a user who has the required permissions to access that page.
- **System Configuration, Installation**: Use the access control capabilities of your operating system and server environment and define your access control lists accordingly. Use a "default deny" policy when defining these ACLs.

## Related attack patterns (CAPEC)
- [CAPEC-665](https://capec.mitre.org/data/definitions/665.html)

## Related weaknesses
- CWE-285 (ChildOf)
- CWE-284 (ChildOf)

## Observed examples (CVE)
- **CVE-2026-32228**: workflow management product does not check authorization for running a workflow, allowing UI and API users to trigger workflow objects for which they have no access
- **CVE-2024-6845**: chatbot Wordpress plugin does not perform authorization on a REST endpoint, allowing retrieval of an API key
- **CVE-2025-2224**: AI-enabled WordPress plugin has a missing capability check for a particular function, allowing changing public status of posts
- **CVE-2022-24730**: Go-based continuous deployment product does not check that a user has certain privileges to update or create an app, allowing adversaries to read sensitive repository information
- **CVE-2009-3168**: Web application does not restrict access to admin scripts, allowing authenticated users to reset administrative passwords.
- **CVE-2009-3597**: Web application stores database file under the web root with insufficient access control (CWE-219), allowing direct request.
- **CVE-2009-2282**: Terminal server does not check authorization for guest access.
- **CVE-2008-5027**: System monitoring software allows users to bypass authorization by creating custom forms.
- **CVE-2009-3781**: Content management system does not check access permissions for private files, allowing others to view those files.
- **CVE-2008-6548**: Product does not check the ACL of a page accessed using an "include" directive, allowing attackers to read unauthorized files.
- **CVE-2009-2960**: Web application does not restrict access to admin scripts, allowing authenticated users to modify passwords of other users.
- **CVE-2009-3230**: Database server does not use appropriate privileges for certain sensitive operations.
- **CVE-2009-2213**: Gateway uses default "Allow" configuration for its authorization settings.
- **CVE-2009-0034**: Chain: product does not properly interpret a configuration option for a system group, allowing users to gain privileges.
- **CVE-2008-6123**: Chain: SNMP product does not properly parse a configuration option for which hosts are allowed to connect, allowing unauthorized IP addresses to connect.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/862.html
