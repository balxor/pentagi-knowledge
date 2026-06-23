---
capec_id: CAPEC-14
name: Client-side Injection-induced Buffer Overflow
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-120, CWE-353, CWE-118, CWE-119, CWE-74, CWE-20, CWE-680, CWE-697]
related_attack: []
url: https://capec.mitre.org/data/definitions/14.html
tags: [mitre-capec, attack-pattern, CAPEC-14]
---

# CAPEC-14 - Client-side Injection-induced Buffer Overflow

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-14](https://capec.mitre.org/data/definitions/14.html)

## Description
This type of attack exploits a buffer overflow vulnerability in targeted client software through injection of malicious content from a custom-built hostile service. This hostile service is created to deliver the correct content to the client software. For example, if the client-side application is a browser, the service will host a webpage that the browser loads.

## Prerequisites
- The targeted client software communicates with an external server.
- The targeted client software has a buffer overflow vulnerability.

## Skills required
- **High**: Exploiting a buffer overflow to inject malicious code into the stack of a software system or even the heap requires a more in-depth knowledge and higher skill level.
- **Low**: To achieve a denial of service, an attacker can simply overflow a buffer by inserting a long string into an attacker-modifiable injection vector.

## Consequences
- **Availability**: Resource Consumption (Denial of Service), Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Read Data, Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Modify Data, Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Identify target client-side application: The adversary identifies a target client-side application to perform the buffer overflow on. The most common are browsers. If there is a known browser vulnerability an adversary could target that. Experiment Find injection vector: The adversary identifies an injection vector to deliver the excessive content to the targeted application's buffer. Techniques Many times client side applications will be open source, so an adversary can examine the source code to identify possible injection vectors. Examine APIs of the client-side application and look for areas where a buffer overflow might be possible. Create hostile service: The adversary creates a hostile service that will deliver content to the client-side application. If the intent is to simply cause the software to crash, the content need only consist of an excessive quantity of random data. If the intent is to leverage the overflow for execution of arbitrary code, the adversary crafts the payload in such a way that the overwritten return address is replaced with one of the adversary's choosing. Techniques If the client-side application is a browser, the adversary will create a service that delivers a malicious webpage to the browser. Create malicious shellcode that will execute when the program execution is returned to it. Use a NOP-sled in the overflow content to more easily "slide" into the malicious code. This is done so that the exact return address need not be correct, only in the range of all of the NOPs Exploit Overflow the buffer: Using the injection vector, the adversary delivers the content to the client-side application using the hostile service and overflows the buffer. Techniques If the adversary is targeting a local client-side application, they just need to use the service themselves. If the adversary is attempting to cause an overflow on an external user's client-side application, they must get the user to attach to their service by some other means. This could be getting a user to visit their hostile webpage to target a user's browser.

## Mitigations
- The client software should not install untrusted code from a non-authenticated server.
- The client software should have the latest patches and should be audited for vulnerabilities before being used to communicate with potentially hostile servers.
- Perform input validation for length of buffer inputs.
- Use a language or compiler that performs automatic bounds checking.
- Use an abstraction library to abstract away risky APIs. Not a complete solution.
- Compiler-based canary mechanisms such as StackGuard, ProPolice and the Microsoft Visual Studio /GS flag. Unless this provides automatic bounds checking, it is not a complete solution.
- Ensure all buffer uses are consistently bounds-checked.
- Use OS-level preventative functionality. Not a complete solution.

## Related weaknesses (CWE)
- [CWE-120](https://cwe.mitre.org/data/definitions/120.html)
- [CWE-353](https://cwe.mitre.org/data/definitions/353.html)
- [CWE-118](https://cwe.mitre.org/data/definitions/118.html)
- [CWE-119](https://cwe.mitre.org/data/definitions/119.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)
- [CWE-680](https://cwe.mitre.org/data/definitions/680.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/14.html
