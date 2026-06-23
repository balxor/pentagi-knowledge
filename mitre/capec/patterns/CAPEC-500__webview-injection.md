---
capec_id: CAPEC-500
name: WebView Injection
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: [CWE-749, CWE-940]
related_attack: []
url: https://capec.mitre.org/data/definitions/500.html
tags: [mitre-capec, attack-pattern, CAPEC-500]
---

# CAPEC-500 - WebView Injection

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-500](https://capec.mitre.org/data/definitions/500.html)

## Description
An adversary, through a previously installed malicious application, injects code into the context of a web page displayed by a WebView component. Through the injected code, an adversary is able to manipulate the DOM tree and cookies of the page, expose sensitive information, and can launch attacks against the web application from within the web page.

## Prerequisites
- An adversary must be able install a purpose built malicious application onto the device and convince the user to execute it. The malicious application is designed to target a specific web application and is used to load the target web pages via the WebView component. For example, an adversary may develop an application that interacts with Facebook via WebView and adds a new feature that a user desires. The user would install this 3rd party app instead of the Facebook app.

## Execution flow
Execution Flow Explore Determine target web application: An adversary first needs to determine what web application they wish to target. Techniques Target web applications that require users to enter sensitive information. Target web applications that an adversary wishes to operate on behalf of a logged in user. Experiment Create malicious application: An adversary creates an application, often mobile, that incorporates a WebView component to display the targeted web application. This malicious application needs to downloaded by a user, so adversaries will make this application useful in some way. Techniques Create a 3rd party application that adds useful functionality to the targeted web application. Victims will download the application as a means of using the targeted web application. Create a fun game that at some point directs a user to the targeted web application. For example, prompt the user to buy in game currency by directing them to PayPal. Get the victim to download and run the application: An adversary needs to get the victim to willingly download and run the application. Techniques Pay for App Store advertisements Promote the application on social media, either through accounts made by the adversary or by paying for other accounts to advertise. Exploit Inject malicious code: Once the victim runs the malicious application and views the targeted web page in the WebView component, the malicious application will inject malicious JavaScript code into the web application. This is done by using WebView's loadURL() API, which can inject arbitrary JavaScript code into pages loaded by the WebView component with the same privileges. This is often done by adding a script tag to the document body with a src destination to a remote location that serves malicious JavaScript code. Techniques Execute operations on the targeted web page on behalf of an authenticated user. Steal cookie information from the victim. Add in extra fields to the DOM in an attempt to get a user to divulge sensitive information.

## Mitigations
- The only known mitigation to this type of attack is to keep the malicious application off the system. There is nothing that can be done to the target application to protect itself from a malicious application that has been installed and executed.

## Related weaknesses (CWE)
- [CWE-749](https://cwe.mitre.org/data/definitions/749.html)
- [CWE-940](https://cwe.mitre.org/data/definitions/940.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/500.html
