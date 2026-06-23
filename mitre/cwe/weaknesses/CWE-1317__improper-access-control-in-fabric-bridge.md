---
cwe_id: CWE-1317
name: Improper Access Control in Fabric Bridge
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Processor Hardware, Not Technology-Specific]
related_capec: [CAPEC-122]
url: https://cwe.mitre.org/data/definitions/1317.html
tags: [mitre-cwe, weakness, CWE-1317]
---

# CWE-1317 - Improper Access Control in Fabric Bridge

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1317](https://cwe.mitre.org/data/definitions/1317.html)

## Description
The product uses a fabric bridge for transactions between two Intellectual Property (IP) blocks, but the bridge does not properly perform the expected privilege, identity, or other access control checks between those IP blocks.

## Extended description
In hardware designs, different IP blocks are connected through interconnect-bus fabrics (e.g. AHB and OCP). Within a System on Chip (SoC), the IP block subsystems could be using different bus protocols. In such a case, the IP blocks are then linked to the central bus (and to other IP blocks) through a fabric bridge. Bridges are used as bus-interconnect-routing modules that link different protocols or separate, different segments of the overall SoC interconnect. For overall system security, it is important that the access-control privileges associated with any fabric transaction are consistently maintained and applied, even when they are routed or translated by a fabric bridge. A bridge that is connected to a fabric without security features forwards transactions to the slave without checking the privilege level of the master and results in a weakness in SoC access-control security. The same weakness occurs if a bridge does not check the hardware identity of the transaction received from the slave interface of the bridge.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Processor Hardware, Not Technology-Specific

## Common consequences
- **Confidentiality, Integrity, Access Control, Availability**: DoS: Crash, Exit, or Restart, Bypass Protection Mechanism, Read Memory, Modify Memory

## Potential mitigations
- **Architecture and Design**: Ensure that the design includes provisions for access-control checks in the bridge for both upstream and downstream transactions.
- **Implementation**: Implement access-control checks in the bridge for both upstream and downstream transactions.

## Related attack patterns (CAPEC)
- [CAPEC-122](https://capec.mitre.org/data/definitions/122.html)

## Related weaknesses
- CWE-284 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-6260**: Baseboard Management Controller (BMC) device implements Advanced High-performance Bus (AHB) bridges that do not require authentication for arbitrary read and write access to the BMC's physical address space from the host, and possibly the network [REF-1138].

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1317.html
