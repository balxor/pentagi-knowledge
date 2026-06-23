---
cwe_id: CWE-311
name: Missing Encryption of Sensitive Data
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-157, CAPEC-158, CAPEC-204, CAPEC-31, CAPEC-37, CAPEC-383, CAPEC-384, CAPEC-385, CAPEC-386, CAPEC-387, CAPEC-388, CAPEC-477, CAPEC-609, CAPEC-65]
url: https://cwe.mitre.org/data/definitions/311.html
tags: [mitre-cwe, weakness, CWE-311]
---

# CWE-311 - Missing Encryption of Sensitive Data

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-311](https://cwe.mitre.org/data/definitions/311.html)

## Description
The product does not encrypt sensitive or critical information before storage or transmission.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data
- **Confidentiality, Integrity**: Modify Application Data

## Potential mitigations
- **Requirements**: Clearly specify which data or resources are valuable enough that they should be protected by encryption. Require that any transmission or storage of this data/resource should use well-vetted encryption algorithms.
- **Architecture and Design**: Ensure that encryption is properly integrated into the system design, including but not necessarily limited to: Encryption that is needed to store or transmit private data of the users of the system Encryption that is needed to protect the system itself from unauthorized disclosure or tampering Identify the separate needs and contexts for encryption: One-way (i.e., only the user or recipient needs to have the key). This can be achieved using public key cryptography, or other techniques in which the encrypting party (i.e., the product) does not need to have access to a private key. Two-way (i.e., the encryption can be automatically performed on behalf of a user, but the key must be available so that the plaintext can be automatically recoverable by that user). This requires storage of the private key in a format that is recoverable only by the user (or perhaps by the operating system) in a way that cannot be recovered by others. Using threat modeling or other techniques, assume that data can be compromised through a separate vulnerability or weakness, and determine where encryption will be most effective. Ensure that data that should be private is not being inadvertently exposed using weaknesses such as insecure permissions (CWE-732). [REF-7]
- **Architecture and Design**: When there is a need to store or transmit sensitive data, use strong, up-to-date cryptographic algorithms to encrypt that data. Select a well-vetted algorithm that is currently considered to be strong by experts in the field, and use well-tested implementations. As with all cryptographic mechanisms, the source code should be available for analysis. For example, US government systems require FIPS 140-2 certification. Do not develop custom or private cryptographic algorithms. They will likely be exposed to attacks that are well-understood by cryptographers. Reverse engineering techniques are mature. If the algorithm can be compromised if attackers find out how it works, then it is especially weak. Periodically ensure that the cryptography has not become obsolete. Some older algorithms, once thought to require a billion years of computing time, can now be broken in days or hours. This includes MD4, MD5, SHA1, DES, and other algorithms that were once regarded as strong. [REF-267]
- **Architecture and Design**: Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.
- **Implementation, Architecture and Design**: When using industry-approved techniques, use them correctly. Don't cut corners by skipping resource-intensive steps (CWE-325). These steps are often essential for preventing common attacks.
- **Implementation**: Use naming conventions and strong types to make it easier to spot when sensitive data is being used. When creating structures, objects, or other complex entities, separate the sensitive and non-sensitive data as much as possible.

## Related attack patterns (CAPEC)
- [CAPEC-157](https://capec.mitre.org/data/definitions/157.html)
- [CAPEC-158](https://capec.mitre.org/data/definitions/158.html)
- [CAPEC-204](https://capec.mitre.org/data/definitions/204.html)
- [CAPEC-31](https://capec.mitre.org/data/definitions/31.html)
- [CAPEC-37](https://capec.mitre.org/data/definitions/37.html)
- [CAPEC-383](https://capec.mitre.org/data/definitions/383.html)
- [CAPEC-384](https://capec.mitre.org/data/definitions/384.html)
- [CAPEC-385](https://capec.mitre.org/data/definitions/385.html)
- [CAPEC-386](https://capec.mitre.org/data/definitions/386.html)
- [CAPEC-387](https://capec.mitre.org/data/definitions/387.html)
- [CAPEC-388](https://capec.mitre.org/data/definitions/388.html)
- [CAPEC-477](https://capec.mitre.org/data/definitions/477.html)
- [CAPEC-609](https://capec.mitre.org/data/definitions/609.html)
- [CAPEC-65](https://capec.mitre.org/data/definitions/65.html)

## Related weaknesses
- CWE-693 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-26390**: wireless battery product stores credentials and Personal Health Information (PHI) without encryption
- **CVE-2009-2272**: password and username stored in cleartext in a cookie
- **CVE-2009-1466**: password stored in cleartext in a file with insecure permissions
- **CVE-2009-0152**: chat program disables SSL in some circumstances even when the user says to use SSL.
- **CVE-2009-1603**: Chain: product uses an incorrect public exponent when generating an RSA key, which effectively disables the encryption
- **CVE-2009-0964**: storage of unencrypted passwords in a database
- **CVE-2008-6157**: storage of unencrypted passwords in a database
- **CVE-2008-6828**: product stores a password in cleartext in memory
- **CVE-2008-1567**: storage of a secret key in cleartext in a temporary file
- **CVE-2008-0174**: SCADA product uses HTTP Basic Authentication, which is not encrypted
- **CVE-2007-5778**: login credentials stored unencrypted in a registry key
- **CVE-2002-1949**: Passwords transmitted in cleartext.
- **CVE-2008-4122**: Chain: Use of HTTPS cookie without "secure" flag causes it to be transmitted across unencrypted HTTP.
- **CVE-2008-3289**: Product sends password hash in cleartext in violation of intended policy.
- **CVE-2008-4390**: Remote management feature sends sensitive information including passwords in cleartext.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/311.html
