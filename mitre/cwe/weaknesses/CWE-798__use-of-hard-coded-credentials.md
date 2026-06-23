---
cwe_id: CWE-798
name: Use of Hard-coded Credentials
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Mobile, ICS/OT]
related_capec: [CAPEC-191, CAPEC-70]
url: https://cwe.mitre.org/data/definitions/798.html
tags: [mitre-cwe, weakness, CWE-798]
---

# CWE-798 - Use of Hard-coded Credentials

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-798](https://cwe.mitre.org/data/definitions/798.html)

## Description
The product contains hard-coded credentials, such as a password or cryptographic key.

## Extended description
There are two main variations: Inbound: the product contains an authentication mechanism that checks the input credentials against a hard-coded set of credentials. In this variant, a default administration account is created, and a simple password is hard-coded into the product and associated with that account. This hard-coded password is the same for each installation of the product, and it usually cannot be changed or disabled by system administrators without manually modifying the program, or otherwise patching the product. It can also be difficult for the administrator to detect. Outbound: the product connects to another system or component, and it contains hard-coded credentials for connecting to that component. This variant applies to front-end systems that authenticate with a back-end service. The back-end service may require a fixed password that can be easily discovered. The programmer may simply hard-code those back-end credentials into the front-end product.

## Applicable platforms / languages
Not Language-Specific, Mobile, ICS/OT

## Common consequences
- **Access Control**: Bypass Protection Mechanism
- **Integrity, Confidentiality, Availability, Access Control, Other**: Read Application Data, Gain Privileges or Assume Identity, Execute Unauthorized Code or Commands, Other

## Potential mitigations
- **Architecture and Design**: For outbound authentication: store passwords, keys, and other credentials outside of the code in a strongly-protected, encrypted configuration file or database that is protected from access by all outsiders, including other local users on the same system. Properly protect the key (CWE-320). If you cannot use encryption to protect the file, then make sure that the permissions are as restrictive as possible [REF-7]. In Windows environments, the Encrypted File System (EFS) may provide some protection.
- **Architecture and Design**: For inbound authentication: Rather than hard-code a default username and password, key, or other authentication credentials for first time logins, utilize a "first login" mode that requires the user to enter a unique strong password or key.
- **Architecture and Design**: If the product must contain hard-coded credentials or they cannot be removed, perform access control checks and limit which entities can access the feature that requires the hard-coded credentials. For example, a feature might only be enabled through the system console instead of through a network connection.
- **Architecture and Design**: For inbound authentication using passwords: apply strong one-way hashes to passwords and store those hashes in a configuration file or database with appropriate access control. That way, theft of the file/database still requires the attacker to try to crack the password. When handling an incoming password during authentication, take the hash of the password and compare it to the saved hash. Use randomly assigned salts for each separate hash that is generated. This increases the amount of computation that an attacker needs to conduct a brute-force attack, possibly limiting the effectiveness of the rainbow table method.
- **Architecture and Design**: For front-end to back-end connections: Three solutions are possible, although none are complete. The first suggestion involves the use of generated passwords or keys that are changed automatically and must be entered at given time intervals by a system administrator. These passwords will be held in memory and only be valid for the time intervals. Next, the passwords or keys should be limited at the back end to only performing actions valid for the front end, as opposed to having full access. Finally, the messages sent should be tagged and checksummed with time sensitive values so as to prevent replay-style attacks.

## Related attack patterns (CAPEC)
- [CAPEC-191](https://capec.mitre.org/data/definitions/191.html)
- [CAPEC-70](https://capec.mitre.org/data/definitions/70.html)

## Related weaknesses
- CWE-1391 (ChildOf)
- CWE-287 (ChildOf)
- CWE-344 (ChildOf)
- CWE-671 (ChildOf)
- CWE-257 (PeerOf)

## Observed examples (CVE)
- **CVE-2022-40263**: Software for biological cell analysus has hard-coded credentials, leading to leak of Protected Health Information (PHI)
- **CVE-2022-29953**: Condition Monitor firmware has a maintenance interface with hard-coded credentials
- **CVE-2022-29960**: Engineering Workstation uses hard-coded cryptographic keys that could allow for unathorized filesystem access and privilege escalation
- **CVE-2022-29964**: Distributed Control System (DCS) has hard-coded passwords for local shell access
- **CVE-2022-30997**: Programmable Logic Controller (PLC) has a maintenance service that uses undocumented, hard-coded credentials
- **CVE-2022-30314**: Firmware for a Safety Instrumented System (SIS) has hard-coded credentials for access to boot configuration
- **CVE-2022-30271**: Remote Terminal Unit (RTU) uses a hard-coded SSH private key that is likely to be used in typical deployments
- **CVE-2021-37555**: Telnet service for IoT feeder for dogs and cats has hard-coded password [REF-1288]
- **CVE-2021-35033**: Firmware for a WiFi router uses a hard-coded password for a BusyBox shell, allowing bypass of authentication through the UART port
- **CVE-2012-3503**: Installation script has a hard-coded secret token value, allowing attackers to bypass authentication
- **CVE-2010-2772**: SCADA system uses a hard-coded password to protect back-end database containing authorization information, exploited by Stuxnet worm
- **CVE-2010-2073**: FTP server library uses hard-coded usernames and passwords for three default accounts
- **CVE-2010-1573**: Chain: Router firmware uses hard-coded username and password for access to debug functionality, which can be used to execute arbitrary code
- **CVE-2008-2369**: Server uses hard-coded authentication key
- **CVE-2008-0961**: Backup product uses hard-coded username and password, allowing attackers to bypass authentication via the RPC interface

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/798.html
