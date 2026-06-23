---
cwe_id: CWE-804
name: Guessable CAPTCHA
type: weakness
abstraction: Base
status: Incomplete
languages: [Not Language-Specific, Web Server]
related_capec: []
url: https://cwe.mitre.org/data/definitions/804.html
tags: [mitre-cwe, weakness, CWE-804]
---

# CWE-804 - Guessable CAPTCHA

**Abstraction:** Base  -  **Status:** Incomplete  -  **CWE:** [CWE-804](https://cwe.mitre.org/data/definitions/804.html)

## Description
The product uses a CAPTCHA challenge, but the challenge can be guessed or automatically recognized by a non-human actor.

## Extended description
An automated attacker could bypass the intended protection of the CAPTCHA challenge and perform actions at a higher frequency than humanly possible, such as launching spam attacks. There can be several different causes of a guessable CAPTCHA: An audio or visual image that does not have sufficient distortion from the unobfuscated source image. A question is generated with a format that can be automatically recognized, such as a math question. A question for which the number of possible answers is limited, such as birth years or favorite sports teams. A general-knowledge or trivia question for which the answer can be accessed using a data base, such as country capitals or popular entertainers. Other data associated with the CAPTCHA may provide hints about its contents, such as an image whose filename contains the word that is used in the CAPTCHA.

## Applicable platforms / languages
Not Language-Specific, Web Server

## Common consequences
- **Access Control, Other**: Bypass Protection Mechanism, Other

## Related weaknesses
- CWE-863 (ChildOf)
- CWE-1390 (ChildOf)

## Observed examples (CVE)
- **CVE-2022-4036**: Chain: appointment booking app uses a weak hash (CWE-328) for generating a CAPTCHA, making it guessable (CWE-804)

Source: MITRE CWE - https://cwe.mitre.org/data/definitions/804.html
