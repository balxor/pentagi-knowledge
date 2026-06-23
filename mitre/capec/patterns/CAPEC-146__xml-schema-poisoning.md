---
capec_id: CAPEC-146
name: XML Schema Poisoning
type: attack-pattern
abstraction: Detailed
likelihood: Low
severity: High
related_cwe: [CWE-15, CWE-472]
related_attack: []
url: https://capec.mitre.org/data/definitions/146.html
tags: [mitre-capec, attack-pattern, CAPEC-146]
---

# CAPEC-146 - XML Schema Poisoning

**Abstraction:** Detailed  -  **Likelihood:** Low  -  **Severity:** High  -  **CAPEC:** [CAPEC-146](https://capec.mitre.org/data/definitions/146.html)

## Description
An adversary corrupts or modifies the content of XML schema information passed between a client and server for the purpose of undermining the security of the target. XML Schemas provide the structure and content definitions for XML documents. Schema poisoning is the ability to manipulate a schema either by replacing or modifying it to compromise the programs that process documents that use this schema.

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
Execution Flow Explore Determine if XML schema is local or remote: Because this attack differs slightly if the target uses remote XML schemas versus local schemas, the adversary first needs to determine which of the two are used. Experiment Gain access to XML schema: The adversary gains access to the XML schema so that they can modify the contents. Techniques For a local scenario, the adversary needs access to the machine that the schema is located on and needs to gain permissions to alter the contents of the file. For a remote scenario, the adversary needs to be able to sniff HTTP traffic that contains an XML schema. Exploit Poison XML schema: Once the adversary gains access to the XML schema, they will alter it to achieve a desired effect. Locally, they can simply modify the file. For remote schemas, the adversary will alter the schema in transit by performing an adversary in the middle attack. Techniques Cause a denial of service by modifying the schema so that it does not contain required information for subsequent processing. For example, the unaltered schema may require a @name attribute in all submitted documents. If the adversary removes this attribute from the schema then documents created using the new grammar may lack this field, which may cause the processing application to enter an unexpected state or record incomplete data. Manipulation of the data types described in the schema may affect the results of calculations. For example, a float field could be changed to an int field. Change the encoding defined in the schema for certain fields allowing the contents to bypass filters that scan for dangerous strings. For example, the modified schema might use a URL encoding instead of ASCII, and a filter that catches a semicolon (;) might fail to detect its URL encoding (%3B).

## Mitigations
- Design: Protect the schema against unauthorized modification.
- Implementation: For applications that use a known schema, use a local copy or a known good repository instead of the schema reference supplied in the XML document. Additionally, ensure that the proper permissions are set on local files to avoid unauthorized modification.
- Implementation: For applications that leverage remote schemas, use the HTTPS protocol to prevent modification of traffic in transit and to avoid unauthorized modification.

## Related weaknesses (CWE)
- [CWE-15](https://cwe.mitre.org/data/definitions/15.html)
- [CWE-472](https://cwe.mitre.org/data/definitions/472.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/146.html
