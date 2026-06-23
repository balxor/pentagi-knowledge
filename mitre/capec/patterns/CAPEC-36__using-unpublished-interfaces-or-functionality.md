---
capec_id: CAPEC-36
name: Using Unpublished Interfaces or Functionality
type: attack-pattern
abstraction: Standard
likelihood: Medium
severity: High
related_cwe: [CWE-306, CWE-693, CWE-695, CWE-1242]
related_attack: []
url: https://capec.mitre.org/data/definitions/36.html
tags: [mitre-capec, attack-pattern, CAPEC-36]
---

# CAPEC-36 - Using Unpublished Interfaces or Functionality

**Abstraction:** Standard  -  **Likelihood:** Medium  -  **Severity:** High  -  **CAPEC:** [CAPEC-36](https://capec.mitre.org/data/definitions/36.html)

## Description
An adversary searches for and invokes interfaces or functionality that the target system designers did not intend to be publicly available. If interfaces fail to authenticate requests, the attacker may be able to invoke functionality they are not authorized for.

## Extended description
Adversaries can also search for undocumented bits on a hardware device, commonly known as "chicken bits". These bits are used to enable/disable certain functionality, but are not published. Adversaries can reverse engineer firmware to identify hidden features and change these bits at runtime to achieve malicious behavior.

## Prerequisites
- The architecture under attack must publish or otherwise make available services that clients can attach to, either in an unauthenticated fashion, or having obtained an authentication token elsewhere. The service need not be 'discoverable', but in the event it isn't it must have some way of being discovered by an attacker. This might include listening on a well-known port. Ultimately, the likelihood of exploit depends on discoverability of the vulnerable service.

## Skills required
- **Low**: A number of web service digging tools are available for free that help discover exposed web services and their interfaces. In the event that a web service is not listed, the attacker does not need to know much more in addition to the format of web service messages that they can sniff/monitor for.

## Resources required
- None: No specialized resources are required to execute this type of attack. Web service digging tools may be helpful.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Read Data, Gain Privileges

## Execution flow
Execution Flow Explore Identify services: Discover a service of interest by exploring service registry listings or by connecting on a known port or some similar means. Techniques Search via internet for known, published services. Use automated tools to scan known ports to identify internet-enabled services. Dump the code from the chip and then perform reverse engineering to analyze the code. Authenticate to service: Authenticate to the service, if required, in order to explore it. Techniques Use published credentials to access system. Find unpublished credentials to access service. Use other attack pattern or weakness to bypass authentication. Identify all interfaces: Determine the exposed interfaces by querying the registry as well as probably sniffing to expose interfaces that are not explicitly listed. Techniques For any published services, determine exposed interfaces via the documentation provided. For any services found, use error messages from poorly formed service calls to determine valid interfaces. In some cases, services will respond to poorly formed calls with valid ones. Experiment Attempt to discover unpublished functions: Using manual or automated means, discover unpublished or undocumented functions exposed by the service. Techniques Manually attempt calls to the service using an educated guess approach, including the use of terms like' 'test', 'debug', 'delete', etc. Use automated tools to scan the service to attempt to reverse engineer exposed, but undocumented, features. Exploit Exploit unpublished functions: Using information determined via experimentation, exploit the unpublished features of the service. Techniques Execute features that are not intended to be used by general system users. Craft malicious calls to features not intended to be used by general system users that take advantage of security flaws found in the functions.

## Mitigations
- Authenticating both services and their discovery, and protecting that authentication mechanism simply fixes the bulk of this problem. Protecting the authentication involves the standard means, including: 1) protecting the channel over which authentication occurs, 2) preventing the theft, forgery, or prediction of authentication credentials or the resultant tokens, or 3) subversion of password reset and the like.

## Related weaknesses (CWE)
- [CWE-306](https://cwe.mitre.org/data/definitions/306.html)
- [CWE-693](https://cwe.mitre.org/data/definitions/693.html)
- [CWE-695](https://cwe.mitre.org/data/definitions/695.html)
- [CWE-1242](https://cwe.mitre.org/data/definitions/1242.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/36.html
