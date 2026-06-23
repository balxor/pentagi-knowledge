---
capec_id: CAPEC-41
name: Using Meta-characters in E-mail Headers to Inject Malicious Payloads
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-150, CWE-88, CWE-697]
related_attack: []
url: https://capec.mitre.org/data/definitions/41.html
tags: [mitre-capec, attack-pattern, CAPEC-41]
---

# CAPEC-41 - Using Meta-characters in E-mail Headers to Inject Malicious Payloads

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-41](https://capec.mitre.org/data/definitions/41.html)

## Description
This type of attack involves an attacker leveraging meta-characters in email headers to inject improper behavior into email programs. Email software has become increasingly sophisticated and feature-rich. In addition, email applications are ubiquitous and connected directly to the Web making them ideal targets to launch and propagate attacks. As the user demand for new functionality in email applications grows, they become more like browsers with complex rendering and plug in routines. As more email functionality is included and abstracted from the user, this creates opportunities for attackers. Virtually all email applications do not list email header information by default, however the email header contains valuable attacker vectors for the attacker to exploit particularly if the behavior of the email client application is known. Meta-characters are hidden from the user, but can contain scripts, enumerations, probes, and other attacks against the user's system.

## Prerequisites
- This attack targets most widely deployed feature rich email applications, including web based email programs.

## Skills required
- **Low**: To distribute email

## Consequences
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Experiment Identify and characterize metacharacter-processing vulnerabilities in email headers: An attacker creates emails with headers containing various metacharacter-based malicious payloads in order to determine whether the target application processes the malicious content and in what manner it does so. Techniques Use an automated tool (fuzzer) to create malicious emails headers containing metacharacter-based payloads. Manually tampering email headers to inject malicious metacharacter-based payload content in them. Exploit An attacker leverages vulnerabilities identified during the Experiment Phase to inject malicious email headers and cause the targeted email application to exhibit behavior outside of its expected constraints. Techniques Send emails with specifically-constructed, metacharacter-based malicious payloads in the email headers to targeted systems running email processing applications identified as vulnerable during the Experiment Phase.

## Mitigations
- Design: Perform validation on email header data
- Implementation: Implement email filtering solutions on mail server or on MTA, relay server.
- Implementation: Mail servers that perform strict validation may catch these attacks, because metacharacters are not allowed in many header variables such as dns names

## Related weaknesses (CWE)
- [CWE-150](https://cwe.mitre.org/data/definitions/150.html)
- [CWE-88](https://cwe.mitre.org/data/definitions/88.html)
- [CWE-697](https://cwe.mitre.org/data/definitions/697.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/41.html
