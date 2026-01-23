# Session 9: Synthetic Data Generation for Evals

## Goal

Learn to generate high-quality synthetic test data for evaluating RAG applications when you don't have existing evaluation datasets, and understand the metrics-driven development process for systematic improvement.

---

## Learning Outcomes

By the end of this session, you will be able to:

1. **Generate synthetic test data** using RAGAS TestsetGenerator from document corpora
2. **Understand the knowledge graph approach** that enables diverse, multi-hop question generation
3. **Apply RAGAS evaluation metrics** (faithfulness, context precision/recall, answer relevancy) to measure RAG quality
4. **Load datasets into LangSmith** for versioned, repeatable evaluations
5. **Implement metrics-driven development** to systematically improve RAG applications

---

## Tools Introduced

| Tool | Purpose | Documentation |
|------|---------|---------------|
| **RAGAS** | Synthetic testset generation and RAG evaluation metrics | [docs.ragas.io](https://docs.ragas.io/) |
| **TestsetGenerator** | Transforms documents into knowledge graphs and synthesizes QA pairs | [Testset Generation](https://docs.ragas.io/en/stable/getstarted/rag_testset_generation/) |
| **LangSmith Evaluations** | Dataset management and experiment tracking | [LangSmith Evaluation](https://docs.langchain.com/langsmith/evaluation) |

---

## Key Concepts

### 1. The Evaluation Data Challenge

Creating evaluation datasets manually is expensive, time-consuming, and doesn't scale when documents change. Synthetic data generation automates this process.

> "By using synthetic data generation, developer time in data aggregation process can be reduced by 90%."
> — RAGAS Blog

**When to use synthetic data:**
- Bootstrapping evaluation for new RAG applications
- Testing retrieval changes with consistent baselines
- Generating domain-specific test cases at scale

**When to supplement with human review:**
- High-stakes domains (legal, medical, financial)
- Production monitoring (real user queries are gold)
- Validating synthetic data quality

---

### 2. Knowledge Graph Approach

Rather than generating questions from random document chunks, RAGAS constructs a knowledge graph that connects related documents, enabling:

- **Multi-hop queries** requiring information from multiple sources
- **Cross-document reasoning** questions
- **Diverse complexity levels** beyond simple factual recall

```
┌─────────────────────────────────────────────────────────────┐
│              KNOWLEDGE GRAPH GENERATION                      │
│                                                              │
│         Doc A ◄──────────► Doc B                            │
│           │    (shared      │                               │
│           │     entity)     │                               │
│           ▼                 ▼                               │
│         Doc C ◄──────────► Doc D                            │
│                                                              │
│   Enables: Multi-hop reasoning, cross-document queries      │
└─────────────────────────────────────────────────────────────┘
```

---

### 3. Query Evolution Types

Different question types test different RAG capabilities:

| Type | Description | Tests |
|------|-------------|-------|
| **Simple** | Direct factual questions | Basic retrieval accuracy |
| **Reasoning** | Requires inference from facts | LLM reasoning capability |
| **Multi-context** | Needs info from multiple chunks | Cross-document retrieval |

The default distribution balances coverage:
- 50% simple (ensure basics work)
- 25% reasoning (test inference)
- 25% multi-context (test complex retrieval)

---

### 4. RAGAS Evaluation Metrics

Four core metrics evaluate RAG pipeline quality:

```
┌─────────────────────────────────────────────────────────────┐
│                    RAG EVALUATION METRICS                    │
│                                                              │
│   RETRIEVAL                        GENERATION                │
│   ─────────                        ──────────                │
│   Context Precision                Faithfulness              │
│   (ranking quality)                (grounded in context?)    │
│                                                              │
│   Context Recall                   Answer Relevancy          │
│   (coverage completeness)          (addresses the query?)    │
└─────────────────────────────────────────────────────────────┘
```

| Metric | Question It Answers | Range |
|--------|---------------------|-------|
| **Faithfulness** | Is the response factually grounded in context? | 0-1 |
| **Context Precision** | Are relevant chunks ranked at the top? | 0-1 |
| **Context Recall** | Are all relevant facts retrieved? | 0-1 |
| **Answer Relevancy** | Does the response address the query? | 0-1 |

---

### 5. Metrics-Driven Development

Use evaluation scores to guide systematic improvement:

```
┌───────────────────────────────────────────────────────────┐
│              METRICS-DRIVEN DEVELOPMENT                    │
│                                                            │
│   1. BASELINE          2. ANALYZE           3. IMPROVE    │
│   Run initial      →   Identify weak    →   Make targeted │
│   evaluation           metrics              changes        │
│        │                                         │         │
│        └─────────────── 4. MEASURE ◄────────────┘         │
│                         Re-run and                         │
│                         compare                            │
└───────────────────────────────────────────────────────────┘
```

**Improvement strategies by metric:**

| Low Metric | Likely Cause | Fix |
|------------|--------------|-----|
| Faithfulness | Hallucination | Constrain prompt, add citations |
| Context Precision | Poor ranking | Add reranker, tune embeddings |
| Context Recall | Missing chunks | Increase k, improve chunking |
| Answer Relevancy | Off-topic response | Refine prompt template |

---

## Recommended Reading

### Required
1. [All About Synthetic Data Generation](https://blog.ragas.io/all-about-synthetic-data-generation) - RAGAS Blog (Nov 2024)
2. [RAG Testset Generation](https://docs.ragas.io/en/stable/getstarted/rag_testset_generation/) - RAGAS Documentation
3. [LangSmith Evaluation Quickstart](https://docs.langchain.com/langsmith/evaluation-quickstart) - LangChain

### Recommended
4. [RAGAS: Automated Evaluation of RAG](https://arxiv.org/abs/2309.15217) - Original paper (Sep 2023)
5. [Mastering LLM Techniques: Evaluation](https://developer.nvidia.com/blog/mastering-llm-techniques-evaluation/) - NVIDIA (Jan 2025)
6. [In Defense of Evals](https://www.sh-reya.com/blog/in-defense-ai-evals/) - Shreya Shankar (Sep 2025)
7. [Hard-Earned Lessons from 2 Years of Improving AI Applications](https://blog.ragas.io/hard-earned-lessons-from-2-years-of-improving-ai-applications) - RAGAS (May 2025)

### Reference Project
8. [GDELT Knowledge Base](https://github.com/donbr/gdelt-knowledge-base) - Certification challenge example using RAGAS 0.2.10 with 4 retrieval strategies

---

## Assignment

### Core Requirements

1. **Generate a synthetic testset** from your document corpus using RAGAS TestsetGenerator
   - Include at least 3 question types (simple, reasoning, multi_context)
   - Generate minimum 10-20 test examples

2. **Export to LangSmith** for versioned tracking
   - Upload the testset as a LangSmith dataset
   - Verify examples appear correctly in the UI

3. **Run RAGAS evaluation** on your agentic RAG application
   - Evaluate with at least 2 metrics (e.g., faithfulness + context precision)
   - Document your baseline scores

4. **Analyze and document** findings
   - Which metric is lowest? What might cause this?
   - Propose one improvement based on metrics-driven development

---

## Advanced Build

**Implement testset generation using a LangGraph agent** instead of the knowledge graph approach.

Design an agent that:
- Reads documents and extracts key concepts
- Generates diverse question types through tool calls
- Validates question quality before adding to testset
- Outputs in RAGAS-compatible format

**Reflection questions:**
- How do the generated questions differ from knowledge graph synthesis?
- What are the tradeoffs between agent-based and graph-based generation?
- When would you choose one approach over the other?

---

## Session Connections

| Previous Sessions | This Session | Next Sessions |
|-------------------|--------------|---------------|
| Session 4: Agentic RAG | Evaluate RAG quality | Session 10: Agentic RAG Evaluation |
| Session 8: Deep Research | Test complex retrieval | Session 11: Advanced Retrievers |

---

*Session 9 | AIE9 Cohort | January 2026*
