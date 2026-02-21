#!/usr/bin/env python3
import yaml
from datetime import date
from collections import defaultdict
from pathlib import Path

entries = yaml.safe_load(Path("data/entries.yaml").read_text())

sections = [
("Surveys & Taxonomies", "surveys_taxonomies"),
("Systems & Frameworks", "systems_frameworks"),
("Memory Representations / summary/notes", "repr_summary_notes"),
("Memory Representations / vector / retrieval memory", "repr_vector_retrieval"),
("Memory Representations / graph / knowledge memory", "repr_graph_knowledge"),
("Memory Representations / hybrid / hierarchical", "repr_hybrid_hierarchical"),
("Writing / Updating / Forgetting", "write_update_forget"),
("Benchmarks & Evaluation", "benchmarks_evaluation"),
("Datasets", "datasets"),
("Related Awesome Lists", "related_awesome"),
]

bucket = defaultdict(list)
for e in entries:
    bucket[e["category"]].append(e)

for k in bucket:
    bucket[k] = sorted(bucket[k], key=lambda x: (str(x["year"]), x["name"]))

lines = []
lines.append("# awesome-llm-memory")
lines.append("")
lines.append("> Curated resources for LLM/Agent memory: papers, repos, benchmarks, datasets.")
lines.append("")
lines.append(f"**Last updated: {date.today().isoformat()}**")
lines.append("")
lines.append("## 0. Starter Paths (Researcher / Builder / Product)")
lines.append("- See [docs/starter-paths.md](docs/starter-paths.md)")
lines.append("")
idx=1
for title,key in sections:
    lines.append(f"## {idx}. {title}")
    for e in bucket.get(key,[]):
        link = e["links"][0]
        lines.append(f"- [{e['name']}]({link}) ({e['year']}) — Type: {e['type']}. Scope: {e['scope']}. Notes: {e['key_idea']}")
    lines.append("")
    idx += 1

lines.append("## FAQ")
lines.append("- **Does this list guarantee quality or safety?** No. It is curated best-effort and continuously improved.")
lines.append("- **How to add entries?** See CONTRIBUTING.md and open a PR.")
lines.append("")
lines.append("## Contributing")
lines.append("See [CONTRIBUTING.md](CONTRIBUTING.md)")

Path("README.md").write_text("\n".join(lines))
print("README.md generated")
