---
cwe_id: CWE-521
name: Weak Password Requirements
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: [CAPEC-112, CAPEC-16, CAPEC-49, CAPEC-509, CAPEC-55, CAPEC-555, CAPEC-561, CAPEC-565, CAPEC-70]
url: https://cwe.mitre.org/data/definitions/521.html
tags: [mitre-cwe, weakness, CWE-521]
---

# CWE-521 - Weak Password Requirements

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-521](https://cwe.mitre.org/data/definitions/521.html)

## Description
The product does not require that users should have strong passwords.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: A product's design should require adherance to an appropriate password policy. Specific password requirements depend strongly on contextual factors, but it is recommended to contain the following attributes: Enforcement of a minimum and maximum length Restrictions against password reuse Restrictions against using common passwords Restrictions against using contextual string in the password (e.g., user id, app name) Depending on the threat model, the password policy may include several additional attributes. Complex passwords requiring mixed character sets (alpha, numeric, special, mixed case) Increasing the range of characters makes the password harder to crack and may be appropriate for systems relying on single factor authentication. Unfortunately, a complex password may be difficult to memorize, encouraging a user to select a short password or to incorrectly manage the password (write it down). Another disadvantage of this approach is that it often does not result in a significant increases in overal password complexity due to people's predictable usage of various symbols. Large Minimum Length (encouraging passphrases instead of passwords) Increasing the number of characters makes the password harder to crack and may be appropriate for systems relying on single factor authentication. A disadvantage of this approach is that selecting a good passphrase is not easy and poor passwords can still be generated. Some prompting may be needed to encourage long un-predictable passwords. Randomly Chosen Secrets Generating a password for the user can help make sure that length and complexity requirements are met, and can result in secure passwords being used. A disadvantage of this approach is that the resulting password or passpharse may be too difficult to memorize, encouraging them to be written down. See NIST 800-63B [REF-1053] for further information on password requirements.
- **Architecture and Design**: Consider a second authentication factor beyond the password, which prevents the password from being a single point of failure. See CWE-308 for further information.
- **Implementation**: Consider implementing a password complexity meter to inform users when a chosen password meets the required attributes.
- **Implementation**: Previously, "password expiration" was widely advocated as a defense-in-depth approach to minimize the risk of weak passwords, and it has become a common practice. Password expiration requires a password to be changed within a fixed time window (such as every 90 days). However, this approach has significant limitations in the current threat landscape, and its utility has been reduced in light of the adoption of related protection mechanisms (such as password complexity and computational effort), along with the recognition that regular password changes often caused users to generate more predictable passwords. As a result, this is now a Discouraged Common Practice [REF-1488] [REF-1489], especially as the sole factor in protecting passwords. It is still strongly encouraged to force password changes in case of evidence of compromise, but this is not the same as a forced "expiration" on an arbitrary time frame.

## Related attack patterns (CAPEC)
- [CAPEC-112](https://capec.mitre.org/data/definitions/112.html)
- [CAPEC-16](https://capec.mitre.org/data/definitions/16.html)
- [CAPEC-49](https://capec.mitre.org/data/definitions/49.html)
- [CAPEC-509](https://capec.mitre.org/data/definitions/509.html)
- [CAPEC-55](https://capec.mitre.org/data/definitions/55.html)
- [CAPEC-555](https://capec.mitre.org/data/definitions/555.html)
- [CAPEC-561](https://capec.mitre.org/data/definitions/561.html)
- [CAPEC-565](https://capec.mitre.org/data/definitions/565.html)
- [CAPEC-70](https://capec.mitre.org/data/definitions/70.html)

## Related weaknesses
- CWE-1391 (ChildOf)
- CWE-287 (ChildOf)

## Observed examples (CVE)
- **CVE-2020-4574**: key server application does not require strong passwords

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/521.html
