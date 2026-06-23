---
cwe_id: CWE-259
name: Use of Hard-coded Password
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific, ICS/OT]
related_capec: []
url: https://cwe.mitre.org/data/definitions/259.html
tags: [mitre-cwe, weakness, CWE-259]
---

# CWE-259 - Use of Hard-coded Password

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-259](https://cwe.mitre.org/data/definitions/259.html)

## Description
The product contains a hard-coded password, which it uses for its own inbound authentication or for outbound communication to external components.

## Extended description
There are two main variations of a hard-coded password: Inbound: the product contains an authentication mechanism that checks for a hard-coded password. Outbound: the product connects to another system or component, and it contains a hard-coded password for connecting to that component.

## Applicable platforms / languages
Not Language-Specific, ICS/OT

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity
- **Access Control**: Gain Privileges or Assume Identity, Hide Activities, Reduce Maintainability

## Potential mitigations
- **Architecture and Design**: For outbound authentication: store passwords outside of the code in a strongly-protected, encrypted configuration file or database that is protected from access by all outsiders, including other local users on the same system. Properly protect the key (CWE-320). If you cannot use encryption to protect the file, then make sure that the permissions are as restrictive as possible.
- **Architecture and Design**: For inbound authentication: Rather than hard-code a default username and password for first time logins, utilize a "first login" mode that requires the user to enter a unique strong password.
- **Architecture and Design**: Perform access control checks and limit which entities can access the feature that requires the hard-coded password. For example, a feature might only be enabled through the system console instead of through a network connection.
- **Architecture and Design**: For inbound authentication: apply strong one-way hashes to your passwords and store those hashes in a configuration file or database with appropriate access control. That way, theft of the file/database still requires the attacker to try to crack the password. When receiving an incoming password during authentication, take the hash of the password and compare it to the hash that you have saved. Use randomly assigned salts for each separate hash that you generate. This increases the amount of computation that an attacker needs to conduct a brute-force attack, possibly limiting the effectiveness of the rainbow table method.
- **Architecture and Design**: For front-end to back-end connections: Three solutions are possible, although none are complete. The first suggestion involves the use of generated passwords which are changed automatically and must be entered at given time intervals by a system administrator. These passwords will be held in memory and only be valid for the time intervals. Next, the passwords used should be limited at the back end to only performing actions valid for the front end, as opposed to having full access. Finally, the messages sent should be tagged and checksummed with time sensitive values so as to prevent replay style attacks.

## Related weaknesses
- CWE-798 (ChildOf)
- CWE-798 (ChildOf)
- CWE-798 (ChildOf)
- CWE-321 (PeerOf)
- CWE-257 (PeerOf)

## Observed examples (CVE)
- **CVE-2022-29964**: Distributed Control System (DCS) has hard-coded passwords for local shell access
- **CVE-2021-37555**: Telnet service for IoT feeder for dogs and cats has hard-coded password [REF-1288]
- **CVE-2021-35033**: Firmware for a WiFi router uses a hard-coded password for a BusyBox shell, allowing bypass of authentication through the UART port

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/259.html
