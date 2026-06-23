---
capec_id: CAPEC-11
name: Cause Web Server Misclassification
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-430]
related_attack: [T1036.006]
url: https://capec.mitre.org/data/definitions/11.html
tags: [mitre-capec, attack-pattern, CAPEC-11]
---

# CAPEC-11 - Cause Web Server Misclassification

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-11](https://capec.mitre.org/data/definitions/11.html)

## Description
An attack of this type exploits a Web server's decision to take action based on filename or file extension. Because different file types are handled by different server processes, misclassification may force the Web server to take unexpected action, or expected actions in an unexpected sequence. This may cause the server to exhaust resources, supply debug or system data to the attacker, or bind an attacker to a remote process.

## Extended description
This type of vulnerability has been found in many widely used servers including IIS, Lotus Domino, and Orion. The attacker's job in this case is straightforward, standard communication protocols and methods are used and are generally appended with malicious information at the tail end of an otherwise legitimate request. The attack payload varies, but it could be special characters like a period or simply appending a tag that has a special meaning for operations on the server side like .jsp for a java application server. The essence of this attack is that the attacker deceives the server into executing functionality based on the name of the request, i.e. login.jsp, not the contents.

## Prerequisites
- Web server software must rely on file name or file extension for processing.
- The attacker must be able to make HTTP requests to the web server.

## Skills required
- **Low**: To modify file name or file extension
- **Medium**: To use misclassification to force the Web server to disclose configuration information, source, or binary data

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Read Data, Gain Privileges

## Execution flow
Execution Flow Explore Footprint file input vectors: Manually or using an automated tool, an attacker searches for all input locations where a user has control over the filenames or MIME types of files submitted to the web server. Techniques Attacker manually crawls application to identify file inputs Attacker uses an automated tool to crawl application identify file inputs Attacker manually assesses strength of access control protecting native application files from user control Attacker explores potential for submitting files directly to the web server via independently constructed HTTP Requests Experiment File misclassification shotgunning: An attacker makes changes to file extensions and MIME types typically processed by web servers and looks for abnormal behavior. Techniques Attacker submits files with switched extensions (e.g. .php on a .jsp file) to web server. Attacker adds extra characters (e.g. adding an extra . after the file extension) to filenames of files submitted to web server. File misclassification sniping: Understanding how certain file types are processed by web servers, an attacker crafts varying file payloads and modifies their file extension or MIME type to be that of the targeted type to see if the web server is vulnerable to misclassification of that type. Techniques Craft a malicious file payload, modify file extension to the targeted file type and submit it to the web server. Craft a malicious file payload, modify its associated MIME type to the targeted file type and submit it to the web server. Exploit Disclose information: The attacker, by manipulating a file extension or MIME type is able to make the web server return raw information (not executed). Techniques Manipulate the file names that are explicitly sent to the server. Manipulate the MIME sent in order to confuse the web server.

## Mitigations
- Implementation: Server routines should be determined by content not determined by filename or file extension.

## Related weaknesses (CWE)
- [CWE-430](https://cwe.mitre.org/data/definitions/430.html)

## Related ATT&CK techniques
- T1036.006

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/11.html
