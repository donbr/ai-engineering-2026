# Session 11: Advanced Retrievers - Slides

---

## Slide 1: Title

### Advanced Retrievers
**Session 11 | AIE9 Bootcamp**

*Beyond Dense Vector Search: Hybrid, Reranking, and Production Patterns*

---

**Visual**: Mermaid diagram showing retriever ecosystem

```mermaid
graph TB
    subgraph "Retriever Landscape"
        Q[Query] --> S[Sparse<br/>BM25]
        Q --> D[Dense<br/>Vector]
        Q --> H[Hybrid<br/>Ensemble]
        S --> F[Fusion]
        D --> F
        H --> F
        F --> R[Reranking]
        R --> O[Results]
    end

    style Q fill:#e1f5fe
    style S fill:#fff3e0
    style D fill:#e8f5e9
    style H fill:#fce4ec
    style R fill:#f3e5f5
    style O fill:#e0f2f1
```

---

**Speaker Notes**:
- Welcome to Session 11 on Advanced Retrievers
- We've built RAG systems with basic dense retrieval—now we level up
- Today: hybrid search, reranking, and production patterns
- By the end, you'll know how to improve retrieval accuracy by 20-35%

---

## Slide 2: Learning Objectives

### What You'll Be Able to Do

1. **Compare** sparse (BM25) and dense (embedding) retrieval trade-offs
2. **Implement** hybrid search with Reciprocal Rank Fusion
3. **Build** two-stage retrieval with cross-encoder reranking
4. **Apply** query transformation for complex questions
5. **Evaluate** retrievers using NDCG, MRR, Recall@K

---

**Visual**: Learning path diagram

```mermaid
graph LR
    A[Session 2<br/>Dense Vectors] --> B[Session 4<br/>Basic RAG]
    B --> C[Session 10<br/>Evaluation]
    C --> D[Session 11<br/>Advanced<br/>Retrievers]

    style A fill:#e8f5e9
    style B fill:#e8f5e9
    style C fill:#e8f5e9
    style D fill:#fff3e0,stroke:#ff9800,stroke-width:3px
```

---

**Speaker Notes**:
- These 5 objectives map to real-world RAG optimization
- We build on Session 2 (embeddings), Session 4 (RAG basics), Session 10 (evaluation)
- Today we close the loop: use evaluation to select retriever strategies
- Ask: "Who has experienced poor retrieval results in their RAG systems?"

---

## Slide 3: The Retriever Abstraction

### What is a Retriever?

```
Query (string) ──→ [Retriever] ──→ List[Document]
```

All retrievers share the same interface:
- `.invoke(query)` - synchronous
- `.ainvoke(query)` - asynchronous
- `.batch([queries])` - multiple queries

---

**Visual**: Retriever interface diagram

```mermaid
graph LR
    subgraph "Retriever Interface"
        Q["Query<br/>'How does X work?'"] --> R[Retriever]
        R --> D1[Doc 1]
        R --> D2[Doc 2]
        R --> D3[Doc 3]
    end

    style Q fill:#e1f5fe
    style R fill:#fff3e0
    style D1 fill:#e8f5e9
    style D2 fill:#e8f5e9
    style D3 fill:#e8f5e9
```

---

**Speaker Notes**:
- The retriever is an abstraction—it hides HOW documents are found
- This lets us swap strategies without changing downstream code
- Vector stores become retrievers via `.as_retriever()`
- Question: "If all retrievers have the same interface, what differs between them?"

---

## Slide 4: Sparse vs Dense Retrieval

### Two Fundamental Approaches

| | **BM25 (Sparse)** | **Embeddings (Dense)** |
|---|---|---|
| **Matches** | Keywords | Meaning |
| **Strength** | Exact terms, acronyms | Synonyms, concepts |
| **Speed** | Very fast | Embedding cost |
| **Scaling** | Inverted index | Vector index |

---

**Visual**: Comparison diagram

```mermaid
graph TB
    subgraph "Query: 'GDELT API rate limits'"
        direction TB
        BM[BM25] --> B1["'GDELT API rate limits'"]
        BM --> B2["'rate limit documentation'"]

        VEC[Vector] --> V1["'GDELT throttling policies'"]
        VEC --> V2["'API usage quotas'"]
    end

    style BM fill:#fff3e0
    style VEC fill:#e8f5e9
    style B1 fill:#fff3e0
    style B2 fill:#fff3e0
    style V1 fill:#e8f5e9
    style V2 fill:#e8f5e9
```

---

**Speaker Notes**:
- BM25 uses term frequency and inverse document frequency
- Dense uses learned representations of meaning
- Neither is universally better—they excel at different things
- Question: "For a query about 'ML model performance', which would find docs about 'neural network accuracy'?"

---

## Slide 5: Hybrid Search with RRF

### Best of Both Worlds

```
Query ─┬─→ [BM25] ──→ Ranked List A ─┐
       │                              ├─→ [RRF] ──→ Merged List
       └─→ [Vector] ─→ Ranked List B ─┘
```

**Reciprocal Rank Fusion**:
```
RRF_score(doc) = Σ 1/(k + rank_i(doc))
```

---

**Visual**: RRF fusion process

```mermaid
graph LR
    subgraph "Reciprocal Rank Fusion"
        Q[Query] --> BM[BM25]
        Q --> VEC[Vector]
        BM --> |"[D3,D1,D5]"| RRF[RRF Fusion<br/>k=60]
        VEC --> |"[D1,D2,D3]"| RRF
        RRF --> |"[D1,D3,D2,D5]"| OUT[Final Results]
    end

    style Q fill:#e1f5fe
    style BM fill:#fff3e0
    style VEC fill:#e8f5e9
    style RRF fill:#f3e5f5
    style OUT fill:#e0f2f1
```

---

**Speaker Notes**:
- RRF is the standard fusion method—simple but effective
- k=60 is typical, dampens the impact of very high ranks
- D1 appears high in both lists → highest RRF score
- "Why not just concatenate the lists?" → Duplicates, no ranking

---

## Slide 6: Two-Stage Retrieval

### Recall First, Precision Second

| Stage 1: Recall | Stage 2: Precision |
|-----------------|-------------------|
| Bi-encoder | Cross-encoder |
| Fast (~1ms/doc) | Slow (~100ms/doc) |
| Retrieve 50-100 | Keep top 5-10 |
| Maximize coverage | Maximize relevance |

---

**Visual**: Two-stage pipeline

```mermaid
graph LR
    subgraph "Two-Stage Retrieval"
        Q[Query] --> S1[Stage 1<br/>Bi-encoder]
        S1 --> |"50 docs"| S2[Stage 2<br/>Cross-encoder]
        S2 --> |"5 docs"| OUT[Final]
    end

    N1[" Fast<br/>Scalable<br/>Lower accuracy"] -.-> S1
    N2[" Slow<br/>Not scalable<br/>Higher accuracy"] -.-> S2

    style Q fill:#e1f5fe
    style S1 fill:#fff3e0
    style S2 fill:#f3e5f5
    style OUT fill:#e0f2f1
```

---

**Speaker Notes**:
- Why not just use cross-encoders? Too slow for full corpus
- Bi-encoders embed Q and D separately → can pre-compute D
- Cross-encoders process (Q,D) pair → must run at query time
- Think of it as: cast a wide net, then filter carefully

---

## Slide 7: Cross-Encoder Reranking

### Why Rerankers Are More Accurate

> "Rerankers are much more accurate than embedding models. Bi-encoders must compress all possible meanings into a single vector—meaning we lose information."
> — **Pinecone**

---

**Visual**: Bi-encoder vs Cross-encoder

```mermaid
graph TB
    subgraph "Bi-encoder"
        Q1[Query] --> E1[Encoder]
        D1[Document] --> E2[Encoder]
        E1 --> V1[Vector Q]
        E2 --> V2[Vector D]
        V1 --> SIM[Similarity]
        V2 --> SIM
    end

    subgraph "Cross-encoder"
        Q2[Query] --> PAIR["[Q, D]"]
        D2[Document] --> PAIR
        PAIR --> CE[Cross-Encoder]
        CE --> SCORE[Relevance Score]
    end

    style Q1 fill:#e1f5fe
    style D1 fill:#e8f5e9
    style Q2 fill:#e1f5fe
    style D2 fill:#e8f5e9
    style SIM fill:#fff3e0
    style SCORE fill:#f3e5f5
```

---

**Speaker Notes**:
- Cross-encoders see Q and D together → richer interaction
- They can attend to specific query terms in the document
- Typical improvement: 20-35% better precision
- Trade-off: 200-500ms added latency

---

## Slide 8: Query Transformation

### Improve Retrieval Through Better Queries

| Technique | What It Does | When to Use |
|-----------|--------------|-------------|
| **Multi-Query** | Generate variations | Ambiguous queries |
| **HyDE** | Generate hypothetical answer | Abstract questions |
| **Decomposition** | Break into sub-queries | Multi-hop reasoning |

---

**Visual**: Query transformation patterns

```mermaid
graph TB
    subgraph "Multi-Query"
        Q1["How does X work?"]
        Q1 --> LLM1[LLM]
        LLM1 --> V1["Explain X mechanism"]
        LLM1 --> V2["What is X process?"]
        LLM1 --> V3["X functionality"]
    end

    subgraph "HyDE"
        Q2["What causes Y?"]
        Q2 --> LLM2[LLM]
        LLM2 --> H["Y is caused by A, B, C..."]
        H --> EMB[Embed]
        EMB --> SEARCH[Search]
    end

    style Q1 fill:#e1f5fe
    style Q2 fill:#e1f5fe
    style LLM1 fill:#fff3e0
    style LLM2 fill:#fff3e0
```

---

**Speaker Notes**:
- Multi-Query: LLM generates 3-5 query variations, retrieve for each, merge
- HyDE: "What would a good answer look like?" → embed that → search
- Decomposition: "Compare A and B" → "What is A?" + "What is B?"
- Question: "Which technique would help 'best practices for X'?"

---

## Slide 9: Parent Document Retriever

### Small Chunks to Search, Large Docs to Return

> "A more narrow piece of text will yield a more meaningful vector representation since there is less noise from multiple topics."
> — **Towards Data Science**

---

**Visual**: Parent-child relationship

```mermaid
graph TB
    subgraph "Indexing"
        P[Parent Document] --> C1[Child 1]
        P --> C2[Child 2]
        P --> C3[Child 3]
    end

    subgraph "Retrieval"
        Q[Query] --> MATCH[Match Child 2]
        MATCH --> RETURN[Return Parent]
    end

    C1 -.->|"Stored in<br/>Vector Store"| VS[(Vector Store)]
    C2 -.-> VS
    C3 -.-> VS
    P -.->|"Stored in<br/>Doc Store"| DS[(Doc Store)]

    style Q fill:#e1f5fe
    style P fill:#e8f5e9
    style C1 fill:#fff3e0
    style C2 fill:#fff3e0
    style C3 fill:#fff3e0
```

---

**Speaker Notes**:
- Problem: Large chunks = noisy embeddings. Small chunks = missing context.
- Solution: Index small, return large
- Child chunks (100-200 tokens) for precise matching
- Parent docs (1000+ tokens) for full context to LLM
- Question: "What happens if you set child chunk size too large?"

---

## Slide 10: Retriever Evaluation Metrics

### Measuring What Matters

| Metric | Best For | Intuition |
|--------|----------|-----------|
| **Recall@K** | "Don't miss anything" | % relevant in top K |
| **MRR** | "First result counts" | 1/rank of first relevant |
| **NDCG@K** | "Order matters" | Weighted by position |

---

**Visual**: Metric decision tree

```mermaid
graph TB
    START[What matters most?] --> A["Must find all<br/>relevant docs?"]
    A -->|Yes| RECALL[Use Recall@K]
    A -->|No| B["First result<br/>is critical?"]
    B -->|Yes| MRR[Use MRR]
    B -->|No| C["Order of all<br/>results matters?"]
    C -->|Yes| NDCG[Use NDCG@K]
    C -->|No| MAP[Use MAP@K]

    style RECALL fill:#e8f5e9
    style MRR fill:#fff3e0
    style NDCG fill:#f3e5f5
    style MAP fill:#e1f5fe
```

---

**Speaker Notes**:
- NDCG is industry standard (MTEB leaderboard uses it)
- MRR is great for "I'm feeling lucky" scenarios
- Recall@K when missing info is costly (medical, legal)
- Use RAGAS metrics (Context Precision, Recall) for RAG-specific evaluation

---

## Slide 11: Production Patterns

### From Prototype to Production

> "Retrieval, not generation, is the core constraint. Chunking, metadata, and versioning matter as much as embeddings and prompts."
> — **Towards Data Science**

---

**Visual**: Production architecture

```mermaid
graph TB
    subgraph "Query Routing"
        Q[Query] --> CLS[Query Classifier]
        CLS -->|Simple| FAST[Fast Dense]
        CLS -->|Complex| FULL[Hybrid + Rerank]
        CLS -->|Keyword| BM[BM25 Priority]
    end

    subgraph "Caching"
        FAST --> CACHE[(Cache)]
        FULL --> CACHE
        BM --> CACHE
        CACHE --> OUT[Results]
    end

    style Q fill:#e1f5fe
    style CLS fill:#fff3e0
    style CACHE fill:#f3e5f5
    style OUT fill:#e0f2f1
```

---

**Speaker Notes**:
- Factory pattern: create retrievers lazily, avoid expensive init
- Query routing: classify queries, route to appropriate strategy
- Caching: embed common queries, cache retrieval results
- Cost optimization: simple queries don't need full pipeline

---

## Slide 12: GDELT Reference Implementation

### Real-World Comparison (4 Strategies)

| Retriever | RAGAS Avg | Context Precision |
|-----------|-----------|-------------------|
| Naive (Dense) | 93.9% | 91.4% |
| BM25 | 93.4% | 90.2% |
| Ensemble | 93.6% | 91.0% |
| **Cohere Rerank** | **95.1%** | **93.1%** |

[github.com/donbr/gdelt-knowledge-base](https://github.com/donbr/gdelt-knowledge-base)

---

**Visual**: Performance comparison

```mermaid
xychart-beta
    title "RAGAS Scores by Retriever Strategy"
    x-axis ["Naive", "BM25", "Ensemble", "Rerank"]
    y-axis "Score (%)" 90 --> 96
    bar [93.9, 93.4, 93.6, 95.1]
```

---

**Speaker Notes**:
- Real implementation with 38 GDELT docs, 12 test questions
- Cohere Rerank wins on precision (93.1%)
- Ensemble provides coverage but not huge gains here
- Key insight: reranking is high ROI for precision-critical apps
- The repo shows factory pattern, evaluation pipeline, reproducibility

---

## Slide 13: Implementation Patterns

### Key Code Patterns

**Ensemble Retriever**:
```python
EnsembleRetriever(
    retrievers=[bm25, vector],
    weights=[0.5, 0.5]
)
```

**Reranking Retriever**:
```python
ContextualCompressionRetriever(
    base_compressor=CohereRerank(top_n=5),
    base_retriever=vector.as_retriever(k=20)
)
```

---

**Visual**: Pattern composition

```mermaid
graph LR
    subgraph "Composable Patterns"
        BASE[Base Retriever] --> ENS[+ Ensemble]
        ENS --> COMP[+ Compression]
        COMP --> MQ[+ Multi-Query]
    end

    style BASE fill:#e8f5e9
    style ENS fill:#fff3e0
    style COMP fill:#f3e5f5
    style MQ fill:#e1f5fe
```

---

**Speaker Notes**:
- Patterns are composable: start simple, add layers
- Factory pattern creates all strategies from same docs/vector store
- ContextualCompression wraps any base retriever
- Always retrieve MORE than you need, then filter down

---

## Slide 14: Summary

### Key Takeaways

1. **Retrieval is the bottleneck** — optimize here first
2. **Hybrid > Single** — combine BM25 + Vector
3. **Reranking is high ROI** — 20-35% improvement
4. **Two-stage = recall then precision**
5. **Measure with proper metrics** — NDCG, Recall@K, RAGAS

---

**Visual**: Summary diagram

```mermaid
graph TB
    subgraph "Advanced Retriever Stack"
        Q[Query] --> HYB[Hybrid Search<br/>BM25 + Vector]
        HYB --> |"50 docs"| RERANK[Reranking<br/>Cross-encoder]
        RERANK --> |"5 docs"| EVAL[Evaluate<br/>NDCG, Recall@K]
        EVAL --> |"Iterate"| HYB
    end

    style Q fill:#e1f5fe
    style HYB fill:#fff3e0
    style RERANK fill:#f3e5f5
    style EVAL fill:#e8f5e9
```

---

**Speaker Notes**:
- Start with dense, add hybrid, then reranking
- Measure impact at each step with proper metrics
- The GDELT reference shows this works: 95.1% with reranking
- Next session applies these techniques to your own projects

---

## Slide 15: Assignment

### Build Your Own Retriever Comparison

**Part 1**: Implement 4 retriever strategies
- Dense (baseline)
- BM25 (sparse)
- Ensemble (hybrid)
- Reranking (two-stage)

**Part 2**: Evaluate with RAGAS
- Context Precision
- Context Recall
- Latency per query

**Part 3**: Analyze results
- Which strategy won? Why?
- What's the latency vs accuracy trade-off?

---

**Visual**: Assignment workflow

```mermaid
graph LR
    DOCS[Your Docs] --> IMPL[Implement<br/>4 Retrievers]
    IMPL --> TEST[Test Set<br/>10 Questions]
    TEST --> EVAL[RAGAS<br/>Evaluation]
    EVAL --> REPORT[Analysis<br/>Report]

    style DOCS fill:#e1f5fe
    style IMPL fill:#fff3e0
    style TEST fill:#e8f5e9
    style EVAL fill:#f3e5f5
    style REPORT fill:#e0f2f1
```

---

**Speaker Notes**:
- Use your own domain corpus or GDELT docs
- Create 10 diverse questions (factual, conceptual, keyword-heavy)
- Measure all 4 strategies on same test set
- Submit analysis: which worked best and why?

---

## Slide 16: Resources & Q&A

### Documentation
- [LangChain Retrievers](https://docs.langchain.com/oss/python/integrations/retrievers/)
- [Cohere Reranker](https://docs.langchain.com/oss/python/integrations/retrievers/cohere-reranker)

### Tutorials
- [Rerankers (Pinecone)](https://www.pinecone.io/learn/series/rag/rerankers/)
- [Evaluation Metrics (Weaviate)](https://weaviate.io/blog/retrieval-evaluation-metrics)

### Reference
- [GDELT Knowledge Base](https://github.com/donbr/gdelt-knowledge-base)

---

**Visual**: Q&A prompt

```mermaid
graph TB
    QA["Questions?"]

    style QA fill:#e1f5fe,stroke:#0288d1,stroke-width:3px
```

---

**Speaker Notes**:
- Questions on any of the 9 concepts?
- Common questions: "When should I NOT use reranking?" (latency-critical apps)
- "How do I choose ensemble weights?" (start 50/50, tune with metrics)
- Remind students: cheatsheet has all code patterns and debugging tips

---

## Appendix: Mermaid Diagram Reference

### Color Palette
- Input nodes: `#e1f5fe` (light blue)
- Model/Process nodes: `#fff3e0` (light orange)
- Tool nodes: `#e8f5e9` (light green)
- Reranking nodes: `#f3e5f5` (light purple)
- Output nodes: `#e0f2f1` (light teal)
- Highlight: `#fce4ec` (light pink)

### Diagram Types Used
1. `graph TB/LR` - Flow diagrams
2. `xychart-beta` - Bar charts
3. `subgraph` - Grouped components

---

*Session 11 Slides | AIE9 Bootcamp | January 2026*
