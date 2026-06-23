---
cwe_id: CWE-1264
name: Hardware Logic with Insecure De-Synchronization between Control and Data Channels
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: [CAPEC-233, CAPEC-663]
url: https://cwe.mitre.org/data/definitions/1264.html
tags: [mitre-cwe, weakness, CWE-1264]
---

# CWE-1264 - Hardware Logic with Insecure De-Synchronization between Control and Data Channels

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1264](https://cwe.mitre.org/data/definitions/1264.html)

## Description
The hardware logic for error handling and security checks can incorrectly forward data before the security check is complete.

## Extended description
Many high-performance on-chip bus protocols and processor data-paths employ separate channels for control and data to increase parallelism and maximize throughput. Bugs in the hardware logic that handle errors and security checks can make it possible for data to be forwarded before the completion of the security checks. If the data can propagate to a location in the hardware observable to an attacker, loss of data confidentiality can occur. 'Meltdown' is a concrete example of how de-synchronization between data and permissions checking logic can violate confidentiality requirements. Data loaded from a page marked as privileged was returned to the CPU regardless of current privilege level for performance reasons. The assumption was that the CPU could later remove all traces of this data during the handling of the illegal memory access exception, but this assumption was proven false as traces of the secret data were not removed from the microarchitectural state.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Memory, Read Application Data

## Potential mitigations
- **Architecture and Design**: Thoroughly verify the data routing logic to ensure that any error handling or security checks effectively block illegal dataflows.

## Related attack patterns (CAPEC)
- [CAPEC-233](https://capec.mitre.org/data/definitions/233.html)
- [CAPEC-663](https://capec.mitre.org/data/definitions/663.html)

## Related weaknesses
- CWE-821 (ChildOf)
- CWE-1037 (PeerOf)

## Observed examples (CVE)
- **CVE-2017-5754**: Systems with microprocessors utilizing speculative execution and indirect branch prediction may allow unauthorized disclosure of information to an attacker with local user access via a side-channel analysis of the data cache.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1264.html
