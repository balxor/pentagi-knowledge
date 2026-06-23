---
capec_id: CAPEC-163
name: Spear Phishing
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-451]
related_attack: [T1534, T1566.001, T1566.002, T1566.003, T1598.001, T1598.002, T1598.003]
url: https://capec.mitre.org/data/definitions/163.html
tags: [mitre-capec, attack-pattern, CAPEC-163]
---

# CAPEC-163 - Spear Phishing

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-163](https://capec.mitre.org/data/definitions/163.html)

## Description
An adversary targets a specific user or group with a Phishing (CAPEC-98) attack tailored to a category of users in order to have maximum relevance and deceptive capability. Spear Phishing is an enhanced version of the Phishing attack targeted to a specific user or group. The quality of the targeted email is usually enhanced by appearing to come from a known or trusted entity. If the email account of some trusted entity has been compromised the message may be digitally signed. The message will contain information specific to the targeted users that will enhance the probability that they will follow the URL to the compromised site. For example, the message may indicate knowledge of the targets employment, residence, interests, or other information that suggests familiarity. As soon as the user follows the instructions in the message, the attack proceeds as a standard Phishing attack.

## Prerequisites
- None. Any user can be targeted by a Spear Phishing attack.

## Skills required
- **Medium**: Spear phishing attacks require specific knowledge of the victims being targeted, such as which bank is being used by the victims, or websites they commonly log into (Google, Facebook, etc).

## Resources required
- An adversay must have the ability communicate their phishing scheme to the victims (via email, instance message, etc.), as well as a website or other platform for victims to enter personal information into.

## Consequences
- **Accountability**: Gain Privileges (Privilege Escalation)
- **Authentication**: Gain Privileges (Privilege Escalation)
- **Authorization**: Gain Privileges (Privilege Escalation)
- **Confidentiality**: Read Data (Information Leakage)
- **Integrity**: Modify Data (Data Modification)
- **Non-Repudiation**: Gain Privileges (Privilege Escalation)

## Execution flow
Execution Flow Explore Obtain useful contextual detailed information about the targeted user or organization: An adversary collects useful contextual detailed information about the targeted user or organization in order to craft a more deceptive and enticing message to lure the target into responding. Techniques Conduct web searching research of target. See also: CAPEC-118. Identify trusted associates, colleagues and friends of target. See also: CAPEC-118. Utilize social engineering attack patterns such as Pretexting. See also: CAPEC-407. Collect social information via dumpster diving. See also: CAPEC-406. Collect social information via traditional sources. See also: CAPEC-118. Collect social information via Non-traditional sources. See also: CAPEC-118. Experiment Optional: Obtain domain name and certificate to spoof legitimate site: This optional step can be used to help the adversary impersonate the legitimate site more convincingly. The adversary can use homograph attacks to convince users that they are using the legitimate website. Note that this step is not required for phishing attacks, and many phishing attacks simply supply URLs containing an IP address and no SSL certificate. Techniques Optionally obtain a domain name that visually looks similar to the legitimate site's domain name. An example is www.paypaI.com vs. www.paypal.com (the first one contains a capital i, instead of a lower case L). Optionally obtain a legitimate SSL certificate for the new domain name. Optional: Explore legitimate website and create duplicate: An adversary creates a website (optionally at a URL that looks similar to the original URL) that closely resembles the website that they are trying to impersonate. That website will typically have a login form for the victim to put in their authentication credentials. There can be different variations on a theme here. Techniques Use spidering software to get copy of web pages on legitimate site. Manually save copies of required web pages from legitimate site. Create new web pages that have the legitimate site's look at feel, but contain completely new content. Optional: Build variants of the website with very specific user information e.g., living area, etc.: Once the adversary has their website which duplicates a legitimate website, they need to build very custom user related information in it. For example, they could create multiple variants of the website which would target different living area users by providing information such as local news, local weather, etc. so that the user believes this is a new feature from the website. Techniques Integrate localized information in the web pages created to duplicate the original website. Those localized information could be dynamically generated based on unique key or IP address of the future victim. Exploit Convince user to enter sensitive information on adversary's site.: An adversary sends a message (typically an e-mail) to the victim that has some sort of a call to action to get the user to click on the link included in the e-mail (which takes the victim to adversary's website) and log in. The key is to get the victim to believe that the message is coming from a legitimate entity trusted by the victim or with which the victim or does business and that the website pointed to by the URL in the e-mail is the legitimate website. A call to action will usually need to sound legitimate and urgent enough to prompt action from the user. Techniques Send the user a message from a spoofed legitimate-looking e-mail address that asks the user to click on the included link. Place phishing link in post to online forum. Use stolen credentials to log into legitimate site: Once the adversary captures some sensitive information through phishing (login credentials, credit card information, etc.) the adversary can leverage this information. For instance, the adversary can use the victim's login credentials to log into their bank account and transfer money to an account of their choice. Techniques Log in to the legitimate site using another user's supplied credentials.

## Mitigations
- Do not follow any links that you receive within your e-mails and certainly do not input any login credentials on the page that they take you too. Instead, call your Bank, PayPal, eBay, etc., and inquire about the problem. A safe practice would also be to type the URL of your bank in the browser directly and only then log in. Also, never reply to any e-mails that ask you to provide sensitive information of any kind.

## Related weaknesses (CWE)
- [CWE-451](https://cwe.mitre.org/data/definitions/451.html)

## Related ATT&CK techniques
- T1534
- T1566.001
- T1566.002
- T1566.003
- T1598.001
- T1598.002
- T1598.003

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/163.html
