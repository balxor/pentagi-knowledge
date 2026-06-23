---
cwe_id: CWE-1313
name: Hardware Allows Activation of Test or Debug Logic at Runtime
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-121]
url: https://cwe.mitre.org/data/definitions/1313.html
tags: [mitre-cwe, weakness, CWE-1313]
---

# CWE-1313 - Hardware Allows Activation of Test or Debug Logic at Runtime

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1313](https://cwe.mitre.org/data/definitions/1313.html)

## Description
During runtime, the hardware allows for test or debug logic (feature) to be activated, which allows for changing the state of the hardware. This feature can alter the intended behavior of the system and allow for alteration and leakage of sensitive data by an adversary.

## Extended description
An adversary can take advantage of test or debug logic that is made accessible through the hardware during normal operation to modify the intended behavior of the system. For example, an accessible Test/debug mode may allow read/write access to any system data. Using error injection (a common test/debug feature) during a transmit/receive operation on a bus, data may be modified to produce an unintended message. Similarly, confidentiality could be compromised by such features allowing access to secrets.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Availability**: Modify Memory, Read Memory, DoS: Crash, Exit, or Restart, DoS: Instability, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Resource Consumption (Other), Execute Unauthorized Code or Commands, Gain Privileges or Assume Identity, Bypass Protection Mechanism, Alter Execution Logic, Quality Degradation, Unexpected State, Reduce Performance, Reduce Reliability

## Potential mitigations
- **Architecture and Design**: Insert restrictions on when the hardware's test or debug features can be activated. For example, during normal operating modes, the hardware's privileged modes that allow access to such features cannot be activated. Configuring the hardware to only enter a test or debug mode within a window of opportunity such as during boot or configuration stage. The result is disablement of such test/debug features and associated modes during normal runtime operations.
- **Implementation**: Insert restrictions on when the hardware's test or debug features can be activated. For example, during normal operating modes, the hardware's privileged modes that allow access to such features cannot be activated. Configuring the hardware to only enter a test or debug mode within a window of opportunity such as during boot or configuration stage. The result is disablement of such test/debug features and associated modes during normal runtime operations.
- **Integration**: Insert restrictions on when the hardware's test or debug features can be activated. For example, during normal operating modes, the hardware's privileged modes that allow access to such features cannot be activated. Configuring the hardware to only enter a test or debug mode within a window of opportunity such as during boot or configuration stage. The result is disablement of such test/debug features and associated modes during normal runtime operations.

## Related attack patterns (CAPEC)
- [CAPEC-121](https://capec.mitre.org/data/definitions/121.html)

## Related weaknesses
- CWE-284 (ChildOf)

## Observed examples (CVE)
- **CVE-2021-33150**: Hardware processor allows activation of test or debug logic at runtime.
- **CVE-2021-0146**: Processor allows the activation of test or debug logic at runtime, allowing escalation of privileges

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1313.html
