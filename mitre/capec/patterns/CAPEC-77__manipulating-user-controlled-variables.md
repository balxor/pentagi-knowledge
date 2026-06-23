---
capec_id: CAPEC-77
name: Manipulating User-Controlled Variables
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Very High
related_cwe: [CWE-15, CWE-94, CWE-96, CWE-285, CWE-302, CWE-473, CWE-1321]
related_attack: []
url: https://capec.mitre.org/data/definitions/77.html
tags: [mitre-capec, attack-pattern, CAPEC-77]
---

# CAPEC-77 - Manipulating User-Controlled Variables

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-77](https://capec.mitre.org/data/definitions/77.html)

## Description
This attack targets user controlled variables (DEBUG=1, PHP Globals, and So Forth). An adversary can override variables leveraging user-supplied, untrusted query variables directly used on the application server without any data sanitization. In extreme cases, the adversary can change variables controlling the business logic of the application. For instance, in languages like PHP, a number of poorly set default configurations may allow the user to override variables.

## Prerequisites
- A variable consumed by the application server is exposed to the client.
- A variable consumed by the application server can be overwritten by the user.
- The application server trusts user supplied data to compute business logic.
- The application server does not perform proper input validation.

## Skills required
- **Low**: The malicious user can easily try some well-known global variables and find one which matches.
- **Medium**: The adversary can use automated tools to probe for variables that they can control.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Execute Unauthorized Commands (Run Arbitrary Code), Read Data, Gain Privileges
- **Integrity**: Modify Data, Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Probe target application: The adversary first probes the target application to determine important information about the target. This information could include types software used, software versions, what user input the application consumes, and so on. Experiment Find user-controlled variables: Using the information found by probing the application, the adversary attempts to manipulate many user-controlled variables and observes the effects on the application. If the adversary notices any significant changes to the application, they will know that a certain variable is useful to the application. Techniques Adversaries will try to alter many common variable names such as "count", "tempFile", "i", etc. The hope is that they can alter the flow of the application without knowing the inner-workings. Adversaries will try to alter known environment variables. Exploit Manipulate user-controlled variables: Once the adversary has found a user-controller variable(s) that is important to the application, they will manipulate it to change the normal behavior in a way that benefits the adversary.

## Mitigations
- Do not allow override of global variables and do Not Trust Global Variables. If the register_globals option is enabled, PHP will create global variables for each GET, POST, and cookie variable included in the HTTP request. This means that a malicious user may be able to set variables unexpectedly. For instance make sure that the server setting for PHP does not expose global variables.
- A software system should be reluctant to trust variables that have been initialized outside of its trust boundary. Ensure adequate checking is performed when relying on input from outside a trust boundary.
- Separate the presentation layer and the business logic layer. Variables at the business logic layer should not be exposed at the presentation layer. This is to prevent computation of business logic from user controlled input data.
- Use encapsulation when declaring your variables. This is to lower the exposure of your variables.
- Assume all input is malicious. Create an allowlist that defines all valid input to the software system based on the requirements specifications. Input that does not match against the allowlist should be rejected by the program.

## Related weaknesses (CWE)
- [CWE-15](https://cwe.mitre.org/data/definitions/15.html)
- [CWE-94](https://cwe.mitre.org/data/definitions/94.html)
- [CWE-96](https://cwe.mitre.org/data/definitions/96.html)
- [CWE-285](https://cwe.mitre.org/data/definitions/285.html)
- [CWE-302](https://cwe.mitre.org/data/definitions/302.html)
- [CWE-473](https://cwe.mitre.org/data/definitions/473.html)
- [CWE-1321](https://cwe.mitre.org/data/definitions/1321.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/77.html
