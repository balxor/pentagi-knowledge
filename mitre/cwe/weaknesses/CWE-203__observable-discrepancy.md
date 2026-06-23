---
cwe_id: CWE-203
name: Observable Discrepancy
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-189]
url: https://cwe.mitre.org/data/definitions/203.html
tags: [mitre-cwe, weakness, CWE-203]
---

# CWE-203 - Observable Discrepancy

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-203](https://cwe.mitre.org/data/definitions/203.html)

## Description
The product behaves differently or sends different responses under different circumstances in a way that is observable to an unauthorized actor.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Access Control**: Read Application Data, Bypass Protection Mechanism
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Architecture and Design**: Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.
- **Implementation**: Ensure that error messages only contain minimal details that are useful to the intended audience and no one else. The messages need to strike the balance between being too cryptic (which can confuse users) or being too detailed (which may reveal more than intended). The messages should not reveal the methods that were used to determine the error. Attackers can use detailed information to refine or optimize their original attack, thereby increasing their chances of success. If errors must be captured in some detail, record them in log messages, but consider what could occur if the log messages can be viewed by attackers. Highly sensitive information such as passwords should never be saved to log files. Avoid inconsistent messaging that might accidentally tip off an attacker about internal state, such as whether a user account exists or not.

## Related attack patterns (CAPEC)
- [CAPEC-189](https://capec.mitre.org/data/definitions/189.html)

## Related weaknesses
- CWE-200 (ChildOf)
- CWE-200 (ChildOf)

## Observed examples (CVE)
- **CVE-2020-8695**: Observable discrepancy in the RAPL interface for some Intel processors allows information disclosure.
- **CVE-2019-14353**: Crypto hardware wallet's power consumption relates to total number of pixels illuminated, creating a side channel in the USB connection that allows attackers to determine secrets displayed such as PIN numbers and passwords
- **CVE-2019-10071**: Java-oriented framework compares HMAC signatures using String.equals() instead of a constant-time algorithm, causing timing discrepancies
- **CVE-2002-2094**: This, and others, use ".." attacks and monitor error responses, so there is overlap with directory traversal.
- **CVE-2001-1483**: Enumeration of valid usernames based on inconsistent responses
- **CVE-2001-1528**: Account number enumeration via inconsistent responses.
- **CVE-2004-2150**: User enumeration via discrepancies in error messages.
- **CVE-2005-1650**: User enumeration via discrepancies in error messages.
- **CVE-2004-0294**: Bulletin Board displays different error messages when a user exists or not, which makes it easier for remote attackers to identify valid users and conduct a brute force password guessing attack.
- **CVE-2004-0243**: Operating System, when direct remote login is disabled, displays a different message if the password is correct, which allows remote attackers to guess the password via brute force methods.
- **CVE-2002-0514**: Product allows remote attackers to determine if a port is being filtered because the response packet TTL is different than the default TTL.
- **CVE-2002-0515**: Product sets a different TTL when a port is being filtered than when it is not being filtered, which allows remote attackers to identify filtered ports by comparing TTLs.
- **CVE-2002-0208**: Product modifies TCP/IP stack and ICMP error messages in unusual ways that show the product is in use.
- **CVE-2004-2252**: Behavioral infoleak by responding to SYN-FIN packets.
- **CVE-2001-1387**: Product may generate different responses than specified by the administrator, possibly leading to an information leak.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/203.html
