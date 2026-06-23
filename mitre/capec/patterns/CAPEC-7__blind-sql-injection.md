---
capec_id: CAPEC-7
name: Blind SQL Injection
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-89, CWE-209, CWE-74, CWE-20, CWE-697, CWE-707]
related_attack: []
url: https://capec.mitre.org/data/definitions/7.html
tags: [mitre-capec, attack-pattern, CAPEC-7]
---

# CAPEC-7 - Blind SQL Injection

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-7](https://capec.mitre.org/data/definitions/7.html)

## Description
Blind SQL Injection results from an insufficient mitigation for SQL Injection. Although suppressing database error messages are considered best practice, the suppression alone is not sufficient to prevent SQL Injection. Blind SQL Injection is a form of SQL Injection that overcomes the lack of error messages. Without the error messages that facilitate SQL Injection, the adversary constructs input strings that probe the target through simple Boolean SQL expressions. The adversary can determine if the syntax and structure of the injection was successful based on whether the query was executed or not. Applied iteratively, the adversary determines how and where the target is vulnerable to SQL Injection.

## Prerequisites
- SQL queries used by the application to store, retrieve or modify data.
- User-controllable input that is not properly validated by the application as part of SQL queries.

## Skills required
- **Medium**: Determining the database type and version, as well as the right number and type of parameters to the query being injected in the absence of error messages requires greater skill than reverse-engineering database error messages.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Read Data, Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Modify Data, Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore [Hypothesize SQL queries in application] Generated hypotheses regarding the SQL queries in an application. For example, the adversary may hypothesize that their input is passed directly into a query that looks like: "SELECT * FROM orders WHERE ordernum = _____"or"SELECT * FROM orders WHERE ordernum IN (_____)"or"SELECT * FROM orders WHERE ordernum in (_____) ORDER BY _____" Of course, there are many other possibilities. Techniques Research types of SQL queries and determine which ones could be used at various places in an application. [Determine how to inject information into the queries] Determine how to inject information into the queries from the previous step such that the injection does not impact their logic. For example, the following are possible injections for those queries: "5' OR 1=1; --"and"5) OR 1=1; --"and"ordernum DESC; --" Techniques Add clauses to the SQL queries such that the query logic does not change. Add delays to the SQL queries in case server does not provide clear error messages (e.g. WAITFOR DELAY '0:0:10' in SQL Server or BENCHMARK(1000000000,MD5(1) in MySQL). If these can be injected into the queries, then the length of time that the server takes to respond reveals whether the query is injectable or not. Experiment Determine user-controllable input susceptible to injection: Determine the user-controllable input susceptible to injection. For each user-controllable input that the adversary suspects is vulnerable to SQL injection, attempt to inject the values determined in the previous step. If an error does not occur, then the adversary knows that the SQL injection was successful. Techniques Use web browser to inject input through text fields or through HTTP GET parameters. Use a web application debugging tool such as Tamper Data, TamperIE, WebScarab,etc. to modify HTTP POST parameters, hidden fields, non-freeform fields, etc. Use network-level packet injection tools such as netcat to inject input Use modified client (modified by reverse engineering) to inject input. Determine database type: Determines the type of the database, such as MS SQL Server or Oracle or MySQL, using logical conditions as part of the injected queries Techniques Try injecting a string containing char(0x31)=char(0x31) (this evaluates to 1=1 in SQL Server only) Try injecting a string containing 0x313D31 (this evaluates to 1=1 in MySQL only) Inject other database-specific commands into input fields susceptible to SQL Injection. The adversary can determine the type of database that is running by checking whether the query executed successfully or not (i.e. whether the adversary received a normal response from the server or not). Exploit Extract information about database schema: Extract information about database schema by getting the database to answer yes/no questions about the schema. Techniques Automatically extract database schema using a tool such as Absinthe. Manually perform the blind SQL Injection to extract desired information about the database schema. Exploit SQL Injection vulnerability: Use the information obtained in the previous steps to successfully inject the database in order to bypass checks or modify, add, retrieve or delete data from the database Techniques Use information about how to inject commands into SQL queries as well as information about the database schema to execute attacks such as dropping tables, inserting records, etc.

## Mitigations
- Security by Obscurity is not a solution to preventing SQL Injection. Rather than suppress error messages and exceptions, the application must handle them gracefully, returning either a custom error page or redirecting the user to a default page, without revealing any information about the database or the application internals.
- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as SQL content. Keywords such as UNION, SELECT or INSERT must be filtered in addition to characters such as a single-quote(') or SQL-comments (--) based on the context in which they appear.

## Related weaknesses (CWE)
- [CWE-89](https://cwe.mitre.org/data/definitions/89.html)
- [CWE-209](https://cwe.mitre.org/data/definitions/209.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)
- [CWE-707](https://cwe.mitre.org/data/definitions/707.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/7.html
