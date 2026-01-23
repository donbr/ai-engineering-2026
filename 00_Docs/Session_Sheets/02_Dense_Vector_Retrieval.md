# Session 2: Dense Vector Retrieval

## Goal
Build RAG from first principles by understanding how embeddings enable semantic search and how retrieval augments LLM generation.

## Learning Outcomes
By the end of this session, you will be able to:
- Explain why in-context learning is the foundation of modern LLM applications
- Convert text to embedding vectors and interpret their semantic meaning
- Implement similarity search using cosine similarity from scratch
- Build a complete RAG pipeline without frameworks
- Evaluate retrieval quality through vibe checks and systematic testing

## Tools Introduced
- **Embedding Model**: OpenAI `text-embedding-3-small` (1536 dimensions)
- **Vector Storage**: Custom Python dictionary-based vector database
- **Orchestration**: OpenAI Python SDK for both embeddings and chat
- **Data Processing**: NumPy for vector operations

---

## Key Concepts

### 1. In-Context Learning

> *"In-context learning refers to a model's ability to temporarily learn from prompts."*
> ~ GPT-3 Paper (2020)

The entire LLM application stack is built on this design pattern. When we add information to a prompt, the model uses that context to generate better responses. RAG automates this process by retrieving relevant context before generation.

**The critical insight**: We're not training the model - we're providing information at inference time that the model can reason over. This is fundamentally different from fine-tuning.

```
┌─────────────────────────────────────────────────────────┐
│                   IN-CONTEXT LEARNING                    │
├─────────────────────────────────────────────────────────┤
│                                                          │
│   Manual:  Engineer writes context into prompt           │
│            ↓                                             │
│   RAG:     System retrieves context automatically        │
│            ↓                                             │
│   Result:  LLM generates informed response               │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### 2. Embeddings: Text to Numbers

Embedding models solve a fundamental problem: **computers can't read text**. We must convert natural language into a machine-readable format - vectors of floating-point numbers.

> *"You shall know a word by the company it keeps."*
> ~ John Firth (1957)

High-quality embeddings preserve **semantic meaning**. Words with similar meanings cluster together in vector space. The classic Word2Vec demonstration: `king - man + woman ≈ queen` shows that mathematical operations on embeddings reflect conceptual relationships.

**Key properties of embeddings**:
- Fixed dimensionality (e.g., 1536 for text-embedding-3-small)
- Normalized (unit length) for efficient similarity computation
- Trained to place semantically similar text near each other

### 3. Semantic Similarity

Unlike keyword matching, semantic similarity finds documents based on **meaning**. The query "What causes rain?" should retrieve documents about precipitation, weather patterns, and the water cycle - even if they never use the word "rain."

This is the superpower of dense vector retrieval: it captures paraphrases, synonyms, and conceptual relationships that lexical search misses.

### 4. Distance Metrics

How do we measure "closeness" in high-dimensional space?

| Metric | Formula | When to Use |
|--------|---------|-------------|
| **Cosine Similarity** | dot(A,B) / (||A|| * ||B||) | Most common; direction matters, magnitude doesn't |
| **Euclidean (L2)** | sqrt(sum((A-B)^2)) | When absolute distances matter |
| **Dot Product** | sum(A * B) | When vectors are normalized (equivalent to cosine) |

For normalized embeddings (unit vectors), cosine similarity and dot product produce identical rankings. Most embedding APIs return normalized vectors.

### 5. Vector Databases

A vector database stores embeddings and enables efficient similarity search. At its simplest, it's a dictionary mapping text to vectors:

```
┌─────────────────────────────────────────────────────────┐
│                    VECTOR DATABASE                       │
├─────────────────────────────────────────────────────────┤
│                                                          │
│   "The sky is blue"     →  [0.12, -0.34, 0.56, ...]     │
│   "Water is essential"  →  [0.23, 0.45, -0.12, ...]     │
│   "Plants need sun"     →  [-0.11, 0.67, 0.23, ...]     │
│                                                          │
│   Query: "nature topics" →  [0.15, 0.42, 0.31, ...]     │
│                                                          │
│   Search: Compare query vector to all stored vectors     │
│   Return: Top-k most similar documents                   │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

Production systems use specialized databases (Pinecone, Weaviate, pgvector, Chroma) with indexing for scale, but the concept remains the same.

### 6. Chunking Strategies

Documents must be split into chunks before embedding. Why?

1. **Context window limits**: LLMs have maximum input sizes
2. **Retrieval precision**: Smaller chunks enable more targeted retrieval
3. **Embedding quality**: Models perform better on focused text segments

**Common approaches**:
- **Fixed-size**: Split every N characters with overlap
- **Sentence-based**: Split at sentence boundaries
- **Semantic**: Split at topic or section changes

The overlap between chunks prevents losing information at boundaries.

### 7. The RAG Pipeline

RAG = **Retrieval** + **Augmented** + **Generation**

```
┌─────────────────────────────────────────────────────────┐
│                    RAG PIPELINE                          │
├─────────────────────────────────────────────────────────┤
│                                                          │
│   INDEXING (Offline)                                     │
│   ┌──────────┐   ┌──────────┐   ┌──────────────────┐   │
│   │Documents │ → │ Chunker  │ → │ Embedding Model  │   │
│   └──────────┘   └──────────┘   └────────┬─────────┘   │
│                                           ↓              │
│                                  ┌────────────────┐     │
│                                  │ Vector Store   │     │
│                                  └────────────────┘     │
│                                           ↑              │
│   RETRIEVAL (Online)                      │              │
│   ┌──────────┐   ┌──────────────────┐     │              │
│   │  Query   │ → │ Embedding Model  │ ────┘              │
│   └──────────┘   └──────────────────┘                    │
│                           ↓                              │
│   GENERATION             ┌──────────────────┐            │
│   ┌──────────┐   ┌───── │  Top-k Chunks    │            │
│   │   LLM    │ ← │      └──────────────────┘            │
│   └────┬─────┘   │                                       │
│        ↓         │      ┌──────────────────┐            │
│   ┌──────────┐   └───── │  User Question   │            │
│   │ Response │          └──────────────────┘            │
│   └──────────┘                                           │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### 8. Indexing & Search Complexity

With a small corpus, brute-force search (comparing against every vector) works fine. At scale, we need approximate methods:

| Method | Complexity | Trade-off |
|--------|-----------|-----------|
| **Brute Force** | O(n) | Exact but slow |
| **HNSW** | O(log n) | Fast, slight accuracy loss |
| **IVF** | O(sqrt(n)) | Good for large datasets |

For learning, brute-force with NumPy is perfect. Production systems use indexes like HNSW (Hierarchical Navigable Small World graphs).

### 9. The LLM Application Stack

The a16z reference architecture shows how RAG fits into production systems:

```
┌─────────────────────────────────────────────────────────┐
│              LLM APPLICATION STACK                       │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌─────────────┐                    ┌─────────────┐     │
│  │   Data      │ ──────────────────→│  Embedding  │     │
│  │   Sources   │                    │   Model     │     │
│  └─────────────┘                    └──────┬──────┘     │
│                                            ↓             │
│                                    ┌─────────────┐      │
│                                    │   Vector    │      │
│                                    │   Store     │      │
│                                    └──────┬──────┘      │
│                                            ↓             │
│  ┌─────────────┐   ┌─────────────┐ ┌─────────────┐      │
│  │    User     │ → │Orchestration│ → │    LLM     │      │
│  │   Request   │   │   Layer     │   │    API     │      │
│  └─────────────┘   └─────────────┘   └─────────────┘     │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

This pattern recurs throughout the course. Tools change; the architecture persists.

### 10. Evaluating Retrieval

How do we know if retrieval is working?

**Quick checks (Vibe Checks)**:
- Do retrieved chunks seem relevant to the query?
- Does the LLM response use the retrieved context?
- Are answers factually grounded in source documents?

**Systematic evaluation**:
- Precision@k: What fraction of top-k results are relevant?
- Recall: Did we retrieve all relevant documents?
- Mean Reciprocal Rank (MRR): How high is the first relevant result?

Start with vibe checks. Graduate to metrics as you iterate.

---

## Recommended Reading

1. **[Language Models are Few-Shot Learners (2020)](https://arxiv.org/abs/2005.14165)** - The GPT-3 paper that introduced in-context learning
2. **[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (2020)](https://arxiv.org/abs/2005.11401)** - The original RAG paper
3. **[Emerging Architectures for LLM Applications (2023)](https://a16z.com/emerging-architectures-for-llm-applications/)** - The LLM application stack by a16z
4. **[12-Factor Agents](https://github.com/humanlayer/12-factor-agents)** - Context engineering principles by Dex Horthy
5. **[Illustrated Word2Vec](https://jalammar.github.io/illustrated-word2vec/)** - Visual introduction to embeddings
6. **[Sentence-BERT Paper](https://arxiv.org/abs/1908.10084)** - Foundation for modern sentence embeddings
7. **[PydanticAI RAG Example](https://ai.pydantic.dev/examples/rag/)** - Clean from-scratch RAG implementation
8. **[OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)** - Official embedding documentation
9. **[MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard)** - Embedding model benchmarks
10. **[pgvector Documentation](https://github.com/pgvector/pgvector)** - PostgreSQL vector extension

---

## Assignment

**Build Phase**: Run the Pythonic RAG notebook to build a complete RAG system from scratch using pure Python, NumPy, and the OpenAI API.

**Ship Phase**: Augment the RAG pipeline with one of these enhancements:
- Add PDF file support to `TextFileLoader`
- Implement a new distance metric (Euclidean, Manhattan)
- Add metadata support to the vector database
- Use a different embedding model
- Add YouTube transcript ingestion

**Share Phase**:
- Create a diagram of your RAG pipeline
- Record a Loom walkthrough explaining your enhancement
- Share 3 lessons learned and 3 questions that remain

---

## Advanced Build

For those seeking deeper understanding:

1. **Implement HNSW from scratch** - Build the hierarchical navigable small world algorithm to understand approximate nearest neighbor search

2. **Compare embedding models** - Benchmark `text-embedding-3-small` vs `text-embedding-3-large` vs open-source alternatives (BAAI/bge-small)

3. **Build a hybrid retriever** - Combine dense vector search with BM25 keyword search and implement score fusion

4. **Add re-ranking** - Implement a cross-encoder re-ranker to improve precision on top-k results

5. **Instrument with observability** - Add logging to track retrieval latency, embedding costs, and result quality

---

## Discussion Questions

1. Why does RAG work better than simply using a larger context window?

2. When would you choose Euclidean distance over cosine similarity?

3. How does chunk size affect retrieval precision vs. recall?

4. What happens when the retrieved context contradicts the LLM's training data?

5. How would you handle a query that requires information from multiple documents?

---

*Session prepared for AIE9 - AI Engineering Bootcamp*
