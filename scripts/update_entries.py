#!/usr/bin/env python3
import re
import yaml
import requests
from datetime import datetime
from pathlib import Path

SEEDS = [
    ("A", "https://raw.githubusercontent.com/IAAR-Shanghai/Awesome-AI-Memory/main/README.md"),
    ("B", "https://raw.githubusercontent.com/TsinghuaC3I/Awesome-Memory-for-Agents/main/README.md"),
    ("C", "https://raw.githubusercontent.com/DEEP-PolyU/Awesome-GraphMemory/main/README.md"),
]
ARXIV_API = "http://export.arxiv.org/api/query?search_query=all:(LLM+memory+agent)&start=0&max_results=30&sortBy=submittedDate&sortOrder=descending"

PAT_MD = re.compile(r"\[([^\]]{3,120})\]\((https?://[^)\s]+)\)")
PAT_YEAR = re.compile(r"(20\d{2})")


def infer_type(url, name):
    l = (url + " " + name).lower()
    if "github.com" in l:
        return "Repo"
    if any(k in l for k in ["benchmark", "eval", "leaderboard", "mteb", "beir"]):
        return "Benchmark"
    if any(k in l for k in ["dataset", "qa", "hotpot", "musique", "quality", "triviaqa"]):
        return "Dataset"
    return "Paper"


def infer_scope(name):
    l = name.lower()
    if any(k in l for k in ["user", "personal"]):
        return "user"
    if any(k in l for k in ["session", "dialog"]):
        return "session"
    if any(k in l for k in ["memory", "agent", "long", "graph", "persistent"]):
        return "long"
    return "short"


def infer_category(t, n):
    l = n.lower()
    if "awesome" in l:
        return "related_awesome"
    if t == "Benchmark":
        return "benchmarks_evaluation"
    if t == "Dataset":
        return "datasets"
    if any(k in l for k in ["survey", "taxonomy"]):
        return "surveys_taxonomies"
    if any(k in l for k in ["framework", "system", "langgraph", "letta", "llamaindex", "haystack", "mem0", "zep"]):
        return "systems_frameworks"
    if any(k in l for k in ["graph", "knowledge"]):
        return "repr_graph_knowledge"
    if any(k in l for k in ["hierarch", "hybrid"]):
        return "repr_hybrid_hierarchical"
    if any(k in l for k in ["rag", "vector", "retriev"]):
        return "repr_vector_retrieval"
    if any(k in l for k in ["forget", "update", "reflection", "privacy", "write"]):
        return "write_update_forget"
    return "repr_summary_notes"


def infer_year(name, url):
    m = re.search(r'arxiv\.org/(?:abs|pdf|html)/([0-9]{4})\.[0-9]{4,5}', url)
    if m:
        yy = int(m.group(1)[:2])
        return 2000 + yy
    m = re.search(r'aclanthology\.org/[A-Z](\d{2})-', url)
    if m:
        return 2000 + int(m.group(1))
    m = PAT_YEAR.search(url) or PAT_YEAR.search(name)
    if m:
        y = int(m.group(1))
        if 2000 <= y <= 2099:
            return y
    return "Unknown"


def load_entries(path):
    if not path.exists():
        return []
    return yaml.safe_load(path.read_text()) or []


def main():
    p = Path("data/entries.yaml")
    entries = load_entries(p)
    by_name_year = {(e["name"].strip().lower(), str(e["year"])) for e in entries}
    by_url = {u for e in entries for u in e.get("links", [])}

    added = []

    # Seed awesome lists
    for src, url in SEEDS:
        try:
            txt = requests.get(url, timeout=20).text
        except Exception:
            continue
        for name, link in PAT_MD.findall(txt):
            if any(x in link for x in ["img.shields", "awesome.re/badge.svg", "/issues", "/pulls", "/stargazers"]):
                continue
            name = re.sub(r"\s+", " ", name).strip(" -*•")
            if len(name) < 4 or link in by_url:
                continue
            year = infer_year(name, link)
            key = (name.lower(), str(year))
            if key in by_name_year:
                continue
            t = infer_type(link, name)
            e = {
                "name": name,
                "year": year,
                "type": t,
                "scope": infer_scope(name),
                "key_idea": "Auto-added from curated seed lists; verify and refine notes.",
                "links": [link],
                "category": infer_category(t, name),
                "source": src,
            }
            entries.append(e)
            by_name_year.add(key)
            by_url.add(link)
            added.append(e)

    # Lightweight arXiv latest scan
    try:
        atom = requests.get(ARXIV_API, timeout=20).text
        for m in re.finditer(r"<entry>.*?<title>(.*?)</title>.*?<id>(https?://arxiv.org/abs/.*?)</id>", atom, flags=re.S):
            name = re.sub(r"\s+", " ", m.group(1)).strip()
            link = m.group(2).strip()
            if link in by_url:
                continue
            year = infer_year(name, link)
            key = (name.lower(), str(year))
            if key in by_name_year:
                continue
            t = "Paper"
            e = {
                "name": name,
                "year": year,
                "type": t,
                "scope": infer_scope(name),
                "key_idea": "Recent arXiv memory-related paper; note to be curated by maintainers.",
                "links": [link],
                "category": infer_category(t, name),
                "source": "arxiv",
            }
            entries.append(e)
            by_name_year.add(key)
            by_url.add(link)
            added.append(e)
    except Exception:
        pass

    # keep readable order
    entries = sorted(entries, key=lambda x: (str(x["year"]), x["type"], x["name"]))
    p.write_text(yaml.safe_dump(entries, sort_keys=False, allow_unicode=True))

    Path("data/update-report.md").write_text(
        f"# Update report\n\nGenerated: {datetime.utcnow().isoformat()}Z\n\nAdded entries: {len(added)}\n"
        + "\n".join([f"- {e['name']} ({e['year']})" for e in added[:50]])
    )
    print(f"Added {len(added)} entries")


if __name__ == "__main__":
    main()
