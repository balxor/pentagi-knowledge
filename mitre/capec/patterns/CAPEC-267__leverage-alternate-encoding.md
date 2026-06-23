---
capec_id: CAPEC-267
name: Leverage Alternate Encoding
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-173, CWE-172, CWE-180, CWE-181, CWE-73, CWE-74, CWE-20, CWE-697, CWE-692]
related_attack: [T1027]
url: https://capec.mitre.org/data/definitions/267.html
tags: [mitre-capec, attack-pattern, CAPEC-267]
---

# CAPEC-267 - Leverage Alternate Encoding

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-267](https://capec.mitre.org/data/definitions/267.html)

## Description
An adversary leverages the possibility to encode potentially harmful input or content used by applications such that the applications are ineffective at validating this encoding standard.

## Prerequisites
- The application's decoder accepts and interprets encoded characters. Data canonicalization, input filtering and validating is not done properly leaving the door open to harmful characters for the target host.

## Skills required
- **Low**: An adversary can inject different representation of a filtered character in a different encoding.
- **Medium**: An adversary may craft subtle encoding of input data by using the knowledge that they have gathered about the target host.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Accountability**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges, Bypass Protection Mechanism
- **Availability**: Unreliable Execution (Denial of Service), Resource Consumption (Denial of Service)
- **Confidentiality**: Read Data
- **Integrity**: Modify Data
- **Non-Repudiation**: Gain Privileges

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs: Using a browser, an automated tool or by inspecting the application, an adversary records all entry points to the application. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters in the URL. Use a proxy tool to record all user input entry points visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Manually inspect the application to find entry points. Experiment Probe entry points to locate vulnerabilities: The adversary uses the entry points gathered in the "Explore" phase as a target list and injects various payloads using a variety of different types of encodings to determine if an entry point actually represents a vulnerability with insufficient validation logic and to characterize the extent to which the vulnerability can be exploited. Techniques Try to use different encodings of content in order to bypass validation routines.

## Mitigations
- Assume all input might use an improper representation. Use canonicalized data inside the application; all data must be converted into the representation used inside the application (UTF-8, UTF-16, etc.)
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system. Test your decoding process against malicious input.

## Related weaknesses (CWE)
- [CWE-173](https://cwe.mitre.org/data/definitions/173.html)
- [CWE-172](https://cwe.mitre.org/data/definitions/172.html)
- [CWE-180](https://cwe.mitre.org/data/definitions/180.html)
- [CWE-181](https://cwe.mitre.org/data/definitions/181.html)
- [CWE-73](https://cwe.mitre.org/data/definitions/73.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)
- [CWE-692](https://cwe.mitre.org/data/definitions/692.html)

## Related ATT&CK techniques
- T1027

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/267.html
