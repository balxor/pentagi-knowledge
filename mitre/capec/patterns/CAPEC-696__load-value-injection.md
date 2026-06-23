---
capec_id: CAPEC-696
name: Load Value Injection
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: Very High
related_cwe: [CWE-1342]
related_attack: []
url: https://capec.mitre.org/data/definitions/696.html
tags: [mitre-capec, attack-pattern, CAPEC-696]
---

# CAPEC-696 - Load Value Injection

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-696](https://capec.mitre.org/data/definitions/696.html)

## Description
An adversary exploits a hardware design flaw in a CPU implementation of transient instruction execution in which a faulting or assisted load instruction transiently forwards adversary-controlled data from microarchitectural buffers. By inducing a page fault or microcode assist during victim execution, an adversary can force legitimate victim execution to operate on the adversary-controlled data which is stored in the microarchitectural buffers. The adversary can then use existing code gadgets and side channel analysis to discover victim secrets that have not yet been flushed from microarchitectural state or hijack the system control flow.

## Extended description
This attack is a mix of techniques used in traditional Meltdown and Spectre attacks. It uses microarchitectural data leakage combined with code gadget abuse. Intel has identified that this attack is not applicable in scenarios where the OS and the VMM (Virtual Memory Manager) are both trusted. Because of this, Intel SGX is a prime target for this attack because it assumes that the OS or VMM may be malicious.

## Prerequisites
- The adversary needs at least user execution access to a system and a maliciously crafted program/application/process with unprivileged code to misuse transient instruction set execution of the CPU.
- The CPU incorrectly transiently forwards values from microarchitectural buffers after faulting or assisted loads
- The adversary needs the ability to induce page faults or microcode assists on the target system.
- Code gadgets exist that allow the adversary to hijack transient execution and encode secrets into the microarchitectural state.

## Skills required
- **High**: The ability to provoke faulting or assisted loads in legitimate execution.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Authorization**: Execute Unauthorized Commands
- **Confidentiality**: Read Data

## Execution flow
Execution Flow Explore Survey target application and relevant OS shared code libraries: Adversary identifies vulnerable transient instruction sets and the code/function calls to trigger them as well as instruction sets or code fragments (gadgets) to perform attack. The adversary looks for code gadgets which will allow them to load an adversary-controlled value into trusted memory. They also look for code gadgets which might operate on this controlled value. Techniques Utilize Disassembler and Debugger tools to examine and trace instruction set execution of source code and shared code libraries on a system. Experiment Fill microarchitectural buffer with controlled value: The adversary will utilize the found code gadget from the previous step to load a value into a microarchitectural buffer. Techniques The adversary may choose the controlled value to be memory address of sensitive information that they want the system to access The adversary may choose the controlled value to be the memory address of other code gadgets that they wish to execute by hijacking the control flow of the system Set up instruction to page fault or microcode assist: The adversary must manipulate the system such that a page fault or microcode assist occurs when a valid instruction is run. If the instruction that fails is near where the adversary-controlled value was loaded, the system may forward this value from the microarchitectural buffer incorrectly. Techniques When targeting Intel SGX enclaves, adversaries that have privileges can manipulate PTEs to provoke page-fault exceptions or microcode assists. When targeting Intel SGX enclaves, adversaries can indirectly revoke permissions for enclave code through the “mprotect” system call An adversary can evict selected virtual memory pages using legacy interfaces or by increasing physical memory utilization When attacking a Windows machine, wait until the OS clears the PTE accessed bit. When the page is next accessed, the CPU will always issue a microcode assist for re-setting this bit Exploit Operate on adversary-controlled data: Once the attack has been set up and the page fault or microcode assist occurs, the system operates on the adversary-controlled data. Techniques Influence the system to load sensitive information into microarchitectural state which can be read by the adversary using a code gadget. Hijack execution by jumping to second stage gadgets found in the address space. By utilizing return-oriented programming, this can chain gadgets together and allow the adversary to execute a sequence of gadgets.

## Mitigations
- Do not allow the forwarding of data resulting from a faulting or assisted instruction. Some current mitigations claim to zero out the forwarded data, but this mitigation still does not suffice.
- Insert explicit “lfence” speculation barriers in software before potentially faulting or assisted loads. This halts transient execution until all previous instructions have been executed and ensures that the architecturally correct value is forwarded.

## Related weaknesses (CWE)
- [CWE-1342](https://cwe.mitre.org/data/definitions/1342.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/696.html
