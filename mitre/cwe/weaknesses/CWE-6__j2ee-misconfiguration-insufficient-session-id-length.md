---
cwe_id: CWE-6
name: J2EE Misconfiguration: Insufficient Session-ID Length
type: weakness
abstraction: Variant
status: Incomplete
languages: [Java, Web Based, Web Server]
related_capec: [CAPEC-21, CAPEC-59]
url: https://cwe.mitre.org/data/definitions/6.html
tags: [mitre-cwe, weakness, CWE-6]
---

# CWE-6 - J2EE Misconfiguration: Insufficient Session-ID Length

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-6](https://cwe.mitre.org/data/definitions/6.html)

## Description
The J2EE application is configured to use an insufficient session ID length.

## Extended description
If an attacker can guess or steal a session ID, then they may be able to take over the user's session (called session hijacking). The number of possible session IDs increases with increased session ID length, making it more difficult to guess or steal a session ID.

## Applicable platforms / languages
Java, Web Based, Web Server

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity

## Potential mitigations
- **Implementation**: Session identifiers should be at least 128 bits long to prevent brute-force session guessing. A shorter session identifier leaves the application open to brute-force session guessing attacks.
- **Implementation**: A lower bound on the number of valid session identifiers that are available to be guessed is the number of users that are active on a site at any given moment. However, any users that abandon their sessions without logging out will increase this number. (This is one of many good reasons to have a short inactive session timeout.) With a 64 bit session identifier, assume 32 bits of entropy. For a large web site, assume that the attacker can try 1,000 guesses per second and that there are 10,000 valid session identifiers at any given moment. Given these assumptions, the expected time for an attacker to successfully guess a valid session identifier is less than 4 minutes. Now assume a 128 bit session identifier that provides 64 bits of entropy. With a very large web site, an attacker might try 10,000 guesses per second with 100,000 valid session identifiers available to be guessed. Given these assumptions, the expected time for an attacker to successfully guess a valid session identifier is greater than 292 years.

## Related attack patterns (CAPEC)
- [CAPEC-21](https://capec.mitre.org/data/definitions/21.html)
- [CAPEC-59](https://capec.mitre.org/data/definitions/59.html)

## Related weaknesses
- CWE-334 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/6.html
