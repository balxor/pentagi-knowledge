---
cwe_id: CWE-1318
name: Missing Support for Security Features in On-chip Fabrics or Buses
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Processor Hardware, Not Technology-Specific]
related_capec: [CAPEC-1, CAPEC-180]
url: https://cwe.mitre.org/data/definitions/1318.html
tags: [mitre-cwe, weakness, CWE-1318]
---

# CWE-1318 - Missing Support for Security Features in On-chip Fabrics or Buses

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1318](https://cwe.mitre.org/data/definitions/1318.html)

## Description
On-chip fabrics or buses either do not support or are not configured to support privilege separation or other security features, such as access control.

## Extended description
Certain on-chip fabrics and buses, especially simple and low-power buses, do not support security features. Apart from data transfer and addressing ports, some fabrics and buses do not have any interfaces to transfer privilege, immutable identity, or any other security attribute coming from the bus master. Similarly, they do not have dedicated signals to transport security-sensitive data from slave to master, such as completions for certain types of transactions. Few other on-chip fabrics and buses support security features and define specific interfaces/signals for transporting security attributes from master to slave or vice-versa. However, including these signals is not mandatory and could be left unconfigured when generating the register-transfer-level (RTL) description for the fabric. Such fabrics or buses should not be used to transport any security attribute coming from the bus master. In general, peripherals with security assets should not be connected to such buses before the transaction from the bus master reaches the bus, unless some form of access control is performed at a fabric bridge or another intermediate module.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Processor Hardware, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Access Control, Availability**: DoS: Crash, Exit, or Restart, Read Memory, Modify Memory

## Potential mitigations
- **Architecture and Design**: If fabric does not support security features, implement security checks in a bridge or any component that is between the master and the fabric. Alternatively, connect all fabric slaves that do not have any security assets under one such fabric and connect peripherals with security assets to a different fabric that supports security features.

## Related attack patterns (CAPEC)
- [CAPEC-1](https://capec.mitre.org/data/definitions/1.html)
- [CAPEC-180](https://capec.mitre.org/data/definitions/180.html)

## Related weaknesses
- CWE-693 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1318.html
