# Session 10 Cheatsheet: Agentic RAG Evaluation

> From Vibe Checks to Systematic Measurement

---

## Quick Reference

| Concept | Definition | Key API/Pattern |
|---------|------------|-----------------|
| Offline Evaluation | Pre-deployment testing on curated datasets | `evaluate()` |
| Online Evaluation | Production monitoring on real traffic | LangSmith rules |
| Context Precision | Ranking quality of retrieved documents | RAGAS metric |
| Context Recall | Completeness of retrieved information | RAGAS metric |
| Faithfulness | Response grounding in context | RAGAS metric |
| Answer Relevancy | Response alignment with query | RAGAS metric |
| Trajectory Match | Exact comparison against reference path | AgentEvals |
| LLM-as-Judge | LLM scoring against rubric | Custom evaluator |
| Golden Dataset | Curated, versioned test set | LangSmith dataset |
| Evaluation-Driven Dev | Metrics guide improvements | Cycle pattern |

---

## Setup Requirements

### Dependencies
```bash
pip install langsmith>=0.2.0 ragas>=0.2.0 langchain-openai agentevals
```

### Environment Variables
```python
import os
os.environ["OPENAI_API_KEY"] = "your-key"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-langsmith-key"
os.environ["LANGCHAIN_PROJECT"] = "AIE9-Session10"
```

---

## 1. The Evaluation Hierarchy

### Progression of Rigor
```
┌───────────────────────────────────────────────────────────────┐
│                   EVALUATION HIERARCHY                         │
│                                                                │
│   DEVELOPMENT              PRE-PRODUCTION         PRODUCTION   │
│   ───────────              ─────────────          ──────────   │
│                                                                │
│   ┌─────────┐   ┌─────────┐   ┌───────────┐   ┌───────────┐  │
│   │  Vibe   │ → │  Unit   │ → │  Offline  │ → │  Online   │  │
│   │  Check  │   │  Tests  │   │  Evals    │   │ Monitoring│  │
│   └─────────┘   └─────────┘   └───────────┘   └───────────┘  │
│                                                                │
│   Informal      Deterministic   Datasets       Real traffic   │
│   cursory       fast            metrics        continuous     │
└───────────────────────────────────────────────────────────────┘
```

### When to Use Each
| Stage | Use Case | Cost |
|-------|----------|------|
| Vibe Check | Early sanity checks, quick iterations | Low |
| Unit Tests | Deterministic logic, regression prevention | Low |
| Offline Evals | Pre-release quality gates, comparisons | Medium |
| Online Monitoring | Production quality, drift detection | Higher |

> "Evaluations are a quantitative way to measure the performance of LLM applications."
> — [LangSmith Documentation](https://docs.langchain.com/langsmith/evaluation-quickstart)

**Official Docs**: [LangSmith Evaluation](https://docs.langchain.com/langsmith/evaluation)

---

## 2. Component-Level vs End-to-End

### Architecture Diagram
```
┌────────────────────────────────────────────────────────────────┐
│              COMPONENT-LEVEL EVALUATION                         │
│                                                                 │
│        ┌─────────────────┐         ┌─────────────────┐         │
│        │    RETRIEVAL    │         │   GENERATION    │         │
│        │                 │         │                 │         │
│        │ Did we find the │         │ Did we answer   │         │
│        │ right documents?│    +    │ faithfully and  │         │
│        │                 │         │ relevantly?     │         │
│        └────────┬────────┘         └────────┬────────┘         │
│                 │                           │                   │
│                 ▼                           ▼                   │
│         Context Precision           Faithfulness               │
│         Context Recall              Answer Relevancy           │
│         Hit Rate, MRR               Hallucination Rate         │
└────────────────────────────────────────────────────────────────┘
```

### Why Component-Level?
- **Faster debugging**: Isolate retrieval vs generation failures
- **Targeted fixes**: Know exactly what to improve
- **Clear accountability**: Each component has its own metrics

> "Rather than treating RAG as a black box, evaluating retrieval and generation separately enables faster debugging."
> — [Evidently AI](https://www.evidentlyai.com/llm-guide/rag-evaluation)

**Official Docs**: [RAG Evaluation Tutorial](https://docs.langchain.com/langsmith/evaluate-rag-tutorial)

---

## 3. Retrieval Evaluation Metrics

### Core Retrieval Metrics
| Metric | Formula Concept | What It Measures |
|--------|-----------------|------------------|
| **Context Precision** | Relevant@k / k | Ranking quality (relevant docs at top?) |
| **Context Recall** | Retrieved relevant / Total relevant | Coverage (did we get everything?) |
| **Hit Rate** | 1 if any relevant in top-k, else 0 | Basic success check |
| **MRR** | 1 / rank of first relevant | How early is the first hit? |
| **nDCG@k** | Graded relevance with position decay | Comprehensive ranking quality |

### Metric Interpretation
```
┌───────────────────────────────────────────────────────────────┐
│             RETRIEVAL METRIC DIAGNOSTICS                       │
│                                                                │
│   Low Context Precision              Low Context Recall        │
│   ──────────────────────            ─────────────────────      │
│   ✗ Irrelevant docs retrieved       ✗ Relevant docs missed    │
│   → Add reranker                    → Increase k               │
│   → Tune embedding model            → Improve chunking         │
│   → Refine query expansion          → Add query reformulation  │
└───────────────────────────────────────────────────────────────┘
```

### RAGAS Retrieval Evaluation
```python
from ragas.metrics import ContextPrecision, ContextRecall
from ragas import evaluate

metrics = [ContextPrecision(), ContextRecall()]
results = evaluate(dataset=eval_dataset, metrics=metrics)
```

**Official Docs**: [RAGAS Metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)

---

## 4. Generation Evaluation Metrics

### Core Generation Metrics
| Metric | What It Measures | Failure Mode |
|--------|------------------|--------------|
| **Faithfulness** | Is response grounded in context? | Hallucination |
| **Answer Relevancy** | Does response address the query? | Off-topic |
| **Hallucination Rate** | Unsupported/fabricated claims | Confabulation |
| **Citation Coverage** | Are claims backed by sources? | Unverifiable |

### Metric Interpretation
```
┌───────────────────────────────────────────────────────────────┐
│             GENERATION METRIC DIAGNOSTICS                      │
│                                                                │
│   Low Faithfulness                   Low Answer Relevancy      │
│   ────────────────                   ─────────────────────     │
│   ✗ Model hallucinating             ✗ Response off-topic      │
│   → Constrain prompt                → Refine prompt template  │
│   → Add "cite your sources"         → Add query in system msg │
│   → Lower temperature               → Check context relevance │
└───────────────────────────────────────────────────────────────┘
```

### RAGAS Generation Evaluation
```python
from ragas.metrics import Faithfulness, AnswerRelevancy
from ragas import evaluate

metrics = [Faithfulness(), AnswerRelevancy()]
results = evaluate(dataset=eval_dataset, metrics=metrics)
```

**Official Docs**: [RAGAS Faithfulness](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/)

---

## 5. Agentic-Specific Evaluation

### Beyond Traditional RAG
```
┌───────────────────────────────────────────────────────────────┐
│              AGENTIC EVALUATION DIMENSIONS                     │
│                                                                │
│   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐        │
│   │    Tool     │   │  Argument   │   │    Task     │        │
│   │  Selection  │   │ Correctness │   │ Completion  │        │
│   │             │   │             │   │             │        │
│   │ Right tool? │   │ Valid args? │   │ Goal met?   │        │
│   └─────────────┘   └─────────────┘   └─────────────┘        │
│                                                                │
│                   ┌─────────────┐                             │
│                   │ Trajectory  │                             │
│                   │   Quality   │                             │
│                   │             │                             │
│                   │ Efficient?  │                             │
│                   │ Appropriate?│                             │
│                   └─────────────┘                             │
└───────────────────────────────────────────────────────────────┘
```

### Agentic Failure Modes
| Failure | What Went Wrong | Detection |
|---------|-----------------|-----------|
| Wrong tool | Agent called irrelevant tool | Tool name mismatch |
| Bad arguments | Malformed or invalid params | Argument validation |
| Incomplete task | Goal not achieved | Task completion score |
| Inefficient path | Too many steps | Trajectory length |

> "Many agent behaviors only emerge when using a real LLM, such as which tool the agent decides to call."
> — [LangSmith Trajectory Evals](https://docs.langchain.com/langsmith/trajectory-evals)

**Official Docs**: [Agent Evaluation Approaches](https://docs.langchain.com/langsmith/evaluation-approaches#agents)

---

## 6. LLM-as-Judge Pattern

### How It Works
```
┌───────────────────────────────────────────────────────────────┐
│                   LLM-AS-JUDGE PATTERN                         │
│                                                                │
│   INPUTS                           JUDGE PROCESS               │
│   ──────                           ─────────────               │
│   ┌─────────────┐                 ┌─────────────────────────┐ │
│   │ User Query  │───────┐         │                         │ │
│   └─────────────┘       │         │  Judge LLM evaluates:   │ │
│   ┌─────────────┐       │         │                         │ │
│   │  Context    │───────┼────────►│  • Against rubric       │ │
│   └─────────────┘       │         │  • Structured scoring   │ │
│   ┌─────────────┐       │         │  • With reasoning       │ │
│   │  Response   │───────┤         │                         │ │
│   └─────────────┘       │         └───────────┬─────────────┘ │
│   ┌─────────────┐       │                     │               │
│   │   Rubric    │───────┘                     ▼               │
│   └─────────────┘                      Score + Explanation    │
└───────────────────────────────────────────────────────────────┘
```

### Best Practices
| Practice | Why It Matters |
|----------|----------------|
| Low-precision scales (0-3) | Clearer rubrics, more consistent |
| Include reasoning | Debuggable, explainable scores |
| Calibrate with humans | Validate judge accuracy |
| Use specialized judges | Lynx, Glider for hallucination |

> "LLM-as-a-judge agrees with human grading on over 80% of judgments."
> — [Databricks](https://www.databricks.com/blog/LLM-auto-eval-best-practices-RAG)

### Basic LLM-as-Judge Implementation
```python
from langsmith.evaluation import evaluate

def llm_judge(run, example):
    # Your judge logic here
    score = judge_llm.invoke(prompt)
    return {"score": score, "reasoning": reasoning}

results = evaluate(target, data=dataset, evaluators=[llm_judge])
```

**Official Docs**: [LLM-as-Judge Evaluators](https://docs.langchain.com/langsmith/evaluation-concepts#llm-as-judge)

---

## 7. Trajectory Evaluation

### Two Approaches
```
┌───────────────────────────────────────────────────────────────┐
│              TRAJECTORY EVALUATION APPROACHES                  │
│                                                                │
│   TRAJECTORY MATCH                   LLM JUDGE                 │
│   ────────────────                   ────────                  │
│   ┌───────────────┐                 ┌───────────────┐         │
│   │  Reference:   │                 │   Rubric:     │         │
│   │  tool_a → b → c│                │   "Efficient? │         │
│   └───────┬───────┘                 │    Correct?   │         │
│           │                         │    Complete?" │         │
│           ▼                         └───────┬───────┘         │
│   ┌───────────────┐                         │                 │
│   │   Actual:     │                         ▼                 │
│   │  tool_a → b → c│                 LLM evaluates             │
│   └───────┬───────┘                 trajectory quality        │
│           │                                                    │
│           ▼                                                    │
│   Exact match? ✓/✗                  Score + Reasoning          │
│                                                                │
│   BEST FOR:                         BEST FOR:                  │
│   Deterministic flows              Flexible tasks              │
│   Known-good paths                 Multiple valid paths        │
│   Fast, no LLM cost                Nuanced assessment          │
└───────────────────────────────────────────────────────────────┘
```

### AgentEvals Trajectory Match
```python
from agentevals import create_trajectory_match_evaluator

evaluator = create_trajectory_match_evaluator(
    match_tools=True,      # Check tool names
    match_arguments=True,  # Check arguments
)
```

### AgentEvals LLM Judge
```python
from agentevals import create_trajectory_llm_as_judge

evaluator = create_trajectory_llm_as_judge(
    model="openai:gpt-4o",
    prompt=TRAJECTORY_ACCURACY_PROMPT,
)
```

**Official Docs**: [Trajectory Evaluations](https://docs.langchain.com/langsmith/trajectory-evals)

---

## 8. Golden Dataset Design

### Characteristics of Good Datasets
```
┌───────────────────────────────────────────────────────────────┐
│               GOLDEN DATASET CHARACTERISTICS                   │
│                                                                │
│   ┌─────────────────────────────────────────────────────────┐ │
│   │                    REPRESENTATIVE                        │ │
│   │  • Mirrors real user queries                            │ │
│   │  • Covers full scope of system capabilities             │ │
│   └─────────────────────────────────────────────────────────┘ │
│                                                                │
│   ┌─────────────────────────────────────────────────────────┐ │
│   │                      DIVERSE                             │ │
│   │  • Easy queries (baseline)                              │ │
│   │  • Hard queries (stress test)                           │ │
│   │  • Edge cases (robustness)                              │ │
│   └─────────────────────────────────────────────────────────┘ │
│                                                                │
│   ┌─────────────────────────────────────────────────────────┐ │
│   │                      STABLE                              │ │
│   │  • Versioned for reproducibility                        │ │
│   │  • Frozen during experiments                            │ │
│   │  • Governance for updates                               │ │
│   └─────────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────────┘
```

### Dataset Sources
| Source | Quality | Cost | Best For |
|--------|---------|------|----------|
| Production logs | High (real) | Low | Representative coverage |
| Synthetic (Session 9) | Medium | Low | Scale, diversity |
| Expert curation | High | High | Critical edge cases |
| Adversarial | Variable | Medium | Security, robustness |

> "Golden datasets remain the foundation. These should cover the full scope of the system, balance easy and hard queries."
> — [Label Your Data](https://labelyourdata.com/articles/llm-fine-tuning/rag-evaluation)

### Creating a LangSmith Dataset
```python
from langsmith import Client

client = Client()
dataset = client.create_dataset("agentic-rag-golden-v1")
client.create_examples(
    inputs=[{"query": q} for q in queries],
    outputs=[{"answer": a} for a in answers],
    dataset_id=dataset.id,
)
```

**Official Docs**: [Managing Datasets](https://docs.langchain.com/langsmith/manage-datasets)

---

## 9. Online vs Offline Evaluation

### Comparison
```
┌───────────────────────────────────────────────────────────────┐
│              OFFLINE vs ONLINE EVALUATION                      │
│                                                                │
│   OFFLINE                            ONLINE                    │
│   ───────                            ──────                    │
│   When: Before deployment           When: During production    │
│                                                                │
│   Data: Curated datasets            Data: Real user traffic   │
│                                                                │
│   Purpose:                          Purpose:                   │
│   • Benchmark performance           • Monitor quality drift   │
│   • Compare versions                • Detect anomalies        │
│   • Catch regressions               • Sample for review       │
│                                                                │
│   Cost: Predictable                 Cost: Scales with traffic │
│                                                                │
│   ┌─────────────┐                   ┌─────────────┐           │
│   │  evaluate() │                   │  Rules +    │           │
│   │  function   │                   │  Sampling   │           │
│   └─────────────┘                   └─────────────┘           │
└───────────────────────────────────────────────────────────────┘
```

> "LangSmith supports two types of evaluations: Offline Evaluation to test before you ship, and Online Evaluation to monitor in production."
> — [LangSmith Documentation](https://docs.langchain.com/langsmith/evaluation)

### Running Offline Evaluation
```python
from langsmith.evaluation import evaluate

def target(inputs):
    return my_rag_app(inputs["query"])

results = evaluate(
    target,
    data="my-golden-dataset",
    evaluators=[faithfulness_eval, precision_eval],
    experiment_prefix="v2-baseline"
)
```

**Official Docs**: [Offline Evaluation](https://docs.langchain.com/langsmith/evaluation-quickstart)

---

## 10. Evaluation-Driven Development

### The Improvement Cycle
```
┌───────────────────────────────────────────────────────────────┐
│            EVALUATION-DRIVEN DEVELOPMENT CYCLE                 │
│                                                                │
│                    ┌─────────────┐                            │
│                    │  1. MEASURE │                            │
│                    │   baseline  │                            │
│                    └──────┬──────┘                            │
│                           │                                    │
│     ┌──────────────────── ▼ ────────────────────┐             │
│     │                                            │             │
│     │              ┌─────────────┐              │             │
│     │              │  2. ANALYZE │              │             │
│     │              │ weak metrics│              │             │
│     │              └──────┬──────┘              │             │
│     │                     │                      │             │
│     │                     ▼                      │             │
│     │              ┌─────────────┐              │             │
│     │              │  3. IMPROVE │              │             │
│     │              │  targeted   │              │             │
│     │              │  changes    │              │             │
│     │              └──────┬──────┘              │             │
│     │                     │                      │             │
│     └─────────────────────┴──────────────────────┘             │
│                           │                                    │
│                           ▼                                    │
│                    ┌─────────────┐                            │
│                    │ 4. VALIDATE │                            │
│                    │   re-measure│                            │
│                    └─────────────┘                            │
└───────────────────────────────────────────────────────────────┘
```

### Improvement Strategies by Metric
| Low Metric | Likely Cause | Fix Strategy |
|------------|--------------|--------------|
| **Faithfulness** | Hallucination | Constrain prompt, require citations |
| **Context Precision** | Poor ranking | Add reranker, tune embeddings |
| **Context Recall** | Missing info | Increase k, improve chunking |
| **Answer Relevancy** | Off-topic | Refine prompt template |
| **Task Completion** | Wrong tools | Improve tool descriptions |

**Official Docs**: [LangSmith Experiments](https://docs.langchain.com/langsmith/evaluation-concepts#experiment)

---

## 11. Code Patterns Reference

### Pattern 1: Full RAG Evaluation Pipeline
```python
from langsmith.evaluation import evaluate
from ragas.metrics import Faithfulness, ContextPrecision

def my_rag_target(inputs):
    """Your RAG pipeline."""
    return rag_chain.invoke(inputs["query"])

results = evaluate(
    my_rag_target,
    data="golden-dataset",
    evaluators=[
        Faithfulness(),
        ContextPrecision(),
    ],
)
print(results.to_pandas())
```

### Pattern 2: Trajectory Evaluation
```python
from agentevals import create_trajectory_llm_as_judge
from langsmith.evaluation import evaluate

trajectory_eval = create_trajectory_llm_as_judge(model="openai:gpt-4o")

results = evaluate(
    agent_target,
    data="agent-test-cases",
    evaluators=[trajectory_eval],
)
```

### Pattern 3: Custom LLM Judge
```python
def custom_judge(run, example):
    prompt = f"""Evaluate this response:
    Query: {example.inputs['query']}
    Response: {run.outputs['response']}

    Score 0-3 where:
    0 = Completely wrong
    1 = Partially correct
    2 = Mostly correct
    3 = Fully correct

    Return JSON: {{"score": <int>, "reasoning": "<str>"}}"""

    result = judge_llm.invoke(prompt)
    return {"score": result["score"], "reasoning": result["reasoning"]}
```

### Pattern 4: Evaluation-Driven Comparison
```python
# Run baseline
baseline = evaluate(
    my_rag_v1,
    data="golden-dataset",
    evaluators=[faithfulness, precision],
    experiment_prefix="v1-baseline"
)

# Run after improvement
improved = evaluate(
    my_rag_v2,
    data="golden-dataset",
    evaluators=[faithfulness, precision],
    experiment_prefix="v2-reranker"
)

# Compare in LangSmith UI
```

---

## Common Issues & Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| Low faithfulness scores | Model hallucinating | Add "answer only from context" to prompt |
| Low precision scores | Irrelevant docs retrieved | Add reranker, tune embedding model |
| Trajectory match fails | Multiple valid paths | Switch to LLM judge approach |
| Judge scores inconsistent | Ambiguous rubric | Use binary/3-point scale |
| Dataset not representative | Sample bias | Add production queries |
| Evaluation too slow | Large dataset | Sample subset for iteration |

---

## Breakout Room Tasks Summary

### Breakout Room 1 (Core Evaluation)
- [ ] Create a golden dataset with 10-15 test cases
- [ ] Run RAGAS evaluation (faithfulness + precision)
- [ ] Interpret baseline metrics
- [ ] Identify weakest metric and propose fix
- [ ] **Activity**: Implement one improvement and re-measure

### Breakout Room 2 (Agentic Evaluation)
- [ ] Set up trajectory evaluation for your agent
- [ ] Evaluate 5+ agent interactions
- [ ] Implement custom LLM-as-judge evaluator
- [ ] Compare trajectory match vs LLM judge
- [ ] **Activity**: Build evaluation-driven improvement cycle

---

## Official Documentation Links

### LangSmith Evaluation
- [Evaluation Quickstart](https://docs.langchain.com/langsmith/evaluation-quickstart)
- [Evaluation Concepts](https://docs.langchain.com/langsmith/evaluation-concepts)
- [RAG Evaluation Tutorial](https://docs.langchain.com/langsmith/evaluate-rag-tutorial)
- [Trajectory Evaluations](https://docs.langchain.com/langsmith/trajectory-evals)

### RAGAS
- [RAGAS Documentation](https://docs.ragas.io/)
- [Available Metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)

### AgentEvals
- [AgentEvals GitHub](https://github.com/langchain-ai/agentevals)

### Best Practices
- [Evidently AI RAG Evaluation Guide](https://www.evidentlyai.com/llm-guide/rag-evaluation)
- [Databricks LLM Auto-Eval](https://www.databricks.com/blog/LLM-auto-eval-best-practices-RAG)
- [CodeAnt Multi-Step Agent Evaluation](https://www.codeant.ai/blogs/evaluate-llm-agentic-workflows)

---

## References

1. LangSmith Documentation. "Evaluation Quickstart." https://docs.langchain.com/langsmith/evaluation-quickstart

2. LangSmith Documentation. "Evaluate a RAG Application." https://docs.langchain.com/langsmith/evaluate-rag-tutorial

3. LangSmith Documentation. "Trajectory Evaluations." https://docs.langchain.com/langsmith/trajectory-evals

4. LangSmith Documentation. "Application-specific Evaluation Approaches." https://docs.langchain.com/langsmith/evaluation-approaches

5. Evidently AI. "RAG Evaluation: Complete Guide." https://www.evidentlyai.com/llm-guide/rag-evaluation

6. Databricks. "Best Practices for LLM Evaluation of RAG Applications." https://www.databricks.com/blog/LLM-auto-eval-best-practices-RAG

7. RAGAS Documentation. "RAG Evaluation Metrics." https://docs.ragas.io/

8. Es, S. et al. "RAGAS: Automated Evaluation of Retrieval Augmented Generation." arXiv:2309.15217 (2023). https://arxiv.org/abs/2309.15217

9. CodeAnt. "Evaluating LLM Agents in Multi-Step Workflows." https://www.codeant.ai/blogs/evaluate-llm-agentic-workflows

10. Label Your Data. "RAG Evaluation: 2026 Metrics and Benchmarks." https://labelyourdata.com/articles/llm-fine-tuning/rag-evaluation

---

*Cheatsheet created for AIE9 Session 10: Agentic RAG Evaluation*
*Last updated: January 2026*
