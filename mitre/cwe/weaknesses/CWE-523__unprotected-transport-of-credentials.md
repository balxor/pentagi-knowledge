---
cwe_id: CWE-523
name: Unprotected Transport of Credentials
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-102]
url: https://cwe.mitre.org/data/definitions/523.html
tags: [mitre-cwe, weakness, CWE-523]
---

# CWE-523 - Unprotected Transport of Credentials

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-523](https://cwe.mitre.org/data/definitions/523.html)

## Description
Login pages do not use adequate measures to protect the user name and password while they are in transit from the client to the server.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Operation, System Configuration**: Enforce SSL use for the login page or any page used to transmit user credentials or other sensitive information. Even if the entire site does not use SSL, it MUST use SSL for login. Additionally, to help prevent phishing attacks, make sure that SSL serves the login page. SSL allows the user to verify the identity of the server to which they are connecting. If the SSL serves login page, the user can be certain they are talking to the proper end system. A phishing attack would typically redirect a user to a site that does not have a valid trusted server certificate issued from an authorized supplier.

## Related attack patterns (CAPEC)
- [CAPEC-102](https://capec.mitre.org/data/definitions/102.html)

## Related weaknesses
- CWE-522 (ChildOf)
- CWE-319 (CanAlsoBe)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/523.html
