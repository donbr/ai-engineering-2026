# Session 11: Advanced Retrievers

## Goal

Understand and implement advanced retrieval strategies—hybrid search, reranking, and query transformation—to significantly improve RAG system accuracy beyond basic dense vector retrieval.

## Learning Outcomes

By the end of this session, you will be able to:

1. **Compare** sparse (BM25) and dense (embedding) retrieval and explain when each excels
2. **Implement** hybrid search using EnsembleRetriever with Reciprocal Rank Fusion
3. **Build** two-stage retrieval pipelines with cross-encoder reranking
4. **Apply** query transformation techniques (multi-query, HyDE) for complex questions
5. **Design** parent-child document strategies for better context retrieval
6. **Evaluate** retriever performance using NDCG, MRR, and Recall@K metrics
7. **Architect** production-ready retrieval systems with caching and routing

## Prerequisites

- **Session 2**: Dense Vector Retrieval (embedding fundamentals, cosine similarity)
- **Session 4**: Agentic RAG (basic retriever usage with Qdrant)
- **Session 10**: Agentic RAG Evaluation (RAGAS metrics for context quality)

## Tools Introduced

| Tool | Purpose | Package |
|------|---------|---------|
| `BM25Retriever` | Sparse keyword-based retrieval | `langchain-community` |
| `EnsembleRetriever` | Combine multiple retrieval strategies | `langchain-classic` |
| `ContextualCompressionRetriever` | Two-stage retrieval with reranking | `langchain-classic` |
| `CohereRerank` | Cross-encoder reranking model | `langchain-cohere` |
| `MultiQueryRetriever` | Generate query variations | `langchain-classic` |

## Key Concepts

### 1. The Retriever Abstraction

A **retriever** transforms a string query into a list of relevant documents. All retrievers implement the same interface:

```
Query (str) → Retriever → List[Document]
```

What questions should you ask when selecting a retriever?
- Does your corpus have domain-specific terminology?
- Are exact keyword matches important?
- How much latency can your application tolerate?

### 2. Sparse vs Dense Retrieval

| Aspect | BM25 (Sparse) | Embeddings (Dense) |
|--------|---------------|-------------------|
| **Matching** | Exact keywords | Semantic meaning |
| **Strength** | Acronyms, proper nouns, technical terms | Paraphrases, conceptual similarity |
| **Weakness** | Misses synonyms | May miss exact terminology |
| **Speed** | Very fast | Requires embedding computation |

*Think about it*: When searching for "GDELT API rate limits", which retriever type would find documents mentioning "GDELT throttling policies"?

### 3. Hybrid Search with Reciprocal Rank Fusion

Hybrid search combines the strengths of both approaches:

```
Query → [BM25 Retriever] → Results A ─┐
                                      ├→ RRF Fusion → Final Results
Query → [Vector Retriever] → Results B─┘
```

**Reciprocal Rank Fusion** merges ranked lists by computing:
```
RRF_score(d) = Σ 1/(k + rank(d))
```

Where `k` is typically 60 and the sum is over all retrievers.

### 4. Two-Stage Retrieval Architecture

```
Stage 1 (Recall)         Stage 2 (Precision)
────────────────         ──────────────────
Fast bi-encoder     →    Slow cross-encoder
Retrieve 50-100 docs     Rerank to top 5-10
Optimize for coverage    Optimize for relevance
```

*Why two stages?* Cross-encoders are too slow to run against the entire corpus, but they're far more accurate than bi-encoders for fine-grained relevance scoring.

### 5. Cross-Encoder Reranking

> "Rerankers are much more accurate than embedding models. The intuition behind a bi-encoder's inferior accuracy is that bi-encoders must compress all of the possible meanings of a document into a single vector—meaning we lose information." — Pinecone

The `ContextualCompressionRetriever` wraps this pattern:
1. Base retriever fetches broad set (e.g., 20 documents)
2. Reranker scores each document against the query
3. Return only top-n highest-scoring documents

### 6. Query Transformation

For complex questions, transform the query before retrieval:

| Technique | Description | When to Use |
|-----------|-------------|-------------|
| **Multi-Query** | Generate multiple query variations | Ambiguous questions |
| **HyDE** | Generate hypothetical answer, embed that | Abstract questions |
| **Decomposition** | Break into sub-questions | Multi-hop reasoning |

### 7. Parent Document Retriever

> "A more narrow piece of text will yield a more meaningful vector representation since there is less noise from multiple topics." — Towards Data Science

**Strategy**: Store small chunks for precise retrieval, but return larger parent documents for generation context.

```
Index: [Chunk A₁] [Chunk A₂] [Chunk A₃]  ← Small, focused
        └───────────┬───────────┘
Return:      [Parent Document A]          ← Full context
```

### 8. Retriever Evaluation Metrics

| Metric | Formula Intuition | Best For |
|--------|------------------|----------|
| **Recall@K** | % of relevant docs in top K | "Don't miss important info" |
| **MRR** | Average 1/rank of first relevant | "I'm feeling lucky" scenarios |
| **NDCG@K** | Weighted relevance by position | Ranked result quality |

> "NDCG is the default metric used in the MTEB Leaderboard for the Retrieval category." — Evidently AI

### 9. Production Patterns

> "Retrieval, not generation, is the core constraint. Chunking, metadata, and versioning matter as much as embeddings and prompts." — Towards Data Science

**Factory Pattern**: Create retrievers lazily to avoid expensive initialization.

**Query Routing**: Classify queries and route to appropriate retriever:
- Simple factual → Fast dense retrieval
- Keyword-heavy → BM25 or hybrid
- Complex reasoning → Multi-query + reranking

## Reference Implementation

The [GDELT Knowledge Base](https://github.com/donbr/gdelt-knowledge-base) demonstrates these concepts:

| Retriever | RAGAS Average | Implementation |
|-----------|---------------|----------------|
| Naive (Dense) | 93.9% | `vector_store.as_retriever()` |
| BM25 | 93.4% | `BM25Retriever.from_documents()` |
| Ensemble | 93.6% | `EnsembleRetriever(weights=[0.5, 0.5])` |
| **Cohere Rerank** | **95.1%** | `ContextualCompressionRetriever` |

Key insight: Reranking achieved the highest Context Precision (93.1%), confirming that two-stage retrieval improves precision.

## Recommended Reading

### Foundations
- [Rerankers and Two-Stage Retrieval](https://www.pinecone.io/learn/series/rag/rerankers/) - Pinecone
- [Hybrid Search Explained](https://www.elastic.co/what-is/hybrid-search) - Elastic
- [Retrieval Evaluation Metrics](https://weaviate.io/blog/retrieval-evaluation-metrics) - Weaviate

### LangChain Documentation
- [Retrievers Index](https://docs.langchain.com/oss/python/integrations/retrievers/index)
- [Cohere Reranker](https://docs.langchain.com/oss/python/integrations/retrievers/cohere-reranker)
- [Elasticsearch Hybrid](https://docs.langchain.com/oss/python/integrations/retrievers/elasticsearch_retriever)

### Advanced Techniques
- [RAPTOR: Recursive Abstractive Processing](https://arxiv.org/abs/2401.18059) - Stanford
- [ColBERT: Late Interaction Models](https://weaviate.io/blog/late-interaction-overview) - Weaviate
- [Self-RAG: Learning to Retrieve](https://arxiv.org/abs/2310.11511)

### Production Patterns
- [Six Lessons Building RAG in Production](https://towardsdatascience.com/six-lessons-learned-building-rag-systems-in-production/)
- [RAG Best Practices from 100+ Teams](https://www.kapa.ai/blog/rag-best-practices) - Kapa.ai

## Assignment

### Part 1: Multi-Strategy Retriever Comparison

Build a retriever comparison pipeline similar to the GDELT reference:

1. Load your document corpus into a vector store
2. Implement four retriever strategies:
   - Dense (baseline)
   - BM25 (sparse)
   - Ensemble (hybrid with RRF)
   - Reranking (two-stage with Cohere or FlashRank)
3. Create a test set of 10 questions spanning different query types

### Part 2: Evaluation

For each retriever, measure:
- Context Precision (using RAGAS)
- Context Recall (using RAGAS)
- Latency (wall-clock time per query)

### Part 3: Analysis

Answer these questions in your submission:
1. Which retriever performed best on Context Precision? Why?
2. Which retriever had the best latency vs accuracy trade-off?
3. For what types of queries did hybrid search outperform dense-only?

## Advanced Build (Optional)

Implement **Adaptive RAG**:
1. Train a query classifier (or use an LLM) to predict query complexity
2. Route simple queries to fast dense retrieval
3. Route complex queries to multi-query + reranking pipeline
4. Measure the cost and latency savings vs accuracy trade-off

## Connection to Course Arc

```
Session 2:  Dense Vector Retrieval  ← Foundation
    ↓
Session 4:  Basic Retriever in RAG  ← Application
    ↓
Session 10: Retrieval Evaluation    ← Measurement
    ↓
Session 11: Advanced Retrievers     ← YOU ARE HERE (Optimization)
```

This session teaches you how to use the evaluation metrics from Session 10 to select and tune retriever strategies that improve your RAG system's accuracy.
