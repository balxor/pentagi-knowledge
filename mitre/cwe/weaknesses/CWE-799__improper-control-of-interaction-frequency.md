---
cwe_id: CWE-799
name: Improper Control of Interaction Frequency
type: weakness
abstraction: Class
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific, Web Based, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/799.html
tags: [mitre-cwe, weakness, CWE-799]
---

# CWE-799 - Improper Control of Interaction Frequency

**Abstraction:** Class  -  **Status:** Incomplete  -  **CWE:** [CWE-799](https://cwe.mitre.org/data/definitions/799.html)

## Description
The product does not properly limit the number or frequency of interactions that it has with an actor, such as the number of incoming requests.

## Extended description
This can allow the actor to perform actions more frequently than expected. The actor could be a human or an automated process such as a virus or bot. This could be used to cause a denial of service, compromise program logic (such as limiting humans to a single vote), or other consequences. For example, an authentication routine might not limit the number of times an attacker can guess a password. Or, a web site might conduct a poll but only expect humans to vote a maximum of once a day.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific, Web Based, Web Server

## Common consequences
- **Availability, Access Control, Other**: DoS: Resource Consumption (Other), Bypass Protection Mechanism, Other

## Related weaknesses
- CWE-691 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-50653**: Chain: e-commerce product has a "front-end restriction" for coupon use (CWE-602), but the server does not restrict the number of requests for the same coupon (CWE-799)
- **CVE-2002-1876**: Mail server allows attackers to prevent other users from accessing mail by sending large number of rapid requests.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/799.html
