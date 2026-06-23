---
cwe_id: CWE-777
name: Regular Expression without Anchors
type: weakness
abstraction: Variant
status: Incomplete
languages: [Not Language-Specific, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/777.html
tags: [mitre-cwe, weakness, CWE-777]
---

# CWE-777 - Regular Expression without Anchors

**Abstraction:** Variant  -  **Status:** Incomplete  -  **CWE:** [CWE-777](https://cwe.mitre.org/data/definitions/777.html)

## Description
The product uses a regular expression to perform neutralization, but the regular expression is not anchored and may allow malicious or malformed data to slip through.

## Extended description
When performing tasks such as validating against a set of allowed inputs (allowlist), data is examined and possibly modified to ensure that it is well-formed and adheres to a list of safe values. If the regular expression is not anchored, malicious or malformed data may be included before or after any string matching the regular expression. The type of malicious data that is allowed will depend on the context of the application and which anchors are omitted from the regular expression.

## Applicable platforms / languages
Not Language-Specific, Not Technology-Specific

## Common consequences
- **Availability, Confidentiality, Access Control**: Bypass Protection Mechanism

## Potential mitigations
- **Implementation**: Be sure to understand both what will be matched and what will not be matched by a regular expression. Anchoring the ends of the expression will allow the programmer to define an allowlist strictly limited to what is matched by the text in the regular expression. If you are using a package that only matches one line by default, ensure that you can match multi-line inputs if necessary.

## Related weaknesses
- CWE-625 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-30034**: Chain: Web UI for a Python RPC framework does not use regex anchors to validate user login emails (CWE-777), potentially allowing bypass of OAuth (CWE-1390).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/777.html
