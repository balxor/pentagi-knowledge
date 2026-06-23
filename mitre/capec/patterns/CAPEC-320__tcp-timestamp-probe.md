---
capec_id: CAPEC-320
name: TCP Timestamp Probe
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/320.html
tags: [mitre-capec, attack-pattern, CAPEC-320]
---

# CAPEC-320 - TCP Timestamp Probe

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Low  -  **CAPEC:** [CAPEC-320](https://capec.mitre.org/data/definitions/320.html)

## Description
This OS fingerprinting probe examines the remote server's implementation of TCP timestamps. Not all operating systems implement timestamps within the TCP header, but when timestamps are used then this provides the attacker with a means to guess the operating system of the target. The attacker begins by probing any active TCP service in order to get response which contains a TCP timestamp. Different Operating systems update the timestamp value using different intervals. This type of analysis is most accurate when multiple timestamp responses are received and then analyzed. TCP timestamps can be found in the TCP Options field of the TCP header.

## Prerequisites
- The ability to monitor and interact with network communications.Access to at least one host, and the privileges to interface with the network interface card.The target OS must support the TCP timestamp option in order to obtain a fingerprint.

## Resources required
- Any type of active probing that involves non-standard packet headers requires the use of raw sockets, which is not available on particular operating systems (Microsoft Windows XP SP 2, for example). Raw socket manipulation on Unix/Linux requires root privileges. A tool capable of sending and receiving packets from a remote system.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Authorization**: Bypass Protection Mechanism
- **Confidentiality**: Read Data, Bypass Protection Mechanism

## Execution flow
Execution Flow Explore Determine if timestamps are present.: The adversary sends a probe packet to the remote host to identify if timestamps are present. Experiment Record and analyze timestamp values.: If the remote host is using timestamp, obtain several timestamps, analyze them and compare them to known values. Techniques The adversary sends several requests and records the timestamp values. The adversary analyzes the timestamp values and determines an average increments per second in the timestamps for the target. The adversary compares this result to a database of known TCP timestamp increments for a possible match.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/320.html
