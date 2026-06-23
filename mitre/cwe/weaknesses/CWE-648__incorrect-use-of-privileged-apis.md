---
cwe_id: CWE-648
name: Incorrect Use of Privileged APIs
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: [CAPEC-107, CAPEC-234]
url: https://cwe.mitre.org/data/definitions/648.html
tags: [mitre-cwe, weakness, CWE-648]
---

# CWE-648 - Incorrect Use of Privileged APIs

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-648](https://cwe.mitre.org/data/definitions/648.html)

## Description
The product does not conform to the API requirements for a function call that requires extra privileges. This could allow attackers to gain privileges by causing the function to be called incorrectly.

## Extended description
When a product contains certain functions that perform operations requiring an elevated level of privilege, the caller of a privileged API must be careful to: ensure that assumptions made by the APIs are valid, such as validity of arguments account for known weaknesses in the design/implementation of the API call the API from a safe context If the caller of the API does not follow these requirements, then it may allow a malicious user or process to elevate their privilege, hijack the process, or steal sensitive data. For instance, it is important to know if privileged APIs do not shed their privileges before returning to the caller or if the privileged function might make certain assumptions about the data, context or state information passed to it by the caller. It is important to always know when and how privileged APIs can be called in order to ensure that their elevated level of privilege cannot be exploited.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Access Control**: Gain Privileges or Assume Identity
- **Confidentiality**: Read Application Data
- **Integrity, Confidentiality, Availability**: Execute Unauthorized Code or Commands

## Potential mitigations
- **Implementation**: Before calling privileged APIs, always ensure that the assumptions made by the privileged code hold true prior to making the call.
- **Architecture and Design**: Know architecture and implementation weaknesses of the privileged APIs and make sure to account for these weaknesses before calling the privileged APIs to ensure that they can be called safely.
- **Implementation**: If privileged APIs make certain assumptions about data, context or state validity that are passed by the caller, the calling code must ensure that these assumptions have been validated prior to making the call.
- **Implementation**: If privileged APIs do not shed their privilege prior to returning to the calling code, then calling code needs to shed these privileges immediately and safely right after the call to the privileged APIs. In particular, the calling code needs to ensure that a privileged thread of execution will never be returned to the user or made available to user-controlled processes.
- **Implementation**: Only call privileged APIs from safe, consistent and expected state.
- **Implementation**: Ensure that a failure or an error will not leave a system in a state where privileges are not properly shed and privilege escalation is possible (i.e. fail securely with regards to handling of privileges).

## Related attack patterns (CAPEC)
- [CAPEC-107](https://capec.mitre.org/data/definitions/107.html)
- [CAPEC-234](https://capec.mitre.org/data/definitions/234.html)

## Related weaknesses
- CWE-269 (ChildOf)

## Observed examples (CVE)
- **CVE-2003-0645**: A Unix utility that displays online help files, if installed setuid, could allow a local attacker to gain privileges when a particular file-opening function is called.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/648.html
