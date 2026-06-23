---
cwe_id: CWE-1331
name: Improper Isolation of Shared Resources in Network On Chip (NoC)
type: weakness
abstraction: Base
status: Stable
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Security Hardware, Not Technology-Specific]
related_capec: [CAPEC-124]
url: https://cwe.mitre.org/data/definitions/1331.html
tags: [mitre-cwe, weakness, CWE-1331]
---

# CWE-1331 - Improper Isolation of Shared Resources in Network On Chip (NoC)

**Abstraction:** Base  -  **Status:** Stable  -  **CWE:** [CWE-1331](https://cwe.mitre.org/data/definitions/1331.html)

## Description
The Network On Chip (NoC) does not isolate or incorrectly isolates its on-chip-fabric and internal resources such that they are shared between trusted and untrusted agents, creating timing channels.

## Extended description
Typically, network on chips (NoC) have many internal resources that are shared between packets from different trust domains. These resources include internal buffers, crossbars and switches, individual ports, and channels. The sharing of resources causes contention and introduces interference between differently trusted domains, which poses a security threat via a timing channel, allowing attackers to infer data that belongs to a trusted agent. This may also result in introducing network interference, resulting in degraded throughput and latency.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Security Hardware, Not Technology-Specific

## Common consequences
- **Confidentiality, Availability**: DoS: Resource Consumption (Other), Varies by Context, Other

## Potential mitigations
- **Architecture and Design, Implementation**: Implement priority-based arbitration inside the NoC and have dedicated buffers or virtual channels for routing secret data from trusted agents.

## Related attack patterns (CAPEC)
- [CAPEC-124](https://capec.mitre.org/data/definitions/124.html)

## Related weaknesses
- CWE-653 (ChildOf)
- CWE-668 (ChildOf)
- CWE-1189 (PeerOf)

## Observed examples (CVE)
- **CVE-2021-33096**: Improper isolation of shared resource in a network-on-chip leads to denial of service

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1331.html
