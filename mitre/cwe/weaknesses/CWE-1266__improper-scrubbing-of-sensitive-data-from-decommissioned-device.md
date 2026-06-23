---
cwe_id: CWE-1266
name: Improper Scrubbing of Sensitive Data from Decommissioned Device
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-150, CAPEC-37, CAPEC-545, CAPEC-546, CAPEC-675]
url: https://cwe.mitre.org/data/definitions/1266.html
tags: [mitre-cwe, weakness, CWE-1266]
---

# CWE-1266 - Improper Scrubbing of Sensitive Data from Decommissioned Device

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1266](https://cwe.mitre.org/data/definitions/1266.html)

## Description
The product does not properly provide a capability for the product administrator to remove sensitive data at the time the product is decommissioned. A scrubbing capability could be missing, insufficient, or incorrect.

## Extended description
When a product is decommissioned - i.e., taken out of service - best practices or regulatory requirements may require the administrator to remove or overwrite sensitive data first, i.e. "scrubbing." Improper scrubbing of sensitive data from a decommissioned device leaves that data vulnerable to acquisition by a malicious actor. Sensitive data may include, but is not limited to, device/manufacturer proprietary information, user/device credentials, network configurations, and other forms of sensitive data.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Memory

## Potential mitigations
- **Architecture and Design**: Functionality to completely scrub data from a product at the conclusion of its lifecycle should be part of the design phase. Trying to add this function on top of an existing architecture could lead to incomplete removal of sensitive information/data.
- **Policy**: The manufacturer should describe the location(s) where sensitive data is stored and the policies and procedures for its removal. This information may be conveyed, for example, in an Administrators Guide or a Statement of Volatility.
- **Implementation**: If the capability to wipe sensitive data isn't built-in, the manufacturer may need to provide a utility to scrub sensitive data from storage if that data is located in a place which is non-accessible by the administrator. One example of this could be when sensitive data is stored on an EEPROM for which there is no user/admin interface provided by the system.

## Related attack patterns (CAPEC)
- [CAPEC-150](https://capec.mitre.org/data/definitions/150.html)
- [CAPEC-37](https://capec.mitre.org/data/definitions/37.html)
- [CAPEC-545](https://capec.mitre.org/data/definitions/545.html)
- [CAPEC-546](https://capec.mitre.org/data/definitions/546.html)
- [CAPEC-675](https://capec.mitre.org/data/definitions/675.html)

## Related weaknesses
- CWE-404 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1266.html
