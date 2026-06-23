---
capec_id: CAPEC-174
name: Flash Parameter Injection
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: Medium
related_cwe: [CWE-88]
related_attack: []
url: https://capec.mitre.org/data/definitions/174.html
tags: [mitre-capec, attack-pattern, CAPEC-174]
---

# CAPEC-174 - Flash Parameter Injection

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-174](https://capec.mitre.org/data/definitions/174.html)

## Description
An adversary takes advantage of improper data validation to inject malicious global parameters into a Flash file embedded within an HTML document. Flash files can leverage user-submitted data to configure the Flash document and access the embedding HTML document.

## Extended description
These 'FlashVars' are most often passed to the Flash file via URL arguments or from the Object or Embed tag within the embedding HTML document. If these FlashVars are not properly sanitized, an adversary may be able to embed malicious content (such as scripts) into the HTML document. The injected parameters can also provide the adversary control over other objects within the Flash file as well as full control over the parent document's DOM model. As such, this is a form of HTTP parameter injection, but the abilities granted to the Flash document (such as access to a page's document model, including associated cookies) make this attack more flexible. Flash Parameter Injection attacks can also preface further attacks such as various forms of Cross-Site Scripting (XSS) attacks in addition to Session Hijacking attacks.

## Skills required
- **Medium**: The adversary need inject values into the global parameters to the Flash file and understand the parent HTML document DOM structure. The adversary needs to be smart enough to convince the victim to click on their crafted link.

## Resources required
- The adversary must convince the victim to click their crafted link.

## Consequences
- **Authorization**: Execute Unauthorized Commands (Run Arbitrary Code)
- **Confidentiality**: Other (Information Leakage)

## Execution flow
Execution Flow Explore Spider: Using a browser or an automated tool, an adversary records all instances of HTML documents that have embedded Flash files. If there is an embedded Flash file, they list how to pass global parameters to the Flash file from the embedding object. Techniques Use an automated tool to record all instances of URLs which have embedded Flash files and list the parameters passing to the Flash file. Use a browser to manually explore the website to see whether the HTML document has embedded Flash files or not and list the parameters passing to the Flash file. Experiment Determine the application susceptibility to Flash parameter injection: Determine the application susceptibility to Flash parameter injection. For each URL identified in the Explore phase, the adversary attempts to use various techniques such as DOM based, reflected, flashvars, and persistent attacks depending on the type of parameter passed to the embedded Flash file. Techniques When the JavaScript 'document.location' variable is used as part of the parameter, inject '#' and the payload into the parameter in the URL. When the name of the Flash file is exposed as a form or a URL parameter, the adversary injects '?' and the payload after the file name in the URL to override some global value. When the arguments passed in the 'flashvars' attributes, the adversary injects '&' and payload in the URL. If some of the attributes of the tag are received as parameters, the 'flashvars' attribute is injected into the tag without the creator of the Web page ever intending to allow arguments to be passed into the Flash file. If shared objects are used to save data that is entered by the user persistent Flash parameter injection may occur, with malicious code being injected into the Flash file and executed, every time the Flash file is loaded. Exploit Execute Flash Parameter Injection Attack: Inject parameters into Flash file. Based on the results of the Experiment phase, the adversary crafts the underlying malicious URL containing injected Flash parameters and submits it to the web server. Once the web server receives the request, the embedding HTML document will controllable by the adversary. Techniques Craft underlying malicious URL and send it to the web server to take control of the embedding HTML document.

## Mitigations
- User input must be sanitized according to context before reflected back to the user. The JavaScript function 'encodeURI' is not always sufficient for sanitizing input intended for global Flash parameters. Extreme caution should be taken when saving user input in Flash cookies. In such cases the Flash file itself will need to be fixed and recompiled, changing the name of the local shared objects (Flash cookies).

## Related weaknesses (CWE)
- [CWE-88](https://cwe.mitre.org/data/definitions/88.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/174.html
