# awesome-llm-memory

> LLM/Agent Memory 资源清单：论文、仓库、评测、数据集。

**最后更新：2026-02-21**
**统计：** 共 68 条 · Paper 48 · Repo 8 · Benchmark 6 · Dataset 6

[English](./README.md) | 中文

## 0. 入门路径（研究 / 工程 / 产品）
- 见 [docs/starter-paths.md](docs/starter-paths.md)

## 1. 综述与分类法
| 名称 | 年份 | 类型 | Memory Scope | 核心点 |
|---|---:|---|---|---|
| [Graph-based Agent Memory survey](https://arxiv.org/html/2602.05665v1) | 2026 | Paper | long | Surveys graph-structured memory for agents, covering representations, operations, and evaluation trade-offs. |
| [Graph-based Agent Memory: Taxonomy, Techniques, and Applications](https://arxiv.org/pdf/2602.05665) | 2026 | Paper | long | Systematically reviews memory methods, organizes design dimensions, and highlights open research gaps. |

## 2. 系统与框架（有状态 Agent / 记忆管理）
| 名称 | 年份 | 类型 | Memory Scope | 核心点 |
|---|---:|---|---|---|
| [Haystack](https://github.com/deepset-ai/haystack) | Unknown | Repo | short | Seed-curated memory resource for LLM/agent memory workflows. |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Unknown | Repo | long | Seed-curated memory resource for LLM/agent memory workflows. |
| [Letta (formerly MemGPT)](https://github.com/letta-ai/letta) | Unknown | Repo | long | Virtual context paging for persistent agent memory. |
| [LlamaIndex](https://github.com/run-llama/llama_index) | Unknown | Repo | short | Seed-curated memory resource for LLM/agent memory workflows. |
| [Mem0](https://github.com/mem0ai/mem0) | Unknown | Repo | long | Seed-curated memory resource for LLM/agent memory workflows. |
| [Zep](https://github.com/getzep/zep) | Unknown | Repo | short | Seed-curated memory resource for LLM/agent memory workflows. |

## 3. 记忆表征——摘要/笔记
| 名称 | 年份 | 类型 | Memory Scope | 核心点 |
|---|---:|---|---|---|
| [MemDaily](https://arxiv.org/pdf/2409.20163) | 2016 | Paper | long | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [Recurrent Memory Transformer](https://arxiv.org/abs/2207.06881) | 2022 | Paper | long | Maintains recurrent memory states across segments to scale sequence modeling beyond fixed windows. |
| [WebShop](https://arxiv.org/pdf/2207.01206) | 2022 | Paper | short | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [Generative Agents](https://arxiv.org/abs/2304.03442) | 2023 | Paper | long | Combines observation, reflection, and planning to simulate believable long-term agent behavior. |
| [LongBench](https://arxiv.org/abs/2308.14508) | 2023 | Paper | long | Defines evaluation settings and metrics for long-horizon memory, retrieval quality, and consistency. |
| [LongMem](https://arxiv.org/abs/2306.07174) | 2023 | Paper | long | Enhances transformers with long-term memory modules for better extrapolation to lengthy contexts. |
| [MemGPT](https://arxiv.org/abs/2310.08560) | 2023 | Paper | long | Introduces virtual memory-style paging to extend LLM context with persistent long-term memory. |
| [Voyager](https://arxiv.org/abs/2305.16291) | 2023 | Paper | short | Builds a lifelong skill library in Minecraft using iterative prompting, memory, and automatic curriculum. |
| [WebArena](https://arxiv.org/pdf/2307.13854) | 2023 | Paper | short | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [BABILong](https://arxiv.org/pdf/2406.10149) | 2024 | Paper | long | Presents mechanisms for persistent agent memory across tasks, sessions, or long-horizon workflows. |
| [DialSim](https://arxiv.org/pdf/2406.13144) | 2024 | Paper | short | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [HOMER](https://arxiv.org/pdf/2404.10308) | 2024 | Paper | short | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [LaMP](https://aclanthology.org/2024.acl-long.399.pdf) | 2024 | Paper | short | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [LongBench V2](https://arxiv.org/pdf/2412.15204) | 2024 | Paper | long | Defines evaluation settings and metrics for long-horizon memory, retrieval quality, and consistency. |
| [MADial-Bench](https://arxiv.org/abs/2409.15240) | 2024 | Paper | short | Defines evaluation settings and metrics for long-horizon memory, retrieval quality, and consistency. |
| [MemoryLLM](https://arxiv.org/abs/2402.04624) | 2024 | Paper | long | Uses dedicated memory tokens and retrieval to maintain long-horizon information across interactions. |
| [MT-Mind2Web](https://arxiv.org/pdf/2402.15057) | 2024 | Paper | short | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [RULER](https://arxiv.org/pdf/2404.06654) | 2024 | Paper | short | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [SCBENCH](https://arxiv.org/abs/2412.10319) | 2024 | Paper | short | Defines evaluation settings and metrics for long-horizon memory, retrieval quality, and consistency. |
| [StreamBench](https://arxiv.org/pdf/2406.08747) | 2024 | Paper | short | Defines evaluation settings and metrics for long-horizon memory, retrieval quality, and consistency. |
| [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) | 2025 | Paper | long | Proposes agentic memory operations that decide what to write, update, and retrieve over time. |
| [HaluMem](https://arxiv.org/pdf/2511.03506) | 2025 | Paper | long | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [IMPLEXCONV](https://aclanthology.org/2025.emnlp-main.580.pdf) | 2025 | Paper | short | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [LifelongAgentBench](https://arxiv.org/pdf/2505.11942) | 2025 | Paper | long | Defines evaluation settings and metrics for long-horizon memory, retrieval quality, and consistency. |
| [LOCCO](https://aclanthology.org/2025.findings-acl.1014.pdf) | 2025 | Paper | short | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [MemBench](https://aclanthology.org/2025.findings-acl.989.pdf) | 2025 | Paper | long | Defines evaluation settings and metrics for long-horizon memory, retrieval quality, and consistency. |
| [MemoryAgentBench](https://arxiv.org/pdf/2507.05257) | 2025 | Paper | long | Defines evaluation settings and metrics for long-horizon memory, retrieval quality, and consistency. |
| [MemoryBench](https://arxiv.org/pdf/2510.17281) | 2025 | Paper | long | Defines evaluation settings and metrics for long-horizon memory, retrieval quality, and consistency. |
| [Minerva](https://arxiv.org/pdf/2502.03358) | 2025 | Paper | short | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [MiniLongBench](https://aclanthology.org/2025.acl-long.560.pdf) | 2025 | Paper | long | Defines evaluation settings and metrics for long-horizon memory, retrieval quality, and consistency. |
| [MM-Needle](https://aclanthology.org/2025.naacl-long.166.pdf) | 2025 | Paper | short | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [PersonaBench](https://aclanthology.org/2025.findings-acl.49.pdf) | 2025 | Paper | short | Defines evaluation settings and metrics for long-horizon memory, retrieval quality, and consistency. |
| [PersonaFeedback](https://arxiv.org/pdf/2506.12915) | 2025 | Paper | short | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [PERSONAMEM](https://arxiv.org/pdf/2504.14225) | 2025 | Paper | long | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [PERSONAMEM-v2](https://www.arxiv.org/pdf/2512.06688) | 2025 | Paper | long | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [StoryBench](https://arxiv.org/pdf/2506.13356) | 2025 | Paper | short | Defines evaluation settings and metrics for long-horizon memory, retrieval quality, and consistency. |
| [WebChoreArena](https://arxiv.org/pdf/2506.01952) | 2025 | Paper | short | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [CloneMem](https://arxiv.org/pdf/2601.07023) | 2026 | Paper | long | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [KnowMe-Bench](https://arxiv.org/abs/2601.04745) | 2026 | Paper | short | Defines evaluation settings and metrics for long-horizon memory, retrieval quality, and consistency. |
| [Mem-Gallery](https://arxiv.org/pdf/2601.03515) | 2026 | Paper | long | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [RealMem](https://arxiv.org/pdf/2601.06966) | 2026 | Paper | long | Investigates memory-aware modeling to improve long-context reasoning, persistence, and adaptation. |
| [LongGenBench](https://arxiv.org/pdf/2409.02076) | 2025 | Paper | long | Defines evaluation settings and metrics for long-horizon memory, retrieval quality, and consistency. |
| [A-mem](https://github.com/agiresearch/A-mem) | 2025 | Repo | long | Agentic memory pipeline for write/retrieve decisions. |
| [MemoryLLM repo](https://github.com/wangyu-ustc/MemoryLLM) | 2024 | Repo | long | Explicit memory tokens with retrieval-augmented updates. |

## 4. 记忆表征——向量/检索记忆
| 名称 | 年份 | 类型 | Memory Scope | 核心点 |
|---|---:|---|---|---|
| [RAGAs](https://arxiv.org/abs/2309.15217) | 2023 | Paper | short | Provides reference-free metrics to evaluate retrieval-augmented generation pipelines end-to-end. |
| [SELF-RAG](https://arxiv.org/abs/2310.11511) | 2023 | Paper | short | Trains models to self-retrieve and self-critique, improving controllability and factual grounding in generation. |

## 5. 记忆表征——图/知识记忆
| 名称 | 年份 | 类型 | Memory Scope | 核心点 |
|---|---:|---|---|---|

## 6. 记忆表征——混合/层级
| 名称 | 年份 | 类型 | Memory Scope | 核心点 |
|---|---:|---|---|---|

## 7. 写入 / 更新 / 遗忘
| 名称 | 年份 | 类型 | Memory Scope | 核心点 |
|---|---:|---|---|---|
| [Reflexion](https://arxiv.org/abs/2303.11366) | 2023 | Paper | short | Improves agents via verbal self-reflection that updates future decision-making without weight updates. |
| [RET-LLM: read-write memory](https://arxiv.org/abs/2305.14322) | 2023 | Paper | long | Adds explicit read-write external memory to improve long-context reasoning and factual consistency. |

## 8. 基准与评测
| 名称 | 年份 | 类型 | Memory Scope | 核心点 |
|---|---:|---|---|---|
| [BEIR](https://arxiv.org/abs/2104.08663) | 2021 | Benchmark | short | Seed-curated memory resource for LLM/agent memory workflows. |
| [MTEB](https://arxiv.org/abs/2210.07316) | 2022 | Benchmark | short | Seed-curated memory resource for LLM/agent memory workflows. |
| [L-CiteEval](https://arxiv.org/pdf/2410.02115) | 2024 | Benchmark | short | Seed-curated memory resource for LLM/agent memory workflows. |
| [LOCOMO](https://aclanthology.org/2024.acl-long.747.pdf) | 2024 | Benchmark | short | Seed-curated memory resource for LLM/agent memory workflows. |
| [LongMemEval](https://arxiv.org/pdf/2410.10813) | 2024 | Benchmark | long | Seed-curated memory resource for LLM/agent memory workflows. |
| [PREFEVAL](https://arxiv.org/pdf/2502.09597) | 2025 | Benchmark | short | Seed-curated memory resource for LLM/agent memory workflows. |

## 9. 数据集
| 名称 | 年份 | 类型 | Memory Scope | 核心点 |
|---|---:|---|---|---|
| [HotpotQA](https://aclanthology.org/D18-1259.pdf) | 2018 | Dataset | short | Seed-curated memory resource for LLM/agent memory workflows. |
| [MuSiQue](https://arxiv.org/abs/2108.00573) | 2021 | Dataset | short | Seed-curated memory resource for LLM/agent memory workflows. |
| [QuALITY](https://arxiv.org/abs/2112.08608) | 2021 | Dataset | short | Seed-curated memory resource for LLM/agent memory workflows. |
| [PerLTQA](https://aclanthology.org/2024.sighan-1.18.pdf) | 2024 | Dataset | short | Seed-curated memory resource for LLM/agent memory workflows. |
| [Natural Questions](https://ai.google.com/research/NaturalQuestions) | Unknown | Dataset | short | Seed-curated memory resource for LLM/agent memory workflows. |
| [TriviaQA](http://nlp.cs.washington.edu/triviaqa/) | Unknown | Dataset | short | Seed-curated memory resource for LLM/agent memory workflows. |

## 10. 相关 Awesome 列表
| 名称 | 年份 | 类型 | Memory Scope | 核心点 |
|---|---:|---|---|---|

## FAQ
- **这个列表保证质量或安全性吗？** 不保证。这是 best-effort 的持续维护型整理。
- **如何新增条目？** 按 [CONTRIBUTING.md](CONTRIBUTING.md) 的格式提交 PR。

## 参与贡献
见 [CONTRIBUTING.md](CONTRIBUTING.md)
