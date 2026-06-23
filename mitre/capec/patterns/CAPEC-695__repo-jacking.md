---
capec_id: CAPEC-695
name: Repo Jacking
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: High
related_cwe: [CWE-494, CWE-829]
related_attack: [T1195.001]
url: https://capec.mitre.org/data/definitions/695.html
tags: [mitre-capec, attack-pattern, CAPEC-695]
---

# CAPEC-695 - Repo Jacking

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-695](https://capec.mitre.org/data/definitions/695.html)

## Description
<xhtml:p>An adversary takes advantage of the redirect property of directly linked Version Control System (VCS) repositories to trick users into incorporating malicious code into their applications.</xhtml:p>

## Extended description
Software developers may directly reference a VCS repository (i.e., via a hardcoded URL) within source code to integrate the repository as a dependency for the underlying application. If the repository owner/maintainer modifies the repository name, changes their VCS username, or transfers ownership of the repository, the VCS implements a redirect to the new repository location so that existing software referencing the repository will not break. However, if the original location of the repository is reestablished, the VCS will revert to resolving the hardcoded path. Adversaries may, therefore, re-register deleted or previously used usernames and recreate repositories with malicious code to infect applications referencing the repository. When an application then fetches the desired dependency, it will now reference the adversary's malicious repository since the hardcoded repository path is once again active. This ultimately allows the adversary to infect numerous applications, while achieving a variety of negative technical impacts.

## Prerequisites
- Identification of a popular repository that may be directly referenced in numerous software applications
- A repository owner/maintainer who has recently changed their username or deleted their account

## Skills required
- **Low**: Ability to create malware that can exploit various software applications.

## Consequences
- **Access_Control**: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges
- **Authorization**: Execute Unauthorized Commands, Alter Execution Logic, Gain Privileges
- **Integrity**: Read Data, Modify Data

## Execution flow
Execution Flow Explore Identify target: The adversary must first identify a target repository that is commonly used and whose owner/maintainer has either changed/deleted their username or transferred ownership of the repository and then deleted their account. The target should typically be a popular and widely used package, as to increase the scope of the attack. Experiment Recreate initial repository path: The adversary re-registers the account that was renamed/deleted by the target repository's owner/maintainer and recreates the target repository with malicious code intended to exploit an application. These steps may need to happen in reverse (i.e., recreate repository and then rename an existing account to the target account) if protections are in place to prevent repository reuse. Exploit Exploit victims: The adversary's malicious code is incorporated into applications that directly reference the initial repository, which further allows the adversary to conduct additional attacks.

## Mitigations
- Leverage dedicated package managers instead of directly linking to VCS repositories.
- Utilize version pinning and lock files to prevent use of maliciously modified repositories.
- Implement "vendoring" (i.e., including third-party dependencies locally) and leverage automated testing techniques (e.g., static analysis) to determine if the software behaves maliciously.
- Leverage automated tools, such as Checkmarx's "ChainJacking" tool, to determine susceptibility to Repo Jacking attacks.

## Related weaknesses (CWE)
- [CWE-494](https://cwe.mitre.org/data/definitions/494.html)
- [CWE-829](https://cwe.mitre.org/data/definitions/829.html)

## Related ATT&CK techniques
- T1195.001

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/695.html
