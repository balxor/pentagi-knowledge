---
capec_id: CAPEC-71
name: Using Unicode Encoding to Bypass Validation Logic
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-176, CWE-179, CWE-180, CWE-173, CWE-172, CWE-184, CWE-183, CWE-74, CWE-20, CWE-697, CWE-692]
related_attack: []
url: https://capec.mitre.org/data/definitions/71.html
tags: [mitre-capec, attack-pattern, CAPEC-71]
---

# CAPEC-71 - Using Unicode Encoding to Bypass Validation Logic

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-71](https://capec.mitre.org/data/definitions/71.html)

## Description
An attacker may provide a Unicode string to a system component that is not Unicode aware and use that to circumvent the filter or cause the classifying mechanism to fail to properly understanding the request. That may allow the attacker to slip malicious data past the content filter and/or possibly cause the application to route the request incorrectly.

## Prerequisites
- Filtering is performed on data that has not be properly canonicalized.

## Skills required
- **Medium**: An attacker needs to understand Unicode encodings and have an idea (or be able to find out) what system components may not be Unicode aware.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Authorization**: Bypass Protection Mechanism
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code), Unreliable Execution
- **Confidentiality**: Bypass Protection Mechanism, Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code), Modify Data

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs: Using a browser or an automated tool, an attacker follows all public links and actions on a web site. They record all the links, the forms, the resources accessed and all other potential entry-points for the web application. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters in the URL. Use a proxy tool to record all user input entry points visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Experiment Probe entry points to locate vulnerabilities: The attacker uses the entry points gathered in the "Explore" phase as a target list and injects various Unicode encoded payloads to determine if an entry point actually represents a vulnerability with insufficient validation logic and to characterize the extent to which the vulnerability can be exploited. Techniques Try to use Unicode encoding of content in Scripts in order to bypass validation routines. Try to use Unicode encoding of content in HTML in order to bypass validation routines. Try to use Unicode encoding of content in CSS in order to bypass validation routines.

## Mitigations
- Ensure that the system is Unicode aware and can properly process Unicode data. Do not make an assumption that data will be in ASCII.
- Ensure that filtering or input validation is applied to canonical data.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.

## Related weaknesses (CWE)
- [CWE-176](https://cwe.mitre.org/data/definitions/176.html)
- [CWE-179](https://cwe.mitre.org/data/definitions/179.html)
- [CWE-180](https://cwe.mitre.org/data/definitions/180.html)
- [CWE-173](https://cwe.mitre.org/data/definitions/173.html)
- [CWE-172](https://cwe.mitre.org/data/definitions/172.html)
- [CWE-184](https://cwe.mitre.org/data/definitions/184.html)
- [CWE-183](https://cwe.mitre.org/data/definitions/183.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)
- [CWE-692](https://cwe.mitre.org/data/definitions/692.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/71.html
