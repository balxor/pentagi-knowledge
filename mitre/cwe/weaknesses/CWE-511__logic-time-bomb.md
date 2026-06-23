---
cwe_id: CWE-511
name: Logic/Time Bomb
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Mobile]
related_capec: []
url: https://cwe.mitre.org/data/definitions/511.html
tags: [mitre-cwe, weakness, CWE-511]
---

# CWE-511 - Logic/Time Bomb

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-511](https://cwe.mitre.org/data/definitions/511.html)

## Description
The product contains code that is designed to disrupt the legitimate operation of the product (or its environment) when a certain time passes, or when a certain logical condition is met.

## Extended description
When the time bomb or logic bomb is detonated, it may perform a denial of service such as crashing the system, deleting critical data, or degrading system response time. This bomb might be placed within either a replicating or non-replicating Trojan horse.

## Applicable platforms / languages
Not Language-Specific, Mobile

## Common consequences
- **Other, Integrity**: Varies by Context, Alter Execution Logic

## Potential mitigations
- **Installation**: Always verify the integrity of the product that is being installed.

## Related weaknesses
- CWE-506 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/511.html
