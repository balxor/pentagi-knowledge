---
cwe_id: CWE-512
name: Spyware
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/512.html
tags: [mitre-cwe, weakness, CWE-512]
---

# CWE-512 - Spyware

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-512](https://cwe.mitre.org/data/definitions/512.html)

## Description
The product collects personally identifiable information about a human user or the user's activities, but the product accesses this information using other resources besides itself, and it does not require that user's explicit approval or direct input into the product.

## Extended description
"Spyware" is a commonly used term with many definitions and interpretations. In general, it is meant to refer to products that collect information or install functionality that human users might not allow if they were fully aware of the actions being taken by the software. For example, a user might expect that tax software would collect a social security number and include it when filing a tax return, but that same user would not expect gaming software to obtain the social security number from that tax software's data.

## Applicable platforms / languages
Not Language-Specific

## Common consequences
- **Confidentiality**: Read Application Data

## Potential mitigations
- **Operation**: Use spyware detection and removal software.
- **Installation**: Always verify the integrity of the product that is being installed.

## Related weaknesses
- CWE-506 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/512.html
