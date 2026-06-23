---
capec_id: CAPEC-164
name: Mobile Phishing
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-451]
related_attack: []
url: https://capec.mitre.org/data/definitions/164.html
tags: [mitre-capec, attack-pattern, CAPEC-164]
---

# CAPEC-164 - Mobile Phishing

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-164](https://capec.mitre.org/data/definitions/164.html)

## Description
An adversary targets mobile phone users with a phishing attack for the purpose of soliciting account passwords or sensitive information from the user. Mobile Phishing is a variation of the Phishing social engineering technique where the attack is initiated via a text or SMS message, rather than email. The user is enticed to provide information or visit a compromised web site via this message. Apart from the manner in which the attack is initiated, the attack proceeds as a standard Phishing attack.

## Prerequisites
- An adversary needs mobile phone numbers to initiate contact with the victim.
- An adversary needs to correctly guess the entity with which the victim does business and impersonate it. Most of the time phishers just use the most popular banks/services and send out their "hooks" to many potential victims.
- An adversary needs to have a sufficiently compelling call to action to prompt the user to take action.
- The replicated website needs to look extremely similar to the original website and the URL used to get to that website needs to look like the real URL of the said business entity.

## Skills required
- **Medium**: Basic knowledge about websites: obtaining them, designing and implementing them, etc.

## Resources required
- Either mobile phone or access to a web resource that allows text messages to be sent to mobile phones. Resources needed for regular Phishing attack.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Obtain domain name and certificate to spoof legitimate site: This optional step can be used to help the adversary impersonate the legitimate site more convincingly. The adversary can use homograph or similar attacks to convince users that they are using the legitimate website. Note that this step is not required for phishing attacks, and many phishing attacks simply supply URLs containing an IP address and no SSL certificate. Techniques Optionally obtain a domain name that visually looks similar to the legitimate site's domain name. An example is www.paypaI.com vs. www.paypal.com (the first one contains a capital i, instead of a lower case L) Optionally obtain a legitimate SSL certificate for the new domain name. Explore legitimate website and create duplicate: An adversary creates a website (optionally at a URL that looks similar to the original URL) that closely resembles the website that they are trying to impersonate. That website will typically have a login form for the victim to put in their authentication credentials. There can be different variations on a theme here. Techniques Use spidering software to get copy of web pages on legitimate site. Manually save copies of required web pages from legitimate site. Create new web pages that have the legitimate site's look and feel, but contain completely new content. Exploit Convince user to enter sensitive information on adversary's site.: An adversary sends a text message to the victim that has a call-to-action, in order to persuade the user into clicking the included link (which then takes the victim to the adversary's website) and logging in. The key is to get the victim to believe that the text message originates from a legitimate entity with which the victim does business and that the website pointed to by the URL in the text message is the legitimate website. A call-to-action will usually need to sound legitimate and urgent enough to prompt action from the user. Techniques Send the user a message from a spoofed legitimate-looking mobile number that asks the user to click on the included link. Use stolen credentials to log into legitimate site: Once the adversary captures some sensitive information through phishing (login credentials, credit card information, etc.) the adversary can leverage this information. For instance, the adversary can use the victim's login credentials to log into their bank account and transfer money to an account of their choice. Techniques Log in to the legitimate site using another user's supplied credentials

## Mitigations
- Do not follow any links that you receive within text messages and do not input any login credentials on the page that they take you too. Instead, call your Bank, PayPal, eBay, etc., and inquire about the problem. Safe practices also include leveraging the entity's mobile application or directly typing the entity's URL in the browser and only then logging in. Never reply to any text messages that ask you to provide sensitive information of any kind.

## Related weaknesses (CWE)
- [CWE-451](https://cwe.mitre.org/data/definitions/451.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/164.html
