---
cwe_id: CWE-400
name: Uncontrolled Resource Consumption
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, AI/ML]
related_capec: [CAPEC-147, CAPEC-227, CAPEC-492]
url: https://cwe.mitre.org/data/definitions/400.html
tags: [mitre-cwe, weakness, CWE-400]
---

# CWE-400 - Uncontrolled Resource Consumption

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-400](https://cwe.mitre.org/data/definitions/400.html)

## Description
The product does not properly control the allocation and maintenance of a limited resource.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, AI/ML

## Common consequences
- **Availability**: DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Resource Consumption (Other)
- **Access Control, Other**: Bypass Protection Mechanism, Other

## Potential mitigations
- **Architecture and Design**: Design throttling mechanisms into the system architecture. The best protection is to limit the amount of resources that an unauthorized user can cause to be expended. A strong authentication and access control model will help prevent such attacks from occurring in the first place. The login application should be protected against DoS attacks as much as possible. Limiting the database access, perhaps by caching result sets, can help minimize the resources expended. To further limit the potential for a DoS attack, consider tracking the rate of requests received from users and blocking requests that exceed a defined rate threshold.
- **Architecture and Design**: Mitigation of resource exhaustion attacks requires that the target system either: recognizes the attack and denies that user further access for a given amount of time, or uniformly throttles all requests in order to make it more difficult to consume resources more quickly than they can again be freed. The first of these solutions is an issue in itself though, since it may allow attackers to prevent the use of the system by a particular valid user. If the attacker impersonates the valid user, they may be able to prevent the user from accessing the server in question. The second solution is simply difficult to effectively institute -- and even when properly done, it does not provide a full solution. It simply makes the attack require more resources on the part of the attacker.
- **Architecture and Design**: Ensure that protocols have specific limits of scale placed on them.
- **Implementation**: Ensure that all failures in resource allocation place the system into a safe posture.

## Related attack patterns (CAPEC)
- [CAPEC-147](https://capec.mitre.org/data/definitions/147.html)
- [CAPEC-227](https://capec.mitre.org/data/definitions/227.html)
- [CAPEC-492](https://capec.mitre.org/data/definitions/492.html)

## Related weaknesses
- CWE-664 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-19911**: Chain: Python library does not limit the resources used to process images that specify a very large number of bands (CWE-1284), leading to excessive memory consumption (CWE-789) or an integer overflow (CWE-190).
- **CVE-2020-7218**: Go-based workload orchestrator does not limit resource usage with unauthenticated connections, allowing a DoS by flooding the service
- **CVE-2020-3566**: Resource exhaustion in distributed OS because of "insufficient" IGMP queue management, as exploited in the wild per CISA KEV.
- **CVE-2009-2874**: Product allows attackers to cause a crash via a large number of connections.
- **CVE-2009-1928**: Malformed request triggers uncontrolled recursion, leading to stack exhaustion.
- **CVE-2009-2858**: Chain: memory leak (CWE-404) leads to resource exhaustion.
- **CVE-2009-2726**: Driver does not use a maximum width when invoking sscanf style functions, causing stack consumption.
- **CVE-2009-2540**: Large integer value for a length property in an object causes a large amount of memory allocation.
- **CVE-2009-2299**: Web application firewall consumes excessive memory when an HTTP request contains a large Content-Length value but no POST data.
- **CVE-2009-2054**: Product allows exhaustion of file descriptors when processing a large number of TCP packets.
- **CVE-2008-5180**: Communication product allows memory consumption with a large number of SIP requests, which cause many sessions to be created.
- **CVE-2008-2121**: TCP implementation allows attackers to consume CPU and prevent new connections using a TCP SYN flood attack.
- **CVE-2008-2122**: Port scan triggers CPU consumption with processes that attempt to read data from closed sockets.
- **CVE-2008-1700**: Product allows attackers to cause a denial of service via a large number of directives, each of which opens a separate window.
- **CVE-2007-4103**: Product allows resource exhaustion via a large number of calls that do not complete a 3-way handshake.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/400.html
