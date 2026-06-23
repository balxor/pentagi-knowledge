---
capec_id: CAPEC-676
name: NoSQL Injection
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-943, CWE-1286]
related_attack: []
url: https://capec.mitre.org/data/definitions/676.html
tags: [mitre-capec, attack-pattern, CAPEC-676]
---

# CAPEC-676 - NoSQL Injection

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-676](https://capec.mitre.org/data/definitions/676.html)

## Description
<xhtml:p>An adversary targets software that constructs NoSQL statements based on user input or with parameters vulnerable to operator replacement in order to achieve a variety of technical impacts such as escalating privileges, bypassing authentication, and/or executing code.</xhtml:p>

## Extended description
NoSQL database calls are written in an application's programming language, via a custom API call, or formatted in a common convention (e.g., JSON, XML, etc.), any of which the adversary can exploit to achieve the aforementioned goals. NoSQL attacks usually result from improper sanitization and validation of data that originates from a user, either via special character or JavaScript injection. In both cases, the adversary crafts input strings so that when the target software constructs NoSQL statements based on the input, the resulting NoSQL statement performs actions other than those intended by the application. However, unlike traditional SQL Injection attacks, NoSQL injection attacks can also occur in instances where the application does not rely upon user input, as is the case in operator replacements. This entails the adversary overriding reserved NoSQL variable names with ones that have been modified with malicious functionality (e.g., $where in MongoDB). In all cases, depending on the NoSQL API and data model used, successful injection can cause information disclosure, data modification, and code execution at the application level. Note: NoSQL Injection attacks are executed within a procedural language (e.g., C, C++, Perl), as opposed to the declarative SQL language itself. As a result, NoSQL injection attacks can potentially result in greater impacts than traditional SQL Injection attacks [REF-668].

## Prerequisites
- Awareness of the technology stack being leveraged by the target application.
- NoSQL queries used by the application to store, retrieve, or modify data.
- User-controllable input that is not properly validated by the application as part of NoSQL queries.
- Target potentially susceptible to operator replacement attacks.

## Skills required
- **Low**: For keyword and JavaScript injection attacks, it is fairly simple for someone with basic NoSQL knowledge to perform NoSQL injection, once the target's technology stack has been determined.
- **Medium**: For operator replacement attacks, the adversary must also have knowledge of HTTP Parameter Pollution attacks and how to conduct them.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Read Data, Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges
- **Integrity**: Modify Data, Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Survey target application: Due to the number of NoSQL databases available and the numerous language/API combinations of each, the adversary must first survey the target application to learn what technologies are being leveraged and how they interact with user-driven data. Techniques Determine the technology stack leveraged by the target application, such as the application server, drivers, frameworks, APIs, and databases being utilized. Identify areas of the application that interact with user input and may be involved with NoSQL queries. Experiment Identify user-controllable input susceptible to injection: After identifying the technology stack being used and where user-driven input is leveraged, determine the user-controllable input susceptible to injection such as authentication or search forms. For each user-controllable input that the adversary suspects is vulnerable to NoSQL injection, attempt to inject characters or keywords that have special meaning in the given NoSQL database or language (e.g., "$ne" for MongoDB or "$exists" for PHP/MongoDB), or JavaScript that can be executed within the application. The goal is to create a NoSQL query with an invalid syntax. Techniques Use web browser to inject input through text fields or through HTTP GET parameters. Use a web application debugging tool such as Tamper Data, TamperIE, WebScarab,etc. to modify HTTP POST parameters, hidden fields, non-freeform fields, etc. Use network-level packet injection tools such as netcat to inject input Use modified client (modified by reverse engineering) to inject input. Experiment with NoSQL Injection vulnerabilities: After determining that a given input is vulnerable to NoSQL Injection, hypothesize what the underlying query looks like. Iteratively try to add logic to the query to extract information from the database, modify/delete information in the database, or execute commands on the server. Techniques Use public resources such as OWASP's "Testing for NoSQL Injection" [REF-668] or Null Sweep's "NoSQL Injection Cheatsheet" [REF-669] and try different approaches for adding logic to NoSQL queries. Iteratively add logic to the NoSQL query and use detailed error messages from the server to debug the query. Attempt an HTTP Parameter Pollution attack to replace language-specific keywords, such as "where" within PHP [CAPEC-460]. Exploit Exploit NoSQL Injection vulnerability: After refining and adding various logic to NoSQL queries, craft and execute the underlying NoSQL query that will be used to attack the target system. Techniques Craft and Execute underlying NoSQL query

## Mitigations
- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as relevant NoSQL and JavaScript content. NoSQL-specific keywords, such as $ne, $eq or $gt for MongoDB, must be filtered in addition to characters such as a single-quote(') or semicolons (;) based on the context in which they appear. Validation should also extend to expected types.
- If possible, leverage safe APIs (e.g., PyMongo and Flask-PyMongo for Python and MongoDB) for queries as opposed to building queries from strings.
- Ensure the most recent version of a NoSQL database and it's corresponding API are used by the application.
- Use of custom error pages - Adversaries can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the database or application.
- Exercise the principle of Least Privilege with regards to application accounts to minimize damage if a NoSQL injection attack is successful.
- If using MongoDB, disable server-side JavaScript execution and leverage a sanitization module such as "mongo-sanitize".
- If using PHP with MongoDB, ensure all special query operators (starting with $) use single quotes to prevent operator replacement attacks.
- Additional mitigations will depend on the NoSQL database, API, and programming language leveraged by the application.

## Related weaknesses (CWE)
- [CWE-943](https://cwe.mitre.org/data/definitions/943.html)
- [CWE-1286](https://cwe.mitre.org/data/definitions/1286.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/676.html
