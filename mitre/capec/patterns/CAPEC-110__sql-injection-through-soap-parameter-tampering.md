---
capec_id: CAPEC-110
name: SQL Injection through SOAP Parameter Tampering
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Very High
related_cwe: [CWE-89, CWE-20]
related_attack: []
url: https://capec.mitre.org/data/definitions/110.html
tags: [mitre-capec, attack-pattern, CAPEC-110]
---

# CAPEC-110 - SQL Injection through SOAP Parameter Tampering

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-110](https://capec.mitre.org/data/definitions/110.html)

## Description
An attacker modifies the parameters of the SOAP message that is sent from the service consumer to the service provider to initiate a SQL injection attack. On the service provider side, the SOAP message is parsed and parameters are not properly validated before being used to access a database in a way that does not use parameter binding, thus enabling the attacker to control the structure of the executed SQL query. This pattern describes a SQL injection attack with the delivery mechanism being a SOAP message.

## Prerequisites
- SOAP messages are used as a communication mechanism in the system
- SOAP parameters are not properly validated at the service provider
- The service provider does not properly utilize parameter binding when building SQL queries

## Skills required
- **High**: If the attacker has to perform Blind SQL Injection
- **Medium**: If the attacker is able to gain good understanding of the system's database schema

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Unreliable Execution, Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Read Data, Gain Privileges, Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Modify Data, Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Detect Incorrect SOAP Parameter Handling: The attacker tampers with the SOAP message parameters and looks for indications that the tampering caused a change in behavior of the targeted application. Techniques The attacker tampers with the SOAP message parameters by injecting some special characters such as single quotes, double quotes, semi columns, etc. The attacker observes system behavior. Experiment Probe for SQL Injection vulnerability: The attacker injects SQL syntax into vulnerable SOAP parameters identified during the Explore phase to search for unfiltered execution of the SQL syntax in a query. Exploit Inject SQL via SOAP Parameters: The attacker injects SQL via SOAP parameters identified as vulnerable during Explore phase to launch a first or second order SQL injection attack. Techniques An attacker performs a SQL injection attack via the usual methods leveraging SOAP parameters as the injection vector. An attacker has to be careful not to break the XML parser at the service provider which may prevent the payload getting through to the SQL query. The attacker may also look at the WSDL for the web service (if available) to better understand what is expected by the service provider.

## Mitigations
- Properly validate and sanitize/reject user input at the service provider.
- Ensure that prepared statements or other mechanism that enables parameter binding is used when accessing the database in a way that would prevent the attackers' supplied data from controlling the structure of the executed query.
- At the database level, ensure that the database user used by the application in a particular context has the minimum needed privileges to the database that are needed to perform the operation. When possible, run queries against pre-generated views rather than the tables directly.

## Related weaknesses (CWE)
- [CWE-89](https://cwe.mitre.org/data/definitions/89.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/110.html
