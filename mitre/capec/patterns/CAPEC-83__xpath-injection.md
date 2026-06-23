---
capec_id: CAPEC-83
name: XPath Injection
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-91, CWE-74, CWE-20, CWE-707]
related_attack: []
url: https://capec.mitre.org/data/definitions/83.html
tags: [mitre-capec, attack-pattern, CAPEC-83]
---

# CAPEC-83 - XPath Injection

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-83](https://capec.mitre.org/data/definitions/83.html)

## Description
An attacker can craft special user-controllable input consisting of XPath expressions to inject the XML database and bypass authentication or glean information that they normally would not be able to. XPath Injection enables an attacker to talk directly to the XML database, thus bypassing the application completely. XPath Injection results from the failure of an application to properly sanitize input used as part of dynamic XPath expressions used to query an XML database.

## Prerequisites
- XPath queries used to retrieve information stored in XML documents
- User-controllable input not properly sanitized before being used as part of XPath queries

## Skills required
- **Low**: XPath Injection shares the same basic premises with SQL Injection. An attacker must have knowledge of XPath syntax and constructs in order to successfully leverage XPath Injection

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges, Read Data

## Execution flow
Execution Flow Explore Survey the target: Using a browser or an automated tool, an adversary records all instances of user-controllable input used to contruct XPath queries. Techniques Use an automated tool to record all instances of user-controllable input used to contruct XPath queries. Use a browser to manually explore the website and analyze how the application processes inputs. Determine the tructure of queries: Using manual or automated means, test inputs found for XPath weaknesses. Techniques Use an automated tool automatically probe the inputs for XPath weaknesses. Manually probe the inputs using characters such as single quote (') that can cause XPath-releated errors, thus indicating an XPath weakness. Exploit Inject content into XPath query: Craft malicious content containing XPath expressions that is not validated by the application and is executed as part of the XPath queries. Techniques Use the crafted input to execute unexpected queries that can disclose sensitive database information to the attacker. Use a combination of single quote (') and boolean expressions such as "or 1=1" to manipulate XPath logic. Use XPath functions in the malicious content such as "string-length", "substring", or "count" to gain information about the XML document structure being used.

## Mitigations
- Strong input validation - All user-controllable input must be validated and filtered for illegal characters as well as content that can be interpreted in the context of an XPath expression. Characters such as a single-quote(') or operators such as or (|), and (&) and such should be filtered if the application does not expect them in the context in which they appear. If such content cannot be filtered, it must at least be properly escaped to avoid them being interpreted as part of XPath expressions.
- Use of parameterized XPath queries - Parameterization causes the input to be restricted to certain domains, such as strings or integers, and any input outside such domains is considered invalid and the query fails.
- Use of custom error pages - Attackers can glean information about the nature of queries from descriptive error messages. Input validation must be coupled with customized error pages that inform about an error without disclosing information about the database or application.

## Related weaknesses (CWE)
- [CWE-91](https://cwe.mitre.org/data/definitions/91.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-707](https://cwe.mitre.org/data/definitions/707.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/83.html
