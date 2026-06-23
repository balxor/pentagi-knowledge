---
cwe_id: CWE-1427
name: Improper Neutralization of Input Used for LLM Prompting
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Not OS-Specific, Not Architecture-Specific, AI/ML]
related_capec: []
url: https://cwe.mitre.org/data/definitions/1427.html
tags: [mitre-cwe, weakness, CWE-1427]
---

# CWE-1427 - Improper Neutralization of Input Used for LLM Prompting

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-1427](https://cwe.mitre.org/data/definitions/1427.html)

## Description
The product uses externally-provided data to build prompts provided to large language models (LLMs), but the way these prompts are constructed causes the LLM to fail to distinguish between user-supplied inputs and developer provided system directives.

## Extended description
When prompts are constructed using externally controllable data, it is often possible to cause an LLM to ignore the original guidance provided by its creators (known as the "system prompt") by inserting malicious instructions in plain human language or using bypasses such as special characters or tags. Because LLMs are designed to treat all instructions as legitimate, there is often no way for the model to differentiate between what prompt language is malicious when it performs inference and returns data. Many LLM systems incorporate data from other adjacent products or external data sources like Wikipedia using API calls and retrieval augmented generation (RAG). Any external sources in use that may contain untrusted data should also be considered potentially malicious.

## Applicable platforms / languages
Not Language-Specific, Not OS-Specific, Not Architecture-Specific, AI/ML

## Common consequences
- **Confidentiality, Integrity, Availability**: Execute Unauthorized Code or Commands, Varies by Context
- **Confidentiality**: Read Application Data
- **Integrity**: Modify Application Data, Execute Unauthorized Code or Commands
- **Access Control**: Read Application Data, Modify Application Data, Gain Privileges or Assume Identity

## Potential mitigations
- **Architecture and Design**: LLM-enabled applications should be designed to ensure proper sanitization of user-controllable input, ensuring that no intentionally misleading or dangerous characters can be included. Additionally, they should be designed in a way that ensures that user-controllable input is identified as untrusted and potentially dangerous.
- **Implementation**: LLM prompts should be constructed in a way that effectively differentiates between user-supplied input and developer-constructed system prompting to reduce the chance of model confusion at inference-time.
- **Architecture and Design**: LLM-enabled applications should be designed to ensure proper sanitization of user-controllable input, ensuring that no intentionally misleading or dangerous characters can be included. Additionally, they should be designed in a way that ensures that user-controllable input is identified as untrusted and potentially dangerous.
- **Implementation**: Ensure that model training includes training examples that avoid leaking secrets and disregard malicious inputs. Train the model to recognize secrets, and label training data appropriately. Note that due to the non-deterministic nature of prompting LLMs, it is necessary to perform testing of the same test case several times in order to ensure that troublesome behavior is not possible. Additionally, testing should be performed each time a new model is used or a model's weights are updated.
- **Installation, Operation**: During deployment/operation, use components that operate externally to the system to monitor the output and act as a moderator. These components are called different terms, such as supervisors or guardrails.
- **System Configuration**: During system configuration, the model could be fine-tuned to better control and neutralize potentially dangerous inputs.

## Related weaknesses
- CWE-77 (ChildOf)

## Observed examples (CVE)
- **CVE-2023-32786**: Chain: LLM integration framework has prompt injection (CWE-1427) that allows an attacker to force the service to retrieve data from an arbitrary URL, essentially providing SSRF (CWE-918) and potentially injecting content into downstream tasks.
- **CVE-2024-5184**: ML-based email analysis product uses an API service that allows a malicious user to inject a direct prompt and take over the service logic, forcing it to leak the standard hard-coded system prompts and/or execute unwanted prompts to leak sensitive data.
- **CVE-2024-5565**: Chain: library for generating SQL via LLMs using RAG uses a prompt function to present the user with visualized results, allowing altering of the prompt using prompt injection (CWE-1427) to run arbitrary Python code (CWE-94) instead of the intended visualization code.
- **CVE-2024-48746**: AI-based integration with business intel dashboard allows prompt injection through its natural language component, allowing execution of arbitrary code

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/1427.html
