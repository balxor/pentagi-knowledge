---
capec_id: CAPEC-73
name: User-Controlled Filename
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-20, CWE-184, CWE-96, CWE-348, CWE-116, CWE-350, CWE-86, CWE-697]
related_attack: []
url: https://capec.mitre.org/data/definitions/73.html
tags: [mitre-capec, attack-pattern, CAPEC-73]
---

# CAPEC-73 - User-Controlled Filename

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-73](https://capec.mitre.org/data/definitions/73.html)

## Description
An attack of this type involves an adversary inserting malicious characters (such as a XSS redirection) into a filename, directly or indirectly that is then used by the target software to generate HTML text or other potentially executable content. Many websites rely on user-generated content and dynamically build resources like files, filenames, and URL links directly from user supplied data. In this attack pattern, the attacker uploads code that can execute in the client browser and/or redirect the client browser to a site that the attacker owns. All XSS attack payload variants can be used to pass and exploit these vulnerabilities.

## Prerequisites
- The victim must trust the name and locale of user controlled filenames.

## Skills required
- **High**: Exploiting a client side vulnerability to inject malicious scripts into the browser's executable process.
- **Low**: To achieve a redirection and use of less trusted source, an attacker can simply edit data that the host uses to build the filename
- **Medium**: Deploying a malicious "look-a-like" site (such as a site masquerading as a bank or online auction site) that the user enters their authentication data into.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code), Alter Execution Logic
- **Confidentiality**: Gain Privileges, Execute Unauthorized Commands (Run Arbitrary Code), Read Data
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Mitigations
- Design: Use browser technologies that do not allow client side scripting.
- Implementation: Ensure all content that is delivered to client is sanitized against an acceptable content specification.
- Implementation: Perform input validation for all remote content.
- Implementation: Perform output validation for all remote content.
- Implementation: Disable scripting languages such as JavaScript in browser
- Implementation: Scan dynamically generated content against validation specification

## Related weaknesses (CWE)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-184](https://cwe.mitre.org/data/definitions/184.html)
- [CWE-96](https://cwe.mitre.org/data/definitions/96.html)
- [CWE-348](https://cwe.mitre.org/data/definitions/348.html)
- [CWE-116](https://cwe.mitre.org/data/definitions/116.html)
- [CWE-350](https://cwe.mitre.org/data/definitions/350.html)
- [CWE-86](https://cwe.mitre.org/data/definitions/86.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/73.html
