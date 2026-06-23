---
capec_id: CAPEC-170
name: Web Application Fingerprinting
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Low
related_cwe: [CWE-497]
related_attack: []
url: https://capec.mitre.org/data/definitions/170.html
tags: [mitre-capec, attack-pattern, CAPEC-170]
---

# CAPEC-170 - Web Application Fingerprinting

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Low  -  **CAPEC:** [CAPEC-170](https://capec.mitre.org/data/definitions/170.html)

## Description
An attacker sends a series of probes to a web application in order to elicit version-dependent and type-dependent behavior that assists in identifying the target. An attacker could learn information such as software versions, error pages, and response headers, variations in implementations of the HTTP protocol, directory structures, and other similar information about the targeted service. This information can then be used by an attacker to formulate a targeted attack plan. While web application fingerprinting is not intended to be damaging (although certain activities, such as network scans, can sometimes cause disruptions to vulnerable applications inadvertently) it may often pave the way for more damaging attacks.

## Prerequisites
- Any web application can be fingerprinted. However, some configuration choices can limit the useful information an attacker may collect during a fingerprinting attack.

## Skills required
- **Low**: Attacker knows how to send HTTP request, SQL query to a web application.

## Resources required
- While simple fingerprinting can be accomplished with only a web browser, for more thorough fingerprinting an attacker requires a variety of tools to collect information about the target. These tools might include protocol analyzers, web-site crawlers, and fuzzing tools. Footprinting a service adequately may also take a few days if the attacker wishes the footprinting attempt to go undetected.

## Consequences
- **Confidentiality**: Other (Information Leakage)

## Execution flow
Execution Flow Explore Request fingerprinting: Use automated tools or send web server specific commands to web server and wait for server's response. Techniques Use automated tools or send web server specific commands to web server and then receive server's response. Experiment Increase the accuracy of server fingerprinting of Web servers: Attacker usually needs to send several different commands to accurately identify the web server. Attacker can also use automated tools to send requests to the server. The responses of the server may be different in terms of protocol behavior. Techniques Observe the ordering of the several HTTP response headers. The ordering of the header of each server may have unique identities. Send bad requests or requests of nonexistent pages to the server. Attacker takes existing automated tools to recognize the type and the version of the web server in use. Identify Web Application Software: After the web server platform software has been identified, the attacker start to identify web application technologies such as ASP, .NET, PHP and Java on the server. Techniques Examine the file name extensions in URL, for example .php indicates PHP script interfaced with Apache server. Examine the HTTP Response Headers. This may leak information about software signatures Examine Cookies that may contain server's software information. Check error pages. Identify Backend Database Version: Determining the database engine type can assist attackers' attempt to successfully execute SQL injection. Some database API such as ODBC will show a database type as part of the driver information when reporting an error. Techniques Use tools to send bogus SQL query to the server and check error pages.

## Mitigations
- Implementation: Obfuscate server fields of HTTP response.
- Implementation: Hide inner ordering of HTTP response header.
- Implementation: Customizing HTTP error codes such as 404 or 500.
- Implementation: Hide URL file extension.
- Implementation: Hide HTTP response header software information filed.
- Implementation: Hide cookie's software information filed.
- Implementation: Appropriately deal with error messages.
- Implementation: Obfuscate database type in Database API's error message.

## Related weaknesses (CWE)
- [CWE-497](https://cwe.mitre.org/data/definitions/497.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/170.html
