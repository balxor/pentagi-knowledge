---
capec_id: CAPEC-79
name: Using Slashes in Alternate Encoding
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-173, CWE-180, CWE-181, CWE-20, CWE-74, CWE-73, CWE-22, CWE-185, CWE-200, CWE-697, CWE-707]
related_attack: []
url: https://capec.mitre.org/data/definitions/79.html
tags: [mitre-capec, attack-pattern, CAPEC-79]
---

# CAPEC-79 - Using Slashes in Alternate Encoding

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-79](https://capec.mitre.org/data/definitions/79.html)

## Description
This attack targets the encoding of the Slash characters. An adversary would try to exploit common filtering problems related to the use of the slashes characters to gain access to resources on the target host. Directory-driven systems, such as file systems and databases, typically use the slash character to indicate traversal between directories or other container components. For murky historical reasons, PCs (and, as a result, Microsoft OSs) choose to use a backslash, whereas the UNIX world typically makes use of the forward slash. The schizophrenic result is that many MS-based systems are required to understand both forms of the slash. This gives the adversary many opportunities to discover and abuse a number of common filtering problems. The goal of this pattern is to discover server software that only applies filters to one version, but not the other.

## Prerequisites
- The application server accepts paths to locate resources.
- The application server does insufficient input data validation on the resource path requested by the user.
- The access right to resources are not set properly.

## Skills required
- **Low**: An adversary can try variation of the slashes characters.
- **Medium**: An adversary can use more sophisticated tool or script to scan a website and find a path filtering problem.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Read Data, Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs: Using a browser, an automated tool or by inspecting the application, an adversary records all entry points to the application. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters in the URL. Use a proxy tool to record all user input entry points visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Manually inspect the application to find entry points. Experiment Probe entry points to locate vulnerabilities: The adversary uses the entry points gathered in the "Explore" phase as a target list and looks for areas where user input is used to access resources on the target host. The adversary attempts different encodings of slash characters to bypass input filters. Techniques Try both backslash and forward slash characters Try different encodings for slash characters such as %5C Exploit Traverse application directories: Once the adversary determines how to bypass filters that filter out slash characters, they will manipulate the user input to include slashes in order to traverse directories and access resources that are not intended for the user.

## Mitigations
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process. Refer to the RFCs to safely decode URL.
- When client input is required from web-based forms, avoid using the "GET" method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the "POST method whenever possible.
- There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx)
- Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding. (See related guideline section)
- Test your path decoding process against malicious input.
- In the case of path traversals, use the principle of least privilege when determining access rights to file systems. Do not allow users to access directories/files that they should not access.
- Assume all input is malicious. Create an allowlist that defines all valid input to the application based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.

## Related weaknesses (CWE)
- [CWE-173](https://cwe.mitre.org/data/definitions/173.html)
- [CWE-180](https://cwe.mitre.org/data/definitions/180.html)
- [CWE-181](https://cwe.mitre.org/data/definitions/181.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-73](https://cwe.mitre.org/data/definitions/73.html)
- [CWE-22](https://cwe.mitre.org/data/definitions/22.html)
- [CWE-185](https://cwe.mitre.org/data/definitions/185.html)
- [CWE-200](https://cwe.mitre.org/data/definitions/200.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)
- [CWE-707](https://cwe.mitre.org/data/definitions/707.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/79.html
