# Session 8 Cheatsheet: Deep Research

> Build research agents that can scope, research, and write comprehensive reports

---

## Quick Reference

| Concept | Definition | Key Pattern |
|---------|------------|-------------|
| Deep Research | Specialized agent for research workflows | Three-step process |
| Scope Phase | Define objectives, decompose queries | Query decomposition |
| Research Phase | Iterative gathering, fact verification | Multi-hop reasoning |
| Write Phase | Synthesize with citations | Report synthesis |
| Query Decomposition | Break complex queries into sub-queries | Parallel/Sequential/Hierarchical |
| Multi-Hop Reasoning | Iterative retrieval informing next query | Search → Evaluate → Refine |
| RACE | Report quality evaluation | Coherence, depth, clarity |
| FACT | Citation evaluation | Accuracy, abundance, trustworthiness |
| Bitter Lesson | General methods > specialized structures | Scale over architecture |

---

## Setup Requirements

### Dependencies
```bash
pip install deepagents langchain langgraph langsmith tavily-python
```

### Environment Variables
```python
import os
os.environ["OPENAI_API_KEY"] = "your-key"
os.environ["TAVILY_API_KEY"] = "your-tavily-key"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-langsmith-key"
os.environ["LANGCHAIN_PROJECT"] = "AIE9-Session8"
```

### Key Repositories
- **Tutorial**: [deep_research_from_scratch](https://github.com/langchain-ai/deep_research_from_scratch)
- **Production**: [open_deep_research](https://github.com/langchain-ai/open_deep_research)

---

## Tutorial Notebooks

The [deep_research_from_scratch](https://github.com/langchain-ai/deep_research_from_scratch) repository provides hands-on tutorials for building research agents.

### Notebook Overview

| Notebook | Title | Concepts Covered | Section |
|----------|-------|------------------|---------|
| 1 | Setup & Foundations | Environment, API config, baseline | Section 1 |
| 2 | Query Planning | Decomposition, sub-queries | Section 3 |
| 3 | Iterative Retrieval | Multi-hop, source gathering | Section 4 |
| 4 | Report Generation | Synthesis, citations | Section 5 |
| 5 | Full Pipeline | Complete architecture, evaluation | Section 8 |

### Learning Path

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TUTORIAL PROGRESSION                              │
│                                                                      │
│   Notebook 1: Setup & Foundations                                    │
│        │                                                             │
│        v                                                             │
│   Notebook 2: Query Planning ──────────────────┐                    │
│        │                                        │                    │
│        v                                        v                    │
│   Notebook 3: Iterative Retrieval      (SCOPE Phase)                │
│        │                                                             │
│        v                                                             │
│   Notebook 4: Report Generation         (RESEARCH + WRITE)          │
│        │                                                             │
│        v                                                             │
│   Notebook 5: Full Pipeline             (Complete System)           │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 1. Deep Research vs Deep Agents

### Industry Definition
> **"Deep agents come with planning capabilities, file systems for context management, and the ability to spawn subagents. Use deep agents when you need agents that can handle complex, multi-step tasks that require planning and decomposition."**
> — LangChain Documentation [[1]](https://docs.langchain.com/oss/python/deepagents/overview)

### Comparison

| Aspect | Deep Agents (Session 7) | Deep Research (Session 8) |
|--------|------------------------|---------------------------|
| **Purpose** | General complex tasks | Research and report generation |
| **Workflow** | Four elements | Three-step process |
| **Key Tools** | Filesystem, subagents | Search, citation tools |
| **Output** | Task completion | Reports with citations |
| **Evaluation** | Task success | RACE + FACT metrics |

### When to Use What

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AGENT SELECTION DECISION                          │
│                                                                      │
│   Research task with report output?                                  │
│       YES → Deep Research (three-step process)                       │
│       NO  ↓                                                          │
│                                                                      │
│   Complex, multi-step task?                                          │
│       YES → Deep Agents (four elements)                              │
│       NO  ↓                                                          │
│                                                                      │
│   Custom workflow needed?                                            │
│       YES → LangGraph (build from scratch)                           │
│       NO  → create_agent() (simple agent)                            │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

**Blog Post**: [Learning the Bitter Lesson](https://rlancemartin.github.io/2025/07/30/bitter_lesson/) [[2]](https://rlancemartin.github.io/2025/07/30/bitter_lesson/)

---

## 2. The Three-Step Process

### Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THREE-STEP RESEARCH PROCESS                       │
│                                                                      │
│   ┌──────────────┐     ┌──────────────┐     ┌──────────────┐        │
│   │    SCOPE     │ --> │   RESEARCH   │ --> │    WRITE     │        │
│   │              │     │              │     │              │        │
│   │ - Define     │     │ - Search     │     │ - Outline    │        │
│   │ - Decompose  │     │ - Retrieve   │     │ - Draft      │        │
│   │ - Boundaries │     │ - Evaluate   │     │ - Cite       │        │
│   │              │     │ - Iterate    │     │ - Verify     │        │
│   └──────────────┘     └──────────────┘     └──────────────┘        │
│          │                    │                    │                 │
│          └────────────────────┴────────────────────┘                 │
│                         Feedback Loop                                │
└─────────────────────────────────────────────────────────────────────┘
```

### Phase Details

| Phase | Activities | Output |
|-------|------------|--------|
| **SCOPE** | Define objectives, decompose query, set boundaries | Sub-queries, research plan |
| **RESEARCH** | Execute searches, evaluate sources, iterate | Gathered facts, verified sources |
| **WRITE** | Structure report, add citations, verify facts | Final report with attribution |

### Industry Quote
> **"Agentic search systems typically reformulate user queries through rewriting or decomposition to improve recall, retrieve and re-rank candidate documents, and produce concise answers supported by explicit citations."**
> — Deep Research and Agentic Search Research [[3]](https://arxiv.org/html/2506.18959v2)

---

## 3. Query Decomposition

**Tutorial**: Notebook 2 covers query planning and decomposition strategies.

### Why Decomposition Matters

> **"Existing LLMs augmented with retrieval often struggle with multi-hop question answering due to inaccurate query decomposition and error propagation."**
> — Multi-Hop Reasoning Research [[4]](https://arxiv.org/html/2601.00536)

### Decomposition Patterns

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DECOMPOSITION PATTERNS                            │
│                                                                      │
│   PARALLEL                                                           │
│   ┌─────────┐                                                        │
│   │ Query Q │                                                        │
│   └────┬────┘                                                        │
│        │                                                             │
│   ┌────┼────┬────┐                                                   │
│   v    v    v    v                                                   │
│  Q1   Q2   Q3   Q4  (Independent, run simultaneously)                │
│   │    │    │    │                                                   │
│   └────┴────┴────┘                                                   │
│         │                                                            │
│         v                                                            │
│   [Combined Results]                                                 │
│                                                                      │
│   SEQUENTIAL                                                         │
│   Q1 --> R1 --> Q2 --> R2 --> Q3 --> R3  (Each informs next)        │
│                                                                      │
│   HIERARCHICAL                                                       │
│       Q                                                              │
│      / \                                                             │
│    Q1   Q2                                                           │
│   / \   / \                                                          │
│  Q1a Q1b Q2a Q2b  (Tree structure with dependencies)                 │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Choosing a Pattern

| Pattern | Use When | Tradeoff |
|---------|----------|----------|
| **Parallel** | Sub-queries are independent | Fast but may miss connections |
| **Sequential** | Each answer informs next query | Thorough but slower |
| **Hierarchical** | Complex dependencies exist | Most thorough, most complex |

---

## 4. Multi-Hop Reasoning

**Tutorial**: Notebook 3 covers iterative retrieval and multi-hop patterns.

### The Research Cycle

```
┌─────────────────────────────────────────────────────────────────────┐
│                    MULTI-HOP REASONING CYCLE                         │
│                                                                      │
│   ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐  │
│   │   Plan   │ --> │  Search  │ --> │ Evaluate │ --> │  Refine  │  │
│   └──────────┘     └──────────┘     └──────────┘     └──────────┘  │
│        ^                                                    │        │
│        │                                                    │        │
│        └────────────────── Iterate ─────────────────────────┘        │
│                                                                      │
│   Stop conditions:                                                   │
│   - Sufficient coverage achieved                                     │
│   - Max iterations reached                                           │
│   - No new information found                                         │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Preventing Context Rot

> **"Building AI agents is hard because it combines unpredictability from the model with determinism from the system, requiring planning reliability to ensure agents don't get stuck in reasoning loops."**
> — AI Engineering Best Practices [[5]](https://growthx.club/blog/ai-engineering-skills-2026)

**Strategies:**
- Summarize findings before next iteration
- Offload raw data to filesystem (Session 7 pattern)
- Set explicit iteration limits
- Use subagents for isolated research streams

---

## 5. Source Evaluation and Citation

**Tutorial**: Notebook 4 covers report generation with citations.

### Citation Quality Factors

| Factor | Description | Evaluation |
|--------|-------------|------------|
| **Authority** | Source credibility (institutional vs. community) | FACT metric |
| **Accuracy** | Quote matches source content | Semantic verification |
| **Format** | Consistent citation style | Style check |
| **Grounding** | Claims tied to specific sources | Fact verification |

### Citation Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CITATION WORKFLOW                                 │
│                                                                      │
│   Retrieved Content                                                  │
│        │                                                             │
│        v                                                             │
│   ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐  │
│   │ Extract  │ --> │ Verify   │ --> │ Format   │ --> │ Insert   │  │
│   │  Facts   │     │ Against  │     │ Citation │     │ in Report│  │
│   │          │     │  Source  │     │          │     │          │  │
│   └──────────┘     └──────────┘     └──────────┘     └──────────┘  │
│                                                                      │
│   Verification checks:                                               │
│   - Semantic alignment with source                                   │
│   - No hallucinated URLs                                             │
│   - Proper attribution                                               │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Industry Quote
> **"FACT evaluates an agent's information retrieval and collection capabilities by assessing its effective citation count and overall citation accuracy, with RACE targeting the assessment of report generation quality."**
> — DeepResearch Bench [[6]](https://arxiv.org/abs/2506.11763)

---

## 6. Report Synthesis

### Report Structure

```
┌─────────────────────────────────────────────────────────────────────┐
│                    REPORT STRUCTURE                                  │
│                                                                      │
│   1. Executive Summary                                               │
│      - Key findings (2-3 sentences)                                  │
│      - Main conclusions                                              │
│                                                                      │
│   2. Introduction                                                    │
│      - Research question                                             │
│      - Scope and methodology                                         │
│                                                                      │
│   3. Findings (per sub-query)                                        │
│      - Topic heading                                                 │
│      - Evidence with citations                                       │
│      - Analysis                                                      │
│                                                                      │
│   4. Synthesis                                                       │
│      - Cross-cutting themes                                          │
│      - Contradictions resolved                                       │
│                                                                      │
│   5. Conclusions                                                     │
│      - Answers to original query                                     │
│      - Confidence levels                                             │
│                                                                      │
│   6. References                                                      │
│      - All cited sources                                             │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Synthesis Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Generator-Critic** | Draft then review for accuracy | High-stakes reports |
| **Incremental** | Build report section by section | Long reports |
| **Parallel Sections** | Generate sections independently | Speed-optimized |

---

## 7. The Bitter Lesson

### Core Insight

> **"By 2026, the most valuable engineers were no longer those who wrote the best prompts, but those who understood how to build systems around models - systems that think, retrieve, evaluate, and act."**
> — AI Engineering Industry Analysis [[5]](https://growthx.club/blog/ai-engineering-skills-2026)

### Applied to Research Agents

```
┌─────────────────────────────────────────────────────────────────────┐
│                    BITTER LESSON APPLICATION                         │
│                                                                      │
│   AVOID (Specialized Architecture)          PREFER (General Methods)│
│   ┌────────────────────────┐          ┌────────────────────────┐    │
│   │ Hard-coded routing     │          │ Flexible planning      │    │
│   │ Domain-specific agents │          │ Broad tool access      │    │
│   │ Fixed query patterns   │          │ Adaptive decomposition │    │
│   │ Manual source ranking  │          │ Learned evaluation     │    │
│   └────────────────────────┘          └────────────────────────┘    │
│                                                                      │
│   Key insight: Systems that leverage computation scale better        │
│   than hand-crafted, specialized structures.                         │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Practical Implications

1. **Use general-purpose tools** (Tavily search vs. domain-specific APIs)
2. **Let the model plan** (don't hard-code research paths)
3. **Embrace multi-agent flexibility** (orchestrate vs. single monolith)
4. **Scale with computation** (more iterations > better prompts)

**Blog Post**: [Learning the Bitter Lesson](https://rlancemartin.github.io/2025/07/30/bitter_lesson/) [[2]](https://rlancemartin.github.io/2025/07/30/bitter_lesson/)

---

## 8. Research Evaluation Frameworks

**Tutorial**: Notebook 5 covers evaluation and the complete pipeline.

### RACE Framework (Report Quality)

| Dimension | Description | Score Range |
|-----------|-------------|-------------|
| **Relevance** | Addresses research question | 0-25 |
| **Coherence** | Logical flow and structure | 0-25 |
| **Depth** | Comprehensive analysis | 0-25 |
| **Clarity** | Understandable presentation | 0-25 |

### FACT Framework (Citation Quality)

| Dimension | Description | Score Range |
|-----------|-------------|-------------|
| **Abundance** | Sufficient citations | Count metric |
| **Accuracy** | Citations match sources | % correct |
| **Diversity** | Range of sources used | Source count |
| **Trustworthiness** | No fabricated citations | Binary check |

### Evaluation Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    EVALUATION PIPELINE                               │
│                                                                      │
│   Generated Report                                                   │
│        │                                                             │
│        ├──────────────────────────────────────────┐                 │
│        │                                          │                  │
│        v                                          v                  │
│   ┌──────────┐                            ┌──────────┐              │
│   │   RACE   │                            │   FACT   │              │
│   │ Evaluator│                            │ Evaluator│              │
│   └────┬─────┘                            └────┬─────┘              │
│        │                                       │                     │
│        v                                       v                     │
│   Report Quality                        Citation Quality             │
│   Score (0-100)                         Score (0-100)                │
│        │                                       │                     │
│        └───────────────┬───────────────────────┘                    │
│                        │                                             │
│                        v                                             │
│                 Combined Assessment                                  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Industry Quote
> **"Quality is the production killer, with 32% citing it as a top barrier. Observability is table stakes, with nearly 89% of respondents having implemented observability for their agents."**
> — LangChain State of Agent Engineering [[7]](https://www.langchain.com/state-of-agent-engineering)

**Benchmark**: [DeepResearch Bench](https://deepresearch-bench.github.io/) [[8]](https://deepresearch-bench.github.io/)

---

## 9. Complete Architecture

### Full System Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEEP RESEARCH ARCHITECTURE                        │
│                                                                      │
│   User Query                                                         │
│        │                                                             │
│        v                                                             │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                         SCOPE                                │   │
│   │   ┌──────────┐     ┌──────────┐     ┌──────────┐           │   │
│   │   │  Query   │ --> │Decompose │ --> │  Plan    │           │   │
│   │   │ Analysis │     │ Strategy │     │ Research │           │   │
│   │   └──────────┘     └──────────┘     └──────────┘           │   │
│   └─────────────────────────────────────────────────────────────┘   │
│        │                                                             │
│        v                                                             │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                        RESEARCH                              │   │
│   │   ┌──────────┐     ┌──────────┐     ┌──────────┐           │   │
│   │   │  Search  │ --> │ Retrieve │ --> │ Evaluate │           │   │
│   │   │  (Tavily)│     │  Sources │     │  Quality │           │   │
│   │   └──────────┘     └──────────┘     └────┬─────┘           │   │
│   │        ^                                  │                  │   │
│   │        └──────────── Iterate ────────────┘                  │   │
│   │                                                              │   │
│   │   ┌──────────────────────────────────────────────────────┐  │   │
│   │   │                    MEMORY                             │  │   │
│   │   │   Gathered facts, source links, intermediate notes   │  │   │
│   │   └──────────────────────────────────────────────────────┘  │   │
│   └─────────────────────────────────────────────────────────────┘   │
│        │                                                             │
│        v                                                             │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                         WRITE                                │   │
│   │   ┌──────────┐     ┌──────────┐     ┌──────────┐           │   │
│   │   │ Outline  │ --> │  Draft   │ --> │  Cite    │           │   │
│   │   │ Report   │     │ Sections │     │  & Verify│           │   │
│   │   └──────────┘     └──────────┘     └──────────┘           │   │
│   └─────────────────────────────────────────────────────────────┘   │
│        │                                                             │
│        v                                                             │
│   Final Report with Citations                                        │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Integration with Deep Agents (Session 7)

| Deep Agents Element | Deep Research Usage |
|---------------------|---------------------|
| **Planning (write_todos)** | Research plan, sub-query tracking |
| **Filesystem** | Store intermediate findings, notes |
| **Subagents** | Parallel research streams |
| **Memory** | Persist findings across iterations |

---

## Common Issues & Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| Incomplete coverage | Insufficient decomposition | Use hierarchical decomposition |
| Hallucinated citations | No source verification | Add FACT evaluation step |
| Context overflow | Too many iterations | Summarize between iterations |
| Slow research | Sequential when parallel possible | Identify independent sub-queries |
| Low coherence | Sections written independently | Add synthesis pass |
| Missing sources | Single search per query | Implement multi-hop retrieval |

---

## Debugging Tips

### Research Quality Checks

```python
# Check decomposition coverage
assert len(sub_queries) >= 3, "Decomposition too shallow"

# Verify all sub-queries answered
for sq in sub_queries:
    assert sq.has_answer, f"Unanswered: {sq.text}"

# Check citation density
citations_per_section = len(citations) / len(sections)
assert citations_per_section >= 2, "Insufficient citations"
```

### Common Debug Points

1. **Scope issues**: Print sub-queries, check coverage
2. **Research issues**: Log search queries, track iterations
3. **Write issues**: Verify citation links, check synthesis

---

## Interview Questions

### Fundamentals
- What are the three phases of deep research?
- How does query decomposition improve research quality?
- What is the difference between RACE and FACT evaluation?

### Architecture
- When would you use parallel vs. sequential decomposition?
- How do you prevent context rot in multi-hop reasoning?
- How does deep research differ from deep agents?

### Philosophy
- What is the Bitter Lesson and how does it apply to research agents?
- Why do general methods outperform specialized architectures?

---

## Breakout Room Tasks Summary

### Breakout Room 1 (Tasks 1-5)
- [ ] Set up environment with API keys
- [ ] Work through Notebook 1 (Setup)
- [ ] Work through Notebook 2 (Query Planning)
- [ ] Work through Notebook 3 (Iterative Retrieval)
- [ ] **Activity**: Compare decomposition strategies

### Breakout Room 2 (Tasks 6-10)
- [ ] Work through Notebook 4 (Report Generation)
- [ ] Work through Notebook 5 (Full Pipeline)
- [ ] Configure citation attribution
- [ ] Apply RACE or FACT evaluation
- [ ] **Activity**: Build your own research agent

---

## Official Documentation Links

### Deep Research
- [Deep Agents Overview](https://docs.langchain.com/oss/python/deepagents/overview) [[1]](https://docs.langchain.com/oss/python/deepagents/overview)
- [Deep Agents Quickstart](https://docs.langchain.com/oss/python/deepagents/quickstart) [[9]](https://docs.langchain.com/oss/python/deepagents/quickstart)
- [Multi-Agent Patterns](https://docs.langchain.com/oss/python/langchain/multi-agent/index) [[10]](https://docs.langchain.com/oss/python/langchain/multi-agent/index)
- [Subagents](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents) [[11]](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents)

### Evaluation
- [DeepResearch Bench](https://deepresearch-bench.github.io/) [[8]](https://deepresearch-bench.github.io/)
- [DeepResearch Bench Paper](https://arxiv.org/abs/2506.11763) [[6]](https://arxiv.org/abs/2506.11763)

### Blog Posts
- [Learning the Bitter Lesson](https://rlancemartin.github.io/2025/07/30/bitter_lesson/) [[2]](https://rlancemartin.github.io/2025/07/30/bitter_lesson/)
- [State of Agent Engineering](https://www.langchain.com/state-of-agent-engineering) [[7]](https://www.langchain.com/state-of-agent-engineering)

### Code Repositories
- [Open Deep Research](https://github.com/langchain-ai/open_deep_research) [[12]](https://github.com/langchain-ai/open_deep_research)
- [Deep Research from Scratch](https://github.com/langchain-ai/deep_research_from_scratch) [[13]](https://github.com/langchain-ai/deep_research_from_scratch)

---

## References

1. LangChain Documentation. "Deep Agents Overview." https://docs.langchain.com/oss/python/deepagents/overview

2. Lance Martin. "Learning the Bitter Lesson." July 2025. https://rlancemartin.github.io/2025/07/30/bitter_lesson/

3. Deep Research and Agentic Search Research. arXiv. https://arxiv.org/html/2506.18959v2

4. Multi-Hop Reasoning Research. arXiv. https://arxiv.org/html/2601.00536

5. AI Engineering Skills 2026. GrowthX. https://growthx.club/blog/ai-engineering-skills-2026

6. DeepResearch Bench Paper. arXiv 2506.11763. https://arxiv.org/abs/2506.11763

7. LangChain. "State of Agent Engineering." https://www.langchain.com/state-of-agent-engineering

8. DeepResearch Bench. https://deepresearch-bench.github.io/

9. LangChain Documentation. "Deep Agents Quickstart." https://docs.langchain.com/oss/python/deepagents/quickstart

10. LangChain Documentation. "Multi-Agent Patterns." https://docs.langchain.com/oss/python/langchain/multi-agent/index

11. LangChain Documentation. "Subagents." https://docs.langchain.com/oss/python/langchain/multi-agent/subagents

12. LangChain GitHub. "Open Deep Research." https://github.com/langchain-ai/open_deep_research

13. LangChain GitHub. "Deep Research from Scratch." https://github.com/langchain-ai/deep_research_from_scratch

---

*Cheatsheet created for AIE9 Session 8: Deep Research*
*Last updated: January 2026*
