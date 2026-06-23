---
capec_id: CAPEC-44
name: Overflow Binary Resource File
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Very High
related_cwe: [CWE-120, CWE-119, CWE-697]
related_attack: []
url: https://capec.mitre.org/data/definitions/44.html
tags: [mitre-capec, attack-pattern, CAPEC-44]
---

# CAPEC-44 - Overflow Binary Resource File

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-44](https://capec.mitre.org/data/definitions/44.html)

## Description
An attack of this type exploits a buffer overflow vulnerability in the handling of binary resources. Binary resources may include music files like MP3, image files like JPEG files, and any other binary file. These attacks may pass unnoticed to the client machine through normal usage of files, such as a browser loading a seemingly innocent JPEG file. This can allow the adversary access to the execution stack and execute arbitrary code in the target process.

## Extended description
This attack pattern is a variant of standard buffer overflow attack using an unexpected vector (binary files) to wrap its attack and open up a new attack vector. The adversary is required to either directly serve the binary content to the victim, or place it in a locale like a MP3 sharing application for the victim to download. The adversary then is notified upon the download or otherwise locates the vulnerability opened up by the buffer overflow.

## Prerequisites
- Target software processes binary resource files.
- Target software contains a buffer overflow vulnerability reachable through input from a user-controllable binary resource file.

## Skills required
- **Medium**: To modify file, deceive client into downloading, locate and exploit remote stack or heap vulnerability

## Consequences
- **Availability**: Unreliable Execution, Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Identify target software: The adversary identifies software that uses external binary files in some way. This could be a file upload, downloading a file from a shared location, or other means. Experiment Find injection vector: The adversary creates a malicious binary file by altering the header to make the file seem shorter than it is. Additional bytes are added to the end of the file to be placed in the overflowed location. The adversary then deploys the file to the software to determine if a buffer overflow was successful. Craft overflow content: Once the adversary has determined that this attack is viable, they will specially craft the binary file in a way that achieves the desired behavior. If the source code is available, the adversary can carefully craft the malicious file so that the return address is overwritten to an intended value. If the source code is not available, the adversary will iteratively alter the file in order to overwrite the return address correctly. Techniques Create malicious shellcode that will execute when the program execution is returned to it. Use a NOP-sled in the overflow content to more easily "slide" into the malicious code. This is done so that the exact return address need not be correct, only in the range of all of the NOPs Exploit Overflow the buffer: Once the adversary has constructed a file that will effectively overflow the targeted software in the intended way. The file is deployed to the software, either by serving it directly to the software or placing it in a shared location for a victim to load into the software.

## Mitigations
- Perform appropriate bounds checking on all buffers.
- Design: Enforce principle of least privilege
- Design: Static code analysis
- Implementation: Execute program in less trusted process space environment, do not allow lower integrity processes to write to higher integrity processes
- Implementation: Keep software patched to ensure that known vulnerabilities are not available for adversaries to target on host.

## Related weaknesses (CWE)
- [CWE-120](https://cwe.mitre.org/data/definitions/120.html)
- [CWE-119](https://cwe.mitre.org/data/definitions/119.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/44.html
