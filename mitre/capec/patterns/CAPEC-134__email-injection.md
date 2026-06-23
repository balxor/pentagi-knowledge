---
capec_id: CAPEC-134
name: Email Injection
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: [CWE-150]
related_attack: []
url: https://capec.mitre.org/data/definitions/134.html
tags: [mitre-capec, attack-pattern, CAPEC-134]
---

# CAPEC-134 - Email Injection

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-134](https://capec.mitre.org/data/definitions/134.html)

## Description
An adversary manipulates the headers and content of an email message by injecting data via the use of delimiter characters native to the protocol.

## Extended description
Many applications allow users to send email messages by filling in fields. For example, a web site may have a link to "share this site with a friend" where the user provides the recipient's email address and the web application fills out all the other fields, such as the subject and body. In this pattern, an adversary adds header and body information to an email message by injecting additional content in an input field used to construct a header of the mail message. This attack takes advantage of the fact that RFC 822 requires that headers in a mail message be separated by a carriage return. As a result, an adversary can inject new headers or content simply by adding a delimiting carriage return and then supplying the new heading and body information. This attack will not work if the user can only supply the message body since a carriage return in the body is treated as a normal character.

## Prerequisites
- The target application must allow the user to send email to some recipient, to specify the content at least one header field in the message, and must fail to sanitize against the injection of command separators.
- The adversary must have the ability to access the target mail application.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Related weaknesses (CWE)
- [CWE-150](https://cwe.mitre.org/data/definitions/150.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/134.html
