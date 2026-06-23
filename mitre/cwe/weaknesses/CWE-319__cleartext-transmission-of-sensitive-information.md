---
cwe_id: CWE-319
name: Cleartext Transmission of Sensitive Information
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Technology-Specific, Cloud Computing, Mobile, ICS/OT, System on Chip, Test/Debug Hardware]
related_capec: [CAPEC-102, CAPEC-117, CAPEC-383, CAPEC-477, CAPEC-65]
url: https://cwe.mitre.org/data/definitions/319.html
tags: [mitre-cwe, weakness, CWE-319]
---

# CWE-319 - Cleartext Transmission of Sensitive Information

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-319](https://cwe.mitre.org/data/definitions/319.html)

## Description
The product transmits sensitive or security-critical data in cleartext in a communication channel that can be sniffed by unauthorized actors.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Cloud Computing, Mobile, ICS/OT, System on Chip, Test/Debug Hardware

## Common consequences
- **Integrity, Confidentiality**: Read Application Data, Modify Files or Directories
- **Integrity, Confidentiality**: Read Application Data, Modify Files or Directories, Other

## Potential mitigations
- **Architecture and Design**: Before transmitting, encrypt the data using reliable, confidentiality-protecting cryptographic protocols.
- **Implementation**: When using web applications with SSL, use SSL for the entire session from login to logout, not just for the initial login page.
- **Implementation**: When designing hardware platforms, ensure that approved encryption algorithms (such as those recommended by NIST) protect paths from security critical data to trusted user applications.
- **Testing**: Use tools and techniques that require manual (human) analysis, such as penetration testing, threat modeling, and interactive tools that allow the tester to record and modify an active session. These may be more effective than strictly automated techniques. This is especially the case with weaknesses that are related to design and business rules.
- **Operation**: Configure servers to use encrypted channels for communication, which may include SSL or other secure protocols.

## Related attack patterns (CAPEC)
- [CAPEC-102](https://capec.mitre.org/data/definitions/102.html)
- [CAPEC-117](https://capec.mitre.org/data/definitions/117.html)
- [CAPEC-383](https://capec.mitre.org/data/definitions/383.html)
- [CAPEC-477](https://capec.mitre.org/data/definitions/477.html)
- [CAPEC-65](https://capec.mitre.org/data/definitions/65.html)

## Related weaknesses
- CWE-311 (ChildOf)
- CWE-311 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-29519**: Programmable Logic Controller (PLC) sends sensitive information in plaintext, including passwords and session tokens.
- **CVE-2022-30312**: Building Controller uses a protocol that transmits authentication credentials in plaintext.
- **CVE-2022-31204**: Programmable Logic Controller (PLC) sends password in plaintext.
- **CVE-2002-1949**: Passwords transmitted in cleartext.
- **CVE-2008-4122**: Chain: Use of HTTPS cookie without "secure" flag causes it to be transmitted across unencrypted HTTP.
- **CVE-2008-3289**: Product sends password hash in cleartext in violation of intended policy.
- **CVE-2008-4390**: Remote management feature sends sensitive information including passwords in cleartext.
- **CVE-2007-5626**: Backup routine sends password in cleartext in email.
- **CVE-2004-1852**: Product transmits Blowfish encryption key in cleartext.
- **CVE-2008-0374**: Printer sends configuration information, including administrative password, in cleartext.
- **CVE-2007-4961**: Chain: cleartext transmission of the MD5 hash of password enables attacks against a server that is susceptible to replay (CWE-294).
- **CVE-2007-4786**: Product sends passwords in cleartext to a log server.
- **CVE-2005-3140**: Product sends file with cleartext passwords in e-mail message intended for diagnostic purposes.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/319.html
