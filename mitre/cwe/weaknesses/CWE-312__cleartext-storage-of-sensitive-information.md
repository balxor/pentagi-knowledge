---
cwe_id: CWE-312
name: Cleartext Storage of Sensitive Information
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Cloud Computing, ICS/OT, Mobile]
related_capec: [CAPEC-37]
url: https://cwe.mitre.org/data/definitions/312.html
tags: [mitre-cwe, weakness, CWE-312]
---

# CWE-312 - Cleartext Storage of Sensitive Information

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-312](https://cwe.mitre.org/data/definitions/312.html)

## Description
The product stores sensitive information in cleartext within a resource that might be accessible to another control sphere.

## Applicable platforms / languages
Not Language-Specific, Cloud Computing, ICS/OT, Mobile

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Implementation, System Configuration, Operation**: When storing data in the cloud (e.g., S3 buckets, Azure blobs, Google Cloud Storage, etc.), use the provider's controls to encrypt the data at rest. [REF-1297] [REF-1299] [REF-1301]
- **Implementation, System Configuration, Operation**: In some systems/environments such as cloud, the use of "double encryption" (at both the software and hardware layer) might be required, and the developer might be solely responsible for both layers, instead of shared responsibility with the administrator of the broader system/environment.

## Related attack patterns (CAPEC)
- [CAPEC-37](https://capec.mitre.org/data/definitions/37.html)

## Related weaknesses
- CWE-311 (ChildOf)
- CWE-311 (ChildOf)
- CWE-922 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-26390**: wireless battery product stores credentials and Personal Health Information (PHI) without encryption
- **CVE-2022-30275**: Remote Terminal Unit (RTU) uses a driver that relies on a password stored in plaintext.
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
- **CVE-2001-1481**: Plaintext credentials in world-readable file.
- **CVE-2005-1828**: Password in cleartext in config file.
- **CVE-2005-2209**: Password in cleartext in config file.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/312.html
