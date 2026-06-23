---
capec_id: CAPEC-136
name: LDAP Injection
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-77, CWE-90, CWE-20]
related_attack: []
url: https://capec.mitre.org/data/definitions/136.html
tags: [mitre-capec, attack-pattern, CAPEC-136]
---

# CAPEC-136 - LDAP Injection

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-136](https://capec.mitre.org/data/definitions/136.html)

## Description
An attacker manipulates or crafts an LDAP query for the purpose of undermining the security of the target. Some applications use user input to create LDAP queries that are processed by an LDAP server. For example, a user might provide their username during authentication and the username might be inserted in an LDAP query during the authentication process. An attacker could use this input to inject additional commands into an LDAP query that could disclose sensitive information. For example, entering a * in the aforementioned query might return information about all users on the system. This attack is very similar to an SQL injection attack in that it manipulates a query to gather additional information or coerce a particular return value.

## Prerequisites
- The target application must accept a string as user input, fail to sanitize characters that have a special meaning in LDAP queries in the user input, and insert the user-supplied string in an LDAP query which is then processed.

## Skills required
- **Medium**: The attacker needs to have knowledge of LDAP, especially its query syntax.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Accountability**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges, Bypass Protection Mechanism
- **Availability**: Unreliable Execution
- **Confidentiality**: Read Data
- **Integrity**: Modify Data
- **Non-Repudiation**: Gain Privileges

## Execution flow
Execution Flow Explore Survey application: The attacker takes an inventory of the entry points of the application. Techniques Spider web sites for all available links Sniff network communications with application using a utility such as WireShark. Experiment Determine user-controllable input susceptible to LDAP injection: For each user-controllable input that the attacker suspects is vulnerable to LDAP injection, attempt to inject characters that have special meaning in LDAP (such as a single quote character, etc.). The goal is to create a LDAP query with an invalid syntax Techniques Use web browser to inject input through text fields or through HTTP GET parameters Use a web application debugging tool such as Tamper Data, TamperIE, WebScarab,etc. to modify HTTP POST parameters, hidden fields, non-freeform fields, or other HTTP header. Use modified client (modified by reverse engineering) to inject input. Try to exploit the LDAP injection vulnerability: After determining that a given input is vulnerable to LDAP Injection, hypothesize what the underlying query looks like. Possibly using a tool, iteratively try to add logic to the query to extract information from the LDAP, or to modify or delete information in the LDAP. Techniques Add logic to the LDAP query to change the meaning of that command. Automated tools could be used to generate the LDAP injection strings. Use a web application debugging tool such as Tamper Data, TamperIE, WebScarab,etc. to modify HTTP POST parameters, hidden fields, non-freeform fields, or other HTTP header.

## Mitigations
- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as LDAP content.
- Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the LDAP or application.

## Related weaknesses (CWE)
- [CWE-77](https://cwe.mitre.org/data/definitions/77.html)
- [CWE-90](https://cwe.mitre.org/data/definitions/90.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/136.html
