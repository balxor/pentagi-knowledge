---
capec_id: CAPEC-178
name: Cross-Site Flashing
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Medium
related_cwe: [CWE-601]
related_attack: []
url: https://capec.mitre.org/data/definitions/178.html
tags: [mitre-capec, attack-pattern, CAPEC-178]
---

# CAPEC-178 - Cross-Site Flashing

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-178](https://capec.mitre.org/data/definitions/178.html)

## Description
An attacker is able to trick the victim into executing a Flash document that passes commands or calls to a Flash player browser plugin, allowing the attacker to exploit native Flash functionality in the client browser. This attack pattern occurs where an attacker can provide a crafted link to a Flash document (SWF file) which, when followed, will cause additional malicious instructions to be executed. The attacker does not need to serve or control the Flash document. The attack takes advantage of the fact that Flash files can reference external URLs. If variables that serve as URLs that the Flash application references can be controlled through parameters, then by creating a link that includes values for those parameters, an attacker can cause arbitrary content to be referenced and possibly executed by the targeted Flash application.

## Prerequisites
- The targeted Flash application must reference external URLs and the locations thus referenced must be controllable through parameters. The Flash application must fail to sanitize such parameters against malicious manipulation. The victim must follow a crafted link created by the attacker.

## Skills required
- **Medium**: knowledge of Flash internals, parameters and remote referencing.

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Accountability**: Gain Privileges
- **Authentication**: Gain Privileges
- **Authorization**: Execute Unauthorized Commands (Run Arbitrary Code), Gain Privileges, Bypass Protection Mechanism
- **Confidentiality**: Read Data
- **Integrity**: Modify Data
- **Non-Repudiation**: Gain Privileges

## Execution flow
Execution Flow Explore Identification: Using a browser or an automated tool, an attacker records all instances of URLs (or partial URL such as domain) passed to a flash file (SWF). Techniques Use an automated tool to record the variables passed to a flash file. Use a browser to manually explore the website and analyze how the flash file receive variables, e.g. JavaScript using SetVariable/GetVariable, HTML FlashVars param tag, etc. Use decompilers to retrieve the flash source code and record all user-controllable variables passed to a loadMovie* directive. Experiment Attempt to inject a remote flash file: The attacker makes use of a remotely available flash file (SWF) that generates a uniquely identifiable output when executed inside the targeted flash file. Techniques Modify the variable of the SWF file that contains the remote movie URL to the attacker controlled flash file. Exploit Access or Modify Flash Application Variables: As the attacker succeeds in exploiting the vulnerability, they target the content of the flash application to steal variable content, password, etc. Techniques Develop malicious Flash application that is injected through vectors identified during the Experiment Phase and loaded by the victim browser's flash plugin and sends document information to the attacker. Develop malicious Flash application that is injected through vectors identified during the Experiment Phase and takes commands from an attacker's server and then causes the flash application to execute appropriately. Execute JavaScript in victim's browser: When the attacker targets the current flash application, they can choose to inject JavaScript in the client's DOM and therefore execute cross-site scripting attack. Techniques Develop malicious JavaScript that is injected from the rogue flash movie to the targeted flash application through vectors identified during the Experiment Phase and loaded by the victim's browser.

## Mitigations
- Implementation: Only allow known URL to be included as remote flash movies in a flash application
- Configuration: Properly configure the crossdomain.xml file to only include the known domains that should host remote flash movies.

## Related weaknesses (CWE)
- [CWE-601](https://cwe.mitre.org/data/definitions/601.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/178.html
