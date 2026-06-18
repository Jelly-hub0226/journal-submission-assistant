# Journal Submission Assistant

A Codex skill for academic journal discovery, evaluation, and article-journal matching.

## Features

- **Journal Lookup**: Query IF, JCR quartile, CAS quartile, SJR, CiteScore for international journals; PKU Core/CSSCI/CSCD status for Chinese journals
- **Article Assessment**: Score your manuscript on novelty, method rigor, argumentation depth, and writing quality
- **Smart Matching**: Get tiered journal recommendations (reach/match/safety) with estimated acceptance probability
- **Submission Roadmap**: Concrete submission strategy with fallback plans
- **Chinese Journal Tools**: Legitimacy check, core journal directories, page fee lookup

## Installation

```bash
# Via skill-installer
python scripts/install-skill-from-github.py --repo <your-username>/journal-submission-assistant --path .
```

## Usage

Once installed, restart Codex and try:

- "查一下 Nature Communications 的 IF 和审稿周期"
- "我这篇文章适合投哪些期刊？" + paste your abstract
- "教育学的 CSSCI 核心期刊有哪些"
- "对比一下这三本期刊：Journal of AI Research, AI & Society, Minds and Machines"

## Structure

```
├── SKILL.md                  # Core skill instructions
├── agents/openai.yaml        # UI metadata
├── scripts/
│   ├── score_article.py      # Article quality scoring engine
│   └── calc_probability.py   # Acceptance probability calculator
└── references/
    ├── data-sources.md       # Data source URLs & scraping strategies
    ├── scoring-rubric.md     # Four-dimension scoring rubric
    ├── matching-rules.md     # Journal matching & probability rules
    └── chinese-journals.md   # Chinese journal classification guide
```
