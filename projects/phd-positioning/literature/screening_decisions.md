# Screening Decisions

## Purpose

This file records title/abstract and full-text screening decisions for the literature search on:

**Multimodal clinical-laboratory intelligence for hematology**

Use the screening labels exactly as defined in:

- [screening_criteria.md](/Users/joaokasprowicz/.codex/worktrees/fafa/research-agent/projects/phd-positioning/literature/screening_criteria.md)

## Allowed Labels

- `directly relevant`
- `adjacent but useful`
- `background only`
- `exclude`

## Instructions

1. Create one row per record after deduplication.
2. Record title/abstract screening first.
3. Update the same row after full-text screening.
4. If a record is excluded at full text, provide a concise exclusion reason.
5. If two reviewers are involved, record both decisions and the consensus.

## Master Screening Table

| Record ID | Citation | Database Source | Title / Abstract Reviewed? | Title / Abstract Label | Title / Abstract Reviewer | Title / Abstract Date | Full Text Retrieved? | Full Text Reviewed? | Full Text Label | Full Text Reviewer | Full Text Date | Exclusion Reason | Consensus Decision | Short Relevance Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| REC-0001 |  |  | yes / no | directly relevant / adjacent but useful / background only / exclude |  |  | yes / no | yes / no | directly relevant / adjacent but useful / background only / exclude |  |  |  |  |  |
| REC-0002 |  |  | yes / no | directly relevant / adjacent but useful / background only / exclude |  |  | yes / no | yes / no | directly relevant / adjacent but useful / background only / exclude |  |  |  |  |  |
| REC-0003 |  |  | yes / no | directly relevant / adjacent but useful / background only / exclude |  |  | yes / no | yes / no | directly relevant / adjacent but useful / background only / exclude |  |  |  |  |  |

## Recommended Exclusion Reasons

Use short controlled reasons where possible:

- no hematology context
- no laboratory context
- no computational method
- radiology-only
- genomics-only
- veterinary-only
- no multimodal relevance
- no decision-support relevance
- commentary/editorial only
- duplicate
- inaccessible full text
- non-scholarly

## Reviewer Workflow

### Title / Abstract Stage

Assign one of:

- `directly relevant`
- `adjacent but useful`
- `background only`
- `exclude`

### Full-Text Stage

Assign one of:

- `directly relevant`
- `adjacent but useful`
- `background only`
- `exclude`

### Consensus Rule

If two reviewers disagree:

1. compare against `screening_criteria.md`
2. document both labels
3. record a consensus decision in the final column

## Optional Dual-Reviewer Decision Block

Use this template only if needed.

```md
### Record ID:

- Citation:
- Reviewer 1 title/abstract label:
- Reviewer 2 title/abstract label:
- Title/abstract consensus:
- Reviewer 1 full-text label:
- Reviewer 2 full-text label:
- Full-text consensus:
- Exclusion reason, if excluded:
- Notes:
```

## Screening Summary Counters

Update during the review process.

### Title / Abstract Summary

- Records screened:
- Directly relevant:
- Adjacent but useful:
- Background only:
- Exclude:

### Full-Text Summary

- Full texts sought:
- Full texts retrieved:
- Full texts assessed:
- Directly relevant:
- Adjacent but useful:
- Background only:
- Exclude:

## Included-for-Extraction Rule

Move a record into the extraction matrix if its **final consensus decision** is:

- `directly relevant`
- `adjacent but useful`
- `background only` only if it is intentionally retained for conceptual background

Normally, the main extraction set should prioritize:

- `directly relevant`
- `adjacent but useful`

## Notes

- Do not delete excluded records from this file.
- This file is the audit trail for the screening phase.
- Keep record IDs stable across the search log, screening file, extraction matrix, and PRISMA flow.
