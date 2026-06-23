---
capec_id: CAPEC-87
name: Forceful Browsing
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-425, CWE-285, CWE-693]
related_attack: []
url: https://capec.mitre.org/data/definitions/87.html
tags: [mitre-capec, attack-pattern, CAPEC-87]
---

# CAPEC-87 - Forceful Browsing

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-87](https://capec.mitre.org/data/definitions/87.html)

## Description
An attacker employs forceful browsing (direct URL entry) to access portions of a website that are otherwise unreachable. Usually, a front controller or similar design pattern is employed to protect access to portions of a web application. Forceful browsing enables an attacker to access information, perform privileged operations and otherwise reach sections of the web application that have been improperly protected.

## Prerequisites
- The forcibly browseable pages or accessible resources must be discoverable and improperly protected.

## Skills required
- **Low**: Forcibly browseable pages can be discovered by using a number of automated tools. Doing the same manually is tedious but by no means difficult.

## Resources required
- None: No specialized resources are required to execute this type of attack. A directory listing is helpful, but not a requirement.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Authorization**: Bypass Protection Mechanism
- **Confidentiality**: Read Data, Bypass Protection Mechanism

## Execution flow
Execution Flow Explore Spider: Using an automated tool, an attacker follows all public links on a web site. They record all the links they find. Techniques Use a spidering tool to follow and record all links. Use a proxy tool to record all links visited during a manual traversal of the web application. Experiment Attempt well-known or guessable resource locations: Using an automated tool, an attacker requests a variety of well-known URLs that correspond to administrative, debugging, or other useful internal actions. They record all the positive responses from the server. Techniques Use a spidering tool to follow and record attempts on well-known URLs. Use a proxy tool to record all links visited during a manual traversal of attempts on well-known URLs. Exploit Use unauthorized resources: By visiting the unprotected resource, the attacker makes use of unauthorized functionality. Techniques Access unprotected functions and execute them. View unauthorized data: The attacker discovers and views unprotected sensitive data. Techniques Direct request of protected pages that directly access database back-ends. (e.g., list.jsp, accounts.jsp, status.jsp, etc.)

## Mitigations
- Authenticate request to every resource. In addition, every page or resource must ensure that the request it is handling has been made in an authorized context.
- Forceful browsing can also be made difficult to a large extent by not hard-coding names of application pages or resources. This way, the attacker cannot figure out, from the application alone, the resources available from the present context.

## Related weaknesses (CWE)
- [CWE-425](https://cwe.mitre.org/data/definitions/425.html)
- [CWE-285](https://cwe.mitre.org/data/definitions/285.html)
- [CWE-693](https://cwe.mitre.org/data/definitions/693.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/87.html
