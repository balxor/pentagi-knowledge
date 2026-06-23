---
cwe_id: CWE-640
name: Weak Password Recovery Mechanism for Forgotten Password
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-50]
url: https://cwe.mitre.org/data/definitions/640.html
tags: [mitre-cwe, weakness, CWE-640]
---

# CWE-640 - Weak Password Recovery Mechanism for Forgotten Password

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-640](https://cwe.mitre.org/data/definitions/640.html)

## Description
The product contains a mechanism for users to recover or change their passwords without knowing the original password, but the mechanism is weak.

## Extended description
It is common for an application to have a mechanism that provides a means for a user to gain access to their account in the event they forget their password. Very often the password recovery mechanism is weak, which has the effect of making it more likely that it would be possible for a person other than the legitimate system user to gain access to that user's account. Weak password recovery schemes completely undermine a strong password authentication scheme. This weakness may be that the security question is too easy to guess or find an answer to (e.g. because the question is too common, or the answers can be found using social media). Or there might be an implementation weakness in the password recovery mechanism code that may for instance trick the system into e-mailing the new password to an e-mail account other than that of the user. There might be no throttling done on the rate of password resets so that a legitimate user can be denied service by an attacker if an attacker tries to recover their password in a rapid succession. The system may send the original password to the user rather than generating a new temporary password. In summary, password recovery functionality, if not carefully designed and implemented can often become the system's weakest link that can be misused in a way that would allow an attacker to gain unauthorized access to the system.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity
- **Availability**: DoS: Resource Consumption (Other)
- **Integrity, Other**: Other

## Potential mitigations
- **Architecture and Design**: Make sure that all input supplied by the user to the password recovery mechanism is thoroughly filtered and validated.
- **Architecture and Design**: Do not use standard weak security questions and use several security questions.
- **Architecture and Design**: Make sure that there is throttling on the number of incorrect answers to a security question. Disable the password recovery functionality after a certain (small) number of incorrect guesses.
- **Architecture and Design**: Require that the user properly answers the security question prior to resetting their password and sending the new password to the e-mail address of record.
- **Architecture and Design**: Never allow the user to control what e-mail address the new password will be sent to in the password recovery mechanism.
- **Architecture and Design**: Assign a new temporary password rather than revealing the original password.

## Related attack patterns (CAPEC)
- [CAPEC-50](https://capec.mitre.org/data/definitions/50.html)

## Related weaknesses
- CWE-1390 (ChildOf)
- CWE-287 (ChildOf)

## Observed examples (CVE)
- **CVE-2025-1570**: password reset functionality for a WordPress plugin allows a brute force attack of the one-time password
- **CVE-2024-9302**: password reset functionality for a WordPress plugin allows a brute force attack of the one-time password
- **CVE-2024-5277**: password recovery mechanism for AI developer toolkit does not invalidate the reset password token after it is used, allowing attackers to reuse the token to change passwords of victims
- **CVE-2024-38287**: web conference product resets passwords to random 8-digit values, allowing brute force attacks by retrieving the hash

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/640.html
