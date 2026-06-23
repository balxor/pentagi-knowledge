---
cwe_id: CWE-405
name: Asymmetric Resource Consumption (Amplification)
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific, Client Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/405.html
tags: [mitre-cwe, weakness, CWE-405]
---

# CWE-405 - Asymmetric Resource Consumption (Amplification)

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-405](https://cwe.mitre.org/data/definitions/405.html)

## Description
The product does not properly control situations in which an adversary can cause the product to consume or produce excessive resources without requiring the adversary to invest equivalent work or otherwise prove authorization, i.e., the adversary's influence is "asymmetric."

## Extended description
This can lead to poor performance due to "amplification" of resource consumption, typically in a non-linear fashion. This situation is worsened if the product allows malicious users or attackers to consume more resources than their access level permits.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific, Client Server

## Common consequences
- **Availability**: DoS: Amplification, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Resource Consumption (Other)

## Potential mitigations
- **Architecture and Design**: An application must make resources available to a client commensurate with the client's access level.
- **Architecture and Design**: An application must, at all times, keep track of allocated resources and meter their usage appropriately.
- **System Configuration**: Consider disabling resource-intensive algorithms on the server side, such as Diffie-Hellman key exchange.

## Related weaknesses
- CWE-400 (ChildOf)

## Observed examples (CVE)
- **CVE-1999-0513**: Classic "Smurf" attack, using spoofed ICMP packets to broadcast addresses.
- **CVE-2003-1564**: Parsing library allows XML bomb
- **CVE-2004-2458**: Tool creates directories before authenticating user.
- **CVE-2020-10735**: Python has "quadratic complexity" issue when converting string to int with many digits in unexpected bases
- **CVE-2020-5243**: server allows ReDOS with crafted User-Agent strings, due to overlapping capture groups that cause excessive backtracking.
- **CVE-2013-5211**: composite: NTP feature generates large responses (high amplification factor) with spoofed UDP source addresses.
- **CVE-2002-20001**: Diffie-Hellman (DHE) Key Agreement Protocol allows attackers to send arbitrary numbers that are not public keys, which causes the server to perform expensive, unnecessary computation of modular exponentiation.
- **CVE-2022-40735**: The Diffie-Hellman Key Agreement Protocol allows use of long exponents, which are more computationally expensive than using certain "short exponents" with particular properties.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/405.html
