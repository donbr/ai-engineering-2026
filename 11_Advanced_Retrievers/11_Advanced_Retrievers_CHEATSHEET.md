# Session 11: Advanced Retrievers - Cheatsheet

## 1. Quick Reference

```
┌─────────────────────────────────────────────────────────────────┐
│                    RETRIEVER DECISION TREE                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Does your corpus have domain-specific terminology?            │
│       ├─ YES → Consider BM25 or Hybrid Search                  │
│       └─ NO  → Dense retrieval may suffice                     │
│                                                                 │
│   Is precision critical (legal, medical)?                       │
│       ├─ YES → Add reranking (two-stage retrieval)             │
│       └─ NO  → Single-stage may be acceptable                  │
│                                                                 │
│   Are queries complex or multi-hop?                             │
│       ├─ YES → Consider query transformation                   │
│       └─ NO  → Direct retrieval is fine                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Key Packages**:
```bash
pip install langchain-classic langchain-cohere langchain-community rank-bm25
```

---

## 2. Concept Overview

### What is a Retriever?

A **retriever** is an abstraction that takes a string query and returns relevant documents:

```
Query (str) ──→ [Retriever] ──→ List[Document]
```

All retrievers implement `.invoke(query)` or the async `.ainvoke(query)`.

### Retriever Taxonomy

```
┌─────────────────────────────────────────────────────────────────┐
│                      RETRIEVER TYPES                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐       │
│  │   SPARSE    │     │    DENSE    │     │   HYBRID    │       │
│  │   (BM25)    │     │  (Vector)   │     │ (Ensemble)  │       │
│  └──────┬──────┘     └──────┬──────┘     └──────┬──────┘       │
│         │                   │                   │               │
│   Keyword match       Semantic match      Both combined        │
│   Fast, exact         Conceptual          Best of both         │
│   No ML required      Requires embeddings Requires both        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. Setup Requirements

### Environment Variables
```bash
# Required for embedding models
OPENAI_API_KEY=sk-...

# Required for Cohere Rerank
COHERE_API_KEY=...

# Optional: for Qdrant cloud
QDRANT_URL=...
QDRANT_API_KEY=...
```

### Package Installation
```bash
# Core retriever packages
pip install langchain-classic           # EnsembleRetriever, MultiQueryRetriever
pip install langchain-community         # BM25Retriever
pip install langchain-cohere            # CohereRerank
pip install rank-bm25                   # BM25 algorithm

# Vector stores (pick one)
pip install langchain-qdrant            # Qdrant
pip install langchain-chroma            # Chroma
pip install langchain-pinecone          # Pinecone
```

---

## 4. Core Concepts

### Concept 1: Sparse vs Dense Retrieval

**Sparse (BM25)**:
- Matches documents by term frequency
- Excellent for exact keywords, acronyms, proper nouns
- No embedding model required

**Dense (Vector)**:
- Matches documents by semantic similarity
- Excellent for paraphrases, conceptual queries
- Requires embedding model

```
┌──────────────────────────────────────────────────────────────┐
│              SPARSE vs DENSE COMPARISON                      │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Query: "GDELT API rate limits"                              │
│                                                              │
│  BM25 finds:                    Dense finds:                 │
│  ├─ "GDELT API rate limits"    ├─ "GDELT throttling"        │
│  ├─ "rate limit documentation" ├─ "API usage policies"      │
│  └─ "GDELT limits reference"   └─ "request quotas"          │
│                                                              │
│  Best for: Exact terms          Best for: Semantic match    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Concept 2: Hybrid Search with RRF

**Reciprocal Rank Fusion** combines ranked results:

```
RRF_score(doc) = Σ 1/(k + rank_i(doc))
```

Where `k` is typically 60, summed across all retrievers.

```
┌──────────────────────────────────────────────────────────────┐
│                    HYBRID SEARCH FLOW                        │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│              ┌──────────────┐                                │
│   Query ────→│    BM25      │────→ [D3, D1, D5]             │
│         │    └──────────────┘           │                    │
│         │                               │                    │
│         │    ┌──────────────┐           ▼                    │
│         └───→│   Vector     │────→ [D1, D2, D3]             │
│              └──────────────┘           │                    │
│                                         ▼                    │
│                              ┌──────────────────┐            │
│                              │   RRF Fusion     │            │
│                              └────────┬─────────┘            │
│                                       ▼                      │
│                              [D1, D3, D2, D5] (merged)       │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Concept 3: Two-Stage Retrieval

```
┌──────────────────────────────────────────────────────────────┐
│                TWO-STAGE RETRIEVAL PIPELINE                  │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  STAGE 1: RECALL                 STAGE 2: PRECISION          │
│  ─────────────────               ──────────────────          │
│                                                              │
│  ┌──────────────┐                ┌──────────────┐            │
│  │  Bi-Encoder  │ ───50 docs───→ │Cross-Encoder │───5 docs──→│
│  │   (fast)     │                │   (slow)     │            │
│  └──────────────┘                └──────────────┘            │
│                                                              │
│  Characteristics:                Characteristics:            │
│  • Embeds Q and D separately     • Processes (Q,D) together │
│  • ~1ms per doc                  • ~100ms per doc           │
│  • Lower accuracy                • Higher accuracy          │
│  • Scalable to millions          • Only feasible for <100   │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Concept 4: Reranking Improves Precision

> "Rerankers are much more accurate than embedding models. The intuition is that bi-encoders must compress all possible meanings into a single vector—meaning we lose information." — Pinecone

**Performance Impact** (from GDELT reference):
| Retriever | Context Precision |
|-----------|------------------|
| Dense only | 93.9% |
| + Reranking | **95.1%** |

---

## 5. Common Patterns

### Pattern 1: Basic Dense Retriever
```python
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)
```

### Pattern 2: BM25 Retriever
```python
from langchain_community.retrievers import BM25Retriever

bm25 = BM25Retriever.from_documents(documents, k=5)
```

### Pattern 3: Ensemble (Hybrid) Retriever
```python
from langchain_classic.retrievers import EnsembleRetriever

ensemble = EnsembleRetriever(
    retrievers=[bm25_retriever, vector_retriever],
    weights=[0.5, 0.5]  # Equal weighting
)
```

### Pattern 4: Reranking with Cohere
```python
from langchain_cohere import CohereRerank
from langchain_classic.retrievers.contextual_compression import (
    ContextualCompressionRetriever
)

compressor = CohereRerank(model="rerank-v3.5", top_n=5)
reranking_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=vector_store.as_retriever(search_kwargs={"k": 20})
)
```

### Pattern 5: Factory Pattern for Multiple Retrievers
```python
def create_retrievers(documents, vector_store, k=5):
    """Factory function to create all retriever strategies."""
    return {
        "naive": vector_store.as_retriever(search_kwargs={"k": k}),
        "bm25": BM25Retriever.from_documents(documents, k=k),
        "ensemble": EnsembleRetriever(
            retrievers=[bm25, vector_retriever],
            weights=[0.5, 0.5]
        ),
        "rerank": ContextualCompressionRetriever(
            base_compressor=CohereRerank(top_n=k),
            base_retriever=vector_store.as_retriever(
                search_kwargs={"k": max(20, k)}
            )
        )
    }
```

### Pattern 6: Multi-Query Retriever
```python
from langchain_classic.retrievers import MultiQueryRetriever

multi_query = MultiQueryRetriever.from_llm(
    retriever=base_retriever,
    llm=llm
)
```

### Pattern 7: Parent Document Retriever
```python
from langchain_classic.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore

parent_retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=InMemoryStore(),
    child_splitter=child_splitter,  # Small chunks
    parent_splitter=parent_splitter  # Large chunks
)
```

---

## 6. Diagrams

### Retriever Selection Matrix

```
┌─────────────────────────────────────────────────────────────────┐
│                  RETRIEVER SELECTION MATRIX                     │
├──────────────┬──────────┬──────────┬───────────┬───────────────┤
│ Requirement  │  Dense   │  BM25    │  Hybrid   │  + Reranking  │
├──────────────┼──────────┼──────────┼───────────┼───────────────┤
│ Semantic     │    ★★★   │    ★     │   ★★★    │     ★★★       │
│ Exact match  │    ★     │   ★★★    │   ★★★    │     ★★★       │
│ Speed        │   ★★★    │   ★★★    │    ★★    │      ★        │
│ Accuracy     │    ★★    │   ★★     │   ★★★    │     ★★★       │
│ Simplicity   │   ★★★    │   ★★★    │    ★★    │      ★        │
└──────────────┴──────────┴──────────┴───────────┴───────────────┘
```

### Query Transformation Patterns

```
┌─────────────────────────────────────────────────────────────────┐
│                 QUERY TRANSFORMATION PATTERNS                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  MULTI-QUERY:                                                   │
│  ┌────────────────────┐                                        │
│  │ "How does X work?" │                                        │
│  └─────────┬──────────┘                                        │
│            │ LLM generates variations                          │
│            ▼                                                    │
│  ├─ "Explain the mechanism of X"                               │
│  ├─ "What is the process behind X?"                            │
│  └─ "X functionality description"                              │
│            │                                                    │
│            ▼ Retrieve for each, merge results                  │
│                                                                 │
│  HyDE (Hypothetical Document Embeddings):                       │
│  ┌────────────────────┐                                        │
│  │ "What causes Y?"   │                                        │
│  └─────────┬──────────┘                                        │
│            │ LLM generates hypothetical answer                 │
│            ▼                                                    │
│  "Y is caused by factors A, B, C which..."                     │
│            │                                                    │
│            ▼ Embed hypothetical doc, search with that          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Parent-Child Document Strategy

```
┌─────────────────────────────────────────────────────────────────┐
│              PARENT-CHILD DOCUMENT RETRIEVER                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  INDEXING PHASE:                                                │
│  ┌──────────────────────────────────────┐                      │
│  │           Parent Document             │ ← Stored in docstore │
│  │  "The GDELT Project monitors world    │                      │
│  │   events through news media..."       │                      │
│  └──────────────────────────────────────┘                      │
│       │              │              │                           │
│       ▼              ▼              ▼                           │
│  ┌────────┐    ┌────────┐    ┌────────┐  ← Embedded in         │
│  │Child 1 │    │Child 2 │    │Child 3 │    vector store        │
│  │"GDELT  │    │"monitors│    │"through│                       │
│  │Project"│    │events"  │    │media"  │                       │
│  └────────┘    └────────┘    └────────┘                        │
│                                                                 │
│  RETRIEVAL PHASE:                                               │
│  Query ──→ Match Child 2 ──→ Return Parent Document            │
│                                                                 │
│  Why? Small chunks = precise matching                           │
│       Large parents = rich context for LLM                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Evaluation Metrics Decision Tree

```
┌─────────────────────────────────────────────────────────────────┐
│              CHOOSING EVALUATION METRICS                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  What matters most for your use case?                           │
│                                                                 │
│  "Don't miss any relevant info"                                 │
│      └─→ Use Recall@K                                          │
│          (% of relevant docs found in top K)                   │
│                                                                 │
│  "First result should be correct"                               │
│      └─→ Use MRR (Mean Reciprocal Rank)                        │
│          (Average of 1/rank of first relevant)                 │
│                                                                 │
│  "Order of all results matters"                                 │
│      └─→ Use NDCG@K                                            │
│          (Discounted cumulative gain, normalized)              │
│                                                                 │
│  "All positions equally important"                              │
│      └─→ Use MAP@K (Mean Average Precision)                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. Best Practices

### Retrieval Pipeline Design

1. **Start simple**: Dense retrieval as baseline
2. **Add diversity**: If results are redundant, use MMR
3. **Add keywords**: If missing exact terms, add BM25 (hybrid)
4. **Add precision**: If top results aren't relevant, add reranking
5. **Measure everything**: Use RAGAS metrics to validate changes

### Production Recommendations

| Aspect | Recommendation |
|--------|---------------|
| Initial retrieval K | 50-100 candidates |
| Final result count | 5-10 documents |
| Chunk size | 100-512 tokens |
| Chunk overlap | 10-20% |
| Reranker latency budget | 200-500ms |

### Cost Optimization

```
┌──────────────────────────────────────────────────────────────┐
│                   COST-LATENCY TRADE-OFF                     │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Approach              Accuracy   Latency      Cost          │
│  ─────────────────────────────────────────────────────       │
│  Dense only            Baseline   50-100ms     Low           │
│  + Hybrid (BM25)       +10-15%    100-200ms    Low           │
│  + Reranking           +20-35%    300-700ms    Medium        │
│  + LLM Reranking       +5-8%      4-6 seconds  High          │
│                                                              │
│  Recommendation: Hybrid + Cohere Rerank for best ROI         │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 8. Common Issues

### Issue 1: Reranking doesn't improve results
**Cause**: Base retrieval K is too small
**Fix**: Retrieve at least 20 docs before reranking

### Issue 2: BM25 retriever returns poor results
**Cause**: Documents weren't preprocessed
**Fix**: Ensure documents have proper text extraction, not raw HTML/PDF

### Issue 3: Ensemble retriever is slow
**Cause**: Running retrievers sequentially
**Fix**: Use async retrieval or parallel execution

### Issue 4: Parent document retriever returns irrelevant context
**Cause**: Child chunks too large
**Fix**: Reduce child chunk size (try 100-200 tokens)

### Issue 5: Multi-query retriever generates bad queries
**Cause**: LLM not understanding domain
**Fix**: Add few-shot examples in the prompt

---

## 9. Debugging Tips

### Check Retrieval Quality
```python
# Inspect what the retriever actually returns
docs = retriever.invoke("your test query")
for i, doc in enumerate(docs):
    print(f"[{i}] {doc.page_content[:200]}...")
    print(f"    Metadata: {doc.metadata}")
```

### Compare Retrievers Side-by-Side
```python
def compare_retrievers(query, retrievers):
    for name, retriever in retrievers.items():
        docs = retriever.invoke(query)
        print(f"\n=== {name} ===")
        for doc in docs[:3]:
            print(f"  - {doc.page_content[:100]}...")
```

### Measure Latency
```python
import time

def timed_retrieve(retriever, query):
    start = time.time()
    docs = retriever.invoke(query)
    elapsed = time.time() - start
    return docs, elapsed
```

### Validate Reranking Impact
```python
# Compare scores before and after reranking
base_docs = base_retriever.invoke(query)
reranked_docs = reranking_retriever.invoke(query)

# Check if order changed
base_ids = [d.metadata.get("id") for d in base_docs]
reranked_ids = [d.metadata.get("id") for d in reranked_docs]
print(f"Order changed: {base_ids != reranked_ids}")
```

---

## 10. Interview Questions

### Conceptual

1. **Q**: What's the difference between a bi-encoder and a cross-encoder?
   **A**: Bi-encoders embed query and document separately (fast, scalable). Cross-encoders process the (query, document) pair together (slow, more accurate).

2. **Q**: When would you use BM25 over dense retrieval?
   **A**: When exact keyword matching is important (technical terms, acronyms, proper nouns) or when you don't have embeddings infrastructure.

3. **Q**: Explain Reciprocal Rank Fusion.
   **A**: RRF combines ranked lists by summing 1/(k + rank) for each document across all retrievers. Higher-ranked documents in any list get boosted.

4. **Q**: Why does reranking improve precision?
   **A**: Cross-encoders can capture fine-grained query-document interactions that bi-encoders miss by compressing everything into a single vector.

### Practical

5. **Q**: Your RAG system misses documents with exact acronyms. What would you try?
   **A**: Add BM25 to create a hybrid retriever, or preprocess to expand acronyms.

6. **Q**: Retrieval latency is too high after adding reranking. How would you optimize?
   **A**: Reduce initial retrieval K, use a faster reranker (FlashRank), or implement caching.

7. **Q**: How would you evaluate if hybrid search is better than dense-only for your corpus?
   **A**: Create a test set with known relevant docs, measure Recall@K and NDCG@K for both approaches.

---

## 11. Resources & Links

### Documentation
- [LangChain Retrievers](https://docs.langchain.com/oss/python/integrations/retrievers/index)
- [LangChain Classic Package](https://docs.langchain.com/oss/python/releases/langchain-v1)
- [Cohere Rerank](https://docs.langchain.com/oss/python/integrations/retrievers/cohere-reranker)

### Tutorials
- [Rerankers and Two-Stage Retrieval](https://www.pinecone.io/learn/series/rag/rerankers/) - Pinecone
- [Hybrid Search Explained](https://www.elastic.co/what-is/hybrid-search) - Elastic
- [Retrieval Evaluation Metrics](https://weaviate.io/blog/retrieval-evaluation-metrics) - Weaviate

### Research
- [RAPTOR: Recursive Abstractive Processing](https://arxiv.org/abs/2401.18059)
- [ColBERT: Late Interaction](https://arxiv.org/abs/2004.12832)
- [Self-RAG](https://arxiv.org/abs/2310.11511)

### Reference Implementation
- [GDELT Knowledge Base](https://github.com/donbr/gdelt-knowledge-base) - Multi-strategy retriever comparison

### Production Guides
- [RAG Best Practices](https://www.kapa.ai/blog/rag-best-practices) - Kapa.ai
- [Six Lessons from Production RAG](https://towardsdatascience.com/six-lessons-learned-building-rag-systems-in-production/)

---

## 12. Key Takeaways

```
┌─────────────────────────────────────────────────────────────────┐
│                     KEY TAKEAWAYS                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Retrieval is the bottleneck                                 │
│     "Retrieval, not generation, is the core constraint"        │
│                                                                 │
│  2. Hybrid > Single approach                                    │
│     BM25 + Vector covers both keywords and semantics           │
│                                                                 │
│  3. Reranking is high ROI                                       │
│     20-35% accuracy improvement for 200-500ms latency          │
│                                                                 │
│  4. Two-stage = recall then precision                           │
│     Broad retrieval first, reranking second                    │
│                                                                 │
│  5. Measure before optimizing                                   │
│     Use NDCG, Recall@K, and RAGAS metrics                      │
│                                                                 │
│  6. Factory pattern for flexibility                             │
│     Create retrievers lazily, swap strategies easily           │
│                                                                 │
│  7. Match chunk size to retrieval needs                         │
│     Small chunks for precision, parent docs for context        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

*Session 11 Cheatsheet | AIE9 Bootcamp | Last Updated: January 2026*
