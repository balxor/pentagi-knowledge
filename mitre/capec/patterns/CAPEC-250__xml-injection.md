---
capec_id: CAPEC-250
name: XML Injection
type: attack-pattern
abstraction: Standard
likelihood: High
severity: n/a
related_cwe: [CWE-91, CWE-74, CWE-20, CWE-707]
related_attack: []
url: https://capec.mitre.org/data/definitions/250.html
tags: [mitre-capec, attack-pattern, CAPEC-250]
---

# CAPEC-250 - XML Injection

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-250](https://capec.mitre.org/data/definitions/250.html)

## Description
An attacker utilizes crafted XML user-controllable input to probe, attack, and inject data into the XML database, using techniques similar to SQL injection. The user-controllable input can allow for unauthorized viewing of data, bypassing authentication or the front-end application for direct XML database access, and possibly altering database information.

## Prerequisites
- XML queries used to process user input and retrieve information stored in XML documents
- User-controllable input not properly sanitized

## Skills required
- **Low**: An attacker must have knowledge of XML syntax and constructs in order to successfully leverage XML Injection

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges, Read Data

## Execution flow
Execution Flow Explore Survey the Target: Using a browser or an automated tool, an adversary records all instances of user-controllable input used to contruct XML queries Techniques Use an automated tool to record all instances of user-controllable input used to contruct XML queries. Use a browser to manually explore the website and analyze how the application processes inputs. Experiment Determine the Structure of Queries: Using manual or automated means, test inputs found for XML weaknesses. Techniques Use XML reserved characters or words, possibly with other input data to attempt to cause unexpected results and identify improper input validation. Exploit Inject Content into XML Queries: Craft malicious content containing XML expressions that is not validated by the application and is executed as part of the XML queries. Techniques Use the crafted input to execute unexpected queries that can disclose sensitive database information to the attacker.

## Mitigations
- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as content that can be interpreted in the context of an XML data or a query.
- Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the database or application.

## Related weaknesses (CWE)
- [CWE-91](https://cwe.mitre.org/data/definitions/91.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-707](https://cwe.mitre.org/data/definitions/707.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/250.html
