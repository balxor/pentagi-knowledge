---
capec_id: CAPEC-117
name: Interception
type: attack-pattern
abstraction: Meta
likelihood: Low
severity: Medium
related_cwe: [CWE-319]
related_attack: []
url: https://capec.mitre.org/data/definitions/117.html
tags: [mitre-capec, attack-pattern, CAPEC-117]
---

# CAPEC-117 - Interception

**Abstraction:** Meta  -  **Likelihood:** Low  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-117](https://capec.mitre.org/data/definitions/117.html)

## Description
An adversary monitors data streams to or from the target for information gathering purposes. This attack may be undertaken to solely gather sensitive information or to support a further attack against the target. This attack pattern can involve sniffing network traffic as well as other types of data streams (e.g. radio). The adversary can attempt to initiate the establishment of a data stream or passively observe the communications as they unfold. In all variants of this attack, the adversary is not the intended recipient of the data stream. In contrast to other means of gathering information (e.g., targeting data leaks), the adversary must actively position themself so as to observe explicit data channels (e.g. network traffic) and read the content. However, this attack differs from a Adversary-In-the-Middle (CAPEC-94) attack, as the adversary does not alter the content of the communications nor forward data to the intended recipient.

## Prerequisites
- The target must transmit data over a medium that is accessible to the adversary.

## Resources required
- The adversary must have the necessary technology to intercept information passing between the nodes of a network. For TCP/IP, the capability to run tcpdump, ethereal, etc. can be useful. Depending upon the data being targeted the technological requirements will change.

## Consequences
- **Confidentiality**: Read Data

## Mitigations
- Leverage encryption to encode the transmission of data thus making it accessible only to authorized parties.

## Related weaknesses (CWE)
- [CWE-319](https://cwe.mitre.org/data/definitions/319.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/117.html
