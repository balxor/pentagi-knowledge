---
cwe_id: CWE-1426
name: Improper Validation of Generative AI Output
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not Architecture-Specific, AI/ML, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1426.html
tags: [mitre-cwe, weakness, CWE-1426]
---

# CWE-1426 - Improper Validation of Generative AI Output

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1426](https://cwe.mitre.org/data/definitions/1426.html)

## Description
The product invokes a generative AI/ML component whose behaviors and outputs cannot be directly controlled, but the product does not validate or insufficiently validates the outputs to ensure that they align with the intended security, content, or privacy policy.

## Applicable platforms / languages
Not Language-Specific, Not Architecture-Specific, AI/ML, Not Technology-Specific

## Common consequences
- **Integrity**: Execute Unauthorized Code or Commands, Varies by Context

## Potential mitigations
- **Architecture and Design**: Since the output from a generative AI component (such as an LLM) cannot be trusted, ensure that it operates in an untrusted or non-privileged space.
- **Operation**: Use "semantic comparators," which are mechanisms that provide semantic comparison to identify objects that might appear different but are semantically similar.
- **Operation**: Use components that operate externally to the system to monitor the output and act as a moderator. These components are called different terms, such as supervisors or guardrails.
- **Build and Compilation**: During model training, use an appropriate variety of good and bad examples to guide preferred outputs.

## Related weaknesses
- CWE-707 (ChildOf)

## Observed examples (CVE)
- **CVE-2024-3402**: chain: GUI for ChatGPT API performs input validation but does not properly "sanitize" or validate model output data (CWE-1426), leading to XSS (CWE-79).

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1426.html
