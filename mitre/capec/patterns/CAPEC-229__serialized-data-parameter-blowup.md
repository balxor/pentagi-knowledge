---
capec_id: CAPEC-229
name: Serialized Data Parameter Blowup
type: attack-pattern
abstraction: Detailed
likelihood: High
severity: High
related_cwe: [CWE-770]
related_attack: []
url: https://capec.mitre.org/data/definitions/229.html
tags: [mitre-capec, attack-pattern, CAPEC-229]
---

# CAPEC-229 - Serialized Data Parameter Blowup

**Abstraction:** Detailed  -  **Likelihood:** High  -  **Severity:** High  -  **CAPEC:** [CAPEC-229](https://capec.mitre.org/data/definitions/229.html)

## Description
This attack exploits certain serialized data parsers (e.g., XML, YAML, etc.) which manage data in an inefficient manner. The attacker crafts an serialized data file with multiple configuration parameters in the same dataset. In a vulnerable parser, this results in a denial of service condition where CPU resources are exhausted because of the parsing algorithm. The weakness being exploited is tied to parser implementation and not language specific.

## Prerequisites
- The server accepts input in the form of serialized data and is using a parser with a runtime longer than O(n) for the insertion of a new configuration parameter in the data container.(examples are .NET framework 1.0 and 1.1)

## Execution flow
Execution Flow Explore Survey the target: Using a browser or an automated tool, an attacker records all instances of web services to process requests using serialized data. Techniques Use an automated tool to record all instances of URLs to process requests from serialized data. Use a browser to manually explore the website and analyze how the application processes requests using serialized data. Exploit Launch a Blowup attack: The attacker crafts malicious messages that contain multiple configuration parameters in the same dataset. Techniques Send the malicious crafted message containing the multiple configuration parameters to the target URL, causing a denial of service.

## Mitigations
- This attack may be mitigated completely by using a parser that is not using a vulnerable container.
- Mitigation may limit the number of configuration parameters per dataset.

## Related weaknesses (CWE)
- [CWE-770](https://cwe.mitre.org/data/definitions/770.html)

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/229.html
