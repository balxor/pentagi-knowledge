---
capec_id: CAPEC-39
name: Manipulating Opaque Client-based Data Tokens
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Medium
related_cwe: [CWE-353, CWE-285, CWE-302, CWE-472, CWE-565, CWE-315, CWE-539, CWE-384, CWE-233]
related_attack: []
url: https://capec.mitre.org/data/definitions/39.html
tags: [mitre-capec, attack-pattern, CAPEC-39]
---

# CAPEC-39 - Manipulating Opaque Client-based Data Tokens

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-39](https://capec.mitre.org/data/definitions/39.html)

## Description
In circumstances where an application holds important data client-side in tokens (cookies, URLs, data files, and so forth) that data can be manipulated. If client or server-side application components reinterpret that data as authentication tokens or data (such as store item pricing or wallet information) then even opaquely manipulating that data may bear fruit for an Attacker. In this pattern an attacker undermines the assumption that client side tokens have been adequately protected from tampering through use of encryption or obfuscation.

## Prerequisites
- An attacker already has some access to the system or can steal the client based data tokens from another user who has access to the system.
- For an Attacker to viably execute this attack, some data (later interpreted by the application) must be held client-side in a way that can be manipulated without detection. This means that the data or tokens are not CRCd as part of their value or through a separate meta-data store elsewhere.

## Skills required
- **High**: If the client site token is encrypted.
- **Medium**: If the client site token is obfuscated.

## Resources required
- The Attacker needs no special hardware-based resources in order to conduct this attack. Software plugins, such as Tamper Data for Firefox, may help in manipulating URL- or cookie-based data.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Enumerate information passed to client side: The attacker identifies the parameters used as part of tokens to take business or security decisions Techniques Use WebScarab to reveal hidden fields while browsing. Use a sniffer to capture packets View source of web page to find hidden fields Examine URL to see if any opaque tokens are in it Disassemble or decompile client-side application Use debugging tools such as File Monitor, Registry Monitor, Debuggers, etc. Determine protection mechanism for opaque token: The attacker determines the protection mechanism used to protect the confidentiality and integrity of these data tokens. They may be obfuscated or a full blown encryption may be used. Techniques Look for signs of well-known character encodings Look for cryptographic signatures Look for delimiters or other indicators of structure Experiment Modify parameter/token values: Trying each parameter in turn, the attacker modifies the values Techniques Modify tokens logically Modify tokens arithmetically Modify tokens bitwise Modify structural components of tokens Modify order of parameters/tokens Cycle through values for each parameter.: Depending on the nature of the application, the attacker now cycles through values of each parameter and observes the effects of this modification in the data returned by the server Techniques Use network-level packet injection tools such as netcat Use application-level data modification tools such as Tamper Data, WebScarab, TamperIE, etc. Use modified client (modified by reverse engineering) Use debugging tools to modify data in client

## Mitigations
- One solution to this problem is to protect encrypted data with a CRC of some sort. If knowing who last manipulated the data is important, then using a cryptographic "message authentication code" (or hMAC) is prescribed. However, this guidance is not a panacea. In particular, any value created by (and therefore encrypted by) the client, which itself is a "malicious" value, all the protective cryptography in the world can't make the value 'correct' again. Put simply, if the client has control over the whole process of generating and encoding the value, then simply protecting its integrity doesn't help.
- Make sure to protect client side authentication tokens for confidentiality (encryption) and integrity (signed hash)
- Make sure that all session tokens use a good source of randomness
- Perform validation on the server side to make sure that client side data tokens are consistent with what is expected.

## Related weaknesses (CWE)
- [CWE-353](https://cwe.mitre.org/data/definitions/353.html)
- [CWE-285](https://cwe.mitre.org/data/definitions/285.html)
- [CWE-302](https://cwe.mitre.org/data/definitions/302.html)
- [CWE-472](https://cwe.mitre.org/data/definitions/472.html)
- [CWE-565](https://cwe.mitre.org/data/definitions/565.html)
- [CWE-315](https://cwe.mitre.org/data/definitions/315.html)
- [CWE-539](https://cwe.mitre.org/data/definitions/539.html)
- [CWE-384](https://cwe.mitre.org/data/definitions/384.html)
- [CWE-233](https://cwe.mitre.org/data/definitions/233.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/39.html
