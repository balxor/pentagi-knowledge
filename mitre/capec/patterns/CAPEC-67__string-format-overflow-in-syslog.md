---
capec_id: CAPEC-67
name: String Format Overflow in syslog()
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Very High
related_cwe: [CWE-120, CWE-134, CWE-74, CWE-20, CWE-680, CWE-697]
related_attack: []
url: https://capec.mitre.org/data/definitions/67.html
tags: [mitre-capec, attack-pattern, CAPEC-67]
---

# CAPEC-67 - String Format Overflow in syslog()

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-67](https://capec.mitre.org/data/definitions/67.html)

## Description
This attack targets applications and software that uses the syslog() function insecurely. If an application does not explicitely use a format string parameter in a call to syslog(), user input can be placed in the format string parameter leading to a format string injection attack. Adversaries can then inject malicious format string commands into the function call leading to a buffer overflow. There are many reported software vulnerabilities with the root cause being a misuse of the syslog() function.

## Prerequisites
- The Syslog function is used without specifying a format string argument, allowing user input to be placed direct into the function call as a format string.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code), Unreliable Execution
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code), Modify Data

## Execution flow
Execution Flow Explore Identify target application: The adversary identifies a target application or program to perform the buffer overflow on. In this attack, adversaries look for applications that use syslog() incorrectly. Experiment Find injection vector: The adversary identifies an injection vector to deliver the excessive content to the targeted application's buffer. For each user-controllable input that the adversary suspects is vulnerable to format string injection, attempt to inject formatting characters such as %n, %s, etc.. The goal is to manipulate the string creation using these formatting characters. Techniques Inject probe payload which contains formatting characters (%s, %d, %n, etc.) through input parameters. Craft overflow content: The adversary crafts the content to be injected. If the intent is to simply cause the software to crash, the content need only consist of an excessive quantity of random data. If the intent is to leverage the overflow for execution of arbitrary code, the adversary will craft a set of content that not only overflows the targeted buffer but does so in such a way that the overwritten return address is replaced with one of the adversaries' choosing which points to code injected by the adversary. Techniques The formatting characters %s and %d are useful for observing memory and trying to print memory addresses. If an adversary has access to the log being written to they can observer this output and use it to help craft their attack. The formatting character %n is useful for adding extra data onto the buffer. Exploit Overflow the buffer: Using the injection vector, the adversary supplies the program with the crafted format string injection, causing a buffer.

## Mitigations
- The code should be reviewed for misuse of the Syslog function call. Manual or automated code review can be used. The reviewer needs to ensure that all format string functions are passed a static string which cannot be controlled by the user and that the proper number of arguments are always sent to that function as well. If at all possible, do not use the %n operator in format strings. The following code shows a correct usage of Syslog(): syslog(LOG_ERR, "%s", cmdBuf); The following code shows a vulnerable usage of Syslog(): syslog(LOG_ERR, cmdBuf); // the buffer cmdBuff is taking user supplied data.

## Related weaknesses (CWE)
- [CWE-120](https://cwe.mitre.org/data/definitions/120.html)
- [CWE-134](https://cwe.mitre.org/data/definitions/134.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-680](https://cwe.mitre.org/data/definitions/680.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/67.html
