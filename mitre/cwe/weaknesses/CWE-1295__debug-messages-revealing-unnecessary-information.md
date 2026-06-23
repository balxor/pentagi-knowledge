---
cwe_id: CWE-1295
name: Debug Messages Revealing Unnecessary Information
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-121]
url: https://cwe.mitre.org/data/definitions/1295.html
tags: [mitre-cwe, weakness, CWE-1295]
---

# CWE-1295 - Debug Messages Revealing Unnecessary Information

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1295](https://cwe.mitre.org/data/definitions/1295.html)

## Description
The product fails to adequately prevent the revealing of unnecessary and potentially sensitive system information within debugging messages.

## Extended description
Debug messages are messages that help troubleshoot an issue by revealing the internal state of the system. For example, debug data in design can be exposed through internal memory array dumps or boot logs through interfaces like UART via TAP commands, scan chain, etc. Thus, the more information contained in a debug message, the easier it is to debug. However, there is also the risk of revealing information that could help an attacker either decipher a vulnerability, and/or gain a better understanding of the system. Thus, this extra information could lower the "security by obscurity" factor. While "security by obscurity" alone is insufficient, it can help as a part of "Defense-in-depth".

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Availability, Access Control, Accountability, Authentication, Authorization, Non-Repudiation**: Read Memory, Bypass Protection Mechanism, Gain Privileges or Assume Identity, Varies by Context

## Potential mitigations
- **Implementation**: Ensure that a debug message does not reveal any unnecessary information during the debug process for the intended response.

## Related attack patterns (CAPEC)
- [CAPEC-121](https://capec.mitre.org/data/definitions/121.html)

## Related weaknesses
- CWE-200 (ChildOf)
- CWE-209 (PeerOf)

## Observed examples (CVE)
- **CVE-2022-34364**: Java-based SDK for TLS has a debug message with unnecessary information
- **CVE-2021-25476**: Digital Rights Management (DRM) capability for mobile platform leaks pointer information, simplifying ASLR bypass
- **CVE-2020-24491**: Processor generates debug message that contains sensitive information ("addresses of memory transactions").
- **CVE-2017-18326**: modem debug messages include cryptographic keys

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1295.html
