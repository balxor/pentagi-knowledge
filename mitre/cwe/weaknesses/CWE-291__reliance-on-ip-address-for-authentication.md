---
cwe_id: CWE-291
name: Reliance on IP Address for Authentication
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-4]
url: https://cwe.mitre.org/data/definitions/291.html
tags: [mitre-cwe, weakness, CWE-291]
---

# CWE-291 - Reliance on IP Address for Authentication

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-291](https://cwe.mitre.org/data/definitions/291.html)

## Description
The product uses an IP address for authentication.

## Extended description
IP addresses can be easily spoofed. Attackers can forge the source IP address of the packets they send, but response packets will return to the forged IP address. To see the response packets, the attacker has to sniff the traffic between the victim machine and the forged IP address. In order to accomplish the required sniffing, attackers typically attempt to locate themselves on the same subnet as the victim machine. Attackers may be able to circumvent this requirement by using source routing, but source routing is disabled across much of the Internet today. In summary, IP address verification can be a useful part of an authentication scheme, but it should not be the single factor required for authentication.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control, Non-Repudiation**: Hide Activities, Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Use other means of identity verification that cannot be simply spoofed. Possibilities include a username/password or certificate.

## Related attack patterns (CAPEC)
- [CAPEC-4](https://capec.mitre.org/data/definitions/4.html)

## Related weaknesses
- CWE-290 (ChildOf)
- CWE-923 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-30319**: S-bus functionality in a home automation product performs access control using an IP allowlist, which can be bypassed by a forged IP address.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/291.html
