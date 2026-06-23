---
capec_id: CAPEC-468
name: Generic Cross-Browser Cross-Domain Theft
type: attack-pattern
abstraction: Standard
likelihood: n/a
severity: Medium
related_cwe: [CWE-707, CWE-149, CWE-177, CWE-838]
related_attack: []
url: https://capec.mitre.org/data/definitions/468.html
tags: [mitre-capec, attack-pattern, CAPEC-468]
---

# CAPEC-468 - Generic Cross-Browser Cross-Domain Theft

**Abstraction:** Standard  -  **Likelihood:** n/a  -  **Severity:** Medium  -  **CAPEC:** [CAPEC-468](https://capec.mitre.org/data/definitions/468.html)

## Description
An attacker makes use of Cascading Style Sheets (CSS) injection to steal data cross domain from the victim's browser. The attack works by abusing the standards relating to loading of CSS: 1. Send cookies on any load of CSS (including cross-domain) 2. When parsing returned CSS ignore all data that does not make sense before a valid CSS descriptor is found by the CSS parser.

## Extended description
By having control of some text in the victim's domain, the attacker is able to inject a seemingly valid CSS string. It does not matter if this CSS string is preceded by other data. The CSS parser will still locate the CSS string. If the attacker is able to control two injection points, one before the cross domain data that the attacker is interested in receiving and the other one after, the attacker can use this attack to steal all of the data in between these two CSS injection points when referencing the injected CSS while performing rendering on the site that the attacker controls. When rendering, the CSS parser will detect the valid CSS string to parse and ignore the data that "does not make sense". That data will simply be rendered. That data is in fact the data that the attacker just stole cross domain. The stolen data may contain sensitive information, such CSRF protection tokens.

## Prerequisites
- No new lines can be present in the injected CSS stringProper HTML or URL escaping of the " and ' characters is not presentThe attacker has control of two injection points: pre-string and post-string

## Skills required
- **High**: Ability to craft a CSS injection

## Resources required
- Attacker controlled site/page to render a page referencing the injected CSS string

## Mitigations
- Design: Prior to performing CSS parsing, require the CSS to start with well-formed CSS when it is a cross-domain load and the MIME type is broken. This is a browser level fix.
- Implementation: Perform proper HTML encoding and URL escaping

## Related weaknesses (CWE)
- [CWE-707](https://cwe.mitre.org/data/definitions/707.html)
- [CWE-149](https://cwe.mitre.org/data/definitions/149.html)
- [CWE-177](https://cwe.mitre.org/data/definitions/177.html)
- [CWE-838](https://cwe.mitre.org/data/definitions/838.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/468.html
