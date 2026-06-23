---
cwe_id: CWE-1327
name: Binding to an Unrestricted IP Address
type: weakness
abstraction: Base
status: Incomplete
languages: [Other, Not OS-Specific, Not Architecture-Specific, Web Server, Client Server, Cloud Computing]
related_capec: [CAPEC-1]
url: https://cwe.mitre.org/data/definitions/1327.html
tags: [mitre-cwe, weakness, CWE-1327]
---

# CWE-1327 - Binding to an Unrestricted IP Address

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1327](https://cwe.mitre.org/data/definitions/1327.html)

## Description
The product assigns the address 0.0.0.0 for a database server, a cloud service/instance, or any computing resource that communicates remotely.

## Extended description
When a server binds to the address 0.0.0.0, it allows connections from every IP address on the local machine, effectively exposing the server to every possible network. This might be much broader access than intended by the developer or administrator, who might only be expecting the server to be reachable from a single interface/network.

## Applicable platforms / languages
Other, Not OS-Specific, Not Architecture-Specific, Web Server, Client Server, Cloud Computing

## Common consequences
- **Availability**: DoS: Amplification

## Potential mitigations
- **System Configuration**: Assign IP addresses that are not 0.0.0.0.
- **System Configuration**: Unwanted connections to the configured server may be denied through a firewall or other packet filtering measures.

## Related attack patterns (CAPEC)
- [CAPEC-1](https://capec.mitre.org/data/definitions/1.html)

## Related weaknesses
- CWE-668 (ChildOf)

## Observed examples (CVE)
- **CVE-2023-41742**: cybersecurity product binds to an unrestricted IP address
- **CVE-2022-21947**: Desktop manager for Kubernetes and container management binds a service to 0.0.0.0, allowing users on the network to make requests to a dashboard API.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1327.html
