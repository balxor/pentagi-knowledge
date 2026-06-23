---
capec_id: CAPEC-226
name: Session Credential Falsification through Manipulation
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-565, CWE-472]
related_attack: []
url: https://capec.mitre.org/data/definitions/226.html
tags: [mitre-capec, attack-pattern, CAPEC-226]
---

# CAPEC-226 - Session Credential Falsification through Manipulation

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-226](https://capec.mitre.org/data/definitions/226.html)

## Description
An attacker manipulates an existing credential in order to gain access to a target application. Session credentials allow users to identify themselves to a service after an initial authentication without needing to resend the authentication information (usually a username and password) with every message. An attacker may be able to manipulate a credential sniffed from an existing connection in order to gain access to a target server.

## Extended description
For example, a credential in the form of a web cookie might have a field that indicates the access rights of a user. By manually tweaking this cookie, a user might be able to increase their access rights to the server. Alternately an attacker may be able to manipulate an existing credential to appear as a different user. This attack differs from falsification through prediction in that the user bases their modified credentials off existing credentials instead of using patterns detected in prior credentials to create a new credential that is accepted because it fits the pattern. As a result, an attacker may be able to impersonate other users or elevate their permissions to a targeted service.

## Prerequisites
- The targeted application must use session credentials to identify legitimate users.

## Resources required
- An attacker will need tools to sniff existing credentials (possibly their own) in order to retrieve a base credential for modification. They will need to understand how the components of the credential affect server behavior and how to manipulate this behavior by changing the credential. Finally, they will need tools to allow them to craft and transmit a modified credential.

## Related weaknesses (CWE)
- [CWE-565](https://cwe.mitre.org/data/definitions/565.html)
- [CWE-472](https://cwe.mitre.org/data/definitions/472.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/226.html
