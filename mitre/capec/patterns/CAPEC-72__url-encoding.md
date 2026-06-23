---
capec_id: CAPEC-72
name: URL Encoding
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-173, CWE-177, CWE-172, CWE-73, CWE-74, CWE-20]
related_attack: []
url: https://capec.mitre.org/data/definitions/72.html
tags: [mitre-capec, attack-pattern, CAPEC-72]
---

# CAPEC-72 - URL Encoding

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-72](https://capec.mitre.org/data/definitions/72.html)

## Description
This attack targets the encoding of the URL. An adversary can take advantage of the multiple way of encoding an URL and abuse the interpretation of the URL.

## Extended description
A URL may contain special character that need special syntax handling in order to be interpreted. Special characters are represented using a percentage character followed by two digits representing the octet code of the original character (%HEX-CODE). For instance US-ASCII space character would be represented with %20. This is often referred as escaped ending or percent-encoding. Since the server decodes the URL from the requests, it may restrict the access to some URL paths by validating and filtering out the URL requests it received. An adversary will try to craft an URL with a sequence of special characters which once interpreted by the server will be equivalent to a forbidden URL. It can be difficult to protect against this attack since the URL can contain other format of encoding such as UTF-8 encoding, Unicode-encoding, etc. The adversary could also subvert the meaning of the URL string request by encoding the data being sent to the server through a GET request. For instance an adversary may subvert the meaning of parameters used in a SQL request and sent through the URL string (See Example section).

## Prerequisites
- The application should accepts and decodes URL input.
- The application performs insufficient filtering/canonicalization on the URLs.

## Skills required
- **Low**: An adversary can try special characters in the URL and bypass the URL validation.
- **Medium**: The adversary may write a script to defeat the input filtering mechanism.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Resource Consumption (Denial of Service), Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Read Data, Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Survey web application for URLs with parameters: Using a browser, an automated tool or by inspecting the application, an adversary records all URLs that contain parameters. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters in the URL. Experiment Probe URLs to locate vulnerabilities: The adversary uses the URLs gathered in the "Explore" phase as a target list and tests parameters with different encodings of special characters to see how the web application will handle them. Techniques Use URL encodings of special characters such as semi-colons, backslashes, or question marks that might be filtered out normally. Combine the use of URL encodings with other encoding techniques such as the triple dot and escape slashes. Exploit Inject special characters into URL parameters: Using the information gathered in the "Experiment" phase, the adversary injects special characters into the URL using URL encoding. This can lead to path traversal, cross-site scripting, SQL injection, etc.

## Mitigations
- Refer to the RFCs to safely decode URL.
- Regular expression can be used to match safe URL patterns. However, that may discard valid URL requests if the regular expression is too restrictive.
- There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx).
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system. Test your decoding process against malicious input.
- Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding. (See related guideline section)
- When client input is required from web-based forms, avoid using the "GET" method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the "POST method whenever possible.

## Related weaknesses (CWE)
- [CWE-173](https://cwe.mitre.org/data/definitions/173.html)
- [CWE-177](https://cwe.mitre.org/data/definitions/177.html)
- [CWE-172](https://cwe.mitre.org/data/definitions/172.html)
- [CWE-73](https://cwe.mitre.org/data/definitions/73.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/72.html
