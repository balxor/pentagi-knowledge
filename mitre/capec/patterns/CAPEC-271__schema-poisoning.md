---
capec_id: CAPEC-271
name: Schema Poisoning
type: attack-pattern
abstraction: Standard
likelihood: Low
severity: High
related_cwe: [CWE-15]
related_attack: []
url: https://capec.mitre.org/data/definitions/271.html
tags: [mitre-capec, attack-pattern, CAPEC-271]
---

# CAPEC-271 - Schema Poisoning

**Abstraction:** Standard  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-271](https://capec.mitre.org/data/definitions/271.html)

## Description
An adversary corrupts or modifies the content of a schema for the purpose of undermining the security of the target. Schemas provide the structure and content definitions for resources used by an application. By replacing or modifying a schema, the adversary can affect how the application handles or interprets a resource, often leading to possible denial of service, entering into an unexpected state, or recording incomplete data.

## Prerequisites
- Some level of access to modify the target schema.
- The schema used by the target application must be improperly secured against unauthorized modification and manipulation.

## Resources required
- Access to the schema and the knowledge and ability modify it. Ability to replace or redirect access to the modified schema.

## Consequences
- **Availability**: Unreliable Execution (A successful schema poisoning attack can compromise the availability of the target system's service by exhausting its available resources.), Resource Consumption (A successful schema poisoning attack can compromise the availability of the target system's service by exhausting its available resources.)
- **Confidentiality**: Read Data
- **Integrity**: Modify Data

## Execution flow
Execution Flow Explore Find target application and schema: The adversary first finds the application that they want to target. This application must use schemas in some way, so the adversary also needs to confirm that schemas are being used. Techniques Gain access to the system that the application is on and look for a schema. Observe HTTP traffic to the application and look for a schema being transmitted. Experiment Gain access to schema: The adversary gains access to the schema so that they can modify the contents. Techniques For a local scenario, the adversary needs access to the machine that the schema is located on and gain permissions to alter the contents of the schema file. For a remote scenario, the adversary needs to be able to perform an adversary in the middle attack on the HTTP traffic that contains a schema. Exploit Poison schema: Once the adversary gains access to the schema, they will alter it to achieve a desired effect. Locally, they can just modify the file. For remote schemas, the adversary will alter the schema in transit by performing an adversary in the middle attack. Techniques Cause a denial of service by modifying the schema so that it does not contain required information for subsequent processing. Manipulation of the data types described in the schema may affect the results of calculations. For example, a float field could be changed to an int field. Change the encoding defined in the schema for certain fields allowing the contents to bypass filters that scan for dangerous strings. For example, the modified schema might use a URL encoding instead of ASCII, and a filter that catches a semicolon (;) might fail to detect its URL encoding (%3B).

## Mitigations
- Design: Protect the schema against unauthorized modification.
- Implementation: For applications that use a known schema, use a local copy or a known good repository instead of the schema reference supplied in the schema document.
- Implementation: For applications that leverage remote schemas, use the HTTPS protocol to prevent modification of traffic in transit and to avoid unauthorized modification.

## Related weaknesses (CWE)
- [CWE-15](https://cwe.mitre.org/data/definitions/15.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/271.html
