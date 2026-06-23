---
capec_id: CAPEC-275
name: DNS Rebinding
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Very High
related_cwe: [CWE-350]
related_attack: []
url: https://capec.mitre.org/data/definitions/275.html
tags: [mitre-capec, attack-pattern, CAPEC-275]
---

# CAPEC-275 - DNS Rebinding

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-275](https://capec.mitre.org/data/definitions/275.html)

## Description
An adversary serves content whose IP address is resolved by a DNS server that the adversary controls. After initial contact by a web browser (or similar client), the adversary changes the IP address to which its name resolves, to an address within the target organization that is not publicly accessible. This allows the web browser to examine this internal address on behalf of the adversary.

## Extended description
Web browsers enforce security zones based on DNS names in order to prevent cross-zone disclosure of information. Because the same name resolves to both these IP addresses, browsers will place both IP addresses in the same security zone and allow information to flow between the addresses. This allows adversaries to discover sensitive information about the internal network of an enterprise. If there is a trust relationship between the computer with the targeted browser and the internal machine the adversary identifies, additional attacks are possible. This attack differs from pharming attacks in that the adversary is the legitimate owner of the malicious DNS server and so does not need to compromise behavior of external DNS services.

## Prerequisites
- The target browser must access content server from the adversary controlled DNS name. Web advertisements are often used for this purpose. The target browser must honor the TTL value returned by the adversary and re-resolve the adversary's DNS name after initial contact.

## Skills required
- **Medium**: Setup DNS server and the adversary's web server. Write a malicious script to allow the victim to connect to the web server.

## Resources required
- The adversary must serve some web content that a victim accesses initially. This content must include executable content that queries the adversary's DNS name (to provide the second DNS resolution) and then performs the follow-on attack against the internal system. The adversary also requires a customized DNS server that serves an IP address for their registered DNS name, but which resolves subsequent requests by a single client to addresses internal to that client's network.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Accountability**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges, Bypass Protection Mechanism
- **Confidentiality**: Read Data
- **Integrity**: Modify Data
- **Non-Repudiation**: Gain Privileges

## Execution flow
Execution Flow Explore Identify potential DNS rebinding targets: An adversary publishes content on their own server with their own name and DNS server. Attract HTTP traffic and explore rebinding vulnerabilities in browsers, flash players of old version. Techniques Adversary uses Web advertisements to attract the victim to access adversary's DNS. Explore the versions of web browser or flash players in HTTP request. Experiment Establish initial target access to adversary DNS: The first time the target accesses the adversary's content, the adversary's name must be resolved to an IP address. The adversary's DNS server performs this resolution, providing a short Time-To-Live (TTL) in order to prevent the target from caching the value. Rebind DNS resolution to target address: The target makes a subsequent request to the adversary's content and the adversary's DNS server must again be queried, but this time the DNS server returns an address internal to the target's organization that would not be accessible from an outside source. Determine exploitability of DNS rebinding access to target address: The adversary can then use scripts in the content the target retrieved from the adversary in the original message to exfiltrate data from the named internal addresses. Exploit Access & exfiltrate data within the victim's security zone: The adversary can then use scripts in the content the target retrieved from the adversary in the original message to exfiltrate data from the internal addresses. This allows adversaries to discover sensitive information about the internal network of an enterprise. Techniques Adversary attempts to use victim's browser as an HTTP proxy to other resources inside the target's security zone. This allows two IP addresses placed in the same security zone. Adversary tries to scan and access all internal hosts in victim's local network by sending multiple short-lived IP addresses.

## Mitigations
- Design: IP Pinning causes browsers to record the IP address to which a given name resolves and continue using this address regardless of the TTL set in the DNS response. Unfortunately, this is incompatible with the design of some legitimate sites.
- Implementation: Reject HTTP request with a malicious Host header.
- Implementation: Employ DNS resolvers that prevent external names from resolving to internal addresses.

## Related weaknesses (CWE)
- [CWE-350](https://cwe.mitre.org/data/definitions/350.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/275.html
