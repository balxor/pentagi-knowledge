---
cwe_id: CWE-1423
name: Exposure of Sensitive Information caused by Shared Microarchitectural Predictor State that Influences Transient Execution
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Microcontroller Hardware, Processor Hardware, Memory Hardware, System on Chip]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1423.html
tags: [mitre-cwe, weakness, CWE-1423]
---

# CWE-1423 - Exposure of Sensitive Information caused by Shared Microarchitectural Predictor State that Influences Transient Execution

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1423](https://cwe.mitre.org/data/definitions/1423.html)

## Description
Shared microarchitectural predictor state may allow code to influence transient execution across a hardware boundary, potentially exposing data that is accessible beyond the boundary over a covert channel.

## Extended description
Many commodity processors have Instruction Set Architecture (ISA) features that protect software components from one another. These features can include memory segmentation, virtual memory, privilege rings, trusted execution environments, and virtual machines, among others. For example, virtual memory provides each process with its own address space, which prevents processes from accessing each other's private data. Many of these features can be used to form hardware-enforced security boundaries between software components. When separate software components (for example, two processes) share microarchitectural predictor state across a hardware boundary, code in one component may be able to influence microarchitectural predictor behavior in another component. If the predictor can cause transient execution, the shared predictor state may allow an attacker to influence transient execution in a victim, and in a manner that could allow the attacker to infer private data from the victim by monitoring observable discrepancies (CWE-203) in a covert channel [REF-1400]. Predictor state may be shared when the processor transitions from one component to another (for example, when a process makes a system call to enter the kernel). Many commodity processors have features which prevent microarchitectural predictions that occur before a boundary from influencing predictions that occur after the boundary. Predictor state may also be shared between hardware threads, for example, sibling hardware threads on a processor that supports simultaneous multithreading (SMT). This sharing may be benign if the hardware threads are simultaneously executing in the same software component, or it could expose a weakness if one sibling is a malicious software component, and the other sibling is a victim software component. Processors that share microarchitectural predictors between hardware threads may have features which prevent microarchitectural predictions that occur on one hardware thread from influencing predictions that occur on another hardware thread. Features that restrict predictor state sharing across transitions or between hardware threads may be always-on, on by default, or may require opt-in from software.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, Microcontroller Hardware, Processor Hardware, Memory Hardware, System on Chip

## Common consequences
- **Confidentiality**: Read Memory

## Potential mitigations
- **Architecture and Design**: The hardware designer can attempt to prevent transient execution from causing observable discrepancies in specific covert channels.
- **Architecture and Design**: Hardware designers may choose to use microarchitectural bits to tag predictor entries. For example, each predictor entry may be tagged with a kernel-mode bit which, when set, indicates that the predictor entry was created in kernel mode. The processor can use this bit to enforce that predictions in the current mode must have been trained in the current mode. This can prevent malicious cross-mode training, such as when user-mode software attempts to create predictor entries that influence transient execution in the kernel. Predictor entry tags can also be used to associate each predictor entry with the SMT thread that created it, and thus the processor can enforce that each predictor entry can only be used by the SMT thread that created it. This can prevent an SMT thread from using predictor entries crafted by a malicious sibling SMT thread.
- **Architecture and Design**: Hardware designers may choose to sanitize microarchitectural predictor state (for example, branch prediction history) when the processor transitions to a different context, for example, whenever a system call is invoked. Alternatively, the hardware may expose instruction(s) that allow software to sanitize predictor state according to the user's threat model. For example, this can allow operating system software to sanitize predictor state when performing a context switch from one process to another.
- **Implementation**: System software can mitigate this weakness by invoking predictor-state-sanitizing operations (for example, the indirect branch prediction barrier on Intel x86) when switching from one context to another, according to the hardware vendor's recommendations.
- **Build and Compilation**: If the weakness is exposed by a single instruction (or a small set of instructions), then the compiler (or JIT, etc.) can be configured to prevent the affected instruction(s) from being generated. One prominent example of this mitigation is retpoline ([REF-1414]).
- **Build and Compilation**: Use control-flow integrity (CFI) techniques to constrain the behavior of instructions that redirect the instruction pointer, such as indirect branch instructions.
- **Build and Compilation**: Use software techniques (including the use of serialization instructions) that are intended to reduce the number of instructions that can be executed transiently after a processor event or misprediction.
- **System Configuration**: Some systems may allow the user to disable predictor sharing. For example, this could be a BIOS configuration, or a model-specific register (MSR) that can be configured by the operating system or virtual machine monitor.
- **Patching and Maintenance**: The hardware vendor may provide a patch to, for example, sanitize predictor state when the processor transitions to a different context, or to prevent predictor entries from being shared across SMT threads. A patch may also introduce new ISA that allows software to toggle a mitigation.
- **Documentation**: If a hardware feature can allow microarchitectural predictor state to be shared between contexts, SMT threads, or other architecturally defined boundaries, the hardware designer may opt to disclose this behavior in architecture documentation. This documentation can inform users about potential consequences and effective mitigations.
- **Requirements**: Processor designers, system software vendors, or other agents may choose to restrict the ability of unprivileged software to access to high-resolution timers that are commonly used to monitor covert channels.

## Related weaknesses
- CWE-1420 (ChildOf)
- CWE-1420 (ChildOf)

## Observed examples (CVE)
- **CVE-2017-5754**: (Branch Target Injection, BTI, Spectre v2). Shared microarchitectural indirect branch predictor state may allow code to influence transient execution across a process, VM, or privilege boundary, potentially exposing data that is accessible beyond the boundary.
- **CVE-2022-0001**: (Branch History Injection, BHI, Spectre-BHB). Shared branch history state may allow user-mode code to influence transient execution in the kernel, potentially exposing kernel data over a covert channel.
- **CVE-2021-33149**: (RSB underflow, Retbleed). Shared return stack buffer state may allow code that executes before a prediction barrier to influence transient execution after the prediction barrier, potentially exposing data that is accessible beyond the barrier over a covert channel.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1423.html
