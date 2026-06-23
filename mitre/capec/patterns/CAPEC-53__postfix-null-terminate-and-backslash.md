---
capec_id: CAPEC-53
name: Postfix, Null Terminate, and Backslash
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-158, CWE-172, CWE-173, CWE-74, CWE-20, CWE-697, CWE-707]
related_attack: []
url: https://capec.mitre.org/data/definitions/53.html
tags: [mitre-capec, attack-pattern, CAPEC-53]
---

# CAPEC-53 - Postfix, Null Terminate, and Backslash

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-53](https://capec.mitre.org/data/definitions/53.html)

## Description
If a string is passed through a filter of some kind, then a terminal NULL may not be valid. Using alternate representation of NULL allows an adversary to embed the NULL mid-string while postfixing the proper data so that the filter is avoided. One example is a filter that looks for a trailing slash character. If a string insertion is possible, but the slash must exist, an alternate encoding of NULL in mid-string may be used.

## Prerequisites
- Null terminators are not properly handled by the filter.

## Skills required
- **Medium**: An adversary needs to understand alternate encodings, what the filter looks for and the data format acceptable to the target API

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Read Data, Gain Privileges
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs: Using a browser, an automated tool or by inspecting the application, an adversary records all entry points to the application. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters in the URL. Use a proxy tool to record all user input entry points visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Manually inspect the application to find entry points. Experiment Probe entry points to locate vulnerabilities: The adversary uses the entry points gathered in the "Explore" phase as a target list and injects postfix null byte(s) followed by a backslash to observe how the application handles them as input. The adversary is looking for areas where user input is placed in the middle of a string, and the null byte causes the application to stop processing the string at the end of the user input. Techniques Try different encodings for null such as \0 or %00 followed by an encoding for the backslash character. Exploit Remove data after null byte(s): After determined entry points that are vulnerable, the adversary places a null byte(s) followed by a backslash such that they bypass an input filter and remove data after the null byte(s) in a way that is beneficial to them. Techniques If the input is a directory as part of a longer file path, add a null byte(s) followed by a backslash at the end of the input to try to traverse to the given directory.

## Mitigations
- Properly handle Null characters. Make sure canonicalization is properly applied. Do not pass Null characters to the underlying APIs.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.

## Related weaknesses (CWE)
- [CWE-158](https://cwe.mitre.org/data/definitions/158.html)
- [CWE-172](https://cwe.mitre.org/data/definitions/172.html)
- [CWE-173](https://cwe.mitre.org/data/definitions/173.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)
- [CWE-707](https://cwe.mitre.org/data/definitions/707.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/53.html
