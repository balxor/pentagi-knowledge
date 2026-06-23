---
capec_id: CAPEC-5
name: Blue Boxing
type: attack-pattern
abstraction: Detailed
likelihood: Medium
severity: Very High
related_cwe: [CWE-285]
related_attack: []
url: https://capec.mitre.org/data/definitions/5.html
tags: [mitre-capec, attack-pattern, CAPEC-5]
---

# CAPEC-5 - Blue Boxing

**Abstraction:** Detailed  -  **Likelihood:** Medium  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-5](https://capec.mitre.org/data/definitions/5.html)

## Description
<xhtml:p>This type of attack against older telephone switches and trunks has been around for decades. A tone is sent by an adversary to impersonate a supervisor signal which has the effect of rerouting or usurping command of the line. While the US infrastructure proper may not contain widespread vulnerabilities to this type of attack, many companies are connected globally through call centers and business process outsourcing. These international systems may be operated in countries which have not upgraded Telco infrastructure and so are vulnerable to Blue boxing. Blue boxing is a result of failure on the part of the system to enforce strong authorization for administrative functions. While the infrastructure is different than standard current applications like web applications, there are historical lessons to be learned to upgrade the access control for administrative functions.</xhtml:p>
            <xhtml:p>
               <xhtml:b>This attack pattern is included in CAPEC for historical purposes.</xhtml:b>
            </xhtml:p>

## Prerequisites
- System must use weak authentication mechanisms for administrative functions.

## Skills required
- **Low**: Given a vulnerable phone system, the attackers' technical vector relies on attacks that are well documented in cracker 'zines and have been around for decades.

## Resources required
- CCITT-5 or other vulnerable lines, with the ability to send tones such as combined 2,400 Hz and 2,600 Hz tones to the switch

## Consequences
- **Access_Control**: Gain Privileges
- **Authorization**: Gain Privileges
- **Availability**: Resource Consumption (Denial of Service)
- **Confidentiality**: Gain Privileges

## Mitigations
- Implementation: Upgrade phone lines. Note this may be prohibitively expensive
- Use strong access control such as two factor access control for administrative access to the switch

## Related weaknesses (CWE)
- [CWE-285](https://cwe.mitre.org/data/definitions/285.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/5.html
