---
cwe_id: CWE-209
name: Generation of Error Message Containing Sensitive Information
type: weakness
abstraction: Base
status: Draft
languages: [PHP, Java, Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-215, CAPEC-463, CAPEC-54, CAPEC-7]
url: https://cwe.mitre.org/data/definitions/209.html
tags: [mitre-cwe, weakness, CWE-209]
---

# CWE-209 - Generation of Error Message Containing Sensitive Information

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-209](https://cwe.mitre.org/data/definitions/209.html)

## Description
The product generates an error message that includes sensitive information about its environment, users, or associated data.

## Applicable platforms / languages
PHP, Java, Not Language-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation**: Ensure that error messages only contain minimal details that are useful to the intended audience and no one else. The messages need to strike the balance between being too cryptic (which can confuse users) or being too detailed (which may reveal more than intended). The messages should not reveal the methods that were used to determine the error. Attackers can use detailed information to refine or optimize their original attack, thereby increasing their chances of success. If errors must be captured in some detail, record them in log messages, but consider what could occur if the log messages can be viewed by attackers. Highly sensitive information such as passwords should never be saved to log files. Avoid inconsistent messaging that might accidentally tip off an attacker about internal state, such as whether a user account exists or not.
- **Implementation**: Handle exceptions internally and do not display errors containing potentially sensitive information to a user.
- **Implementation**: Use naming conventions and strong types to make it easier to spot when sensitive data is being used. When creating structures, objects, or other complex entities, separate the sensitive and non-sensitive data as much as possible.
- **Implementation, Build and Compilation**: Debugging information should not make its way into a production release.
- **Implementation, Build and Compilation**: Debugging information should not make its way into a production release.
- **System Configuration**: Where available, configure the environment to use less verbose error messages. For example, in PHP, disable the display_errors setting during configuration, or at runtime using the error_reporting() function.
- **System Configuration**: Create default error pages or messages that do not leak any information.

## Related attack patterns (CAPEC)
- [CAPEC-215](https://capec.mitre.org/data/definitions/215.html)
- [CAPEC-463](https://capec.mitre.org/data/definitions/463.html)
- [CAPEC-54](https://capec.mitre.org/data/definitions/54.html)
- [CAPEC-7](https://capec.mitre.org/data/definitions/7.html)

## Related weaknesses
- CWE-200 (ChildOf)
- CWE-200 (ChildOf)
- CWE-755 (ChildOf)

## Observed examples (CVE)
- **CVE-2008-2049**: POP3 server reveals a password in an error message after multiple APOP commands are sent. Might be resultant from another weakness.
- **CVE-2007-5172**: Program reveals password in error message if attacker can trigger certain database errors.
- **CVE-2008-4638**: Composite: application running with high privileges (CWE-250) allows user to specify a restricted file to process, which generates a parsing error that leaks the contents of the file (CWE-209).
- **CVE-2008-1579**: Existence of user names can be determined by requesting a nonexistent blog and reading the error message.
- **CVE-2007-1409**: Direct request to library file in web application triggers pathname leak in error message.
- **CVE-2008-3060**: Malformed input to login page causes leak of full path when IMAP call fails.
- **CVE-2005-0603**: Malformed regexp syntax leads to information exposure in error message.
- **CVE-2017-9615**: verbose logging stores admin credentials in a world-readablelog file
- **CVE-2018-1999036**: SSH password for private key stored in build log

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/209.html
