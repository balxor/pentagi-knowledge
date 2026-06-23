---
capec_id: CAPEC-301
name: TCP Connect Scan
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/301.html
tags: [mitre-capec, attack-pattern, CAPEC-301]
---

# CAPEC-301 - TCP Connect Scan

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-301](https://capec.mitre.org/data/definitions/301.html)

## Description
An adversary uses full TCP connection attempts to determine if a port is open on the target system. The scanning process involves completing a 'three-way handshake' with a remote port, and reports the port as closed if the full handshake cannot be established. An advantage of TCP connect scanning is that it works against any TCP/IP stack.

## Extended description
RFC 793 defines how TCP connections are established and torn down. TCP connect scanning commonly involves establishing a full connection, and then subsequently tearing it down, and therefore involves sending a significant number of packets to each port that is scanned. Compared to other types of scans, a TCP Connect scan is slow and methodical. This type of scanning causes considerable noise in system logs and can be spotted by IDS/IPS systems. TCP Connect scanning can detect when a port is open by completing the three-way handshake, but it cannot distinguish a port that is unfiltered with no service running on it from a port that is filtered by a firewall but contains an active service. Due to the significant volume of packets exchanged per port, TCP connect scanning can become very time consuming (performing a full TCP connect scan against a host can take multiple days). Generally, it is not used as a method for performing a comprehensive port scan, but is reserved for checking a short list of common ports.

## Prerequisites
- The adversary requires logical access to the target network. The TCP connect Scan requires the ability to connect to an available port and complete a 'three-way-handshake' This scanning technique does not require any special privileges in order to perform. This type of scan works against all TCP/IP stack implementations.

## Resources required
- The adversary can leverage a network mapper or scanner, or perform this attack via routine socket programming in a scripting language. Packet injection tools are also useful for this purpose. Depending upon the method used it may be necessary to sniff the network to see the response.

## Consequences
- **Confidentiality**: Read Data

## Execution flow
Execution Flow Experiment An adversary attempts to initialize a TCP connection with with the target port. An adversary uses the result of their TCP connection to determine the state of the target port. A successful connection indicates a port is open with a service listening on it while a failed connection indicates the port is not open.

## Mitigations
- Employ a robust network defense posture that includes an IDS/IPS system.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/301.html
