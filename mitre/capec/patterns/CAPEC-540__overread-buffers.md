---
capec_id: CAPEC-540
name: Overread Buffers
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: High
related_cwe: [CWE-125]
related_attack: []
url: https://capec.mitre.org/data/definitions/540.html
tags: [mitre-capec, attack-pattern, CAPEC-540]
---

# CAPEC-540 - Overread Buffers

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-540](https://capec.mitre.org/data/definitions/540.html)

## Description
An adversary attacks a target by providing input that causes an application to read beyond the boundary of a defined buffer. This typically occurs when a value influencing where to start or stop reading is set to reflect positions outside of the valid memory location of the buffer. This type of attack may result in exposure of sensitive information, a system crash, or arbitrary code execution.

## Prerequisites
- For this type of attack to be successful, a few prerequisites must be met. First, the targeted software must be written in a language that enables fine grained buffer control. (e.g., c, c++) Second, the targeted software must actually perform buffer operations and inadequately perform bounds-checking on those buffer operations. Finally, the adversary must have the capability to influence the input that guides these buffer operations.

## Consequences
- **Availability**: Unreliable Execution (Depending on the use of the target buffer, an application or system crash can be achieved.)
- **Confidentiality**: Read Data (By reading outside the boundary of the intended buffer, the adversary is potentially able to see any data that is stored on the disk. This could include secret keys, personal information, and sensitive files.)

## Execution flow
Execution Flow Explore Identify target application: The adversary identifies a target application or program to perform the buffer overread on. Adversaries often look for applications that accept user input and that perform manual memory management. Experiment Find attack vector: The adversary identifies an attack vector by looking for areas in the application where they can specify to read more data than is required. Exploit Overread the buffer: The adversary provides input to the application that gets it to read past the bounds of a buffer, possibly revealing sensitive information that was not intended to be given to the adversary.

## Related weaknesses (CWE)
- [CWE-125](https://cwe.mitre.org/data/definitions/125.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/540.html
