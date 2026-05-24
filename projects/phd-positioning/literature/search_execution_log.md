# Search Execution Log

## Purpose

This file documents the execution of the literature search package for:

**Multimodal clinical-laboratory intelligence for hematology**

It should be completed during the actual search process. Do **not** prefill retrieval counts or screening outcomes.

## Related Files

- [search_protocol.md](/Users/joaokasprowicz/.codex/worktrees/fafa/research-agent/projects/phd-positioning/literature/search_protocol.md)
- [database_search_strings.md](/Users/joaokasprowicz/.codex/worktrees/fafa/research-agent/projects/phd-positioning/literature/database_search_strings.md)
- [screening_criteria.md](/Users/joaokasprowicz/.codex/worktrees/fafa/research-agent/projects/phd-positioning/literature/screening_criteria.md)
- [extraction_form.md](/Users/joaokasprowicz/.codex/worktrees/fafa/research-agent/projects/phd-positioning/literature/extraction_form.md)

## Instructions

Create one log entry per executed query. If the same database is searched with broad, focused, and exploratory versions, create three separate entries.

Record:

- database
- query version
- exact query used
- date searched
- platform/interface
- filters used
- number of records retrieved
- export format
- deduplication status
- number after deduplication
- notes/problems

## Search Session Metadata

- Reviewer:
- Secondary reviewer, if any:
- Project:
- Protocol version:
- Search period start:
- Search period end:
- Citation manager / spreadsheet used for deduplication:
- Notes:

## Master Log Table

| Log ID | Database | Platform / Interface | Query Version | Query Source File | Exact Query Used | Date Searched | Filters Used | Records Retrieved | Exported? | Export Format | Imported to Master Library? | Duplicates Removed in This Batch | Records Remaining After Deduplication | Notes / Problems |
|---|---|---|---|---|---|---|---|---:|---|---|---|---:|---:|---|
| SEARCH-001 |  |  | broad / focused / exploratory | database_search_strings.md |  |  |  |  | yes / no |  | yes / no |  |  |  |
| SEARCH-002 |  |  | broad / focused / exploratory | database_search_strings.md |  |  |  |  | yes / no |  | yes / no |  |  |  |
| SEARCH-003 |  |  | broad / focused / exploratory | database_search_strings.md |  |  |  |  | yes / no |  | yes / no |  |  |  |

## Detailed Query Entry Template

Copy this block once per executed search if you need fuller documentation.

```md
### Log ID:

- Database:
- Platform / Interface:
- Query version:
- Query source:
- Exact query used:
- Date searched:
- Time searched:
- Years filter:
- Language filter:
- Human filter:
- Document type filter:
- Other filters:
- Number of records retrieved:
- Exported:
- Export format:
- Imported to master library:
- Deduplication performed:
- Duplicates removed in this batch:
- Records remaining after deduplication:
- Notes / problems:
```

## Recommended Query Version Labels

Use only these values:

- `broad`
- `focused`
- `exploratory`

## Recommended Database Names

Use standardized names:

- `PubMed/MEDLINE`
- `Scopus`
- `Embase`
- `SciELO`
- `Web of Science`
- `IEEE Xplore`
- `ACM Digital Library`

## Deduplication Tracking

Use this section to document the deduplication workflow across the full search set.

### Deduplication Summary

- Master library created on:
- Software or method used:
- Match fields used for deduplication:
- Manual review of uncertain duplicates completed on:
- Final unique record count after deduplication:
- Notes:

### Deduplication Rules Used

- exact DOI match
- exact title match
- fuzzy title + year + first author match
- manual confirmation for conference/journal duplicates

## Problem Log

Use this section for search-interface or syntax issues.

| Problem ID | Database | Query Version | Problem | Resolution | Impact on Reproducibility |
|---|---|---|---|---|---|
| PROB-001 |  |  |  |  | none / low / moderate / high |

## Final Search Freeze Record

Complete this only after all searches are done.

- Final search date:
- All planned databases executed? yes / no
- Any database skipped? if yes, why:
- Any query materially modified from protocol? yes / no
- If yes, list modifications:
- Search package ready for PRISMA accounting? yes / no
