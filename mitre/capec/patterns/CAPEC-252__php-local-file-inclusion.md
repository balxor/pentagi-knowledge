---
capec_id: CAPEC-252
name: PHP Local File Inclusion
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Medium
related_cwe: [CWE-829]
related_attack: []
url: https://capec.mitre.org/data/definitions/252.html
tags: [mitre-capec, attack-pattern, CAPEC-252]
---

# CAPEC-252 - PHP Local File Inclusion

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-252](https://capec.mitre.org/data/definitions/252.html)

## Description
The attacker loads and executes an arbitrary local PHP file on a target machine. The attacker could use this to try to load old versions of PHP files that have known vulnerabilities, to load PHP files that the attacker placed on the local machine during a prior attack, or to otherwise change the functionality of the targeted application in unexpected ways.

## Prerequisites
- The targeted PHP application must have a bug that allows an attacker to control which code file is loaded at some juncture.

## Resources required
- The attacker needs to have enough access to the target application to control the identity of a locally included PHP file.

## Execution flow
Execution Flow Explore Survey application: Using a browser or an automated tool, an adversary follows all public links on a web site. They record all the links they find. The adversary is looking for URLs that show PHP file inclusion is used, which can look something like "http://vulnerable-website/file.php?file=index.php". Techniques Use a spidering tool to follow and record all links. Make special note of any links that include parameters in the URL. Use a proxy tool to record all links visited during a manual traversal of the web application. Make special note of any links that include parameters in the URL. Manual traversal of this type is frequently necessary to identify forms that are GET method forms rather than POST forms. Use a browser to manually explore the website and analyze how it is constructed. Many browser's plugins are available to facilitate the analysis or automate the URL discovery. Experiment Attempt variations on input parameters: Once the adversary finds a vulnerable URL that takes file input, they attempt a variety of path traversal techniques to attempt to get the application to display the contents of a local file, or execute a different PHP file already stored locally on the server. Techniques Use a list of probe strings to inject in parameters of known URLs. The probe strings are variants of path traversal techniques used to include well known files. Use a proxy tool to record results of manual input of local file inclusion probes in known URLs. Exploit Include desired local file: Once the adversary has determined which techniques of path traversal successfully work with the vulnerable PHP application, they will target a specific local file to include. These can be files such as "/etc/passwd", "/etc/shadow", or configuration files for the application that might expose sensitive information.

## Related weaknesses (CWE)
- [CWE-829](https://cwe.mitre.org/data/definitions/829.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/252.html
