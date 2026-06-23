---
capec_id: CAPEC-3
name: Using Leading 'Ghost' Character Sequences to Bypass Input Filters
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Medium
related_cwe: [CWE-173, CWE-41, CWE-172, CWE-179, CWE-180, CWE-181, CWE-183, CWE-184, CWE-20, CWE-74, CWE-697, CWE-707]
related_attack: []
url: https://capec.mitre.org/data/definitions/3.html
tags: [mitre-capec, attack-pattern, CAPEC-3]
---

# CAPEC-3 - Using Leading 'Ghost' Character Sequences to Bypass Input Filters

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-3](https://capec.mitre.org/data/definitions/3.html)

## Description
Some APIs will strip certain leading characters from a string of parameters. An adversary can intentionally introduce leading "ghost" characters (extra characters that don't affect the validity of the request at the API layer) that enable the input to pass the filters and therefore process the adversary's input. This occurs when the targeted API will accept input data in several syntactic forms and interpret it in the equivalent semantic way, while the filter does not take into account the full spectrum of the syntactic forms acceptable to the targeted API.

## Prerequisites
- The targeted API must ignore the leading ghost characters that are used to get past the filters for the semantics to be the same.

## Skills required
- **Medium**: The ability to make an API request, and knowledge of "ghost" characters that will not be filtered by any input validation. These "ghost" characters must be known to not affect the way in which the request will be interpreted.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs: Using a browser, an automated tool or by inspecting the application, an adversary records all entry points to the application. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters in the URL. Use a proxy tool to record all user input entry points visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Manually inspect the application to find entry points. Experiment Probe entry points to locate vulnerabilities: The adversary uses the entry points gathered in the "Explore" phase as a target list and injects various leading 'Ghost' character sequences to determine how to application filters them. Techniques Add additional characters to common sequences such as "../" to see how the application will filter them. Try repeating special characters (?, @, #, *, etc.) at the beginning of user input to see how the application filters these out. Exploit Bypass input filtering: Using what the adversary learned about how the application filters input data, they craft specific input data that bypasses the filter. This can lead to directory traversal attacks, arbitrary shell command execution, corruption of files, etc.

## Mitigations
- Use an allowlist rather than a denylist input validation.
- Canonicalize all data prior to validation.
- Take an iterative approach to input validation (defense in depth).

## Related weaknesses (CWE)
- [CWE-173](https://cwe.mitre.org/data/definitions/173.html)
- [CWE-41](https://cwe.mitre.org/data/definitions/41.html)
- [CWE-172](https://cwe.mitre.org/data/definitions/172.html)
- [CWE-179](https://cwe.mitre.org/data/definitions/179.html)
- [CWE-180](https://cwe.mitre.org/data/definitions/180.html)
- [CWE-181](https://cwe.mitre.org/data/definitions/181.html)
- [CWE-183](https://cwe.mitre.org/data/definitions/183.html)
- [CWE-184](https://cwe.mitre.org/data/definitions/184.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)
- [CWE-707](https://cwe.mitre.org/data/definitions/707.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/3.html
