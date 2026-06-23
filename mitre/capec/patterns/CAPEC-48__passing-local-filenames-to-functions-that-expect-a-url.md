---
capec_id: CAPEC-48
name: Passing Local Filenames to Functions That Expect a URL
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-241, CWE-706]
related_attack: []
url: https://capec.mitre.org/data/definitions/48.html
tags: [mitre-capec, attack-pattern, CAPEC-48]
---

# CAPEC-48 - Passing Local Filenames to Functions That Expect a URL

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-48](https://capec.mitre.org/data/definitions/48.html)

## Description
This attack relies on client side code to access local files and resources instead of URLs. When the client browser is expecting a URL string, but instead receives a request for a local file, that execution is likely to occur in the browser process space with the browser's authority to local files. The attacker can send the results of this request to the local files out to a site that they control. This attack may be used to steal sensitive authentication data (either local or remote), or to gain system profile information to launch further attacks.

## Prerequisites
- The victim's software must not differentiate between the location and type of reference passed the client software, e.g. browser

## Skills required
- **Medium**: Attacker identifies known local files to exploit

## Consequences
- **Confidentiality**: Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Identify web application URL inputs: Review application inputs to find those that are designed to be URLs. Techniques Manually navigate web site pages to identify URLs. Use automated tools to identify URLs. Experiment Identify URL inputs allowing local access.: Execute test local commands via each URL input to determine which are successful. Techniques Manually execute a local command (such as 'pwd') via the URL inputs. Using an automated tool, test each URL input for weakness. Exploit Execute malicious commands: Using the identified URL inputs that allow local command execution, execute malicious commands. Techniques Execute local commands via the URL input.

## Mitigations
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Ensure all configuration files and resource are either removed or protected when promoting code into production.
- Design: Use browser technologies that do not allow client side scripting.
- Implementation: Perform input validation for all remote content.
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser

## Related weaknesses (CWE)
- [CWE-241](https://cwe.mitre.org/data/definitions/241.html)
- [CWE-706](https://cwe.mitre.org/data/definitions/706.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/48.html
