---
cwe_id: CWE-207
name: Observable Behavioral Discrepancy With Equivalent Products
type: weakness
abstraction: Variant
status: Draft
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/207.html
tags: [mitre-cwe, weakness, CWE-207]
---

# CWE-207 - Observable Behavioral Discrepancy With Equivalent Products

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-207](https://cwe.mitre.org/data/definitions/207.html)

## Description
The product operates in an environment in which its existence or specific identity should not be known, but it behaves differently than other products with equivalent functionality, in a way that is observable to an attacker.

## Extended description
For many kinds of products, multiple products may be available that perform the same functionality, such as a web server, network interface, or intrusion detection system. Attackers often perform "fingerprinting," which uses discrepancies in order to identify which specific product is in use. Once the specific product has been identified, the attacks can be made more customized and efficient. Often, an organization might intentionally allow the specific product to be identifiable. However, in some environments, the ability to identify a distinct product is unacceptable, and it is expected that every product would behave in exactly the same way. In these more restricted environments, a behavioral difference might pose an unacceptable risk if it makes it easier to identify the product's vendor, model, configuration, version, etc.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Access Control**: Read Application Data, Bypass Protection Mechanism

## Related weaknesses
- CWE-205 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-0208**: Product modifies TCP/IP stack and ICMP error messages in unusual ways that show the product is in use.
- **CVE-2004-2252**: Behavioral infoleak by responding to SYN-FIN packets.
- **CVE-2000-1142**: Honeypot generates an error with a "pwd" command in a particular directory, allowing attacker to know they are in a honeypot system.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/207.html
