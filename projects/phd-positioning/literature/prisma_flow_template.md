# PRISMA Flow Template

## Purpose

This file documents the PRISMA-style study flow for the literature search on:

**Multimodal clinical-laboratory intelligence for hematology**

It is a template only. Do **not** prefill counts before the search and screening are completed.

## Data Sources for This Flow

Populate this file using:

- [search_execution_log.md](/Users/joaokasprowicz/.codex/worktrees/fafa/research-agent/projects/phd-positioning/literature/search_execution_log.md)
- [screening_decisions.md](/Users/joaokasprowicz/.codex/worktrees/fafa/research-agent/projects/phd-positioning/literature/screening_decisions.md)

## PRISMA Flow Summary

### Identification

- Records identified from PubMed/MEDLINE:
- Records identified from Scopus:
- Records identified from Embase:
- Records identified from SciELO:
- Records identified from Web of Science:
- Records identified from IEEE Xplore:
- Records identified from ACM Digital Library:
- Records identified from other sources, if any:

- Total records identified before deduplication:

### Deduplication

- Duplicate records removed:
- Records remaining after deduplication:

### Screening

- Records screened at title/abstract:
- Records excluded at title/abstract:

### Retrieval

- Full-text reports sought for retrieval:
- Full-text reports not retrieved:
- Full-text reports assessed for eligibility:

### Eligibility

- Full-text reports excluded:

Reason breakdown:

- no hematology context:
- no laboratory context:
- no computational method:
- radiology-only:
- genomics-only:
- veterinary-only:
- no multimodal relevance:
- no decision-support relevance:
- commentary/editorial only:
- inaccessible full text:
- duplicate:
- other:

### Included

- Studies included as directly relevant:
- Studies included as adjacent but useful:
- Studies retained as background only:
- Total studies included in evidence mapping:

## Compact PRISMA Table

| Stage | Count | Notes |
|---|---:|---|
| Records identified |  |  |
| Duplicates removed |  |  |
| Records after deduplication |  |  |
| Records screened |  | title/abstract |
| Records excluded |  | title/abstract |
| Full texts sought |  |  |
| Full texts not retrieved |  |  |
| Full texts assessed |  |  |
| Full texts excluded |  |  |
| Studies included |  | final evidence mapping set |

## Database-Level Identification Table

| Database | Query Versions Run | Records Retrieved | Notes |
|---|---|---:|---|
| PubMed/MEDLINE | broad / focused / exploratory |  |  |
| Scopus | broad / focused / exploratory |  |  |
| Embase | broad / focused / exploratory |  |  |
| SciELO | broad / focused / exploratory |  |  |
| Web of Science | broad / focused / exploratory |  |  |
| IEEE Xplore | broad / focused / exploratory |  |  |
| ACM Digital Library | broad / focused / exploratory |  |  |

## Screening Outcome Table by Label

### Title / Abstract

| Label | Count |
|---|---:|
| directly relevant |  |
| adjacent but useful |  |
| background only |  |
| exclude |  |

### Full Text

| Label | Count |
|---|---:|
| directly relevant |  |
| adjacent but useful |  |
| background only |  |
| exclude |  |

## Notes on Use

1. Use stable counts that match the search log and screening file exactly.
2. If a study appears in multiple databases, count it once after deduplication.
3. If conference and journal versions of the same study are both found, document the handling rule in notes.
4. Keep excluded full-text reasons concise and auditable.

## Optional Narrative Template

```md
Searches were conducted across PubMed/MEDLINE, Scopus, Embase, SciELO, Web of Science, IEEE Xplore, and ACM Digital Library using broad, focused, and exploratory query variants derived from the predefined search protocol. After deduplication, records were screened by title/abstract and then by full text according to predefined eligibility criteria. Studies classified as directly relevant or adjacent but useful were included in the evidence mapping, with background-only studies retained selectively where conceptually necessary.
```
