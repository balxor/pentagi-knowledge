---
cwe_id: CWE-285
name: Improper Authorization
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, Web Server, Database Server]
related_capec: [CAPEC-1, CAPEC-104, CAPEC-127, CAPEC-13, CAPEC-17, CAPEC-39, CAPEC-402, CAPEC-45, CAPEC-5, CAPEC-51, CAPEC-59, CAPEC-60, CAPEC-647, CAPEC-668, CAPEC-76, CAPEC-77, CAPEC-87]
url: https://cwe.mitre.org/data/definitions/285.html
tags: [mitre-cwe, weakness, CWE-285]
---

# CWE-285 - Improper Authorization

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-285](https://cwe.mitre.org/data/definitions/285.html)

## Description
The product does not perform or incorrectly performs an authorization check when an actor attempts to access a resource or perform an action.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Server, Database Server

## Common consequences
- **Confidentiality**: Read Application Data, Read Files or Directories
- **Integrity**: Modify Application Data, Modify Files or Directories
- **Access Control**: Gain Privileges or Assume Identity, Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design**: Divide the product into anonymous, normal, privileged, and administrative areas. Reduce the attack surface by carefully mapping roles with data and functionality. Use role-based access control (RBAC) to enforce the roles at the appropriate boundaries. Note that this approach may not protect against horizontal authorization, i.e., it will not protect a user from attacking others with the same role.
- **Architecture and Design**: Ensure that you perform access control checks related to your business logic. These checks may be different than the access control checks that you apply to more generic resources such as files, connections, processes, memory, and database records. For example, a database may restrict access for medical records to a specific database user, but each record might only be intended to be accessible to the patient and the patient's doctor.
- **Architecture and Design**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid. For example, consider using authorization frameworks such as the JAAS Authorization Framework [REF-233] and the OWASP ESAPI Access Control feature [REF-45].
- **Architecture and Design**: For web applications, make sure that the access control mechanism is enforced correctly at the server side on every page. Users should not be able to access any unauthorized functionality or information by simply requesting direct access to that page. One way to do this is to ensure that all pages containing sensitive information are not cached, and that all such pages restrict access to requests that are accompanied by an active and authenticated session token associated with a user who has the required permissions to access that page.
- **System Configuration, Installation**: Use the access control capabilities of your operating system and server environment and define your access control lists accordingly. Use a "default deny" policy when defining these ACLs.

## Related attack patterns (CAPEC)
- [CAPEC-1](https://capec.mitre.org/data/definitions/1.html)
- [CAPEC-104](https://capec.mitre.org/data/definitions/104.html)
- [CAPEC-127](https://capec.mitre.org/data/definitions/127.html)
- [CAPEC-13](https://capec.mitre.org/data/definitions/13.html)
- [CAPEC-17](https://capec.mitre.org/data/definitions/17.html)
- [CAPEC-39](https://capec.mitre.org/data/definitions/39.html)
- [CAPEC-402](https://capec.mitre.org/data/definitions/402.html)
- [CAPEC-45](https://capec.mitre.org/data/definitions/45.html)
- [CAPEC-5](https://capec.mitre.org/data/definitions/5.html)
- [CAPEC-51](https://capec.mitre.org/data/definitions/51.html)
- [CAPEC-59](https://capec.mitre.org/data/definitions/59.html)
- [CAPEC-60](https://capec.mitre.org/data/definitions/60.html)
- [CAPEC-647](https://capec.mitre.org/data/definitions/647.html)
- [CAPEC-668](https://capec.mitre.org/data/definitions/668.html)
- [CAPEC-76](https://capec.mitre.org/data/definitions/76.html)
- [CAPEC-77](https://capec.mitre.org/data/definitions/77.html)
- [CAPEC-87](https://capec.mitre.org/data/definitions/87.html)

## Related weaknesses
- CWE-284 (ChildOf)
- CWE-284 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-6845**: chatbot Wordpress plugin does not perform authorization on a REST endpoint, allowing retrieval of an API key
- **CVE-2022-24730**: Go-based continuous deployment product does not check that a user has certain privileges to update or create an app, allowing adversaries to read sensitive repository information
- **CVE-2009-3168**: Web application does not restrict access to admin scripts, allowing authenticated users to reset administrative passwords.
- **CVE-2009-2960**: Web application does not restrict access to admin scripts, allowing authenticated users to modify passwords of other users.
- **CVE-2009-3597**: Web application stores database file under the web root with insufficient access control (CWE-219), allowing direct request.
- **CVE-2009-2282**: Terminal server does not check authorization for guest access.
- **CVE-2009-3230**: Database server does not use appropriate privileges for certain sensitive operations.
- **CVE-2009-2213**: Gateway uses default "Allow" configuration for its authorization settings.
- **CVE-2009-0034**: Chain: product does not properly interpret a configuration option for a system group, allowing users to gain privileges.
- **CVE-2008-6123**: Chain: SNMP product does not properly parse a configuration option for which hosts are allowed to connect, allowing unauthorized IP addresses to connect.
- **CVE-2008-5027**: System monitoring software allows users to bypass authorization by creating custom forms.
- **CVE-2008-7109**: Chain: reliance on client-side security (CWE-602) allows attackers to bypass authorization using a custom client.
- **CVE-2008-3424**: Chain: product does not properly handle wildcards in an authorization policy list, allowing unintended access.
- **CVE-2009-3781**: Content management system does not check access permissions for private files, allowing others to view those files.
- **CVE-2008-4577**: ACL-based protection mechanism treats negative access rights as if they are positive, allowing bypass of intended restrictions.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/285.html
