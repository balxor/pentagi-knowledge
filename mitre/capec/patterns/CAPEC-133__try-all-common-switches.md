---
capec_id: CAPEC-133
name: Try All Common Switches
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: [CWE-912]
related_attack: []
url: https://capec.mitre.org/data/definitions/133.html
tags: [mitre-capec, attack-pattern, CAPEC-133]
---

# CAPEC-133 - Try All Common Switches

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-133](https://capec.mitre.org/data/definitions/133.html)

## Description
An attacker attempts to invoke all common switches and options in the target application for the purpose of discovering weaknesses in the target. For example, in some applications, adding a --debug switch causes debugging information to be displayed, which can sometimes reveal sensitive processing or configuration information to an attacker. This attack differs from other forms of API abuse in that the attacker is indiscriminately attempting to invoke options in the hope that one of them will work rather than specifically targeting a known option. Nonetheless, even if the attacker is familiar with the published options of a targeted application this attack method may still be fruitful as it might discover unpublicized functionality.

## Prerequisites
- The attacker must be able to control the options or switches sent to the target.

## Resources required
- None: No specialized resources are required to execute this type of attack. The only requirement is the ability to send requests to the target.

## Execution flow
Execution Flow Explore Identify application: Discover an application of interest by exploring service registry listings or by connecting on a known port or some similar means. Techniques Search via internet for known, published applications that allow option switches. Use automated tools to scan known ports to identify applications that might be accessible Authenticate to application: Authenticate to the application, if required, in order to explore it. Techniques Use published credentials to access system. Find unpublished credentails to access service. Use other attack pattern or weakness to bypass authentication. Experiment Try all common switches: Using manual or automated means, attempt to run the application with many different known common switches. Observe the output to see if any switches seemed to put the application in a non production mode that might give more information. Techniques Manually execute the application with switches such as --debug, --test, --development, --verbose, etc. Use automated tools to run the application with common switches and observe the output Exploit Use sensitive processing or configuration information: Once extra information is observed from an application through the use of a common switch, this information is used to aid other attacks on the application Techniques Using application information, formulate an attack on the application

## Mitigations
- Design: Minimize switch and option functionality to only that necessary for correct function of the command.
- Implementation: Remove all debug and testing options from production code.

## Related weaknesses (CWE)
- [CWE-912](https://cwe.mitre.org/data/definitions/912.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/133.html
