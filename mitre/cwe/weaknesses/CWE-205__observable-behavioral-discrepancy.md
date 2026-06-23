---
cwe_id: CWE-205
name: Observable Behavioral Discrepancy
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-541, CAPEC-580]
url: https://cwe.mitre.org/data/definitions/205.html
tags: [mitre-cwe, weakness, CWE-205]
---

# CWE-205 - Observable Behavioral Discrepancy

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-205](https://cwe.mitre.org/data/definitions/205.html)

## Description
The product's behaviors indicate important differences that may be observed by unauthorized actors in a way that reveals (1) its internal state or decision process, or (2) differences from other products with equivalent functionality.

## Extended description
Ideally, a product should provide as little information about its internal operations as possible. Otherwise, attackers could use knowledge of these internal operations to simplify or optimize their attack. In some cases, behavioral discrepancies can be used by attackers to form a side channel.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Access Control**: Read Application Data, Bypass Protection Mechanism

## Related attack patterns (CAPEC)
- [CAPEC-541](https://capec.mitre.org/data/definitions/541.html)
- [CAPEC-580](https://capec.mitre.org/data/definitions/580.html)

## Related weaknesses
- CWE-203 (ChildOf)
- CWE-514 (CanPrecede)

## Observed examples (CVE)
- **CVE-2002-0208**: Product modifies TCP/IP stack and ICMP error messages in unusual ways that show the product is in use.
- **CVE-2004-2252**: Behavioral infoleak by responding to SYN-FIN packets.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/205.html
