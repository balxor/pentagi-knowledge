---
capec_id: CAPEC-183
name: IMAP/SMTP Command Injection
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: [CWE-77]
related_attack: []
url: https://capec.mitre.org/data/definitions/183.html
tags: [mitre-capec, attack-pattern, CAPEC-183]
---

# CAPEC-183 - IMAP/SMTP Command Injection

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-183](https://capec.mitre.org/data/definitions/183.html)

## Description
An adversary exploits weaknesses in input validation on web-mail servers to execute commands on the IMAP/SMTP server. Web-mail servers often sit between the Internet and the IMAP or SMTP mail server. User requests are received by the web-mail servers which then query the back-end mail server for the requested information and return this response to the user. In an IMAP/SMTP command injection attack, mail-server commands are embedded in parts of the request sent to the web-mail server. If the web-mail server fails to adequately sanitize these requests, these commands are then sent to the back-end mail server when it is queried by the web-mail server, where the commands are then executed. This attack can be especially dangerous since administrators may assume that the back-end server is protected against direct Internet access and therefore may not secure it adequately against the execution of malicious commands.

## Prerequisites
- The target environment must consist of a web-mail server that the attacker can query and a back-end mail server. The back-end mail server need not be directly accessible to the attacker.
- The web-mail server must fail to adequately sanitize fields received from users and passed on to the back-end mail server.
- The back-end mail server must not be adequately secured against receiving malicious commands from the web-mail server.

## Resources required
- None: No specialized resources are required to execute this type of attack. However, in most cases, the attacker will need to be a recognized user of the web-mail server.

## Execution flow
Execution Flow Explore Identify Target Web-Mail Server: The adversary first identifies the web-mail server they wish to exploit. Experiment Identify Vulnerable Parameters: Once the adversary has identified a web-mail server, they identify any vulnerable parameters by altering their values in requests. The adversary knows that the parameter is vulnerable if the web-mail server returns an error of any sort. Ideally, the adversary is looking for a descriptive error message. Techniques Assign a null value to a parameter being used by the web-mail server and observe the response. Assign a random value to a parameter being used by the web-mail server and observe the response. Add additional values to a parameter being used by the web-mail server and observe the response. Add non standard special characters (i.e.: \, ', ", @, #, !, |) to a parameter being used by the web-mail server and observe the response. Eliminate a parameter being used by the web-mail server and observe the response. Determine Level of Injection: After identifying all vulnerable parameters, the adversary determines what level of injection is possible. Techniques Evaluate error messages to determine what IMAP/SMTP command is being executed for the vulnerable parameter. Sometimes the actually query will be placed in the error message. If there aren't descriptive error messages, the adversary will analyze the affected functionality to deduce the possible commands that could be being used by the mail-server. Exploit Inject IMAP/SMTP Commands: The adversary manipulates the vulnerable parameters to inject an IMAP/SMTP command and execute it on the mail-server. Techniques Structure the injection as a header, body, and footer. The header contains the ending of the expected message, the body contains the injection of the new command, and the footer contains the beginning of the expected command. Each part of the injection payload needs to be terminated with the CRLF (%0d%0a) sequence.

## Related weaknesses (CWE)
- [CWE-77](https://cwe.mitre.org/data/definitions/77.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/183.html
