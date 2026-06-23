---
capec_id: CAPEC-4
name: Using Alternative IP Address Encodings
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-291, CWE-173]
related_attack: []
url: https://capec.mitre.org/data/definitions/4.html
tags: [mitre-capec, attack-pattern, CAPEC-4]
---

# CAPEC-4 - Using Alternative IP Address Encodings

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-4](https://capec.mitre.org/data/definitions/4.html)

## Description
This attack relies on the adversary using unexpected formats for representing IP addresses. Networked applications may expect network location information in a specific format, such as fully qualified domains names (FQDNs), URL, IP address, or IP Address ranges. If the location information is not validated against a variety of different possible encodings and formats, the adversary can use an alternate format to bypass application access control.

## Prerequisites
- The target software must fail to anticipate all of the possible valid encodings of an IP/web address.
- The adversary must have the ability to communicate with the server.

## Skills required
- **Low**: The adversary has only to try IP address format combinations.

## Resources required
- The adversary needs to have knowledge of an alternative IP address encoding that bypasses the access control policy of an application. Alternatively, the adversary can simply try to brute-force various encoding possibilities.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges

## Execution flow
Execution Flow Explore Survey the application for IP addresses as user input: Using a browser, an automated tool or by inspecting the application, an adversary records all entry points to the application where IP addresses are used. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters in the URL. Use a proxy tool to record all user input entry points visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Manually inspect the application to find entry points. Experiment Probe entry points to locate vulnerabilities: The adversary uses the entry points gathered in the "Explore" phase as a target list and attempts alternate IP address encodings, observing application behavior. The adversary will also attempt to access the application through an alternate IP address encoding to see if access control changes Techniques Instead of using a URL, use the IP address that the URL resolves to Specify a port directly to a URL input Omit or add "http://" or "https://" to a URL to see if the application behaves differently Exploit Bypass access control: Using an alternate IP address encoding, the adversary will either access the application or give the alternate encoding as input, bypassing access control restrictions.

## Mitigations
- Design: Default deny access control policies
- Design: Input validation routines should check and enforce both input data types and content against a positive specification. In regards to IP addresses, this should include the authorized manner for the application to represent IP addresses and not accept user specified IP addresses and IP address formats (such as ranges)
- Implementation: Perform input validation for all remote content.

## Related weaknesses (CWE)
- [CWE-291](https://cwe.mitre.org/data/definitions/291.html)
- [CWE-173](https://cwe.mitre.org/data/definitions/173.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/4.html
