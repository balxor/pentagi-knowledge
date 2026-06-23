---
cwe_id: CWE-502
name: Deserialization of Untrusted Data
type: weakness
abstraction: Base
status: Draft
languages: [Java, Ruby, PHP, Python, JavaScript, Not Technology-Specific, ICS/OT, AI/ML]
related_capec: [CAPEC-586]
url: https://cwe.mitre.org/data/definitions/502.html
tags: [mitre-cwe, weakness, CWE-502]
---

# CWE-502 - Deserialization of Untrusted Data

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-502](https://cwe.mitre.org/data/definitions/502.html)

## Description
The product deserializes untrusted data without sufficiently ensuring that the resulting data will be valid.

## Applicable platforms / languages
Java, Ruby, PHP, Python, JavaScript, Not Technology-Specific, ICS/OT, AI/ML

## Common consequences
- **Integrity**: Modify Application Data, Unexpected State
- **Availability**: DoS: Resource Consumption (CPU)
- **Other**: Varies by Context

## Potential mitigations
- **Architecture and Design, Implementation**: If available, use the signing/sealing features of the programming language to assure that deserialized data has not been tainted. For example, a hash-based message authentication code (HMAC) could be used to ensure that data has not been modified.
- **Implementation**: When deserializing data, populate a new object rather than just deserializing. The result is that the data flows through safe input validation and that the functions are safe.
- **Implementation**: Explicitly define a final object() to prevent deserialization.
- **Architecture and Design, Implementation**: Make fields transient to protect them from deserialization. An attempt to serialize and then deserialize a class containing transient fields will result in NULLs where the transient data should be. This is an excellent way to prevent time, environment-based, or sensitive variables from being carried over and used improperly.
- **Implementation**: Avoid having unnecessary types or gadgets (a sequence of instances and method invocations that can self-execute during the deserialization process, often found in libraries) available that can be leveraged for malicious ends. This limits the potential for unintended or unauthorized types and gadgets to be leveraged by the attacker. Add only acceptable classes to an allowlist. Note: new gadgets are constantly being discovered, so this alone is not a sufficient mitigation.
- **Architecture and Design, Implementation**: Employ cryptography of the data or code for protection. However, it's important to note that it would still be client-side security. This is risky because if the client is compromised then the security implemented on the client (the cryptography) can be bypassed.
- **Operation**: Use an application firewall that can detect attacks against this weakness. It can be beneficial in cases in which the code cannot be fixed (because it is controlled by a third party), as an emergency prevention measure while more comprehensive software assurance measures are applied, or to provide defense in depth [REF-1481].

## Related attack patterns (CAPEC)
- [CAPEC-586](https://capec.mitre.org/data/definitions/586.html)

## Related weaknesses
- CWE-913 (ChildOf)
- CWE-913 (ChildOf)
- CWE-915 (PeerOf)

## Observed examples (CVE)
- **CVE-2024-37052**: insecure deserialization in platform for managing AI/ML applications and models allows code execution via a crafted pickled object in a model file
- **CVE-2024-37288**: deserialization of untrusted YAML data in dashboard for data query and visualization of Elasticsearch data
- **CVE-2024-9314**: PHP object injection in WordPress plugin for AI-based SEO
- **CVE-2019-12799**: chain: bypass of untrusted deserialization issue (CWE-502) by using an assumed-trusted class (CWE-183)
- **CVE-2015-8103**: Deserialization issue in commonly-used Java library allows remote execution.
- **CVE-2015-4852**: Deserialization issue in commonly-used Java library allows remote execution.
- **CVE-2013-1465**: Use of PHP unserialize function on untrusted input allows attacker to modify application configuration.
- **CVE-2012-3527**: Use of PHP unserialize function on untrusted input in content management system might allow code execution.
- **CVE-2012-0911**: Use of PHP unserialize function on untrusted input in content management system allows code execution using a crafted cookie value.
- **CVE-2012-0911**: Content management system written in PHP allows unserialize of arbitrary objects, possibly allowing code execution.
- **CVE-2011-2520**: Python script allows local users to execute code via pickled data.
- **CVE-2012-4406**: Unsafe deserialization using pickle in a Python script.
- **CVE-2003-0791**: Web browser allows execution of native methods via a crafted string to a JavaScript function that deserializes the string.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/502.html
