---
cwe_id: CWE-1393
name: Use of Default Password
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific, ICS/OT]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1393.html
tags: [mitre-cwe, weakness, CWE-1393]
---

# CWE-1393 - Use of Default Password

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1393](https://cwe.mitre.org/data/definitions/1393.html)

## Description
The product uses default passwords for potentially critical functionality.

## Extended description
It is common practice for products to be designed to use default passwords for authentication. The rationale is to simplify the manufacturing process or the system administrator's task of installation and deployment into an enterprise. However, if admins do not change the defaults, then it makes it easier for attackers to quickly bypass authentication across multiple organizations. There are many lists of default passwords and default-password scanning tools that are easily available from the World Wide Web.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific, ICS/OT

## Common consequences
- **Authentication**: Gain Privileges or Assume Identity

## Potential mitigations
- **Requirements**: Prohibit use of default, hard-coded, or other values that do not vary for each installation of the product - especially for separate organizations.
- **Documentation**: Ensure that product documentation clearly emphasizes the presence of default passwords and provides steps for the administrator to change them.
- **Architecture and Design**: Force the administrator to change the credential upon installation.
- **Installation, Operation**: The product administrator could change the defaults upon installation or during operation.

## Related weaknesses
- CWE-1392 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-30270**: Remote Terminal Unit (RTU) uses default credentials for some SSH accounts
- **CVE-2022-2336**: OPC Unified Architecture (OPC UA) industrial automation product has a default password
- **CVE-2021-38759**: microcontroller board has default password, allowing admin access
- **CVE-2021-44480**: children's smart watch has default passwords allowing attackers to send SMS commands and listen to the device's surroundings
- **CVE-2020-11624**: surveillance camera has default password for the admin account
- **CVE-2018-15719**: medical dental records product installs a MySQL database with a blank default password
- **CVE-2014-9736**: healthcare system for archiving patient images has default passwords for key management and storage databases
- **CVE-2000-1209**: database product installs admin account with default null password, allowing privileges, as exploited by various worms

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1393.html
