---
capec_id: CAPEC-98
name: Phishing
type: attack-pattern
abstraction: Standard
likelihood: High
severity: Very High
related_cwe: [CWE-451]
related_attack: [T1566, T1598]
url: https://capec.mitre.org/data/definitions/98.html
tags: [mitre-capec, attack-pattern, CAPEC-98]
---

# CAPEC-98 - Phishing

**Abstraction:** Standard  -  **Likelihood:** High  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-98](https://capec.mitre.org/data/definitions/98.html)

## Description
Phishing is a social engineering technique where an attacker masquerades as a legitimate entity with which the victim might do business in order to prompt the user to reveal some confidential information (very frequently authentication credentials) that can later be used by an attacker. Phishing is essentially a form of information gathering or "fishing" for information.

## Prerequisites
- An attacker needs to have a way to initiate contact with the victim. Typically that will happen through e-mail.
- An attacker needs to correctly guess the entity with which the victim does business and impersonate it. Most of the time phishers just use the most popular banks/services and send out their "hooks" to many potential victims.
- An attacker needs to have a sufficiently compelling call to action to prompt the user to take action.
- The replicated website needs to look extremely similar to the original website and the URL used to get to that website needs to look like the real URL of the said business entity.

## Skills required
- **Medium**: Basic knowledge about websites: obtaining them, designing and implementing them, etc.

## Resources required
- Some web development tools to put up a fake website.

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Confidentiality**: Gain Privileges, Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Obtain domain name and certificate to spoof legitimate site: This optional step can be used to help the attacker impersonate the legitimate site more convincingly. The attacker can use homograph attacks to convince users that they are using the legitimate website. Note that this step is not required for phishing attacks, and many phishing attacks simply supply URLs containing an IP address and no SSL certificate. Techniques Optionally obtain a domain name that visually looks similar to the legitimate site's domain name. An example is www.paypaI.com vs. www.paypal.com (the first one contains a capital i, instead of a lower case L) Optionally obtain a legitimate SSL certificate for the new domain name. Explore legitimate website and create duplicate: An attacker creates a website (optionally at a URL that looks similar to the original URL) that closely resembles the website that they are trying to impersonate. That website will typically have a login form for the victim to put in their authentication credentials. There can be different variations on a theme here. Techniques Use spidering software to get copy of web pages on legitimate site. Manually save copies of required web pages from legitimate site. Create new web pages that have the legitimate site's look and feel, but contain completely new content. Exploit Convince user to enter sensitive information on attacker's site.: An attacker sends an e-mail to the victim that has some sort of a call to action to get the user to click on the link included in the e-mail (which takes the victim to attacker's website) and log in. The key is to get the victim to believe that the e-mail is coming from a legitimate entity with which the victim does business and that the website pointed to by the URL in the e-mail is the legitimate website. A call to action will usually need to sound legitimate and urgent enough to prompt action from the user. Techniques Send the user a message from a spoofed legitimate-looking e-mail address that asks the user to click on the included link. Place phishing link in post to online forum. Use stolen credentials to log into legitimate site: Once the attacker captures some sensitive information through phishing (login credentials, credit card information, etc.) the attacker can leverage this information. For instance, the attacker can use the victim's login credentials to log into their bank account and transfer money to an account of their choice. Techniques Log in to the legitimate site using another user's supplied credentials

## Mitigations
- Do not follow any links that you receive within your e-mails and certainly do not input any login credentials on the page that they take you too. Instead, call your Bank, PayPal, eBay, etc., and inquire about the problem. A safe practice would also be to type the URL of your bank in the browser directly and only then log in. Also, never reply to any e-mails that ask you to provide sensitive information of any kind.

## Related weaknesses (CWE)
- [CWE-451](https://cwe.mitre.org/data/definitions/451.html)

## Related ATT&CK techniques
- T1566
- T1598

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/98.html
