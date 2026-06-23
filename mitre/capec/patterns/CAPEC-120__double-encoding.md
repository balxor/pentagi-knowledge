---
capec_id: CAPEC-120
name: Double Encoding
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: Medium
related_cwe: [CWE-173, CWE-172, CWE-177, CWE-181, CWE-183, CWE-184, CWE-74, CWE-20, CWE-697, CWE-692]
related_attack: []
url: https://capec.mitre.org/data/definitions/120.html
tags: [mitre-capec, attack-pattern, CAPEC-120]
---

# CAPEC-120 - Double Encoding

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-120](https://capec.mitre.org/data/definitions/120.html)

## Description
The adversary utilizes a repeating of the encoding process for a set of characters (that is, character encoding a character encoding of a character) to obfuscate the payload of a particular request. This may allow the adversary to bypass filters that attempt to detect illegal characters or strings, such as those that might be used in traversal or injection attacks. Filters may be able to catch illegal encoded strings, but may not catch doubly encoded strings. For example, a dot (.), often used in path traversal attacks and therefore often blocked by filters, could be URL encoded as %2E. However, many filters recognize this encoding and would still block the request. In a double encoding, the % in the above URL encoding would be encoded again as %25, resulting in %252E which some filters might not catch, but which could still be interpreted as a dot (.) by interpreters on the target.

## Prerequisites
- The target's filters must fail to detect that a character has been doubly encoded but its interpreting engine must still be able to convert a doubly encoded character to an un-encoded character.
- The application accepts and decodes URL string request.
- The application performs insufficient filtering/canonicalization on the URLs.

## Resources required
- Tools that automate encoding of data can assist the adversary in generating encoded strings.

## Execution flow
Execution Flow Explore Survey the application for user-controllable inputs: Using a browser, an automated tool or by inspecting the application, an attacker records all entry points to the application. Techniques Use a spidering tool to follow and record all links and analyze the web pages to find entry points. Make special note of any links that include parameters in the URL. Use a proxy tool to record all user input entry points visited during a manual traversal of the web application. Use a browser to manually explore the website and analyze how it is constructed. Many browsers' plugins are available to facilitate the analysis or automate the discovery. Manually inspect the application to find entry points. Experiment Probe entry points to locate vulnerabilities: Try double-encoding for parts of the input in order to try to get past the filters. For instance, by double encoding certain characters in the URL (e.g. dots and slashes) an adversary may try to get access to restricted resources on the web server or force browse to protected pages (thus subverting the authorization service). An adversary can also attempt other injection style attacks using this attack pattern: command injection, SQL injection, etc. Techniques Try to use double-encoding to bypass validation routines.

## Mitigations
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system. Test your decoding process against malicious input.
- Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding.
- When client input is required from web-based forms, avoid using the "GET" method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the "POST method whenever possible.
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.
- Refer to the RFCs to safely decode URL.
- Regular expression can be used to match safe URL patterns. However, that may discard valid URL requests if the regular expression is too restrictive.
- There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx).

## Related weaknesses (CWE)
- [CWE-173](https://cwe.mitre.org/data/definitions/173.html)
- [CWE-172](https://cwe.mitre.org/data/definitions/172.html)
- [CWE-177](https://cwe.mitre.org/data/definitions/177.html)
- [CWE-181](https://cwe.mitre.org/data/definitions/181.html)
- [CWE-183](https://cwe.mitre.org/data/definitions/183.html)
- [CWE-184](https://cwe.mitre.org/data/definitions/184.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)
- [CWE-692](https://cwe.mitre.org/data/definitions/692.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/120.html
