---
cwe_id: CWE-620
name: Unverified Password Change
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/620.html
tags: [mitre-cwe, weakness, CWE-620]
---

# CWE-620 - Unverified Password Change

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-620](https://cwe.mitre.org/data/definitions/620.html)

## Description
When setting a new password for a user, the product does not require knowledge of the original password, or using another form of authentication.

## Extended description
This could be used by an attacker to change passwords for another user, thus gaining the privileges associated with that user.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism, Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: When prompting for a password change, force the user to provide the original password in addition to the new password.
- **Architecture and Design**: Do not use "forgotten password" functionality. But if you must, ensure that you are only providing information to the actual user, e.g. by using an email address or challenge question that the legitimate user already provided in the past; do not allow the current user to change this identity information until the correct password has been provided.

## Related weaknesses
- CWE-1390 (ChildOf)

## Observed examples (CVE)
- **CVE-2025-4903**: Router web interface allows unverified password change
- **CVE-2007-0681**: Web app allows remote attackers to change the passwords of arbitrary users without providing the original password, and possibly perform other unauthorized actions.
- **CVE-2000-0944**: Web application password change utility doesn't check the original password.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/620.html
