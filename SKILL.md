---
name: journal-submission-assistant
description: >-
  Academic journal finder, quality evaluator, and submission strategist.
  Query journal metrics (IF, JCR quartile, CAS quartile, SJR, CiteScore,
  review cycle, acceptance rate) for both international (SCI/SSCI) and
  Chinese journals (PKU core, CSSCI, CSCD). Submit article title/abstract/full-text
  to receive an article quality score (novelty, methodology, argumentation, writing),
  matched journal recommendations in reach/match/safety tiers with estimated
  acceptance probability, and a submission roadmap. Also checks Chinese journals
  for legitimacy (CN number, inclusion in CNKI/Wanfang/VIP) and queries
  page/APC fees. Use when the user asks about journal selection, where to submit,
  journal impact factor, whether a journal is good/easy to publish in, core journal
  lists, journal comparison, article-to-journal matching, submission success rate,
  or Chinese journal legitimacy verification.
---

# Journal Submission Assistant

Help users find, evaluate, and submit to academic journals by querying
public data sources and running article-journal matching.

## Workflow

When a user request falls into one of the functional modules below, first
determine which module(s) are needed, then follow the referenced instructions.
For multi-step requests (e.g., "score my article and recommend journals"),
execute modules in logical order: assessment -> matching -> strategy.

## Modules

### 1. Journal Lookup

Look up a specific journal by name. For international journals, query IF,
JCR quartile, CAS quartile, SJR, CiteScore, self-citation rate, review cycle,
and acceptance rate. For Chinese journals, query whether it is PKU Core / CSSCI /
CSCD / ST Core, composite IF, comprehensive IF, and page fees.

See `references/data-sources.md` for query URLs and scraping strategies.

Output as a structured table. For Chinese journals, always include the
core-journal classification status.

### 2. Multi-Journal Comparison

When the user provides 2-5 journal names, query each using Module 1 and
present a side-by-side comparison table. Highlight the best option for each
metric (highest IF, fastest review, highest acceptance rate).

### 3. Chinese Journal Legitimacy Check

For a Chinese journal name or CN number:
- Verify it is registered with the National Press and Publication Administration
- Check inclusion in CNKI / Wanfang / VIP
- Classify as PKU Core, CSSCI, CSCD, ST Core, or general journal
- Flag if any warning signs exist (no CN number, not in any database, etc.)

See `references/chinese-journals.md` for the verification workflow.

### 4. Article Assessment & Journal Matching

This is the core multi-step module.

**Step A: Quality Assessment**
Read the user's submitted article content (title, abstract, or full text).
Score on four dimensions (1-10 each), then compute a weighted total:

| Dimension | Weight | What to evaluate |
|---|---|---|
| Topic novelty | 25% | Originality of research question, timeliness, gap-filling |
| Method rigor | 30% | Appropriateness of method, sample size, reproducibility |
| Argument depth | 25% | Logical coherence, theoretical grounding, insight quality |
| Writing quality | 20% | Clarity, structure, language, adherence to academic norms |

Use the rubric in `references/scoring-rubric.md` for detailed scoring guidelines.

**Step B: Journal Matching**
Based on the article's subject area, methodology, and quality score,
recommend 9-15 journals in three tiers:

- **Reach tier (3-5 journals)**: Top journals where the article might compete.
  Quality score should be within 1.5 points of the journal's implicit threshold.
- **Match tier (3-5 journals)**: Journals where the fit is strong.
  Quality score within 0.5 points of the journal's threshold.
- **Safety tier (3-5 journals)**: Journals with high acceptance probability.
  Quality score exceeds the journal's threshold by at least 1 point.

Include both international and Chinese journals in each tier when applicable.

**Step C: Acceptance Probability**
For each recommended journal, estimate a percentage range:
- Base rate: the journal's reported acceptance rate (or best estimate)
- Adjust upward/downward based on topic-scope fit and quality-score gap
- Report as a range (e.g., "35-50%")

**Step D: Submission Roadmap**
Provide a concrete plan:
1. Recommended first submission (best balance of prestige and probability)
2. If rejected: next target(s) in order
3. Pre-submission checklist: revisions needed, supplementary materials required
4. Timing estimate: review cycle + revision time for each attempt

See `references/matching-rules.md` for journal threshold defaults and adjustment logic.

### 5. Core Journal Directory

For a given discipline (e.g., "计算机科学", "临床医学", "教育学"),
list the PKU Core / CSSCI / CSCD journals in that field.
If user does not specify a discipline, ask them to narrow down.

## Data Sources

All journal data is obtained by live web queries. Do NOT fabricate journal metrics.
If a query fails, try the fallback source listed in `references/data-sources.md`,
and clearly note which source was used and any data limitations.

Key sources:
- **LetPub** (www.letpub.com.cn): SCI journal metrics, review experience, acceptance rates
- **SJR / Scopus**: CiteScore, quartiles
- **CNKI / Wanfang**: Chinese journal IF, core status
- **万维书刊网** (www.eshukan.com): Chinese journal review experience, fees
- **Crossref / NLM**: Journal metadata, ISSN verification

## Output Format

For all journal information: present in Markdown tables.
For article assessment: present the four-dimension breakdown as a table, then the
weighted total, then the tiered journal recommendations with probability ranges,
and finally the submission roadmap as a numbered list.

Always note the data source and retrieval date for any journal metrics shown.
