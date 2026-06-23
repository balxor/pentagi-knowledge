---
capec_id: CAPEC-159
name: Redirect Access to Libraries
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Very High
related_cwe: [CWE-706]
related_attack: [T1574.008]
url: https://capec.mitre.org/data/definitions/159.html
tags: [mitre-capec, attack-pattern, CAPEC-159]
---

# CAPEC-159 - Redirect Access to Libraries

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-159](https://capec.mitre.org/data/definitions/159.html)

## Description
An adversary exploits a weakness in the way an application searches for external libraries to manipulate the execution flow to point to an adversary supplied library or code base. This pattern of attack allows the adversary to compromise the application or server via the execution of unauthorized code. An application typically makes calls to functions that are a part of libraries external to the application. These libraries may be part of the operating system or they may be third party libraries. If an adversary can redirect an application's attempts to access these libraries to other libraries that the adversary supplies, the adversary will be able to force the targeted application to execute arbitrary code. This is especially dangerous if the targeted application has enhanced privileges. Access can be redirected through a number of techniques, including the use of symbolic links, search path modification, and relative path manipulation.

## Prerequisites
- The target must utilize external libraries and must fail to verify the integrity of these libraries before using them.

## Skills required
- **High**: To reverse engineering the libraries and inject malicious code into the libraries
- **Low**: To modify the entries in the configuration file pointing to malicious libraries
- **Medium**: To force symlink and timing issues for redirecting access to libraries

## Consequences
- **Access_Control**: Bypass Protection Mechanism
- **Authorization**: Execute Unauthorized Commands (Run Arbitrary Code), Bypass Protection Mechanism

## Execution flow
Execution Flow Explore Identify Target: The adversary identifies the target application and determines what libraries are being used. Techniques Find public source code and identify library dependencies. Gain access to the system hosting the application and look for libraries in common locations. Experiment Deploy Malicious Libraries: The adversary crafts malicious libraries and deploys them on the system where the application is running, or in a remote location that can be loaded by the application. Exploit Redirect Library Calls to Malicious Library: Once the malicious library crafted by the adversary is deployed, the adversary will manipulate the flow of the application such that it calls the malicious library. This can be done in a variety of ways based on how the application is loading and calling libraries. Techniques Poison the DNS cache of the system so that it loads a malicious library from a remote location hosted by the adversary instead of the legitimate location Create a symlink that tricks the application into thinking that a malicious library is the legitimate library. Use DLL side-loading to place a malicious verison of a DLL in the windows directory.

## Mitigations
- Implementation: Restrict the permission to modify the entries in the configuration file.
- Implementation: Check the integrity of the dynamically linked libraries before use them.
- Implementation: Use obfuscation and other techniques to prevent reverse engineering the libraries.

## Related weaknesses (CWE)
- [CWE-706](https://cwe.mitre.org/data/definitions/706.html)

## Related ATT&CK techniques
- T1574.008

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/159.html
