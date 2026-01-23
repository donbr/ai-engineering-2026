# Session 10: Agentic RAG Evaluation

## Goal

Move beyond informal "vibe checks" to systematic evaluation of agentic RAG systems using quantitative metrics, structured datasets, and automated evaluation pipelines.

---

## Learning Outcomes

By the end of this session, you will be able to:

1. **Explain the evaluation hierarchy** from vibe checks to production monitoring and when to use each
2. **Design component-level evaluations** that isolate retrieval quality from generation quality
3. **Apply RAG evaluation metrics** (faithfulness, context precision/recall, answer relevancy)
4. **Evaluate agent trajectories** including tool selection, argument correctness, and task completion
5. **Implement LLM-as-judge evaluators** for subjective quality assessment
6. **Build evaluation-driven development workflows** to systematically improve RAG applications

---

## Tools Introduced

| Tool | Purpose | Documentation |
|------|---------|---------------|
| **LangSmith Evaluation** | Datasets, experiments, offline/online evaluation | [LangSmith Evaluation](https://docs.langchain.com/langsmith/evaluation) |
| **AgentEvals** | Trajectory match and LLM judge for agents | [Trajectory Evals](https://docs.langchain.com/langsmith/trajectory-evals) |
| **RAGAS Metrics** | Faithfulness, context precision/recall, answer relevancy | [docs.ragas.io](https://docs.ragas.io/) |

---

## Key Concepts

### 1. The Evaluation Hierarchy

Evaluation approaches form a hierarchy of increasing rigor and cost:

```
┌─────────────────────────────────────────────────────────────┐
│                 EVALUATION HIERARCHY                         │
│                                                              │
│   Development          Pre-Production         Production     │
│   ───────────          ─────────────          ──────────     │
│                                                              │
│   Vibe Check    →    Unit Tests      →    Offline Evals  →  │
│   (informal,         (deterministic,     (golden datasets,  │
│    cursory)           fast)               metrics)          │
│                                                              │
│                                           Online Monitoring  │
│                                           (real traffic,     │
│                                            continuous)       │
└─────────────────────────────────────────────────────────────┘
```

> "Evaluations are a quantitative way to measure the performance of LLM applications. LLMs can behave unpredictably, even small changes to prompts, models, or inputs can significantly affect results."
> — [LangSmith Documentation](https://docs.langchain.com/langsmith/evaluation-quickstart)

**Session 1 (Vibe Check)** established an informal baseline. This session adds systematic measurement.

---

### 2. Component-Level vs End-to-End Evaluation

Rather than treating RAG as a black box, evaluate components separately:

```
┌─────────────────────────────────────────────────────────────┐
│                COMPONENT-LEVEL EVALUATION                    │
│                                                              │
│   RETRIEVAL                         GENERATION               │
│   ─────────                         ──────────               │
│   Question: Did we find            Question: Did we answer   │
│   the right documents?             faithfully and relevantly?│
│                                                              │
│   Metrics:                         Metrics:                  │
│   • Context Precision              • Faithfulness            │
│   • Context Recall                 • Answer Relevancy        │
│   • Hit Rate, MRR, nDCG           • Hallucination Rate       │
└─────────────────────────────────────────────────────────────┘
```

**Why component-level?** When outputs fail, you can quickly identify whether the issue is poor document retrieval or hallucination by the generator. This enables targeted fixes.

---

### 3. RAG Evaluation Metrics Framework

Four core metrics cover the essential quality dimensions:

| Metric | Question It Answers | Component | Range |
|--------|---------------------|-----------|-------|
| **Context Precision** | Are relevant chunks ranked at the top? | Retrieval | 0-1 |
| **Context Recall** | Are all relevant facts retrieved? | Retrieval | 0-1 |
| **Faithfulness** | Is the response grounded in retrieved context? | Generation | 0-1 |
| **Answer Relevancy** | Does the response address the query? | Generation | 0-1 |

**Reading the metrics:**
- Low **Context Precision** → Retrieved irrelevant documents; ranking is poor
- Low **Context Recall** → Missed relevant information; need more chunks or better chunking
- Low **Faithfulness** → Hallucination; model not grounded in context
- Low **Answer Relevancy** → Off-topic; prompt template may need refinement

---

### 4. Agentic-Specific Evaluation

Agents add complexity beyond traditional RAG. Evaluation must account for:

**Tool Selection**: Did the agent call the right tools?
**Argument Correctness**: Were the tool arguments valid?
**Task Completion**: Did the agent achieve the user's goal?
**Trajectory Quality**: Was the path efficient and appropriate?

> "Many agent behaviors only emerge when using a real LLM, such as which tool the agent decides to call, how it formats responses, or whether a prompt modification affects the entire execution trajectory."
> — [LangChain AgentEvals](https://docs.langchain.com/langsmith/trajectory-evals)

**Two trajectory evaluation approaches:**

| Approach | How It Works | Best For |
|----------|--------------|----------|
| **Trajectory Match** | Compare against reference trajectory step-by-step | Deterministic workflows |
| **LLM Judge** | LLM scores trajectory against rubric | Flexible, multi-path tasks |

---

### 5. LLM-as-Judge Pattern

Use a language model to evaluate outputs when human judgment is needed but expensive:

```
┌─────────────────────────────────────────────────────────────┐
│                   LLM-AS-JUDGE PATTERN                       │
│                                                              │
│   Input:                                                     │
│   ├── User Query                                            │
│   ├── Retrieved Context                                     │
│   ├── Generated Response                                    │
│   └── Evaluation Rubric                                     │
│                                                              │
│   Judge LLM evaluates against rubric                        │
│                    ↓                                         │
│   Output: Score + Reasoning                                  │
└─────────────────────────────────────────────────────────────┘
```

> "LLM-as-a-judge agrees with human grading on over 80% of judgments."
> — [Databricks](https://www.databricks.com/blog/LLM-auto-eval-best-practices-RAG)

**Best practices:**
- Use low-precision scales (0-3 or binary) for clearer rubrics
- Calibrate against human-labeled examples
- Consider specialized judge models (Lynx, Glider) for hallucination detection

---

### 6. Golden Datasets

Evaluation requires stable, representative test data:

> "Golden datasets remain the foundation. These should cover the full scope of the system, balance easy and hard queries, and include governance rules for updating without breaking comparability."
> — [Label Your Data](https://labelyourdata.com/articles/llm-fine-tuning/rag-evaluation)

**Golden dataset characteristics:**
- Representative of real user queries
- Includes diverse difficulty levels
- Contains expected outputs (for reference-based evaluation)
- Versioned and frozen during experiments
- Updated periodically through governance process

**Sources for building datasets:**
- Real user queries from production logs
- Synthetic generation (Session 9)
- Manual curation by domain experts
- Adversarial examples for edge cases

---

## Recommended Reading

### Required
1. [LangSmith RAG Evaluation Tutorial](https://docs.langchain.com/langsmith/evaluate-rag-tutorial) - End-to-end evaluation workflow
2. [Trajectory Evaluations](https://docs.langchain.com/langsmith/trajectory-evals) - Agent evaluation with AgentEvals
3. [RAG Evaluation Guide](https://www.evidentlyai.com/llm-guide/rag-evaluation) - Evidently AI comprehensive guide

### Recommended
4. [Application-specific Evaluation Approaches](https://docs.langchain.com/langsmith/evaluation-approaches) - Agents, RAG, chatbots
5. [LLM Auto-Eval Best Practices](https://www.databricks.com/blog/LLM-auto-eval-best-practices-RAG) - Databricks
6. [Evaluating LLM Agents in Multi-Step Workflows](https://www.codeant.ai/blogs/evaluate-llm-agentic-workflows) - CodeAnt 2026 Guide
7. [RAGAS Documentation](https://docs.ragas.io/) - Metrics and testset generation

### Reference
8. [RAGAS Paper](https://arxiv.org/abs/2309.15217) - Original metrics research (Sep 2023)

---

## Assignment

### Core Requirements

1. **Set up evaluation infrastructure**
   - Create a golden dataset with 10-15 diverse test cases
   - Include queries that require retrieval and queries that don't
   - Upload to LangSmith for versioned tracking

2. **Run component-level evaluation**
   - Evaluate retrieval quality (context precision, context recall)
   - Evaluate generation quality (faithfulness, answer relevancy)
   - Document baseline scores for each metric

3. **Implement trajectory evaluation** for your agentic RAG
   - Choose trajectory match or LLM judge approach
   - Evaluate at least 5 agentic interactions
   - Identify any tool selection or argument errors

4. **Analysis and recommendations**
   - Which metric is your weakest? What does this indicate?
   - Propose one specific improvement based on metrics-driven development
   - What would you add to your golden dataset based on findings?

---

## Advanced Build

**Build a custom LLM-as-judge evaluator** tailored to your domain.

Design an evaluator that:
- Defines a rubric specific to your application's quality requirements
- Uses structured output (JSON) for consistent scoring
- Includes reasoning alongside scores
- Handles edge cases gracefully

**Reflection questions:**
- How did you calibrate your rubric against human judgment?
- What makes a good evaluation prompt for your domain?
- How would you detect if your judge has blind spots?

---

## Session Connections

| Previous Sessions | This Session | Next Sessions |
|-------------------|--------------|---------------|
| Session 1: Vibe Check baseline | Systematic RAG evaluation | Session 11: Advanced Retrievers |
| Session 4: Agentic RAG systems | Trajectory evaluation | Certification: Full evaluation pipeline |
| Session 9: Synthetic testsets | Golden dataset design | |

---

*Session 10 | AIE9 Cohort | January 2026*
