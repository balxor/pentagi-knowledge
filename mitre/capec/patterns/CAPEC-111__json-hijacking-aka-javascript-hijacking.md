---
capec_id: CAPEC-111
name: JSON Hijacking (aka JavaScript Hijacking)
type: attack-pattern
abstraction: Standard
likelihood: High
severity: High
related_cwe: [CWE-345, CWE-346, CWE-352]
related_attack: []
url: https://capec.mitre.org/data/definitions/111.html
tags: [mitre-capec, attack-pattern, CAPEC-111]
---

# CAPEC-111 - JSON Hijacking (aka JavaScript Hijacking)

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-111](https://capec.mitre.org/data/definitions/111.html)

## Description
An attacker targets a system that uses JavaScript Object Notation (JSON) as a transport mechanism between the client and the server (common in Web 2.0 systems using AJAX) to steal possibly confidential information transmitted from the server back to the client inside the JSON object by taking advantage of the loophole in the browser's Same Origin Policy that does not prohibit JavaScript from one website to be included and executed in the context of another website.

## Extended description
An attacker gets the victim to visit their malicious page that contains a script tag whose source points to the vulnerable system with a URL that requests a response from the server containing a JSON object with possibly confidential information. The malicious page also contains malicious code to capture the JSON object returned by the server before any other processing on it can take place, typically by overriding the JavaScript function used to create new objects. This hook allows the malicious code to get access to the creation of each object and transmit the possibly sensitive contents of the captured JSON object to the attackers' server. There is nothing in the browser's security model to prevent the attackers' malicious JavaScript code (originating from attacker's domain) to set up an environment (as described above) to intercept a JSON object response (coming from the vulnerable target system's domain), read its contents and transmit to the attackers' controlled site. The same origin policy protects the domain object model (DOM), but not the JSON.

## Prerequisites
- JSON is used as a transport mechanism between the client and the server
- The target server cannot differentiate real requests from forged requests
- The JSON object returned from the server can be accessed by the attackers' malicious code via a script tag

## Skills required
- **Medium**: Once this attack pattern is developed and understood, creating an exploit is not very complex.The attacker needs to have knowledge of the URLs that need to be accessed on the target system to request the JSON objects.

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Consequences
- **Confidentiality**: Read Data

## Execution flow
Execution Flow Explore Understand How to Request JSON Responses from the Target System: An attacker first explores the target system to understand what URLs need to be provided to it in order to retrieve JSON objects that contain information of interest to the attacker. Techniques An attacker creates an account with the target system and observes requests and the corresponding JSON responses from the server. Understanding how to properly elicit responses from the server is crucial to the attackers' ability to craft the exploit. Experiment [Craft a malicious website] The attacker crafts a malicious website to which they plan to lure the victim who is using the vulnerable target system. The malicious website does two things: 1. Contains a hook that intercepts incoming JSON objects, reads their contents and forwards the contents to the server controlled by the attacker (via a new XMLHttpRequest). 2. Uses the script tag with a URL in the source that requests a JSON object from the vulnerable target system. Once the JSON object is transmitted to the victim's browser, the malicious code (as described in step 1) intercepts that JSON object, steals its contents, and forwards to the attacker. This attack step leverages the fact that the same origin policy in the browser does not protect JavaScript originating from one domain from setting up an environment to intercept and access JSON objects arriving from a completely different domain. Exploit Launch JSON hijack: An attacker lures the victim to the malicious website or leverages other means to get their malicious code executing in the victim's browser. Once that happens, the malicious code makes a request to the victim target system to retrieve a JSON object with sensitive information. The request includes the victim's session cookie if the victim is logged in. Techniques An attacker employs a myriad of standard techniques to get the victim to visit their malicious site or by some other means get the attackers' malicious code executing in the victim's browser.

## Mitigations
- Ensure that server side code can differentiate between legitimate requests and forged requests. The solution is similar to protection against Cross Site Request Forger (CSRF), which is to use a hard to guess random nonce (that is unique to the victim's session with the server) that the attacker has no way of knowing (at least in the absence of other weaknesses). Each request from the client to the server should contain this nonce and the server should reject all requests that do not contain the nonce.
- On the client side, the system's design could make it difficult to get access to the JSON object content via the script tag. Since the JSON object is never assigned locally to a variable, it cannot be readily modified by the attacker before being used by a script tag. For instance, if while(1) was added to the beginning of the JavaScript returned by the server, trying to access it with a script tag would result in an infinite loop. On the other hand, legitimate client side code can remove the while(1) statement after which the JavaScript can be evaluated. A similar result can be achieved by surrounding the returned JavaScript with comment tags, or using other similar techniques (e.g. wrapping the JavaScript with HTML tags).
- Make the URLs in the system used to retrieve JSON objects unpredictable and unique for each user session.
- Ensure that to the extent possible, no sensitive data is passed from the server to the client via JSON objects. JavaScript was never intended to play that role, hence the same origin policy does not adequate address this scenario.

## Related weaknesses (CWE)
- [CWE-345](https://cwe.mitre.org/data/definitions/345.html)
- [CWE-346](https://cwe.mitre.org/data/definitions/346.html)
- [CWE-352](https://cwe.mitre.org/data/definitions/352.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/111.html
