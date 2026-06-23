---
cwe_id: CWE-1394
name: Use of Default Cryptographic Key
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1394.html
tags: [mitre-cwe, weakness, CWE-1394]
---

# CWE-1394 - Use of Default Cryptographic Key

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1394](https://cwe.mitre.org/data/definitions/1394.html)

## Description
The product uses a default cryptographic key for potentially critical functionality.

## Extended description
It is common practice for products to be designed to use default keys. The rationale is to simplify the manufacturing process or the system administrator's task of installation and deployment into an enterprise. However, if admins do not change the defaults, it is easier for attackers to bypass authentication quickly across multiple organizations.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Authentication**: Gain Privileges or Assume Identity

## Potential mitigations
- **Requirements**: Prohibit use of default, hard-coded, or other values that do not vary for each installation of the product - especially for separate organizations.
- **Architecture and Design**: Force the administrator to change the credential upon installation.
- **Installation, Operation**: The product administrator could change the defaults upon installation or during operation.

## Related weaknesses
- CWE-1392 (ChildOf)

## Observed examples (CVE)
- **CVE-2018-3825**: cloud cluster management product has a default master encryption key
- **CVE-2016-1561**: backup storage product has a default SSH public key in the authorized_keys file, allowing root access
- **CVE-2010-2306**: Intrusion Detection System (IDS) uses the same static, private SSL keys for multiple devices and installations, allowing decryption of SSL traffic

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1394.html
