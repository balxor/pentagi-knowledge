---
capec_id: CAPEC-326
name: TCP Initial Window Size Probe
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/326.html
tags: [mitre-capec, attack-pattern, CAPEC-326]
---

# CAPEC-326 - TCP Initial Window Size Probe

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Low  -  **CAPEC:** [CAPEC-326](https://capec.mitre.org/data/definitions/326.html)

## Description
This OS fingerprinting probe checks the initial TCP Window size. TCP stacks limit the range of sequence numbers allowable within a session to maintain the "connected" state within TCP protocol logic. The initial window size specifies a range of acceptable sequence numbers that will qualify as a response to an ACK packet within a session. Various operating systems use different Initial window sizes. The initial window size can be sampled by establishing an ordinary TCP connection.

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.

## Resources required
- A tool capable of sending and receiving packets from a remote system.

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Read Data, Bypass Protection Mechanism, Hide Activities

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/326.html
