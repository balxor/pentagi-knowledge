---
cwe_id: CWE-494
name: Download of Code Without Integrity Check
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific]
related_capec: [CAPEC-184, CAPEC-185, CAPEC-186, CAPEC-187, CAPEC-533, CAPEC-538, CAPEC-657, CAPEC-662, CAPEC-691, CAPEC-692, CAPEC-693, CAPEC-695]
url: https://cwe.mitre.org/data/definitions/494.html
tags: [mitre-cwe, weakness, CWE-494]
---

# CWE-494 - Download of Code Without Integrity Check

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-494](https://cwe.mitre.org/data/definitions/494.html)

## Description
The product downloads source code or an executable from a remote location and executes the code without sufficiently verifying the origin and integrity of the code.

## Extended description
An attacker can execute malicious code by compromising the host server, performing DNS spoofing, or modifying the code in transit.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Integrity, Availability, Confidentiality, Other**: Execute Unauthorized Code or Commands, Alter Execution Logic, Other

## Potential mitigations
- **Implementation**: Perform proper forward and reverse DNS lookups to detect DNS spoofing.
- **Architecture and Design, Operation**: Encrypt the code with a reliable encryption scheme before transmitting. This will only be a partial solution, since it will not detect DNS spoofing and it will not prevent your code from being modified on the hosting site.
- **Architecture and Design**: Use a vetted library or framework that does not allow this weakness to occur or provides constructs that make this weakness easier to avoid [REF-1482]. Speficially, it may be helpful to use tools or frameworks to perform integrity checking on the transmitted code. When providing the code that is to be downloaded, such as for automatic updates of the software, then use cryptographic signatures for the code and modify the download clients to verify the signatures. Ensure that the implementation does not contain CWE-295, CWE-320, CWE-347, and related weaknesses. Use code signing technologies such as Authenticode. See references [REF-454] [REF-455] [REF-456].
- **Architecture and Design, Operation**: Run your code using the lowest privileges that are required to accomplish the necessary tasks [REF-76]. If possible, create isolated accounts with limited privileges that are only used for a single task. That way, a successful attack will not immediately give the attacker access to the rest of the software or its environment. For example, database applications rarely need to run as the database administrator, especially in day-to-day operations.
- **Architecture and Design, Operation**: Run the code in a "jail" or similar sandbox environment that enforces strict boundaries between the process and the operating system. This may effectively restrict which files can be accessed in a particular directory or which commands can be executed by the software. OS-level examples include the Unix chroot jail, AppArmor, and SELinux. In general, managed code may provide some protection. For example, java.io.FilePermission in the Java SecurityManager allows the software to specify restrictions on file operations. This may not be a feasible solution, and it only limits the impact to the operating system; the rest of the application may still be subject to compromise. Be careful to avoid CWE-243 and other weaknesses related to jails.

## Related attack patterns (CAPEC)
- [CAPEC-184](https://capec.mitre.org/data/definitions/184.html)
- [CAPEC-185](https://capec.mitre.org/data/definitions/185.html)
- [CAPEC-186](https://capec.mitre.org/data/definitions/186.html)
- [CAPEC-187](https://capec.mitre.org/data/definitions/187.html)
- [CAPEC-533](https://capec.mitre.org/data/definitions/533.html)
- [CAPEC-538](https://capec.mitre.org/data/definitions/538.html)
- [CAPEC-657](https://capec.mitre.org/data/definitions/657.html)
- [CAPEC-662](https://capec.mitre.org/data/definitions/662.html)
- [CAPEC-691](https://capec.mitre.org/data/definitions/691.html)
- [CAPEC-692](https://capec.mitre.org/data/definitions/692.html)
- [CAPEC-693](https://capec.mitre.org/data/definitions/693.html)
- [CAPEC-695](https://capec.mitre.org/data/definitions/695.html)

## Related weaknesses
- CWE-345 (ChildOf)
- CWE-669 (ChildOf)
- CWE-669 (ChildOf)

## Observed examples (CVE)
- **CVE-2019-9534**: Satellite phone does not validate its firmware image.
- **CVE-2021-22909**: Chain: router's firmware update procedure uses curl with "-k" (insecure) option that disables certificate validation (CWE-295), allowing adversary-in-the-middle (AITM) compromise with a malicious firmware image (CWE-494).
- **CVE-2008-3438**: OS does not verify authenticity of its own updates.
- **CVE-2008-3324**: online poker client does not verify authenticity of its own updates.
- **CVE-2001-1125**: anti-virus product does not verify automatic updates for itself.
- **CVE-2002-0671**: VOIP phone downloads applications from web sites without verifying integrity.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/494.html
