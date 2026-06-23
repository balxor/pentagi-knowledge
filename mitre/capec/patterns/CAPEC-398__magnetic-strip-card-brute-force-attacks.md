---
capec_id: CAPEC-398
name: Magnetic Strip Card Brute Force Attacks
type: attack-pattern
abstraction: Detailed
likelihood: n/a
severity: n/a
related_cwe: []
related_attack: []
url: https://capec.mitre.org/data/definitions/398.html
tags: [mitre-capec, attack-pattern, CAPEC-398]
---

# CAPEC-398 - Magnetic Strip Card Brute Force Attacks

**Abstraction:** Detailed  -  **Likelihood:** n/a  -  **Severity:** n/a  -  **CAPEC:** [CAPEC-398](https://capec.mitre.org/data/definitions/398.html)

## Description
An adversary analyzes the data on two or more magnetic strip cards and is able to generate new cards containing valid sequences that allow unauthorized access and/or impersonation of individuals.

## Extended description
Often, magnetic strip encoding methods follow a common format for a given system laid out in up to three tracks. A single card may allow access to a corporate office complex shared by multiple companies. By analyzing how the data is stored on a card, it is also possible to create valid cards via brute-force attacks. For example, a single card can grant access to a building, a floor, and a suite number. Reading and analyzing data on multiple cards, then performing a difference analysis between data encoded on three different cards, can reveal clues as to how to generate valid cards that grant access to restricted areas of a building or suites/rooms within that building. Data stored on magstripe cards is often unencrypted, therefore comparing which data changes when two or more cards are analyzed can yield results that aid in determining the structure of the card data. A trivial example would be a common system data format on a data track which binary encodes the suite number of a building that a card will open. By creating multiple cards with differing binary encoded segments it becomes possible to enter unauthorized areas or pass through checkpoints giving the electronic ID of other persons.

## Prerequisites
- The ability to calculate a card checksum and write out a valid checksum value. Some cards are protected by a checksum calculation, therefore it is necessary to determine what algorithm is being used to calculate the checksum and to employ that algorithm to calculate and write a new valid checksum for the card being created.

Source: MITRE CAPEC - https://capec.mitre.org/data/definitions/398.html
