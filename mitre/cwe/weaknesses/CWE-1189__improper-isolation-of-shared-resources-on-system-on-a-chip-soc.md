---
cwe_id: CWE-1189
name: Improper Isolation of Shared Resources on System-on-a-Chip (SoC)
type: weakness
abstraction: Base
status: Stable
languages: [Not Language-Specific, System on Chip]
related_capec: [CAPEC-124]
url: https://cwe.mitre.org/data/definitions/1189.html
tags: [mitre-cwe, weakness, CWE-1189]
---

# CWE-1189 - Improper Isolation of Shared Resources on System-on-a-Chip (SoC)

**Abstraction:** Base  -  **Status:** Stable  -  **CWE:** [CWE-1189](https://cwe.mitre.org/data/definitions/1189.html)

## Description
The System-On-a-Chip (SoC) does not properly isolate shared resources between trusted and untrusted agents.

## Extended description
A System-On-a-Chip (SoC) has a lot of functionality, but it may have a limited number of pins or pads. A pin can only perform one function at a time. However, it can be configured to perform multiple different functions. This technique is called pin multiplexing. Similarly, several resources on the chip may be shared to multiplex and support different features or functions. When such resources are shared between trusted and untrusted agents, untrusted agents may be able to access the assets intended to be accessed only by the trusted agents.

## Applicable platforms / languages
Not Language-Specific, System on Chip

## Common consequences
- **Access Control**: Bypass Protection Mechanism
- **Integrity**: Quality Degradation

## Potential mitigations
- **Architecture and Design**: When sharing resources, avoid mixing agents of varying trust levels. Untrusted agents should not share resources with trusted agents.

## Related attack patterns (CAPEC)
- [CAPEC-124](https://capec.mitre.org/data/definitions/124.html)

## Related weaknesses
- CWE-653 (ChildOf)
- CWE-668 (ChildOf)
- CWE-1331 (PeerOf)

## Observed examples (CVE)
- **CVE-2020-8698**: Processor has improper isolation of shared resources allowing for information disclosure.
- **CVE-2019-6260**: Baseboard Management Controller (BMC) device implements Advanced High-performance Bus (AHB) bridges that do not require authentication for arbitrary read and write access to the BMC's physical address space from the host, and possibly the network [REF-1138].

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1189.html
