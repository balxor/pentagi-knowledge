---
cwe_id: CWE-1311
name: Improper Translation of Security Attributes by Fabric Bridge
type: weakness
abstraction: Base
status: Draft
languages: [Verilog, VHDL, Not Technology-Specific]
related_capec: [CAPEC-1, CAPEC-180, CAPEC-233]
url: https://cwe.mitre.org/data/definitions/1311.html
tags: [mitre-cwe, weakness, CWE-1311]
---

# CWE-1311 - Improper Translation of Security Attributes by Fabric Bridge

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1311](https://cwe.mitre.org/data/definitions/1311.html)

## Description
The bridge incorrectly translates security attributes from either trusted to untrusted or from untrusted to trusted when converting from one fabric protocol to another.

## Extended description
A bridge allows IP blocks supporting different fabric protocols to be integrated into the system. Fabric end-points or interfaces usually have dedicated signals to transport security attributes. For example, HPROT signals in AHB, AxPROT signals in AXI, and MReqInfo and SRespInfo signals in OCP. The values on these signals are used to indicate the security attributes of the transaction. These include the immutable hardware identity of the controller initiating the transaction, privilege level, and type of transaction (e.g., read/write, cacheable/non-cacheable, posted/non-posted). A weakness can arise if the bridge IP block, which translates the signals from the protocol used in the IP block endpoint to the protocol used by the central bus, does not properly translate the security attributes. As a result, the identity of the initiator could be translated from untrusted to trusted or vice-versa. This could result in access-control bypass, privilege escalation, or denial of service.

## Applicable platforms / languages
Verilog, VHDL, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Access Control**: Modify Memory, Read Memory, Gain Privileges or Assume Identity, Bypass Protection Mechanism, Execute Unauthorized Code or Commands

## Potential mitigations
- **Architecture and Design**: The translation must map signals in such a way that untrusted agents cannot map to trusted agents or vice-versa.
- **Implementation**: Ensure that the translation maps signals in such a way that untrusted agents cannot map to trusted agents or vice-versa.

## Related attack patterns (CAPEC)
- [CAPEC-1](https://capec.mitre.org/data/definitions/1.html)
- [CAPEC-180](https://capec.mitre.org/data/definitions/180.html)
- [CAPEC-233](https://capec.mitre.org/data/definitions/233.html)

## Related weaknesses
- CWE-284 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1311.html
