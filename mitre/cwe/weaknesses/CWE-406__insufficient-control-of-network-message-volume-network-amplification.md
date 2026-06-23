---
cwe_id: CWE-406
name: Insufficient Control of Network Message Volume (Network Amplification)
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/406.html
tags: [mitre-cwe, weakness, CWE-406]
---

# CWE-406 - Insufficient Control of Network Message Volume (Network Amplification)

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-406](https://cwe.mitre.org/data/definitions/406.html)

## Description
The product does not sufficiently monitor or control transmitted network traffic volume, so that an actor can cause the product to transmit more traffic than should be allowed for that actor.

## Extended description
In the absence of a policy to restrict asymmetric resource consumption, the application or system cannot distinguish between legitimate transmissions and traffic intended to serve as an amplifying attack on target systems. Systems can often be configured to restrict the amount of traffic sent out on behalf of a client, based on the client's origin or access level. This is usually defined in a resource allocation policy. In the absence of a mechanism to keep track of transmissions, the system or application can be easily abused to transmit asymmetrically greater traffic than the request or client should be permitted to.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Availability**: DoS: Amplification, DoS: Crash, Exit, or Restart, DoS: Resource Consumption (CPU), DoS: Resource Consumption (Memory), DoS: Resource Consumption (Other)

## Potential mitigations
- **Architecture and Design**: An application must make network resources available to a client commensurate with the client's access level.
- **Policy**: Define a clear policy for network resource allocation and consumption.
- **Implementation**: An application must, at all times, keep track of network resources and meter their usage appropriately.

## Related weaknesses
- CWE-405 (ChildOf)

## Observed examples (CVE)
- **CVE-1999-0513**: Classic "Smurf" attack, using spoofed ICMP packets to broadcast addresses.
- **CVE-1999-1379**: DNS query with spoofed source address causes more traffic to be returned to spoofed address than was sent by the attacker.
- **CVE-2000-0041**: Large datagrams are sent in response to malformed datagrams.
- **CVE-1999-1066**: Game server sends a large amount.
- **CVE-2013-5211**: composite: NTP feature generates large responses (high amplification factor) with spoofed UDP source addresses.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/406.html
