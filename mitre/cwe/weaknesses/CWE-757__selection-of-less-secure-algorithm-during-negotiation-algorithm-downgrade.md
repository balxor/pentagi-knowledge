---
cwe_id: CWE-757
name: Selection of Less-Secure Algorithm During Negotiation ('Algorithm Downgrade')
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-220, CAPEC-606, CAPEC-620]
url: https://cwe.mitre.org/data/definitions/757.html
tags: [mitre-cwe, weakness, CWE-757]
---

# CWE-757 - Selection of Less-Secure Algorithm During Negotiation ('Algorithm Downgrade')

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-757](https://cwe.mitre.org/data/definitions/757.html)

## Description
A protocol or its implementation supports interaction between multiple actors and allows those actors to negotiate which algorithm should be used as a protection mechanism such as encryption or authentication, but it does not select the strongest algorithm that is available to both parties.

## Extended description
When a security mechanism can be forced to downgrade to use a less secure algorithm, this can make it easier for attackers to compromise the product by exploiting weaker algorithm. The victim might not be aware that the less secure algorithm is being used. For example, if an attacker can force a communications channel to use cleartext instead of strongly-encrypted data, then the attacker could read the channel by sniffing, instead of going through extra effort of trying to decrypt the data using brute force techniques.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Related attack patterns (CAPEC)
- [CAPEC-220](https://capec.mitre.org/data/definitions/220.html)
- [CAPEC-606](https://capec.mitre.org/data/definitions/606.html)
- [CAPEC-620](https://capec.mitre.org/data/definitions/620.html)

## Related weaknesses
- CWE-693 (ChildOf)

## Observed examples (CVE)
- **CVE-2006-4302**: Attacker can select an older version of the software to exploit its vulnerabilities.
- **CVE-2006-4407**: Improper prioritization of encryption ciphers during negotiation leads to use of a weaker cipher.
- **CVE-2005-2969**: chain: SSL/TLS implementation disables a verification step (CWE-325) that enables a downgrade attack to a weaker protocol.
- **CVE-2001-1444**: Telnet protocol implementation allows downgrade to weaker authentication and encryption using an Adversary-in-the-Middle AITM attack.
- **CVE-2002-1646**: SSH server implementation allows override of configuration setting to use weaker authentication schemes. This may be a composite with CWE-642.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/757.html
