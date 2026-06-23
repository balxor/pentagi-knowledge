---
cwe_id: CWE-1277
name: Firmware Not Updateable
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-682]
url: https://cwe.mitre.org/data/definitions/1277.html
tags: [mitre-cwe, weakness, CWE-1277]
---

# CWE-1277 - Firmware Not Updateable

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1277](https://cwe.mitre.org/data/definitions/1277.html)

## Description
The product does not provide its users with the ability to update or patch its firmware to address any vulnerabilities or weaknesses that may be present.

## Extended description
Without the ability to patch or update firmware, consumers will be left vulnerable to exploitation of any known vulnerabilities, or any vulnerabilities that are discovered in the future. This can expose consumers to permanent risk throughout the entire lifetime of the device, which could be years or decades. Some external protective measures and mitigations might be employed to aid in preventing or reducing the risk of malicious attack, but the root weakness cannot be corrected.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Access Control, Authentication, Authorization**: Gain Privileges or Assume Identity, Bypass Protection Mechanism, Execute Unauthorized Code or Commands, DoS: Crash, Exit, or Restart

## Potential mitigations
- **Requirements**: Specify requirements to include the ability to update the firmware. Include integrity checks and authentication to ensure that untrusted firmware cannot be installed.
- **Architecture and Design**: Design the device to allow for updating the firmware. Ensure that the design specifies how to distribute the updates and ensure their integrity and authentication.
- **Implementation**: Implement the necessary functionality to allow the firmware to be updated.

## Related attack patterns (CAPEC)
- [CAPEC-682](https://capec.mitre.org/data/definitions/682.html)

## Related weaknesses
- CWE-1329 (ChildOf)

## Observed examples (CVE)
- **CVE-2020-9054**: Chain: network-attached storage (NAS) device has a critical OS command injection (CWE-78) vulnerability that is actively exploited to place IoT devices into a botnet, but some products are "end-of-support" and cannot be patched (CWE-1277). [REF-1097]
- **[REF-1095]**: A hardware "smart lock" has weak key generation that allows attackers to steal the key by BLE sniffing, but the device's firmware cannot be upgraded and hence remains vulnerable [REF-1095].

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1277.html
