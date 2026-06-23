---
cwe_id: CWE-1422
name: Exposure of Sensitive Information caused by Incorrect Data Forwarding during Transient Execution
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1422.html
tags: [mitre-cwe, weakness, CWE-1422]
---

# CWE-1422 - Exposure of Sensitive Information caused by Incorrect Data Forwarding during Transient Execution

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1422](https://cwe.mitre.org/data/definitions/1422.html)

## Description
A processor event or prediction may allow incorrect or stale data to be forwarded to transient operations, potentially exposing data over a covert channel.

## Extended description
Software may use a variety of techniques to preserve the confidentiality of private data that is accessible within the current processor context. For example, the memory safety and type safety properties of some high-level programming languages help to prevent software written in those languages from exposing private data. As a second example, software sandboxes may co-locate multiple users' software within a single process. The processor's Instruction Set Architecture (ISA) may permit one user's software to access another user's data (because the software shares the same address space), but the sandbox prevents these accesses by using software techniques such as bounds checking. If incorrect or stale data can be forwarded (for example, from a cache) to transient operations, then the operations' microarchitectural side effects may correspond to the data. If an attacker can trigger these transient operations and observe their side effects through a covert channel, then the attacker may be able to infer the data. For example, an attacker process may induce transient execution in a victim process that causes the victim to inadvertently access and then expose its private data via a covert channel. In the software sandbox example, an attacker sandbox may induce transient execution in its own code, allowing it to transiently access and expose data in a victim sandbox that shares the same address space. Consequently, weaknesses that arise from incorrect/stale data forwarding might violate users' expectations of software-based memory safety and isolation techniques. If the data forwarding behavior is not properly documented by the hardware vendor, this might violate the software vendor's expectation of how the hardware should behave.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Not Technology-Specific

## Common consequences
- **Confidentiality**: Read Memory

## Potential mitigations
- **Architecture and Design**: The hardware designer can attempt to prevent transient execution from causing observable discrepancies in specific covert channels.
- **Requirements**: Processor designers, system software vendors, or other agents may choose to restrict the ability of unprivileged software to access to high-resolution timers that are commonly used to monitor covert channels.
- **Requirements**: Processor designers may expose instructions or other architectural features that allow software to mitigate the effects of transient execution, but without disabling predictors. These features may also help to limit opportunities for data exposure.
- **Requirements**: Processor designers may expose registers (for example, control registers or model-specific registers) that allow privileged and/or user software to disable specific predictors or other hardware features that can cause confidential data to be exposed during transient execution.
- **Build and Compilation**: Use software techniques (including the use of serialization instructions) that are intended to reduce the number of instructions that can be executed transiently after a processor event or misprediction.
- **Build and Compilation**: Isolate sandboxes or managed runtimes in separate address spaces (separate processes).
- **Build and Compilation**: Include serialization instructions (for example, LFENCE) that prevent processor events or mis-predictions prior to the serialization instruction from causing transient execution after the serialization instruction. For some weaknesses, a serialization instruction can also prevent a processor event or a mis-prediction from occurring after the serialization instruction (for example, CVE-2018-3639 can allow a processor to predict that a load will not depend on an older store; a serialization instruction between the store and the load may allow the store to update memory and prevent the mis-prediction from happening at all).
- **Build and Compilation**: Use software techniques that can mitigate the consequences of transient execution. For example, address masking can be used in some circumstances to prevent out-of-bounds transient reads.
- **Build and Compilation**: If the weakness is exposed by a single instruction (or a small set of instructions), then the compiler (or JIT, etc.) can be configured to prevent the affected instruction(s) from being generated, and instead generate an alternate sequence of instructions that is not affected by the weakness.
- **Documentation**: If a hardware feature can allow incorrect or stale data to be forwarded to transient operations, the hardware designer may opt to disclose this behavior in architecture documentation. This documentation can inform users about potential consequences and effective mitigations.

## Related weaknesses
- CWE-1420 (ChildOf)
- CWE-1420 (ChildOf)

## Observed examples (CVE)
- **CVE-2020-0551**: A fault, microcode assist, or abort may allow transient load operations to forward malicious stale data to dependent operations executed by a victim, causing the victim to unintentionally access and potentially expose its own data over a covert channel.
- **CVE-2020-8698**: A fast store forwarding predictor may allow store operations to forward incorrect data to transient load operations, potentially exposing data over a covert channel.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1422.html
