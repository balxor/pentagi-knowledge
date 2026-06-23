---
capec_id: CAPEC-206
name: Signing Malicious Code
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: Very High
related_cwe: [CWE-732]
related_attack: [T1553.002]
url: https://capec.mitre.org/data/definitions/206.html
tags: [mitre-capec, attack-pattern, CAPEC-206]
---

# CAPEC-206 - Signing Malicious Code

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** Very High  -  **CAPEC:** [CAPEC-206](https://capec.mitre.org/data/definitions/206.html)

## Description
The adversary extracts credentials used for code signing from a production environment and then uses these credentials to sign malicious content with the developer's key. Many developers use signing keys to sign code or hashes of code. When users or applications verify the signatures are accurate they are led to believe that the code came from the owner of the signing key and that the code has not been modified since the signature was applied. If the adversary has extracted the signing credentials then they can use those credentials to sign their own code bundles. Users or tools that verify the signatures attached to the code will likely assume the code came from the legitimate developer and install or run the code, effectively allowing the adversary to execute arbitrary code on the victim's computer. This differs from CAPEC-673, because the adversary is performing the code signing.

## Prerequisites
- The targeted developer must use a signing key to sign code bundles. (Note that not doing this is not a defense - it only means that the adversary does not need to steal the signing key before forging code bundles in the developer's name.)

## Resources required
- None: No specialized resources are required to execute this type of attack.

## Execution flow
Execution Flow Explore The adversary first attempts to obtain a digital certificate in order to sign their malware or tools. This certificate could be stolen, created by the adversary, or acquired normally through a certificate authority. Based on the type of certificate obtained, the adversary will create a goal for their attack. This is either a broad or targeted attack. If an adversary was able to steal a certificate from a targeted organization, they could target this organization by pretending to have legitimate code signed by them. In other cases, the adversary would simply sign their malware and pose as legitimate software such that any user might trust it. This is the more broad approach Experiment The adversary creates their malware and signs it with the obtained digital certificate. The adversary then checks if the code that they signed is valid either through downloading from the targeted source or testing locally. Exploit Once the malware has been signed, it is then deployed to the desired location. They wait for a trusting user to run their malware, thinking that it is legitimate software. This malware could do a variety of things based on the motivation of the adversary.

## Mitigations
- Ensure digital certificates are protected and inaccessible by unauthorized uses.
- If a digital certificate has been compromised it should be revoked and regenerated.
- Even if a piece of software has a valid and trusted digital signature, it should be assessed for any weaknesses and vulnerabilities.

## Related weaknesses (CWE)
- [CWE-732](https://cwe.mitre.org/data/definitions/732.html)

## Related ATT&CK techniques
- T1553.002

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/206.html
