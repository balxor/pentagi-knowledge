---
capec_id: CAPEC-307
name: TCP RPC Scan
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Low
related_cwe: [CWE-200]
related_attack: []
url: https://capec.mitre.org/data/definitions/307.html
tags: [mitre-capec, attack-pattern, CAPEC-307]
---

# CAPEC-307 - TCP RPC Scan

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-307](https://capec.mitre.org/data/definitions/307.html)

## Description
An adversary scans for RPC services listing on a Unix/Linux host.

## Extended description
This type of scan can be obtained via native operating system utilities or via port scanners like nmap. When performed by a scanner, an RPC datagram is sent to a list of UDP ports and the response is recorded. Particular types of responses can be indicative of well-known RPC services running on a UDP port. Discovering RPC services gives the adversary potential targets to attack, as some RPC services are insecure by default. Direct RPC scans that bypass portmapper/sunrpc are typically slow compare to other scan types, are easily detected by IPS/IDS systems, and can only detect open ports when an RPC service responds. ICMP diagnostic message responses can help identify closed ports, however filtered and unfiltered ports cannot be identified through TCP RPC scans. There are two general approaches to RPC scanning: One is to use a native operating system utility, or script, to query the portmapper/rpcbind application running on port 111. Portmapper will return a list of registered RPC services. Alternately, one can use a port scanner or script to scan for RPC services directly.

## Prerequisites
- RPC scanning requires no special privileges when it is performed via a native system utility.

## Resources required
- The ability to craft custom RPC datagrams for use during network reconnaissance via native OS utilities or a port scanning tool. By tailoring the bytes injected one can scan for specific RPC-registered services. Depending upon the method used it may be necessary to sniff the network in order to see the response.

## Consequences
- **Access_Control**: Bypass Protection Mechanism, Hide Activities
- **Authorization**: Bypass Protection Mechanism, Hide Activities
- **Confidentiality**: Other, Bypass Protection Mechanism, Hide Activities

## Execution flow
Execution Flow Experiment An adversary sends RCP packets to target ports. An adversary uses the response from the target to determine which, if any, RPC service is running on that port. Responses will vary based on which RPC service is running.

## Mitigations
- Typically, an IDS/IPS system is very effective against this type of attack.

## Related weaknesses (CWE)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/307.html
