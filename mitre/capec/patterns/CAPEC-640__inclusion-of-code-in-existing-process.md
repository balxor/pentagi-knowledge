---
capec_id: CAPEC-640
name: Inclusion of Code in Existing Process
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: [CWE-114, CWE-829]
related_attack: [T1505.005, T1574.006, T1574.013, T1620]
url: https://capec.mitre.org/data/definitions/640.html
tags: [mitre-capec, attack-pattern, CAPEC-640]
---

# CAPEC-640 - Inclusion of Code in Existing Process

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-640](https://capec.mitre.org/data/definitions/640.html)

## Description
The adversary takes advantage of a bug in an application failing to verify the integrity of the running process to execute arbitrary code in the address space of a separate live process. The adversary could use running code in the context of another process to try to access process's memory, system/network resources, etc. The goal of this attack is to evade detection defenses and escalate privileges by masking the malicious code under an existing legitimate process. Examples of approaches include but not limited to: dynamic-link library (DLL) injection, portable executable injection, thread execution hijacking, ptrace system calls, VDSO hijacking, function hooking, reflective code loading, and more.

## Prerequisites
- The targeted application fails to verify the integrity of the running process that allows an adversary to execute arbitrary code.

## Skills required
- **High**: Knowledge of how to load malicious code into the memory space of a running process, as well as the ability to have the running process execute this code. For example, with DLL injection, the adversary must know how to load a DLL into the memory space of another running process, and cause this process to execute the code inside of the DLL.

## Consequences
- **Confidentiality**: Execute Unauthorized Commands, Read Data
- **Integrity**: Execute Unauthorized Commands, Read Data

## Execution flow
Execution Flow Explore Determine target process: The adversary determines a process with sufficient privileges that they wish to include code into. Techniques On Windows, use the process explorer's security tab to see if a process is running with administror privileges. On Linux, use the ps command to view running processes and pipe the output to a search for a particular user, or the root user. Experiment Attempt to include simple code with known output: The adversary attempts to include very simple code into the existing process to determine if the code inclusion worked. The code will differ based on the approach used to include code into an existing process. Exploit Include arbitrary code into existing process: Once an adversary has determined that including code into the existing process is possible, they will include code for a targeted purpose, such as accessing that process's memory.

## Mitigations
- Prevent unknown or malicious software from loading through using an allowlist policy.
- Properly restrict the location of the software being used.
- Leverage security kernel modules providing advanced access control and process restrictions like SELinux.
- Monitor API calls like CreateRemoteThread, SuspendThread/SetThreadContext/ResumeThread, QueueUserAPC, and similar for Windows.
- Monitor API calls like ptrace system call, use of LD_PRELOAD environment variable, dlfcn dynamic linking API calls, and similar for Linux.
- Monitor API calls like SetWindowsHookEx and SetWinEventHook which install hook procedures for Windows.
- Monitor processes and command-line arguments for unknown behavior related to code injection.

## Related weaknesses (CWE)
- [CWE-114](https://cwe.mitre.org/data/definitions/114.html)
- [CWE-829](https://cwe.mitre.org/data/definitions/829.html)

## Related ATT&CK techniques
- T1505.005
- T1574.006
- T1574.013
- T1620

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/640.html
