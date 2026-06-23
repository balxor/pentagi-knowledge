---
cwe_id: CWE-1434
name: Insecure Setting of Generative AI/ML Model Inference Parameters
type: weakness
abstraction: Base
status: Draft
languages: [Not Language-Specific, Not Architecture-Specific, AI/ML, Not Technology-Specific]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1434.html
tags: [mitre-cwe, weakness, CWE-1434]
---

# CWE-1434 - Insecure Setting of Generative AI/ML Model Inference Parameters

**Abstraction:** Base  -  **Status:** Draft  -  **CWE:** [CWE-1434](https://cwe.mitre.org/data/definitions/1434.html)

## Description
The product has a component that relies on a generative AI/ML model configured with inference parameters that produce an unacceptably high rate of erroneous or unexpected outputs.

## Extended description
Generative AI/ML models, such as those used for text generation, image synthesis, and other creative tasks, rely on inference parameters that control model behavior, such as temperature, Top P, and Top K. These parameters affect the model's internal decision-making processes, learning rate, and probability distributions. Incorrect settings can lead to unusual behavior such as text "hallucinations," unrealistic images, or failure to converge during training. The impact of such misconfigurations can compromise the integrity of the application. If the results are used in security-critical operations or decisions, then this could violate the intended security policy, i.e., introduce a vulnerability.

## Applicable platforms / languages
Not Language-Specific, Not Architecture-Specific, AI/ML, Not Technology-Specific

## Common consequences
- **Integrity, Other**: Varies by Context, Unexpected State
- **Other**: Alter Execution Logic, Unexpected State, Varies by Context

## Potential mitigations
- **Implementation, System Configuration, Operation**: Develop and adhere to robust parameter tuning processes that include extensive testing and validation.
- **Implementation, System Configuration, Operation**: Implement feedback mechanisms to continuously assess and adjust model performance.
- **Documentation**: Provide comprehensive documentation and guidelines for parameter settings to ensure consistent and accurate model behavior.

## Related weaknesses
- CWE-440 (ChildOf)
- CWE-665 (ChildOf)
- CWE-684 (CanPrecede)
- CWE-691 (PeerOf)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1434.html
