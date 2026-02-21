#!/usr/bin/env python3
import yaml
from datetime import date
from collections import defaultdict, Counter
from pathlib import Path

entries = yaml.safe_load(Path("data/entries.yaml").read_text())

SECTIONS_EN = [
    ("Surveys & Taxonomies", "surveys_taxonomies"),
    ("Systems & Frameworks (stateful agents / memory managers)", "systems_frameworks"),
    ("Memory Representations — summary/notes", "repr_summary_notes"),
    ("Memory Representations — vector / retrieval memory", "repr_vector_retrieval"),
    ("Memory Representations — graph / knowledge memory", "repr_graph_knowledge"),
    ("Memory Representations — hybrid / hierarchical", "repr_hybrid_hierarchical"),
    ("Writing / Updating / Forgetting", "write_update_forget"),
    ("Benchmarks & Evaluation", "benchmarks_evaluation"),
    ("Datasets", "datasets"),
    ("Related Awesome Lists", "related_awesome"),
]

SECTIONS_ZH = [
    ("综述与分类法", "surveys_taxonomies"),
    ("系统与框架（有状态 Agent / 记忆管理）", "systems_frameworks"),
    ("记忆表征——摘要/笔记", "repr_summary_notes"),
    ("记忆表征——向量/检索记忆", "repr_vector_retrieval"),
    ("记忆表征——图/知识记忆", "repr_graph_knowledge"),
    ("记忆表征——混合/层级", "repr_hybrid_hierarchical"),
    ("写入 / 更新 / 遗忘", "write_update_forget"),
    ("基准与评测", "benchmarks_evaluation"),
    ("数据集", "datasets"),
    ("相关 Awesome 列表", "related_awesome"),
]

bucket = defaultdict(list)
for e in entries:
    bucket[e["category"]].append(e)

for k in bucket:
    bucket[k] = sorted(bucket[k], key=lambda x: (str(x["year"]), x["name"].lower()))


def table_header(lang="en"):
    if lang == "zh":
        return [
            "| 名称 | 年份 | 类型 | Memory Scope | 核心点 |",
            "|---|---:|---|---|---|",
        ]
    return [
        "| Name | Year | Type | Memory Scope | Key Idea |",
        "|---|---:|---|---|---|",
    ]


def row(e):
    link = e["links"][0]
    return f"| [{e['name']}]({link}) | {e['year']} | {e['type']} | {e['scope']} | {e['key_idea']} |"


def build_en():
    c = Counter(x["type"] for x in entries)
    lines = []
    lines.append("# awesome-llm-memory")
    lines.append("")
    lines.append("> Curated resources for LLM/Agent memory: papers, repos, benchmarks, and datasets.")
    lines.append("")
    lines.append(f"**Last updated: {date.today().isoformat()}**")
    lines.append(f"**Stats:** {len(entries)} entries · Paper {c.get('Paper',0)} · Repo {c.get('Repo',0)} · Benchmark {c.get('Benchmark',0)} · Dataset {c.get('Dataset',0)}")
    lines.append("")
    lines.append("English | [中文](./README.zh-CN.md)")
    lines.append("")
    lines.append("## 0. Starter Paths (Researcher / Builder / Product)")
    lines.append("- See [docs/starter-paths.md](docs/starter-paths.md)")
    lines.append("")

    for idx, (title, key) in enumerate(SECTIONS_EN, start=1):
        lines.append(f"## {idx}. {title}")
        lines.extend(table_header("en"))
        for e in bucket.get(key, []):
            lines.append(row(e))
        lines.append("")

    lines.append("## FAQ")
    lines.append("- **Does this list guarantee quality or safety?** No. This is best-effort curation and is continuously improved.")
    lines.append("- **How to add entries?** Follow [CONTRIBUTING.md](CONTRIBUTING.md) and open a PR.")
    lines.append("")
    lines.append("## Contributing")
    lines.append("See [CONTRIBUTING.md](CONTRIBUTING.md)")
    return "\n".join(lines)


def build_zh():
    c = Counter(x["type"] for x in entries)
    lines = []
    lines.append("# awesome-llm-memory")
    lines.append("")
    lines.append("> LLM/Agent Memory 资源清单：论文、仓库、评测、数据集。")
    lines.append("")
    lines.append(f"**最后更新：{date.today().isoformat()}**")
    lines.append(f"**统计：** 共 {len(entries)} 条 · Paper {c.get('Paper',0)} · Repo {c.get('Repo',0)} · Benchmark {c.get('Benchmark',0)} · Dataset {c.get('Dataset',0)}")
    lines.append("")
    lines.append("[English](./README.md) | 中文")
    lines.append("")
    lines.append("## 0. 入门路径（研究 / 工程 / 产品）")
    lines.append("- 见 [docs/starter-paths.md](docs/starter-paths.md)")
    lines.append("")

    for idx, (title, key) in enumerate(SECTIONS_ZH, start=1):
        lines.append(f"## {idx}. {title}")
        lines.extend(table_header("zh"))
        for e in bucket.get(key, []):
            lines.append(row(e))
        lines.append("")

    lines.append("## FAQ")
    lines.append("- **这个列表保证质量或安全性吗？** 不保证。这是 best-effort 的持续维护型整理。")
    lines.append("- **如何新增条目？** 按 [CONTRIBUTING.md](CONTRIBUTING.md) 的格式提交 PR。")
    lines.append("")
    lines.append("## 参与贡献")
    lines.append("见 [CONTRIBUTING.md](CONTRIBUTING.md)")
    return "\n".join(lines)


Path("README.md").write_text(build_en())
Path("README.zh-CN.md").write_text(build_zh())
print("README.md and README.zh-CN.md generated")
