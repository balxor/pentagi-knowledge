---
capec_id: CAPEC-193
name: PHP Remote File Inclusion
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-98, CWE-80]
related_attack: []
url: https://capec.mitre.org/data/definitions/193.html
tags: [mitre-capec, attack-pattern, CAPEC-193]
---

# CAPEC-193 - PHP Remote File Inclusion

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-193](https://capec.mitre.org/data/definitions/193.html)

## Description
In this pattern the adversary is able to load and execute arbitrary code remotely available from the application. This is usually accomplished through an insecurely configured PHP runtime environment and an improperly sanitized "include" or "require" call, which the user can then control to point to any web-accessible file. This allows adversaries to hijack the targeted application and force it to execute their own instructions.

## Prerequisites
- Target application server must allow remote files to be included in the "require", "include", etc. PHP directives
- The adversary must have the ability to make HTTP requests to the target web application.

## Skills required
- **Low**: To inject the malicious payload in a web page
- **Medium**: To bypass filters in the application

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Accountability**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges, Bypass Protection Mechanism
- **Confidentiality**: Read Data
- **Integrity**: Modify Data
- **Non-Repudiation**: Gain Privileges

## Execution flow
Execution Flow Explore Survey application: Using a browser or an automated tool, an adversary follows all public links on a web site. They record all the links they find. Techniques Use a spidering tool to follow and record all links. Make special note of any links that include parameters in the URL. Use a proxy tool to record all links visited during a manual traversal of the web application. Make special note of any links that include parameters in the URL. Manual traversal of this type is frequently necessary to identify forms that are GET method forms rather than POST forms. Use a browser to manually explore the website and analyze how it is constructed. Many browser's plugins are available to facilitate the analysis or automate the URL discovery. Experiment Attempt variations on input parameters: The attack variants make use of a remotely available PHP script that generates a uniquely identifiable output when executed on the target application server. Possibly using an automated tool, an adversary requests variations on the inputs they surveyed before. They send parameters that include variations of payloads which include a reference to the remote PHP script. They record all the responses from the server that include the output of the execution of remote PHP script. Techniques Use a list of probe strings to inject in parameters of known URLs. The probe strings are variants of PHP remote file inclusion payloads which include a reference to the adversary controlled remote PHP script. Use a proxy tool to record results of manual input of remote file inclusion probes in known URLs. Exploit Run arbitrary server-side code: As the adversary succeeds in exploiting the vulnerability, they are able to execute server-side code within the application. The malicious code has virtual access to the same resources as the targeted application. Note that the adversary might include shell code in their script and execute commands on the server under the same privileges as the PHP runtime is running with. Techniques Develop malicious PHP script that is injected through vectors identified during the Experiment Phase and executed by the application server to execute a custom PHP script.

## Mitigations
- Implementation: Perform input validation for all remote content, including remote and user-generated content
- Implementation: Only allow known files to be included (allowlist)
- Implementation: Make use of indirect references passed in URL parameters instead of file names
- Configuration: Ensure that remote scripts cannot be include in the "include" or "require" PHP directives

## Related weaknesses (CWE)
- [CWE-98](https://cwe.mitre.org/data/definitions/98.html)
- [CWE-80](https://cwe.mitre.org/data/definitions/80.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/193.html
