---
cwe_id: CWE-327
name: Use of a Broken or Risky Cryptographic Algorithm
type: weakness
abstraction: Class
status: Draft
languages: [Not Language-Specific, Verilog, VHDL, Not Technology-Specific, ICS/OT]
related_capec: [CAPEC-20, CAPEC-459, CAPEC-473, CAPEC-475, CAPEC-608, CAPEC-614, CAPEC-97]
url: https://cwe.mitre.org/data/definitions/327.html
tags: [mitre-cwe, weakness, CWE-327]
---

# CWE-327 - Use of a Broken or Risky Cryptographic Algorithm

**Abstraction:** Class  -  **Status:** Draft  -  **CWE:** [CWE-327](https://cwe.mitre.org/data/definitions/327.html)

## Description
The product uses a broken or risky cryptographic algorithm or protocol.

## Extended description
Cryptographic algorithms are the methods by which data is scrambled to prevent observation or influence by unauthorized actors. Insecure cryptography can be exploited to expose sensitive information, modify data in unexpected ways, spoof identities of other users or devices, or other impacts. It is very difficult to produce a secure algorithm, and even high-profile algorithms by accomplished cryptographic experts have been broken. Well-known techniques exist to break or weaken various kinds of cryptography. Accordingly, there are a small number of well-understood and heavily studied algorithms that should be used by most products. Using a non-standard or known-insecure algorithm is dangerous because a determined adversary may be able to break the algorithm and compromise whatever data has been protected. Since the state of cryptography advances so rapidly, it is common for an algorithm to be considered "unsafe" even if it was once thought to be strong. This can happen when new attacks are discovered, or if computing power increases so much that the cryptographic algorithm no longer provides the amount of protection that was originally thought. For a number of reasons, this weakness is even more challenging to manage with hardware deployment of cryptographic algorithms as opposed to software implementation. First, if a flaw is discovered with hardware-implemented cryptography, the flaw cannot be fixed in most cases without a recall of the product, because hardware is not easily replaceable like software. Second, because the hardware product is expected to work for years, the adversary's computing power will only increase over time.

## Applicable platforms / languages
Not Language-Specific, Verilog, VHDL, Not Technology-Specific, ICS/OT

## Common consequences
- **Confidentiality**: Read Application Data
- **Integrity**: Modify Application Data
- **Accountability, Non-Repudiation**: Hide Activities

## Potential mitigations
- **Architecture and Design**: When there is a need to store or transmit sensitive data, use strong, up-to-date cryptographic algorithms to encrypt that data. Select a well-vetted algorithm that is currently considered to be strong by experts in the field, and use well-tested implementations. As with all cryptographic mechanisms, the source code should be available for analysis. For example, US government systems require FIPS 140-2 certification [REF-1192]. Do not develop custom or private cryptographic algorithms. They will likely be exposed to attacks that are well-understood by cryptographers. Reverse engineering techniques are mature. If the algorithm can be compromised if attackers find out how it works, then it is especially weak. Periodically ensure that the cryptography has not become obsolete. Some older algorithms, once thought to require a billion years of computing time, can now be broken in days or hours. This includes MD4, MD5, SHA1, DES, and other algorithms that were once regarded as strong. [REF-267]
- **Architecture and Design**: Ensure that the design allows one cryptographic algorithm to be replaced with another in the next generation or version. Where possible, use wrappers to make the interfaces uniform. This will make it easier to upgrade to stronger algorithms. With hardware, design the product at the Intellectual Property (IP) level so that one cryptographic algorithm can be replaced with another in the next generation of the hardware product.
- **Architecture and Design**: Carefully manage and protect cryptographic keys (see CWE-320). If the keys can be guessed or stolen, then the strength of the cryptography itself is irrelevant.
- **Architecture and Design**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid [REF-1482]. Industry-standard implementations will save development time and may be more likely to avoid errors that can occur during implementation of cryptographic algorithms. Consider the ESAPI Encryption feature.
- **Implementation, Architecture and Design**: When using industry-approved techniques, use them correctly. Don't cut corners by skipping resource-intensive steps (CWE-325). These steps are often essential for preventing common attacks.

## Related attack patterns (CAPEC)
- [CAPEC-20](https://capec.mitre.org/data/definitions/20.html)
- [CAPEC-459](https://capec.mitre.org/data/definitions/459.html)
- [CAPEC-473](https://capec.mitre.org/data/definitions/473.html)
- [CAPEC-475](https://capec.mitre.org/data/definitions/475.html)
- [CAPEC-608](https://capec.mitre.org/data/definitions/608.html)
- [CAPEC-614](https://capec.mitre.org/data/definitions/614.html)
- [CAPEC-97](https://capec.mitre.org/data/definitions/97.html)

## Related weaknesses
- CWE-693 (ChildOf)
- CWE-311 (PeerOf)

## Observed examples (CVE)
- **CVE-2022-30273**: SCADA-based protocol supports a legacy encryption mode that uses Tiny Encryption Algorithm (TEA) in ECB mode, which leaks patterns in messages and cannot protect integrity
- **CVE-2022-30320**: Programmable Logic Controller (PLC) uses a protocol with a cryptographically insecure hashing algorithm for passwords.
- **CVE-2008-3775**: Product uses "ROT-25" to obfuscate the password in the registry.
- **CVE-2007-4150**: product only uses "XOR" to obfuscate sensitive data
- **CVE-2007-5460**: product only uses "XOR" and a fixed key to obfuscate sensitive data
- **CVE-2005-4860**: Product substitutes characters with other characters in a fixed way, and also leaves certain input characters unchanged.
- **CVE-2002-2058**: Attackers can infer private IP addresses by dividing each octet by the MD5 hash of '20'.
- **CVE-2008-3188**: Product uses DES when MD5 has been specified in the configuration, resulting in weaker-than-expected password hashes.
- **CVE-2005-2946**: Default configuration of product uses MD5 instead of stronger algorithms that are available, simplifying forgery of certificates.
- **CVE-2007-6013**: Product uses the hash of a hash for authentication, allowing attackers to gain privileges if they can obtain the original hash.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/327.html
