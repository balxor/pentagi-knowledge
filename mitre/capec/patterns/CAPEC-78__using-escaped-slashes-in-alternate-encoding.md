---
capec_id: CAPEC-78
name: Using Escaped Slashes in Alternate Encoding
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-180, CWE-181, CWE-173, CWE-172, CWE-73, CWE-22, CWE-74, CWE-20, CWE-697, CWE-707]
related_attack: []
url: https://capec.mitre.org/data/definitions/78.html
tags: [mitre-capec, attack-pattern, CAPEC-78]
---

# CAPEC-78 - Using Escaped Slashes in Alternate Encoding

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-78](https://capec.mitre.org/data/definitions/78.html)

## Description
This attack targets the use of the backslash in alternate encoding. An adversary can provide a backslash as a leading character and causes a parser to believe that the next character is special. This is called an escape. By using that trick, the adversary tries to exploit alternate ways to encode the same character which leads to filter problems and opens avenues to attack.

## Prerequisites
- The application accepts the backlash character as escape character.
- The application server does incomplete input data decoding, filtering and validation.

## Skills required
- **Low**: The adversary can naively try backslash character and discover that the target host uses it as escape character.
- **Medium**: The adversary may need deep understanding of the host target in order to exploit the vulnerability. The adversary may also use automated tools to probe for this vulnerability.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Authorization**: Bypass Protection Mechanism
- **Availability**: Resource Consumption (Denial of Service), Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Read Data, Execute Unauthorized Commands (Run Arbitrary Code), Bypass Protection Mechanism
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs: Using a browser, an automated tool or by inspecting the application, an adversary records all entry points to the application. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters in the URL. Use a proxy tool to record all user input entry points visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Manually inspect the application to find entry points. Experiment Probe entry points to locate vulnerabilities: The adversary uses the entry points gathered in the "Explore" phase as a target list and attempts to escape multiple different special characters using a backslash. Techniques Escape a special character with a backslash to bypass input validation. Try different encodings of both the backslash and the special character to see if this bypasses input validation Exploit Manipulate input: Once the adversary determines how to bypass filters that filter out special characters using an escaped slash, they will manipulate the user input in a way that is not intended by the application.

## Mitigations
- Verify that the user-supplied data does not use backslash character to escape malicious characters.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system.
- Be aware of the threat of alternative method of data encoding.
- Regular expressions can be used to filter out backslash. Make sure you decode before filtering and validating the untrusted input data.
- In the case of path traversals, use the principle of least privilege when determining access rights to file systems. Do not allow users to access directories/files that they should not access.
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.
- Avoid making decisions based on names of resources (e.g. files) if those resources can have alternate names.

## Related weaknesses (CWE)
- [CWE-180](https://cwe.mitre.org/data/definitions/180.html)
- [CWE-181](https://cwe.mitre.org/data/definitions/181.html)
- [CWE-173](https://cwe.mitre.org/data/definitions/173.html)
- [CWE-172](https://cwe.mitre.org/data/definitions/172.html)
- [CWE-73](https://cwe.mitre.org/data/definitions/73.html)
- [CWE-22](https://cwe.mitre.org/data/definitions/22.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)
- [CWE-707](https://cwe.mitre.org/data/definitions/707.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/78.html
