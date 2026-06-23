---
capec_id: CAPEC-469
name: HTTP DoS
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Low
related_cwe: [CWE-770, CWE-772]
related_attack: [T1499.002]
url: https://capec.mitre.org/data/definitions/469.html
tags: [mitre-capec, attack-pattern, CAPEC-469]
---

# CAPEC-469 - HTTP DoS

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Low  -  **CAPEC:** [CAPEC-469](https://capec.mitre.org/data/definitions/469.html)

## Description
An attacker performs flooding at the HTTP level to bring down only a particular web application rather than anything listening on a TCP/IP connection. This denial of service attack requires substantially fewer packets to be sent which makes DoS harder to detect. This is an equivalent of SYN flood in HTTP. The idea is to keep the HTTP session alive indefinitely and then repeat that hundreds of times. This attack targets resource depletion weaknesses in web server software. The web server will wait to attacker's responses on the initiated HTTP sessions while the connection threads are being exhausted.

## Prerequisites
- HTTP protocol is usedWeb server used is vulnerable to denial of service via HTTP flooding

## Resources required
- Ability to issues hundreds of HTTP requests

## Mitigations
- Configuration: Configure web server software to limit the waiting period on opened HTTP sessions
- Design: Use load balancing mechanisms

## Related weaknesses (CWE)
- [CWE-770](https://cwe.mitre.org/data/definitions/770.html)
- [CWE-772](https://cwe.mitre.org/data/definitions/772.html)

## Related ATT&CK techniques
- T1499.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/469.html
