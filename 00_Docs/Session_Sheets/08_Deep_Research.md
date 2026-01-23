# Session 8: Deep Research

> Build research agents that can scope, research, and write comprehensive reports

---

## Goal

Understand how deep research systems work under the hood and how to build them using the three-step process: scope, research, write.

---

## Learning Outcomes

By the end of this session, you will be able to:

1. **Explain** the three-step deep research process: scope, research, write
2. **Distinguish** when to use deep research vs. general deep agents patterns
3. **Implement** query decomposition for multi-hop reasoning
4. **Build** iterative research cycles with source evaluation
5. **Configure** report synthesis with explicit citation attribution
6. **Apply** the Bitter Lesson philosophy to research agent design
7. **Evaluate** research quality using RACE and FACT frameworks

---

## Tools Introduced

| Tool | Description |
|------|-------------|
| **Open Deep Research** | Production-ready deep research implementation |
| **Deep Research from Scratch** | Tutorial notebooks for learning deep research patterns |
| **DeepResearch Bench** | Evaluation framework for research quality |
| **Tavily Search API** | Web search integration for research agents |

---

## Key Concepts

### Deep Research vs. Deep Agents

Session 7 introduced Deep Agents as a general framework for complex, long-horizon tasks. Deep Research is a **specialized application** of deep agents optimized for research workflows.

| Aspect | Deep Agents (Session 7) | Deep Research (Session 8) |
|--------|------------------------|---------------------------|
| Purpose | General complex tasks | Research and report generation |
| Workflow | Four elements (plan, filesystem, subagents, memory) | Three-step process (scope, research, write) |
| Output | Task completion | Coherent reports with citations |
| Evaluation | Task success | RACE (quality) + FACT (citations) |

> **"Deep agents come with planning capabilities, file systems for context management, and the ability to spawn subagents. Use deep agents when you need agents that can handle complex, multi-step tasks that require planning and decomposition."**
> — LangChain Documentation

### The Three-Step Process

Deep research follows a structured workflow:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THREE-STEP RESEARCH PROCESS                       │
│                                                                      │
│   ┌──────────┐      ┌──────────┐      ┌──────────┐                  │
│   │  SCOPE   │ ──>  │ RESEARCH │ ──>  │  WRITE   │                  │
│   └──────────┘      └──────────┘      └──────────┘                  │
│        │                 │                 │                         │
│        v                 v                 v                         │
│   - Define query    - Execute search  - Structure report            │
│   - Decompose into  - Evaluate sources- Add citations               │
│     sub-questions   - Iterate until   - Verify facts                │
│   - Set boundaries    complete        - Generate output             │
│                                                                      │
│        └─────────── Feedback Loop ───────────┘                      │
└─────────────────────────────────────────────────────────────────────┘
```

**SCOPE**: Define research objectives, decompose into sub-questions, identify information needs

**RESEARCH**: Execute iterative cycles through query planning, knowledge acquisition, memory management

**WRITE**: Synthesize findings into coherent report with explicit citations and fact verification

### Query Decomposition

Complex research questions require breaking down into manageable sub-queries:

> **"Existing LLMs augmented with retrieval often struggle with multi-hop question answering due to inaccurate query decomposition and error propagation. DeCoR incorporates query decomposition into the expansion process, explicitly modeling multi-step reasoning paths."**
> — Multi-Hop Reasoning Research

**Decomposition patterns:**
- **Parallel**: Independent sub-queries answered simultaneously
- **Sequential**: Each answer informs the next query
- **Hierarchical**: Tree structure with dependent branches

### Multi-Hop Reasoning

Research often requires iterative retrieval where each step's findings inform the next query:

```
Query → Search → Results → Analysis → Refined Query → ...
```

This enables complex reasoning chains across multiple sources while preventing "context rot" from accumulated intermediate results.

### Source Evaluation and Citation

Research quality depends on proper source attribution:

> **"FACT evaluates an agent's information retrieval and collection capabilities by assessing its effective citation count and overall citation accuracy, with RACE targeting the assessment of report generation quality."**
> — DeepResearch Bench

**Key practices:**
- Verify claims against source content
- Distinguish institutional vs. community sources
- Use consistent citation formats
- Detect and prevent hallucinated citations

### The Bitter Lesson

Lance Martin's July 2025 blog post applies Rich Sutton's "Bitter Lesson" to research agents:

> **"By 2026, the most valuable engineers were no longer those who wrote the best prompts, but those who understood how to build systems around models - systems that think, retrieve, evaluate, and act."**
> — AI Engineering Industry Analysis

**Key insight**: General methods leveraging computation (flexible multi-agent systems with broad tool access) outperform specialized, hand-crafted routing logic.

### Research Evaluation Frameworks

**RACE** (Reference-based Adaptive Criteria-driven Evaluation):
- Report coherence and logical flow
- Depth of analysis
- Comprehensiveness of coverage
- Clarity and presentation

**FACT** (Factual Abundance and Citation Trustworthiness):
- Effective citation count
- Citation accuracy
- Source diversity
- Absence of fabricated citations

---

## Recommended Reading

### Required

| Resource | Description |
|----------|-------------|
| [Learning the Bitter Lesson](https://rlancemartin.github.io/2025/07/30/bitter_lesson/) | Key philosophical foundation for research agent design |
| [DeepResearch Bench](https://deepresearch-bench.github.io/) | Evaluation framework for research quality |

### Official Documentation

| Resource | URL |
|----------|-----|
| Deep Agents Overview | https://docs.langchain.com/oss/python/deepagents/overview |
| Deep Agents Quickstart | https://docs.langchain.com/oss/python/deepagents/quickstart |
| Multi-Agent Patterns | https://docs.langchain.com/oss/python/langchain/multi-agent/index |
| Subagents | https://docs.langchain.com/oss/python/langchain/multi-agent/subagents |

### Code Repositories

| Repository | Description |
|------------|-------------|
| [Open Deep Research](https://github.com/langchain-ai/open_deep_research) | Production-ready implementation |
| [Deep Research from Scratch](https://github.com/langchain-ai/deep_research_from_scratch) | Tutorial notebooks (5 notebooks) |

#### Notebook Progression

The `deep_research_from_scratch` repository provides hands-on tutorials:

| Notebook | Focus | Concepts Covered |
|----------|-------|------------------|
| Notebook 1 | Setup & Foundations | Environment, API configuration, basic agent |
| Notebook 2 | Query Planning | Decomposition, sub-query generation |
| Notebook 3 | Iterative Retrieval | Multi-hop reasoning, source gathering |
| Notebook 4 | Report Generation | Synthesis, citation attribution |
| Notebook 5 | Full Pipeline | Complete architecture, evaluation |

> **Recommended order**: Work through notebooks 1→5 sequentially. Each builds on concepts from the previous notebook.

---

## Assignment

**Build an unrolled open source deep research clone**

### Prerequisites

Complete the tutorial notebooks in order before starting the assignment:

1. **Notebook 1** — Set up your environment and understand the baseline
2. **Notebook 2** — Learn query decomposition strategies
3. **Notebook 3** — Implement iterative retrieval cycles
4. **Notebook 4** — Build report synthesis with citations

These notebooks provide the foundation needed for the main assignment.

### Requirements

1. Implement the three-step research process (scope, research, write)
2. Use query decomposition to handle complex research questions
3. Build iterative retrieval with source evaluation
4. Generate reports with explicit citation attribution
5. Include at least one evaluation metric (RACE or FACT dimension)

### Deliverables

- [ ] Working deep research agent with three-step workflow
- [ ] Documentation of your query decomposition strategy
- [ ] Sample research output with citations
- [ ] Evidence of iterative refinement during research
- [ ] Basic quality evaluation results

> **Hint**: The `open_deep_research` repository demonstrates the production architecture. Study how it implements the three-step process before building your own.

---

## Advanced Build

**TBD** — Options include:
- Custom evaluation metrics beyond RACE/FACT
- Multi-domain research with specialized subagents
- Knowledge graph integration for improved synthesis
- Streaming report generation with progressive updates

---

## Session Flow

### Breakout Room 1 (Tasks 1-5)

**Focus**: Notebooks 1-3 (Setup through Iterative Retrieval)

- [ ] Set up environment with required API keys (OpenAI, Tavily)
- [ ] Work through Notebook 1 — understand deep research foundations
- [ ] Work through Notebook 2 — implement query decomposition
- [ ] Work through Notebook 3 — build iterative retrieval
- [ ] **Activity**: Compare different decomposition strategies. How does parallel vs. sequential decomposition affect research quality and latency?

### Breakout Room 2 (Tasks 6-10)

**Focus**: Notebooks 4-5 (Report Generation and Full Pipeline)

- [ ] Work through Notebook 4 — implement report synthesis
- [ ] Work through Notebook 5 — complete pipeline with evaluation
- [ ] Configure citation attribution in your reports
- [ ] Apply RACE or FACT evaluation to your output
- [ ] **Activity**: Build your own research agent. How do you balance thoroughness with efficiency in the research phase?

---

## Connections to Other Sessions

| Session | Connection |
|---------|------------|
| Session 3: The Agent Loop | Research agents extend the basic agent loop with iteration |
| Session 4: Agentic RAG | Deep research builds on retrieval patterns |
| Session 5: Multi-Agent Systems | Research can use specialized subagents |
| Session 6: Agent Memory | Research agents persist findings across iterations |
| Session 7: Deep Agents | Deep research is a specialized deep agent application |
| Session 9: Synthetic Data | Research output can inform evaluation datasets |

---

*Session Sheet created for AIE9 Session 8: Deep Research*
*Last updated: January 2026*
