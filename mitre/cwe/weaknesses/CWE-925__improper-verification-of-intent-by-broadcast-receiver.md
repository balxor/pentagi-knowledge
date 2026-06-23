---
cwe_id: CWE-925
name: Improper Verification of Intent by Broadcast Receiver
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Mobile]
related_capec: [CAPEC-499]
url: https://cwe.mitre.org/data/definitions/925.html
tags: [mitre-cwe, weakness, CWE-925]
---

# CWE-925 - Improper Verification of Intent by Broadcast Receiver

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-925](https://cwe.mitre.org/data/definitions/925.html)

## Description
The Android application uses a Broadcast Receiver that receives an Intent but does not properly verify that the Intent came from an authorized source.

## Extended description
Certain types of Intents, identified by action string, can only be broadcast by the operating system itself, not by third-party applications. However, when an application registers to receive these implicit system intents, it is also registered to receive any explicit intents. While a malicious application cannot send an implicit system intent, it can send an explicit intent to the target application, which may assume that any received intent is a valid implicit system intent and not an explicit intent from another application. This may lead to unintended behavior.

## Applicable platforms / languages
Not Language-Specific, Mobile

## Common consequences
- **Integrity**: Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: Before acting on the Intent, check the Intent Action to make sure it matches the expected System action.

## Related attack patterns (CAPEC)
- [CAPEC-499](https://capec.mitre.org/data/definitions/499.html)

## Related weaknesses
- CWE-940 (ChildOf)

## Observed examples (CVE)
- **CVE-2025-20972**: Mobile app store does not properly verify the intent by the broadcast receiver, allowing local attackers to write arbitrary files
- **CVE-2024-10576**: Mobile device has an application that exposes a broadcast received that allows local attackers to force a factory reset

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/925.html
