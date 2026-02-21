# Contributing

Thanks for improving `awesome-llm-memory`.

## Inclusion criteria
- Must include at least one public link (paper/repo/homepage).
- Must include a short `key_idea` note (<= 20 words preferred for README rendering).
- Year should be provided when possible (`Unknown` if unverifiable).
- Must fit LLM/agent memory scope.

## Required entry fields
Each entry in `data/entries.yaml` must include:
- `name`
- `year`
- `type` (Paper/Repo/Benchmark/Dataset)
- `scope` (short/session/user/long)
- `key_idea`
- `links` (list)
- `category`

## Dedup rules
- Duplicate `name + year` is rejected.
- Same work with multiple mirrors: keep the most authoritative/active link.
- Prefer official repo over forks; prefer arXiv/venue over blog mirrors.

## Non-examples (will be rejected)
- Marketing landing pages with no technical content
- Dead placeholder pages
- Duplicate mirrors without added value

## Local checks
```bash
python -m pip install -r requirements.txt
python scripts/lint_links.py
python scripts/build_readme.py
```
