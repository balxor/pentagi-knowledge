---
capec_id: CAPEC-207
name: Removing Important Client Functionality
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: High
related_cwe: [CWE-602]
related_attack: []
url: https://capec.mitre.org/data/definitions/207.html
tags: [mitre-capec, attack-pattern, CAPEC-207]
---

# CAPEC-207 - Removing Important Client Functionality

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-207](https://capec.mitre.org/data/definitions/207.html)

## Description
An adversary removes or disables functionality on the client that the server assumes to be present and trustworthy.

## Extended description
Adversaries can, in some cases, get around logic put in place to 'guard' sensitive functionality or data. Client applications may include functionality that a server relies on for correct and secure operation. This functionality can include, but is not limited to, filters to prevent the sending of dangerous content to the server, logical functionality such as price calculations, and authentication logic to ensure that only authorized users are utilizing the client. If an adversary can disable this functionality on the client, they can perform actions that the server believes are prohibited. This can result in client behavior that violates assumptions by the server leading to a variety of possible attacks. In the above examples, this could include the sending of dangerous content (such as scripts) to the server, incorrect price calculations, or unauthorized access to server resources.

## Prerequisites
- The targeted server must assume the client performs important actions to protect the server or the server functionality. For example, the server may assume the client filters outbound traffic or that the client performs all price calculations correctly. Moreover, the server must fail to detect when these assumptions are violated by a client.

## Skills required
- **High**: To reverse engineer the client-side code to disable/remove the functionality on the client that the server relies on.
- **Low**: The adversary installs a web tool that allows scripts or the DOM model of web-based applications to be modified before they are executed in a browser. GreaseMonkey and Firebug are two examples of such tools.

## Resources required
- The adversary must have access to a client and be able to modify the client behavior, often through reverse engineering. If the server is assuming specific client functionality, this usually means the server only recognizes a specific client application, rather than a broad class of client applications. Reverse engineering tools would likely be necessary.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Accountability**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Gain Privileges, Bypass Protection Mechanism
- **Confidentiality**: Other (Information Leakage), Read Data
- **Integrity**: Modify Data
- **Non-Repudiation**: Gain Privileges

## Execution flow
Execution Flow Explore Probing: The adversary probes, through brute-forcing, reverse-engineering or other similar means, the functionality on the client that server assumes to be present and trustworthy. Techniques The adversary probes by exploring an application's functionality and its underlying mapping to server-side components. The adversary reverse engineers client-side code to identify the functionality that the server relies on for the proper or secure operation. Experiment Determine which functionality to disable or remove: The adversary tries to determine which functionality to disable or remove through reverse-engineering from the list of functionality identified in the Explore phase. Techniques The adversary reverse engineers the client-side code to determine which functionality to disable or remove. Exploit Disable or remove the critical functionality from the client code: Once the functionality has been determined, the adversary disables or removes the critical functionality from the client code to perform malicious actions that the server believes are prohibited. Techniques The adversary disables or removes the functionality from the client-side code to perform malicious actions, such as sending of dangerous content (such as scripts) to the server.

## Mitigations
- Design: For any security checks that are performed on the client side, ensure that these checks are duplicated on the server side.
- Design: Ship client-side application with integrity checks (code signing) when possible.
- Design: Use obfuscation and other techniques to prevent reverse engineering the client code.

## Related weaknesses (CWE)
- [CWE-602](https://cwe.mitre.org/data/definitions/602.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/207.html
