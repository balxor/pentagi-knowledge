---
cwe_id: CWE-206
name: Observable Internal Behavioral Discrepancy
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/206.html
tags: [mitre-cwe, weakness, CWE-206]
---

# CWE-206 - Observable Internal Behavioral Discrepancy

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-206](https://cwe.mitre.org/data/definitions/206.html)

## Description
The product performs multiple behaviors that are combined to produce a single result, but the individual behaviors are observable separately in a way that allows attackers to reveal internal state or internal decision points.

## Extended description
Ideally, a product should provide as little information as possible to an attacker. Any hints that the attacker may be making progress can then be used to simplify or optimize the attack. For example, in a login procedure that requires a username and password, ultimately there is only one decision: success or failure. However, internally, two separate actions are performed: determining if the username exists, and checking if the password is correct. If the product behaves differently based on whether the username exists or not, then the attacker only needs to concentrate on the password.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality, Access Control**: Read Application Data, Bypass Protection Mechanism

## Potential mitigations
- **general**: Setup generic response pages for error conditions. The error page should not disclose information about the success or failure of a sensitive operation. For instance, the login page should not confirm that the login is correct and the password incorrect. The attacker who tries random account name may be able to guess some of them. Confirming that the account exists would make the login page more susceptible to brute force attack.

## Related weaknesses
- CWE-205 (ChildOf)

## Observed examples (CVE)
- **CVE-2002-2031**: File existence via infoleak monitoring whether "onerror" handler fires or not.
- **CVE-2005-2025**: Valid groupname enumeration via behavioral infoleak (sends response if valid, doesn't respond if not).
- **CVE-2001-1497**: Behavioral infoleak in GUI allows attackers to distinguish between alphanumeric and non-alphanumeric characters in a password, thus reducing the search space.
- **CVE-2003-0190**: Product immediately sends an error message when user does not exist instead of waiting until the password is provided, allowing username enumeration.

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/206.html
