---
capec_id: CAPEC-656
name: Voice Phishing
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/656.html
tags: [mitre-capec, attack-pattern, CAPEC-656]
---

# CAPEC-656 - Voice Phishing

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-656](https://capec.mitre.org/data/definitions/656.html)

## Description
An adversary targets users with a phishing attack for the purpose of soliciting account passwords or sensitive information from the user. Voice Phishing is a variation of the Phishing social engineering technique where the attack is initiated via a voice call, rather than email. The user is enticed to provide sensitive information by the adversary, who masquerades as a legitimate employee of the alleged organization. Voice Phishing attacks deviate from standard Phishing attacks, in that a user doesn't typically interact with a compromised website to provide sensitive information and instead provides this information verbally. Voice Phishing attacks can also be initiated by either the adversary in the form of a "cold call" or by the victim if calling an illegitimate telephone number.

## Prerequisites
- An adversary needs phone numbers to initiate contact with the victim, in addition to a legitimate-looking telephone number to call the victim from.
- An adversary needs to correctly guess the entity with which the victim does business and impersonate it. Most of the time phishers just use the most popular banks/services and send out their "hooks" to many potential victims.
- An adversary needs to have a sufficiently compelling call to action to prompt the user to take action.
- If passively conducting this attack via a spoofed website, replicated website needs to look extremely similar to the original website and the URL used to get to that website needs to look like the real URL of the said business entity.

## Skills required
- **Medium**: Basic knowledge about websites: obtaining them, designing and implementing them, etc.

## Resources required
- Legitimate-looking telephone number(s) to initiate calls with victims

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Obtain domain name and certificate to spoof legitimate site: This optional step can be used to help the adversary impersonate the legitimate organization more convincingly. The adversary can use homograph or similar attacks to convince users that they are using the legitimate website. If the adversary leverages cold-calling for this attack, this step is skipped. Techniques Optionally obtain a domain name that visually looks similar to the legitimate organization's domain name. An example is www.paypaI.com vs. www.paypal.com (the first one contains a capital i, instead of a lower case L) Optionally obtain a legitimate SSL certificate for the new domain name. Explore legitimate website and create duplicate: An adversary optionally creates a website (optionally at a URL that looks similar to the original URL) that closely resembles the organization's website that they are trying to impersonate. That website will contain a telephone number for the victim to call to assist them with their issue and initiate the attack. If the adversary leverages cold-calling for this attack, this step is skipped. Techniques Use spidering software to get copy of web pages on legitimate site. Manually save copies of required web pages from legitimate site. Create new web pages that have the legitimate site's look and feel, but contain completely new content. Exploit Convince user to provide sensitive information to the adversary.: An adversary "cold calls" the victim or receives a call from the victim via the malicious site and provides a call-to-action, in order to persuade the user into providing sensitive details to the adversary (e.g. login credentials, bank account information, etc.). The key is to get the victim to believe that the individual they are talking to is from a legitimate entity with which the victim does business and that the call is occurring for legitimate reasons. A call-to-action will usually need to sound legitimate and urgent enough to prompt action from the user. Techniques Call the user a from a spoofed legitimate-looking telephone number. Use stolen information: Once the adversary obtains the sensitive information, this information can be leveraged to log into the victim's bank account and transfer money to an account of their choice, or to make fraudulent purchases with stolen credit card information. Techniques Login to the legitimate site using another the victim's supplied credentials

## Mitigations
- Do not accept calls from unknown numbers or from numbers that may be flagged as spam. Also, do not call numbers that appear on-screen after being unexpectedly redirected to potentially malicious websites. In either case, do not provide sensitive information over voice calls that are not legitimately initiated. Instead, call your Bank, PayPal, eBay, etc., via the number on their public-facing website and inquire about the problem.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/656.html
