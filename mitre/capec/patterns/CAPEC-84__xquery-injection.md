---
capec_id: CAPEC-84
name: XQuery Injection
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Very High
related_cwe: [CWE-74, CWE-707]
related_attack: []
url: https://capec.mitre.org/data/definitions/84.html
tags: [mitre-capec, attack-pattern, CAPEC-84]
---

# CAPEC-84 - XQuery Injection

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-84](https://capec.mitre.org/data/definitions/84.html)

## Description
This attack utilizes XQuery to probe and attack server systems; in a similar manner that SQL Injection allows an attacker to exploit SQL calls to RDBMS, XQuery Injection uses improperly validated data that is passed to XQuery commands to traverse and execute commands that the XQuery routines have access to. XQuery injection can be used to enumerate elements on the victim's environment, inject commands to the local host, or execute queries to remote files and data sources.

## Prerequisites
- The XQL must execute unvalidated data

## Skills required
- **Low**: Basic understanding of XQuery

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Read Data, Gain Privileges, Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Modify Data, Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs: Using a browser or an automated tool, an attacker follows all public links and actions on a web site. They record all the links, the forms, the resources accessed and all other potential entry-points for the web application. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters in the URL. Use a proxy tool to record all user input entry points visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Experiment Determine user-controllable input susceptible to injection: Determine the user-controllable input susceptible to injection. For each user-controllable input that the attacker suspects is vulnerable to XQL injection, attempt to inject characters that have special meaning in XQL. The goal is to create an XQL query with an invalid syntax. Techniques Use web browser to inject input through text fields or through HTTP GET parameters. Use a web application debugging tool such as Tamper Data, TamperIE, WebScarab,etc. to modify HTTP POST parameters, hidden fields, non-freeform fields, etc. Use XML files to inject input. Use network-level packet injection tools such as netcat to inject input Use modified client (modified by reverse engineering) to inject input. Exploit Information Disclosure: The attacker crafts and injects an XQuery payload which is acted on by an XQL query leading to inappropriate disclosure of information. Techniques Leveraging one of the vulnerable inputs identified during the Experiment phase, inject malicious XQuery payload. The payload aims to get information on the structure of the underlying XML database and/or the content in it. Manipulate the data in the XML database: The attacker crafts and injects an XQuery payload which is acted on by an XQL query leading to modification of application data. Techniques Leveraging one of the vulnerable inputs identified during the Experiment phase, inject malicious XQuery payload.. The payload tries to insert or replace data in the XML database.

## Mitigations
- Design: Perform input allowlist validation on all XML input
- Implementation: Run xml parsing and query infrastructure with minimal privileges so that an attacker is limited in their ability to probe other system resources from XQL.

## Related weaknesses (CWE)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-707](https://cwe.mitre.org/data/definitions/707.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/84.html
