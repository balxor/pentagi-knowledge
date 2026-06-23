---
capec_id: CAPEC-256
name: SOAP Array Overflow
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: High
related_cwe: [CWE-805]
related_attack: []
url: https://capec.mitre.org/data/definitions/256.html
tags: [mitre-capec, attack-pattern, CAPEC-256]
---

# CAPEC-256 - SOAP Array Overflow

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** High  -  **CAPEC:** [CAPEC-256](https://capec.mitre.org/data/definitions/256.html)

## Description
An attacker sends a SOAP request with an array whose actual length exceeds the length indicated in the request. If the server processing the transmission naively trusts the specified size, then an attacker can intentionally understate the size of the array, possibly resulting in a buffer overflow if the server attempts to read the entire data set into the memory it allocated for a smaller array.

## Prerequisites
- The targeted SOAP server must trust that the array size as stated in messages it receives is correct, but read through the entire content of the message regardless of the stated size of the array.

## Resources required
- The attacker must be able to craft malformed SOAP messages, specifically, messages with arrays where the stated array size understates the actual size of the array in the message.

## Execution flow
Execution Flow Explore Identify target application: The adversary identifies a target application to perform the buffer overflow on. In this attack, adversaries look for applications that utilize SOAP as a communication mechanism. Experiment Find injection vector: The adversary identifies an injection vector to deliver the excessive content to the targeted application's buffer. Techniques The adversary creates a SOAP message that incorrectly specifies the size of its array to be smaller than the size of the actual content by a large margin and sends it to the application. If this causes a crash or some unintended behavior, it is likely that this is a valid injection vector. Craft overflow content: The adversary crafts the content to be injected. If the intent is to simply cause the software to crash, the content need only consist of an excessive quantity of random data. If the intent is to leverage the overflow for execution of arbitrary code, the adversary crafts the payload in such a way that the overwritten return address is replaced with one of the adversary's choosing. Techniques Create malicious shellcode that will execute when the program execution is returned to it. Use a NOP-sled in the overflow content to more easily "slide" into the malicious code. This is done so that the exact return address need not be correct, only in the range of all of the NOPs The adversary will choose a SOAP type that allows them to put shellcode into the buffer when the array is read into the application. Exploit Overflow the buffer: Using the injection vector, the adversary sends the crafted SOAP message to the program, overflowing the buffer.

## Mitigations
- If the server either verifies the correctness of the stated array size or if the server stops processing an array once the stated number of elements have been read, regardless of the actual array size, then this attack will fail. The former detects the malformed SOAP message while the latter ensures that the server does not attempt to load more data than was allocated for.

## Related weaknesses (CWE)
- [CWE-805](https://cwe.mitre.org/data/definitions/805.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/256.html
