---
capec_id: CAPEC-101
name: Server Side Include (SSI) Injection
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-97, CWE-74, CWE-20]
related_attack: []
url: https://capec.mitre.org/data/definitions/101.html
tags: [mitre-capec, attack-pattern, CAPEC-101]
---

# CAPEC-101 - Server Side Include (SSI) Injection

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-101](https://capec.mitre.org/data/definitions/101.html)

## Description
An attacker can use Server Side Include (SSI) Injection to send code to a web application that then gets executed by the web server. Doing so enables the attacker to achieve similar results to Cross Site Scripting, viz., arbitrary code execution and information disclosure, albeit on a more limited scale, since the SSI directives are nowhere near as powerful as a full-fledged scripting language. Nonetheless, the attacker can conveniently gain access to sensitive files, such as password files, and execute shell commands.

## Prerequisites
- A web server that supports server side includes and has them enabled
- User controllable input that can carry include directives to the web server

## Skills required
- **Medium**: The attacker needs to be aware of SSI technology, determine the nature of injection and be able to craft input that results in the SSI directives being executed.

## Resources required
- None: No specialized resources are required to execute this type of attack. Determining whether the server supports SSI does not require special tools, and nor does injecting directives that get executed. Spidering tools can make the task of finding and following links easier.

## Consequences
- **Availability**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Read Data, Execute Unauthorized Commands (Run Arbitrary Code)
- **Integrity**: Execute Unauthorized Commands (Run Arbitrary Code)

## Execution flow
Execution Flow Explore Determine applicability: The adversary determines whether server side includes are enabled on the target web server. Techniques Look for popular page file names. The attacker will look for .shtml, .shtm, .asp, .aspx, and other well-known strings in URLs to help determine whether SSI functionality is enabled. Fetch .htaccess file. In Apache web server installations, the .htaccess file may enable server side includes in specific locations. In those cases, the .htaccess file lives inside the directory where SSI is enabled, and is theoretically fetchable from the web server. Although most web servers deny fetching the .htaccess file, a misconfigured server will allow it. Thus, an attacker will frequently try it. Experiment Find Injection Point: Look for user controllable input, including HTTP headers, that can carry server side include directives to the web server. Techniques Use a spidering tool to follow and record all links. Make special note of any links that include parameters in the URL. Use a proxy tool to record all links visited during a manual traversal of the web application. Make special note of any links that include parameters in the URL. Manual traversal of this type is frequently necessary to identify forms that are GET method forms rather than POST forms. Exploit Inject SSI: Using the found injection point, the adversary sends arbitrary code to be inlcuded by the application on the server side. They may then need to view a particular page in order to have the server execute the include directive and run a command or open a file on behalf of the adversary.

## Mitigations
- Set the OPTIONS IncludesNOEXEC in the global access.conf file or local .htaccess (Apache) file to deny SSI execution in directories that do not need them
- All user controllable input must be appropriately sanitized before use in the application. This includes omitting, or encoding, certain characters or strings that have the potential of being interpreted as part of an SSI directive
- Server Side Includes must be enabled only if there is a strong business reason to do so. Every additional component enabled on the web server increases the attack surface as well as administrative overhead

## Related weaknesses (CWE)
- [CWE-97](https://cwe.mitre.org/data/definitions/97.html)
- [CWE-74](https://cwe.mitre.org/data/definitions/74.html)
- [CWE-20](https://cwe.mitre.org/data/definitions/20.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/101.html
