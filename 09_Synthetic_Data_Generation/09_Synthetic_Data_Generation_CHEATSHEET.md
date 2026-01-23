# Session 9: Synthetic Data Generation for Evals - CHEATSHEET

> **Teaching Mode**: This cheatsheet provides reference material for AI Engineering Bootcamp students.
> Concepts are explained before code. Examples are minimal. Learners should discover solutions through practice.

---

## Quick Reference Table

| Concept | Definition | Key API/Pattern |
|---------|------------|-----------------|
| Synthetic Data | LLM-generated test data that simulates production scenarios | `TestsetGenerator.generate()` |
| Knowledge Graph | Document relationship structure enabling multi-hop queries | `KnowledgeGraph(nodes, relationships)` |
| Question Evolution | Transforming simple questions into complex variants | `simple`, `reasoning`, `multi_context` |
| Faithfulness | Whether response is factually grounded in retrieved context | `faithfulness.ascore()` |
| Context Precision | How well retriever ranks relevant chunks at top | `context_precision.single_turn_ascore()` |
| Context Recall | Proportion of reference claims supported by retrieval | `context_recall.single_turn_ascore()` |
| Answer Relevancy | How well response addresses the original query | `answer_relevancy.ascore()` |
| Metrics-Driven Dev | Using quantitative scores to guide systematic improvement | Baseline → Measure → Improve → Repeat |
| LangSmith Dataset | Evaluation dataset with inputs, outputs, references | `client.create_dataset()` |
| LLM-as-Judge | Using LLMs to evaluate other LLM outputs | `evaluate()` with RAGAS metrics |

---

## Setup Requirements

### Dependencies

```bash
pip install ragas>=0.2.0 langchain-openai langsmith pandas
```

### Environment Variables

```bash
export OPENAI_API_KEY="your-key-here"
export LANGSMITH_API_KEY="your-key-here"
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_PROJECT="synthetic-data-evals"
```

### Version Requirements

| Package | Minimum Version | Purpose |
|---------|----------------|---------|
| `ragas` | 0.2.0 | Testset generation and evaluation |
| `langsmith` | 0.2.0 | Dataset management and experiments |
| `langchain-openai` | 0.1.0 | LLM and embedding providers |
| `pandas` | 2.0.0 | DataFrame operations |

---

## Section 3: Why Synthetic Data?

> "Creating evaluation datasets manually is resource-intensive. Synthetic data generation automates this process, enabling rapid testing of LLM applications while simulating diverse real-world scenarios."
> — RAGAS Documentation [[1]](https://blog.ragas.io/all-about-synthetic-data-generation)

### The Problem with Manual Test Data

```
┌─────────────────────────────────────────────────────────────┐
│                  MANUAL DATA CREATION                        │
│                                                              │
│  Subject Matter    ───►  Write Questions  ───►  Validate    │
│  Experts ($$)            (Time-consuming)       (Bias)       │
│                                                              │
│  Problems:                                                   │
│  • Expensive and slow                                        │
│  • Limited diversity                                         │
│  • Human bias in question types                              │
│  • Doesn't scale with document updates                       │
└─────────────────────────────────────────────────────────────┘
```

### When to Use Synthetic Data

| Scenario | Use Synthetic? | Why |
|----------|---------------|-----|
| No existing eval dataset | Yes | Bootstrap evaluation quickly |
| New document corpus | Yes | Generate domain-specific tests |
| Testing retrieval changes | Yes | Consistent baseline comparisons |
| Production monitoring | Partial | Supplement with real user queries |
| High-stakes domains | Partial | Always validate with human review |

**Question to consider**: What are the risks of relying entirely on synthetic data for evaluation?

---

## Section 4: Knowledge Graph Approach

> "Rather than generating QA pairs from random document chunks, a more sophisticated method involves constructing a knowledge graph that connects related documents."
> — RAGAS Blog [[1]](https://blog.ragas.io/all-about-synthetic-data-generation)

### Simple vs. Knowledge Graph Generation

```
┌─────────────────────────────────────────────────────────────┐
│              SIMPLE CHUNK-BASED GENERATION                   │
│                                                              │
│   Doc A        Doc B        Doc C                            │
│   ┌───┐        ┌───┐        ┌───┐                           │
│   │ ? │        │ ? │        │ ? │   Random questions        │
│   └───┘        └───┘        └───┘   per chunk               │
│                                                              │
│   Limitations:                                               │
│   • Cannot create multi-hop queries                          │
│   • Biased toward chunk size                                 │
│   • Overly specific questions                                │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│              KNOWLEDGE GRAPH GENERATION                      │
│                                                              │
│         Doc A ◄──────────► Doc B                            │
│           │                  │                               │
│           │    Entity X      │                               │
│           │        │         │                               │
│           ▼        ▼         ▼                               │
│         Doc C ◄──────────► Doc D                            │
│                                                              │
│   Benefits:                                                  │
│   • Multi-hop reasoning questions                            │
│   • Cross-document relationships                             │
│   • Diverse question complexity                              │
└─────────────────────────────────────────────────────────────┘
```

### Knowledge Graph Structure

After document transformation, RAGAS creates:

| Component | Description | Example |
|-----------|-------------|---------|
| **Nodes** | Documents + extracted entities | Person, Organization, Concept |
| **Relationships** | Semantic connections | "mentions", "relates_to", "contradicts" |
| **Properties** | Metadata on nodes/edges | Source document, confidence score |

**Pattern**: `KnowledgeGraph(nodes: 48, relationships: 605)`

---

## Section 5: TestsetGenerator API

> "The TestsetGenerator transforms documents into a knowledge graph, then synthesizes diverse query types from the graph structure."
> — RAGAS Documentation [[2]](https://docs.ragas.io/en/stable/getstarted/rag_testset_generation/)

### Core Generation Pattern

```python
generator = TestsetGenerator(llm=llm, embedding_model=embeddings)
testset = generator.generate(testset_size=10, query_distribution=dist)
```

### Document Loading Integration

RAGAS integrates with multiple document loaders:

| Loader | Method | Use Case |
|--------|--------|----------|
| LangChain | `generate_with_langchain_docs()` | LangChain document objects |
| LlamaIndex | `generate_with_llamaindex_docs()` | LlamaIndex node objects |
| Plain Text | `generate_with_chunks()` | Pre-chunked string lists |

### Generation Workflow

```
┌──────────────────────────────────────────────────────────────┐
│                    TESTSET GENERATION                         │
│                                                               │
│  ┌─────────┐    ┌─────────────┐    ┌──────────────────────┐  │
│  │Documents│───►│  Transform  │───►│   Knowledge Graph    │  │
│  └─────────┘    │  (Enrich)   │    │  (nodes + edges)     │  │
│                 └─────────────┘    └──────────┬───────────┘  │
│                                               │              │
│                                               ▼              │
│  ┌─────────┐    ┌─────────────┐    ┌──────────────────────┐  │
│  │ Testset │◄───│  Synthesize │◄───│  Query Distribution  │  │
│  │ (Q+A)   │    │  (Generate) │    │  (simple/multi-hop)  │  │
│  └─────────┘    └─────────────┘    └──────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

---

## Section 6: Question Types (Evolutions)

> "Different question types test different aspects of your RAG system: simple questions test basic retrieval, while multi-hop questions test the ability to synthesize across sources."
> — RAGAS Documentation [[2]](https://docs.ragas.io/en/stable/getstarted/rag_testset_generation/)

### Evolution Types

| Type | Description | Tests |
|------|-------------|-------|
| `simple` | Direct factual questions | Basic retrieval accuracy |
| `reasoning` | Requires inference from facts | LLM reasoning capability |
| `multi_context` | Needs info from multiple chunks | Cross-document retrieval |

### Distribution Pattern

```python
distribution = {simple: 0.5, reasoning: 0.25, multi_context: 0.25}
```

### Query Synthesizers

| Synthesizer | Complexity | Example Question |
|-------------|------------|------------------|
| `SingleHopSpecificQuerySynthesizer` | Low | "What is X?" |
| `MultiHopAbstractQuerySynthesizer` | Medium | "How does X relate to Y?" |
| `MultiHopSpecificQuerySynthesizer` | High | "Given X in doc A and Y in doc B, what is Z?" |

**Reflection**: Which distribution would you use for a legal document QA system? Why?

---

## Section 7: RAGAS Evaluation Metrics

> "RAGAS provides objective metrics for evaluating RAG pipelines, measuring both retrieval quality and generation faithfulness."
> — RAGAS Paper [[3]](https://arxiv.org/abs/2309.15217)

### Core Metrics Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    RAG EVALUATION METRICS                    │
│                                                              │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                  RETRIEVAL METRICS                       ││
│  │                                                          ││
│  │  Context Precision: Are relevant chunks ranked high?     ││
│  │  Context Recall: Are all relevant chunks retrieved?      ││
│  │                                                          ││
│  └─────────────────────────────────────────────────────────┘│
│                           │                                  │
│                           ▼                                  │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                 GENERATION METRICS                       ││
│  │                                                          ││
│  │  Faithfulness: Is response grounded in context?          ││
│  │  Answer Relevancy: Does response address the query?      ││
│  │                                                          ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

### Metric Formulas

| Metric | Formula | Range |
|--------|---------|-------|
| Context Precision | Mean(Precision@k) for each ranked chunk | 0-1 |
| Context Recall | Claims supported / Total claims | 0-1 |
| Faithfulness | Faithful claims / Total claims | 0-1 |
| Answer Relevancy | Cosine similarity of generated questions | 0-1 |

### Metric Requirements

| Metric | Requires Reference? | Uses LLM? |
|--------|-------------------|-----------|
| Context Precision | Yes | Yes |
| Context Recall | Yes | Yes |
| Faithfulness | No | Yes |
| Answer Relevancy | No | Yes + Embeddings |

---

## Section 8: Faithfulness Deep Dive

> "Faithfulness measures the factual consistency of the generated answer against the given context. A score of 1.0 means every claim in the response is supported by the retrieved context."
> — RAGAS Documentation [[4]](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/)

### How Faithfulness Works

```
┌─────────────────────────────────────────────────────────────┐
│                  FAITHFULNESS CALCULATION                    │
│                                                              │
│  Response: "Paris is the capital of France, founded         │
│             by Romans in 52 BCE."                           │
│                                                              │
│  Step 1: Extract Claims                                      │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ Claim 1: Paris is the capital of France               │  │
│  │ Claim 2: Paris was founded by Romans in 52 BCE        │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                              │
│  Step 2: Verify Against Context                              │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ Context: "Paris is the capital of France..."          │  │
│  │                                                        │  │
│  │ Claim 1: ✓ Supported                                  │  │
│  │ Claim 2: ✗ Not found in context                       │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                              │
│  Faithfulness = 1/2 = 0.5                                    │
└─────────────────────────────────────────────────────────────┘
```

### Scoring Pattern

```python
score = await faithfulness.ascore(
    user_input="query",
    response="answer",
    retrieved_contexts=["context1", "context2"]
)
```

---

## Section 9: Context Precision & Recall

> "Context Precision evaluates whether relevant chunks are ranked higher. Context Recall measures whether all relevant information was retrieved."
> — RAGAS Documentation [[5]](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/)

### Precision vs. Recall

```
┌─────────────────────────────────────────────────────────────┐
│              CONTEXT PRECISION VS. RECALL                    │
│                                                              │
│  Retrieved Chunks:      Reference (Ground Truth):            │
│  ┌───┐ ┌───┐ ┌───┐     ┌───────────────────────┐            │
│  │ A │ │ B │ │ C │     │ Claims: C1, C2, C3    │            │
│  └───┘ └───┘ └───┘     └───────────────────────┘            │
│    ✓     ✗     ✓                                             │
│                                                              │
│  PRECISION: Are top-ranked chunks relevant?                  │
│  • Chunk A (rank 1): Relevant ✓                              │
│  • Chunk B (rank 2): Not relevant ✗                          │
│  • Chunk C (rank 3): Relevant ✓                              │
│  • Precision@3 = 2/3 = 0.67                                  │
│                                                              │
│  RECALL: Are all reference claims covered?                   │
│  • C1: Found in chunk A ✓                                    │
│  • C2: Found in chunk C ✓                                    │
│  • C3: Not in any chunk ✗                                    │
│  • Recall = 2/3 = 0.67                                       │
└─────────────────────────────────────────────────────────────┘
```

### When to Prioritize Each

| Scenario | Prioritize | Why |
|----------|-----------|-----|
| Limited context window | Precision | Need best chunks at top |
| Comprehensive answers | Recall | Must not miss information |
| Legal/medical | Both high | Accuracy and completeness critical |

---

## Section 10: LangSmith Dataset Integration

> "Datasets enable you to perform repeatable evaluations over time using consistent data."
> — LangSmith Documentation [[6]](https://docs.langchain.com/langsmith/evaluation)

### Dataset Structure

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Unique identifier |
| `inputs` | object | Query/question data |
| `outputs` | object | Generated response |
| `reference_outputs` | object | Ground truth answer |
| `metadata` | object | Additional annotations |

### RAGAS to LangSmith Workflow

```
┌─────────────────────────────────────────────────────────────┐
│              RAGAS → LANGSMITH INTEGRATION                   │
│                                                              │
│  ┌──────────────┐                                           │
│  │    RAGAS     │                                           │
│  │   Testset    │                                           │
│  └──────┬───────┘                                           │
│         │                                                    │
│         ▼                                                    │
│  ┌──────────────┐     ┌──────────────┐                      │
│  │  to_pandas() │────►│  DataFrame   │                      │
│  └──────────────┘     └──────┬───────┘                      │
│                              │                               │
│                              ▼                               │
│  ┌──────────────────────────────────────┐                   │
│  │  client.upload_dataframe(            │                   │
│  │      df=df,                          │                   │
│  │      input_keys=["user_input"],      │                   │
│  │      output_keys=["reference"]       │                   │
│  │  )                                   │                   │
│  └──────────────────────────────────────┘                   │
│                              │                               │
│                              ▼                               │
│  ┌──────────────────────────────────────┐                   │
│  │         LangSmith Dataset            │                   │
│  │   (versioned, shareable, trackable)  │                   │
│  └──────────────────────────────────────┘                   │
└─────────────────────────────────────────────────────────────┘
```

### Upload Pattern

```python
client.upload_dataframe(
    df=testset.to_pandas(),
    input_keys=["user_input"],
    output_keys=["reference"],
    name="rag-eval-dataset"
)
```

---

## Section 11: Metrics-Driven Development

> "Evaluations provide a structured way to identify failures, compare versions, and build more reliable AI applications."
> — LangSmith Documentation [[6]](https://docs.langchain.com/langsmith/evaluation)

### The MDD Loop

```
┌─────────────────────────────────────────────────────────────┐
│              METRICS-DRIVEN DEVELOPMENT                      │
│                                                              │
│           ┌───────────────────────────┐                      │
│           │     1. BASELINE           │                      │
│           │  Run initial evaluation   │                      │
│           └───────────┬───────────────┘                      │
│                       │                                      │
│                       ▼                                      │
│           ┌───────────────────────────┐                      │
│           │     2. ANALYZE            │                      │
│           │  Identify weak metrics    │                      │
│           └───────────┬───────────────┘                      │
│                       │                                      │
│    ┌──────────────────┴──────────────────┐                   │
│    ▼                                     ▼                   │
│ Low Faithfulness?              Low Context Precision?        │
│ • Check prompt grounding       • Tune retriever k            │
│ • Add citations                • Improve chunking            │
│ • Constrain response           • Add reranking               │
│                                                              │
│           ┌───────────────────────────┐                      │
│           │     3. IMPLEMENT          │                      │
│           │  Make targeted changes    │                      │
│           └───────────┬───────────────┘                      │
│                       │                                      │
│                       ▼                                      │
│           ┌───────────────────────────┐                      │
│           │     4. MEASURE            │                      │
│           │  Re-run evaluation        │◄─────── Repeat       │
│           └───────────────────────────┘                      │
└─────────────────────────────────────────────────────────────┘
```

### Improvement Strategies by Metric

| Low Metric | Possible Causes | Improvement Strategies |
|------------|----------------|----------------------|
| Faithfulness | Hallucination | Constrain prompt, add grounding |
| Context Precision | Poor ranking | Add reranker, tune embeddings |
| Context Recall | Missing chunks | Increase k, improve chunking |
| Answer Relevancy | Off-topic | Refine prompt template |

---

## Section 12: Human-in-the-Loop Verification

> "Human oversight remains crucial in synthetic data workflows—multi-rater validation catches LLM-generated errors that automated checks miss."
> — Humanloop Documentation [[18]](https://humanloop.com/docs/v4/guides/evaluation/overview)

### Why Validate Synthetic Data?

Synthetic data can contain:
- **Hallucinated questions** not answerable from context
- **Biased distributions** overrepresenting certain topics
- **Repetitive patterns** reducing dataset diversity
- **Incorrect ground truth** answers

### Quality Assurance Workflow

```
┌─────────────────────────────────────────────────────────────┐
│              SYNTHETIC DATA VALIDATION                       │
│                                                              │
│  ┌──────────────┐     ┌──────────────┐     ┌─────────────┐  │
│  │  Generated   │────►│  Sample      │────►│  Human      │  │
│  │  Testset     │     │  5-10%       │     │  Review     │  │
│  └──────────────┘     └──────────────┘     └──────┬──────┘  │
│                                                    │         │
│                              ┌─────────────────────┼─────┐   │
│                              ▼                     ▼     │   │
│                       ┌──────────┐          ┌──────────┐ │   │
│                       │  Pass    │          │  Fail    │ │   │
│                       │  (Use)   │          │  (Fix)   │─┘   │
│                       └──────────┘          └──────────┘     │
└─────────────────────────────────────────────────────────────┘
```

### Quality Metrics for Synthetic Data

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Human agreement | >80% | Cohen's Kappa on audit sample |
| Uniqueness | >95% | Deduplication pass |
| Answerability | 100% | Human verification |
| Factual accuracy | >95% | Expert review |

**Question to consider**: How would you design a validation process for high-stakes domains like healthcare or legal?

---

## Section 13: Evaluation Framework Comparison

> "DeepEval provides 14+ metrics with self-explaining scores, while RAGAS focuses on RAG-specific evaluation with strong industry adoption."
> — Confident AI [[19]](https://www.confident-ai.com/blog/greatest-llm-evaluation-tools-in-2025)

### Framework Landscape (2026)

| Framework | Best For | Key Metrics | HITL Support | Open Source |
|-----------|----------|-------------|--------------|-------------|
| **RAGAS** | RAG pipelines | 4 core RAG metrics | Manual | Yes |
| **DeepEval** | RAG + Fine-tuning | 14+ with explanations | Native | Yes |
| **MLflow** | Pipeline integration | Modular, extensible | Via plugins | Yes |
| **Promptfoo** | Prompt testing | YAML-based, simple | No | Yes |
| **LangSmith** | Production evals | Full lifecycle | Native | Partial |

### When to Use Each

```
┌─────────────────────────────────────────────────────────────┐
│              FRAMEWORK SELECTION GUIDE                       │
│                                                              │
│  Starting RAG project?                                       │
│  └── Use RAGAS (industry standard, well-documented)         │
│                                                              │
│  Need detailed debugging?                                    │
│  └── Use DeepEval (self-explaining scores)                  │
│                                                              │
│  Have existing ML pipelines?                                 │
│  └── Use MLflow (integrates with MLOps)                     │
│                                                              │
│  Quick prompt experiments?                                   │
│  └── Use Promptfoo (YAML config, fast iteration)            │
│                                                              │
│  Production monitoring needed?                               │
│  └── Use LangSmith (full observability + eval)              │
└─────────────────────────────────────────────────────────────┘
```

### GDELT Project Example

The [GDELT Knowledge Base](https://github.com/donbr/gdelt-knowledge-base) certification project demonstrates production patterns:

| Aspect | Implementation |
|--------|----------------|
| RAGAS version | 0.2.10 (pinned for stability) |
| Retrieval strategies | 4 compared (naive, BM25, ensemble, Cohere rerank) |
| Best result | Cohere-reranked at 95.1% average |
| Provenance | SHA-256 hashes for data lineage |
| Public datasets | 4 Apache 2.0 licensed on Hugging Face |

---

## Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| `TestsetGenerator` timeout | Large document corpus | Reduce document count or chunk size |
| Low faithfulness scores | LLM hallucinating | Use stronger grounding in prompt |
| Empty `retrieved_contexts` | Retriever returning nothing | Check vector DB connection and embeddings |
| `Rate limit exceeded` | Too many API calls | Add delays, use async batching |
| Inconsistent metric scores | Non-deterministic LLM | Set temperature=0 for evaluation LLM |
| `KeyError: 'reference'` | Missing ground truth column | Ensure testset has reference answers |
| LangSmith upload fails | Invalid data types | Convert all values to JSON-serializable types |
| Knowledge graph empty | No relationships extracted | Use stronger LLM for extraction |

---

## References

1. RAGAS Team. "All About Synthetic Data Generation." RAGAS Blog, Nov 2024. https://blog.ragas.io/all-about-synthetic-data-generation

2. RAGAS Documentation. "RAG Testset Generation." https://docs.ragas.io/en/stable/getstarted/rag_testset_generation/

3. Es, S., et al. "RAGAS: Automated Evaluation of Retrieval Augmented Generation." arXiv:2309.15217, Sep 2023. https://arxiv.org/abs/2309.15217

4. RAGAS Documentation. "Faithfulness Metric." https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/

5. RAGAS Documentation. "Context Precision Metric." https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/

6. LangChain. "LangSmith Evaluation." https://docs.langchain.com/langsmith/evaluation

7. LangChain. "Evaluation Quickstart." https://docs.langchain.com/langsmith/evaluation-quickstart

8. LangChain. "Create and Manage Datasets." https://docs.langchain.com/langsmith/manage-datasets-in-application

9. NVIDIA. "Mastering LLM Techniques: Evaluation." NVIDIA Developer Blog, Jan 2025. https://developer.nvidia.com/blog/mastering-llm-techniques-evaluation/

10. LangChain. "Example Data Format." https://docs.langchain.com/langsmith/example-data-format

11. LangChain. "Prebuilt Evaluators." https://docs.langchain.com/langsmith/prebuilt-evaluators

12. LangChain. "LLM-as-a-Judge Evaluator." https://docs.langchain.com/langsmith/llm-as-judge

13. RAGAS Documentation. "Context Recall Metric." https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_recall/

14. RAGAS Documentation. "Answer Relevancy Metric." https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/answer_relevance/

15. LangChain. "Upload Datasets from DataFrame." https://docs.langchain.com/langsmith/manage-datasets-programmatically

16. Shreya Shankar. "In Defense of Evals." Blog, Sep 2025. https://www.sh-reya.com/blog/in-defense-ai-evals/

17. RAGAS Team. "Hard-Earned Lessons from 2 Years of Improving AI Applications." RAGAS Blog, May 2025. https://blog.ragas.io/hard-earned-lessons-from-2-years-of-improving-ai-applications

18. Humanloop. "Evaluation Overview & HITL Workflows." https://humanloop.com/docs/v4/guides/evaluation/overview

19. Confident AI. "Greatest LLM Evaluation Tools in 2025." https://www.confident-ai.com/blog/greatest-llm-evaluation-tools-in-2025

20. GDELT Knowledge Base. "Certification Challenge Example Project." https://github.com/donbr/gdelt-knowledge-base

21. DeepEval Documentation. "RAG Evaluation Metrics." https://docs.confident-ai.com/docs/metrics-rag

22. Langfuse. "Synthetic Dataset Generation for LLM Evaluation." https://langfuse.com/guides/cookbook/example_synthetic_datasets

23. SuperAnnotate. "Human-in-the-Loop AI Complete Guide." https://www.superannotate.com/blog/human-in-the-loop-hitl

---

## Assignment Checklist

Before submitting your Session 9 assignment, verify:

- [ ] Generated synthetic testset with at least 3 question types
- [ ] Exported testset to pandas DataFrame
- [ ] Validated sample (5-10%) for quality and answerability
- [ ] Uploaded dataset to LangSmith successfully
- [ ] Ran evaluation with at least 2 RAGAS metrics
- [ ] Documented baseline metric scores
- [ ] Identified which metric needs most improvement
- [ ] Proposed one improvement based on metrics-driven development

**Advanced Build**: Implement testset generation using a LangGraph agent instead of the knowledge graph approach. Compare the generated questions: How do they differ in complexity, diversity, and domain coverage?

---

*Last updated: January 2026 | AIE9 Cohort*
