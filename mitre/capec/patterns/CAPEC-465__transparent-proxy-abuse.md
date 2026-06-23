---
capec_id: CAPEC-465
name: Transparent Proxy Abuse
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: [CWE-441]
related_attack: [T1090.001]
url: https://capec.mitre.org/data/definitions/465.html
tags: [mitre-capec, attack-pattern, CAPEC-465]
---

# CAPEC-465 - Transparent Proxy Abuse

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-465](https://capec.mitre.org/data/definitions/465.html)

## Description
A transparent proxy serves as an intermediate between the client and the internet at large. It intercepts all requests originating from the client and forwards them to the correct location. The proxy also intercepts all responses to the client and forwards these to the client. All of this is done in a manner transparent to the client.

## Extended description
Transparent proxies are often used by enterprises and ISPs. For requests originating at the client transparent proxies need to figure out the final destination of the client's data packet. Two ways are available to do that: either by looking at the layer three (network) IP address or by examining layer seven (application) HTTP header destination. A browser has same origin policy that typically prevents scripts coming from one domain initiating requests to other websites from which they did not come. To circumvent that, however, malicious Flash or an Applet that is executing in the user's browser can attempt to create a cross-domain socket connection from the client to the remote domain. The transparent proxy will examine the HTTP header of the request and direct it to the remote site thereby partially bypassing the browser's same origin policy. This can happen if the transparent proxy uses the HTTP host header information for addressing rather than the IP address information at the network layer. This attack allows malicious scripts inside the victim's browser to issue cross-domain requests to any hosts accessible to the transparent proxy.

## Prerequisites
- Transparent proxy is usedVulnerable configuration of network topology involving the transparent proxy (e.g., no NAT happening between the client and the proxy)Execution of malicious Flash or Applet in the victim's browser

## Skills required
- **Medium**: Creating malicious Flash or Applet to open a cross-domain socket connection to a remote system

## Mitigations
- Design: Ensure that the transparent proxy uses an actual network layer IP address for routing requests. On the transparent proxy, disable the use of routing based on address information in the HTTP host header.
- Configuration: Disable in the browser the execution of Java Script, Flash, SilverLight, etc.

## Related weaknesses (CWE)
- [CWE-441](https://cwe.mitre.org/data/definitions/441.html)

## Related ATT&CK techniques
- T1090.001

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/465.html
