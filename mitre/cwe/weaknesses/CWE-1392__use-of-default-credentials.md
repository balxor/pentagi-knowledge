---
cwe_id: CWE-1392
name: Use of Default Credentials
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, ICS/OT, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1392.html
tags: [mitre-cwe, weakness, CWE-1392]
---

# CWE-1392 - Use of Default Credentials

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1392](https://cwe.mitre.org/data/definitions/1392.html)

## Description
The product uses default credentials (such as passwords or cryptographic keys) for potentially critical functionality.

## Extended description
It is common practice for products to be designed to use default keys, passwords, or other mechanisms for authentication. The rationale is to simplify the manufacturing process or the system administrator's task of installation and deployment into an enterprise. However, if admins do not change the defaults, it is easier for attackers to bypass authentication quickly across multiple organizations.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, ICS/OT, Not Technology-Specific

## Common consequences
- **Authentication**: Gain Privileges or Assume Identity

## Potential mitigations
- **Requirements**: Prohibit use of default, hard-coded, or other values that do not vary for each installation of the product - especially for separate organizations.
- **Architecture and Design**: Force the administrator to change the credential upon installation.
- **Installation, Operation**: The product administrator could change the defaults upon installation or during operation.

## Related weaknesses
- CWE-1391 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-30270**: Remote Terminal Unit (RTU) uses default credentials for some SSH accounts
- **CVE-2021-41192**: data visualization/sharing package uses default secret keys or cookie values if they are not specified in environment variables
- **CVE-2021-38759**: microcontroller board has default password, allowing admin access
- **CVE-2018-3825**: cloud cluster management product has a default master encryption key
- **CVE-2010-2306**: Intrusion Detection System (IDS) uses the same static, private SSL keys for multiple devices and installations, allowing decryption of SSL traffic

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1392.html
