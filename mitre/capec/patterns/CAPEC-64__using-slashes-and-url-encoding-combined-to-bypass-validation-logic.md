---
capec_id: CAPEC-64
name: Using Slashes and URL Encoding Combined to Bypass Validation Logic
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-177, CWE-173, CWE-172, CWE-73, CWE-22, CWE-74, CWE-20, CWE-697, CWE-707]
related_attack: []
url: https://capec.mitre.org/data/definitions/64.html
tags: [mitre-capec, attack-pattern, CAPEC-64]
---

# CAPEC-64 - Using Slashes and URL Encoding Combined to Bypass Validation Logic

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-64](https://capec.mitre.org/data/definitions/64.html)

## Description
This attack targets the encoding of the URL combined with the encoding of the slash characters. An attacker can take advantage of the multiple ways of encoding a URL and abuse the interpretation of the URL. A URL may contain special character that need special syntax handling in order to be interpreted. Special characters are represented using a percentage character followed by two digits representing the octet code of the original character (%HEX-CODE). For instance US-ASCII space character would be represented with %20. This is often referred as escaped ending or percent-encoding. Since the server decodes the URL from the requests, it may restrict the access to some URL paths by validating and filtering out the URL requests it received. An attacker will try to craft an URL with a sequence of special characters which once interpreted by the server will be equivalent to a forbidden URL. It can be difficult to protect against this attack since the URL can contain other format of encoding such as UTF-8 encoding, Unicode-encoding, etc.

## Prerequisites
- The application accepts and decodes URL string request.
- The application performs insufficient filtering/canonicalization on the URLs.

## Skills required
- **Low**: An attacker can try special characters in the URL and bypass the URL validation.
- **Medium**: The attacker may write a script to defeat the input filtering mechanism.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Resource Consumption (Denial of Service), Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Read Data, Gain Privileges
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore The attacker accesses the server using a specific URL. Experiment The attacker tries to encode some special characters in the URL. The attacker find out that some characters are not filtered properly. Exploit The attacker crafts a malicious URL string request and sends it to the server. The server decodes and interprets the URL string. Unfortunately since the input filtering is not done properly, the special characters have harmful consequences.

## Mitigations
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should not be permitted to enter into the system. Test your decoding process against malicious input.
- Be aware of the threat of alternative method of data encoding and obfuscation technique such as IP address encoding.
- When client input is required from web-based forms, avoid using the "GET" method to submit data, as the method causes the form data to be appended to the URL and is easily manipulated. Instead, use the "POST method whenever possible.
- Any security checks should occur after the data has been decoded and validated as correct data format. Do not repeat decoding process, if bad character are left after decoding process, treat the data as suspicious, and fail the validation process.
- Refer to the RFCs to safely decode URL.
- Regular expression can be used to match safe URL patterns. However, that may discard valid URL requests if the regular expression is too restrictive.
- There are tools to scan HTTP requests to the server for valid URL such as URLScan from Microsoft (http://www.microsoft.com/technet/security/tools/urlscan.mspx).

## Related weaknesses (CWE)
- [CWE-177](https://cwe.mitre.org/data/definitions/177.html)
- [CWE-173](https://cwe.mitre.org/data/definitions/173.html)
- [CWE-172](https://cwe.mitre.org/data/definitions/172.html)
- [CWE-73](https://cwe.mitre.org/data/definitions/73.html)
- [CWE-22](https://cwe.mitre.org/data/definitions/22.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)
- [CWE-707](https://cwe.mitre.org/data/definitions/707.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/64.html
