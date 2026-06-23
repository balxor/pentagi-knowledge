---
capec_id: CAPEC-108
name: Command Line Execution through SQL Injection
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: Very High
related_cwe: [CWE-89, CWE-74, CWE-20, CWE-78, CWE-114]
related_attack: []
url: https://capec.mitre.org/data/definitions/108.html
tags: [mitre-capec, attack-pattern, CAPEC-108]
---

# CAPEC-108 - Command Line Execution through SQL Injection

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-108](https://capec.mitre.org/data/definitions/108.html)

## Description
An attacker uses standard SQL injection methods to inject data into the command line for execution. This could be done directly through misuse of directives such as MSSQL_xp_cmdshell or indirectly through injection of data into the database that would be interpreted as shell commands. Sometime later, an unscrupulous backend application (or could be part of the functionality of the same application) fetches the injected data stored in the database and uses this data as command line arguments without performing proper validation. The malicious data escapes that data plane by spawning new commands to be executed on the host.

## Prerequisites
- The application does not properly validate data before storing in the database
- Backend application implicitly trusts the data stored in the database
- Malicious data is used on the backend as a command line argument

## Skills required
- **High**: The attacker most likely has to be familiar with the internal functionality of the system to launch this attack. Without that knowledge, there are not many feedback mechanisms to give an attacker the indication of how to perform command injection or whether the attack is succeeding.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Unreliable Execution, Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Read Data, Gain Privileges, Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Modify Data, Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Probe for SQL Injection vulnerability: The attacker injects SQL syntax into user-controllable data inputs to search unfiltered execution of the SQL syntax in a query. Exploit Achieve arbitrary command execution through SQL Injection with the MSSQL_xp_cmdshell directive: The attacker leverages a SQL Injection attack to inject shell code to be executed by leveraging the xp_cmdshell directive. Inject malicious data in the database: Leverage SQL injection to inject data in the database that could later be used to achieve command injection if ever used as a command line argument Trigger command line execution with injected arguments: The attacker causes execution of command line functionality which leverages previously injected database content as arguments.

## Mitigations
- Disable MSSQL xp_cmdshell directive on the database
- Properly validate the data (syntactically and semantically) before writing it to the database.
- Do not implicitly trust the data stored in the database. Re-validate it prior to usage to make sure that it is safe to use in a given context (e.g. as a command line argument).

## Related weaknesses (CWE)
- [CWE-89](https://cwe.mitre.org/data/definitions/89.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-78](https://cwe.mitre.org/data/definitions/78.html)
- [CWE-114](https://cwe.mitre.org/data/definitions/114.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/108.html
