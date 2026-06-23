---
cwe_id: CWE-111
name: Direct Use of Unsafe JNI
type: weakness
abstraction: Variant
status: Draft
languages: [Java]
related_capec: []
url: https://cwe.mitre.org/data/definitions/111.html
tags: [mitre-cwe, weakness, CWE-111]
---

# CWE-111 - Direct Use of Unsafe JNI

**Abstraction:** Variant  -  **Status:** Draft  -  **CWE:** [CWE-111](https://cwe.mitre.org/data/definitions/111.html)

## Description
When a Java application uses the Java Native Interface (JNI) to call code written in another programming language, it can expose the application to weaknesses in that code, even if those weaknesses cannot occur in Java.

## Extended description
Many safety features that programmers may take for granted do not apply for native code, so you must carefully review all such code for potential problems. The languages used to implement native code may be more susceptible to buffer overflows and other attacks. Native code is unprotected by the security features enforced by the runtime environment, such as strong typing and array bounds checking.

## Applicable platforms / languages
Java

## Common consequences
- **Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: Implement error handling around the JNI call.
- **Implementation**: Do not use JNI calls if you don't trust the native library.
- **Implementation**: Be reluctant to use JNI calls. A Java API equivalent may exist.

## Related weaknesses
- CWE-695 (ChildOf)
- CWE-20 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/111.html
