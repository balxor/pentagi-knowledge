---
capec_id: CAPEC-42
name: MIME Conversion
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-120, CWE-119, CWE-74, CWE-20]
related_attack: []
url: https://capec.mitre.org/data/definitions/42.html
tags: [mitre-capec, attack-pattern, CAPEC-42]
---

# CAPEC-42 - MIME Conversion

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-42](https://capec.mitre.org/data/definitions/42.html)

## Description
An attacker exploits a weakness in the MIME conversion routine to cause a buffer overflow and gain control over the mail server machine. The MIME system is designed to allow various different information formats to be interpreted and sent via e-mail. Attack points exist when data are converted to MIME compatible format and back.

## Prerequisites
- The target system uses a mail server.
- Mail server vendor has not released a patch for the MIME conversion routine, the patch itself has a security hole or does not fix the original problem, or the patch has not been applied to the user's system.

## Skills required
- **High**: Causing arbitrary code to execute on the target system.
- **Low**: It may be trivial to cause a DoS via this attack pattern

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code), Unreliable Execution
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code), Modify Data

## Execution flow
Execution Flow Explore Identify target mail server: The adversary identifies a target mail server that they wish to attack. Techniques Use Nmap on a system to identify a mail server service. Determine viability of attack: Determine whether the mail server is unpatched and is potentially vulnerable to one of the known MIME conversion buffer overflows (e.g. Sendmail 8.8.3 and 8.8.4). Experiment Find injection vector: Identify places in the system where vulnerable MIME conversion routines may be used. Craft overflow content: The adversary crafts e-mail messages with special headers that will cause a buffer overflow for the vulnerable MIME conversion routine. The intent of this attack is to leverage the overflow for execution of arbitrary code and gain access to the mail server machine, so the adversary will craft an email that not only overflows the targeted buffer but does so in such a way that the overwritten return address is replaced with one of the adversary's choosing. Techniques Create malicious shellcode that will execute when the program execution is returned to it. Use a NOP-sled in the overflow content to more easily "slide" into the malicious code. This is done so that the exact return address need not be correct, only in the range of all of the NOPs Exploit Overflow the buffer: Send e-mail messages to the target system with specially crafted headers that trigger the buffer overflow and execute the shell code.

## Mitigations
- Stay up to date with third party vendor patches
- Disable the 7 to 8 bit conversion. This can be done by removing the F=9 flag from all Mailer specifications in the sendmail.cf file. For example, a sendmail.cf file with these changes applied should look similar to (depending on your system and configuration): Mlocal, P=/usr/libexec/mail.local, F=lsDFMAw5:/|@qrmn, S=10/30, R=20/40, T=DNS/RFC822/X-Unix,A=mail -d $u Mprog, P=/bin/sh, F=lsDFMoqeu, S=10/30, R=20/40, D=$z:/,T=X-Unix,A=sh -c $u This can be achieved for the "Mlocal" and "Mprog" Mailers by modifying the ".mc" file to include the following lines: define(`LOCAL_MAILER_FLAGS', ifdef(`LOCAL_MAILER_FLAGS', `translit(LOCAL_MAILER_FLAGS, `9')',`rmn')) define(`LOCAL_SHELL_FLAGS', ifdef(`LOCAL_SHELL_FLAGS', `translit(LOCAL_SHELL_FLAGS, `9')',`eu')) and then rebuilding the sendmail.cf file using m4(1). From "Exploiting Software", please see reference below.
- Use the sendmail restricted shell program (smrsh)
- Use mail.local

## Related weaknesses (CWE)
- [CWE-120](https://cwe.mitre.org/data/definitions/120.html)
- [CWE-119](https://cwe.mitre.org/data/definitions/119.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/42.html
