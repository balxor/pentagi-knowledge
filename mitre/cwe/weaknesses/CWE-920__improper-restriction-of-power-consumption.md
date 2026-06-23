---
cwe_id: CWE-920
name: Improper Restriction of Power Consumption
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Mobile]
related_capec: []
url: https://cwe.mitre.org/data/definitions/920.html
tags: [mitre-cwe, weakness, CWE-920]
---

# CWE-920 - Improper Restriction of Power Consumption

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-920](https://cwe.mitre.org/data/definitions/920.html)

## Description
The product operates in an environment in which power is a limited resource that cannot be automatically replenished, but the product does not properly restrict the amount of power that its operation consumes.

## Extended description
In environments such as embedded or mobile devices, power can be a limited resource such as a battery, which cannot be automatically replenished by the product itself, and the device might not always be directly attached to a reliable power source. If the product uses too much power too quickly, then this could cause the device (and subsequently, the product) to stop functioning until power is restored, or increase the financial burden on the device owner because of increased power costs. Normal operation of an application will consume power. However, in some cases, an attacker could cause the application to consume more power than intended, using components such as: Display CPU Disk I/O GPS Sound Microphone USB interface

## Applicable platforms / languages
Not Language-Specific, Mobile

## Common consequences
- **Availability**: DoS: Resource Consumption (Other), DoS: Crash, Exit, or Restart

## Related weaknesses
- CWE-400 (ChildOf)
- CWE-400 (ChildOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/920.html
