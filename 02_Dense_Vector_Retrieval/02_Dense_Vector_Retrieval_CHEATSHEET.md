# Dense Vector Retrieval Cheatsheet

## 1. Quick Reference

| Component | Purpose | Key File |
|-----------|---------|----------|
| **TextFileLoader** | Load .txt documents | `aimakerspace/text_utils.py` |
| **CharacterTextSplitter** | Chunk documents | `aimakerspace/text_utils.py` |
| **EmbeddingModel** | Convert text to vectors | `aimakerspace/openai_utils/embedding.py` |
| **VectorDatabase** | Store and search vectors | `aimakerspace/vectordatabase.py` |
| **ChatOpenAI** | Generate responses | `aimakerspace/openai_utils/chatmodel.py` |

**Core Equation**: `RAG = Dense Vector Retrieval + In-Context Learning`

---

## 2. Concept Overview

### What is Dense Vector Retrieval?

Dense vector retrieval finds documents based on **semantic meaning** rather than keyword matching. It works by:

1. Converting text to high-dimensional vectors (embeddings)
2. Measuring similarity between query and document vectors
3. Returning the most similar documents

### Why "Dense"?

- **Dense vectors**: Most elements are non-zero (embeddings from neural networks)
- **Sparse vectors**: Most elements are zero (traditional TF-IDF, BM25)

Dense retrieval captures meaning; sparse retrieval matches keywords. Production systems often combine both.

### The RAG Pattern

```
Query → Embed → Search Vector DB → Retrieve Top-k → Augment Prompt → Generate
```

This pattern appears everywhere in modern AI applications. Master it once, apply it repeatedly.

---

## 3. Setup Requirements

### Environment
```bash
# Install dependencies
uv sync

# Activate environment
source .venv/bin/activate

# Set API key
export OPENAI_API_KEY="sk-..."
```

### Required Imports
```python
import numpy as np
from aimakerspace.text_utils import TextFileLoader, CharacterTextSplitter
from aimakerspace.vectordatabase import VectorDatabase
from aimakerspace.openai_utils.embedding import EmbeddingModel
from aimakerspace.openai_utils.chatmodel import ChatOpenAI
```

### Verify Setup
```python
# Test embedding model
model = EmbeddingModel()
vec = model.get_embedding("test")
print(f"Embedding dimensions: {len(vec)}")  # Should be 1536
```

---

## 4. Core Concepts

### Embeddings

> *"You shall know a word by the company it keeps."* ~ John Firth

**What they are**: Fixed-length vectors of floating-point numbers representing text meaning.

**Key properties**:
- **Dimensionality**: text-embedding-3-small produces 1536 dimensions
- **Normalized**: Unit length vectors enable efficient similarity computation
- **Semantic**: Similar meanings cluster together in vector space

**Mental model**: Embeddings are coordinates in a high-dimensional "meaning space."

### Distance Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| Cosine Similarity | `dot(A,B) / (||A|| × ||B||)` | 1 = identical, 0 = orthogonal, -1 = opposite |
| Euclidean Distance | `sqrt(sum((A-B)^2))` | 0 = identical, larger = more different |
| Dot Product | `sum(A × B)` | Higher = more similar (for normalized vectors) |

**When to use what**:
- **Cosine**: Default choice; direction matters, not magnitude
- **Euclidean**: When absolute distances matter
- **Dot Product**: Equivalent to cosine for normalized vectors

### Vector Database Operations

**Insert**: Store text with its embedding vector
```python
db.insert(text, embedding_vector)
```

**Search**: Find top-k most similar to query
```python
results = db.search(query_vector, k=5)
```

**Search by text**: Embed query, then search
```python
results = db.search_by_text("What is the weather?", k=5)
```

---

## 5. Common Patterns

### Pattern 1: Load and Chunk Documents

```python
# Load documents
loader = TextFileLoader("data/document.txt")
documents = loader.load_documents()

# Split into chunks
splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_texts(documents)
```

**Why chunk?**
- Embeddings work best on focused text segments
- Smaller chunks enable more precise retrieval
- Overlap prevents losing context at boundaries

### Pattern 2: Build Vector Database

```python
# Initialize with embedding model
embedding_model = EmbeddingModel()
vector_db = VectorDatabase(embedding_model)

# Build index (async)
import asyncio
vector_db = asyncio.run(vector_db.abuild_from_list(chunks))
```

**What happens**:
1. Each chunk is sent to embedding API
2. Returns 1536-dimensional vector
3. Stored as text→vector mapping

### Pattern 3: Retrieve Relevant Context

```python
# Search returns [(text, score), ...]
results = vector_db.search_by_text(
    query_text="What are the main themes?",
    k=3,
    distance_measure=cosine_similarity
)

# Extract just the text
context_chunks = [text for text, score in results]
```

### Pattern 4: Augment and Generate

```python
# Build prompt with retrieved context
context = "\n---\n".join(context_chunks)
prompt = f"""Answer based on this context:

{context}

Question: {query}
Answer:"""

# Generate response
llm = ChatOpenAI()
response = llm.run([{"role": "user", "content": prompt}])
```

---

## 6. Architecture Diagrams

### RAG Pipeline (ASCII)

```
                    INDEXING PHASE
    ┌──────────┐    ┌──────────┐    ┌──────────┐
    │Documents │───→│ Chunker  │───→│ Embedder │
    └──────────┘    └──────────┘    └────┬─────┘
                                         │
                                         ▼
                                  ┌─────────────┐
                                  │Vector Store │
                                  └──────┬──────┘
                                         │
                    QUERY PHASE          │
    ┌──────────┐    ┌──────────┐         │
    │  Query   │───→│ Embedder │─────────┘
    └──────────┘    └────┬─────┘    (similarity search)
                         │
                         ▼
                  ┌─────────────┐
                  │ Top-k Docs  │
                  └──────┬──────┘
                         │
                    GENERATION PHASE
                         │
    ┌──────────┐    ┌────▼─────┐    ┌──────────┐
    │ Question │───→│  Prompt  │───→│   LLM    │
    └──────────┘    └──────────┘    └────┬─────┘
                                         │
                                         ▼
                                  ┌─────────────┐
                                  │  Response   │
                                  └─────────────┘
```

### Vector Similarity (ASCII)

```
    Query Vector              Document Vectors
         │
         │                    Doc A: ●────────────→
         │
         ▼                    Doc B: ●─────→
    ●────────→
         θ                    Doc C: ●──────────────→

    cosine(Q, A) = 0.92      (most similar - small angle)
    cosine(Q, B) = 0.45      (moderate similarity)
    cosine(Q, C) = 0.21      (least similar - large angle)
```

### Chunking with Overlap

```
    Original Document:
    ┌─────────────────────────────────────────────────┐
    │ The quick brown fox jumps over the lazy dog... │
    └─────────────────────────────────────────────────┘

    Chunks (size=15, overlap=5):
    ┌───────────────┐
    │ The quick bro │ Chunk 1
    └───────────────┘
         ┌───────────────┐
         │ brown fox jum │ Chunk 2 (overlaps "brown")
         └───────────────┘
              ┌───────────────┐
              │ jumps over th │ Chunk 3 (overlaps "jum")
              └───────────────┘
```

---

## 7. Best Practices

### Chunking
- **Start with**: 1000 characters, 200 overlap
- **Adjust based on**: Document type and query patterns
- **Preserve**: Semantic boundaries when possible

### Embedding
- **Batch requests**: Use async_get_embeddings for multiple texts
- **Cache embeddings**: Don't re-embed unchanged documents
- **Same model**: Always use the same model for indexing and querying

### Retrieval
- **Start with k=3-5**: More context isn't always better
- **Check relevance**: Log retrieved chunks to verify quality
- **Consider reranking**: For production, rerank top-N with cross-encoder

### Prompting
- **Be explicit**: Tell the LLM to use only the provided context
- **Handle failures**: What if no relevant documents are found?
- **Show sources**: Return which chunks were used

---

## 8. Common Issues

| Problem | Symptom | Solution |
|---------|---------|----------|
| **API Key Missing** | `ValueError: OPENAI_API_KEY not set` | Set environment variable |
| **Wrong Dimensions** | Shape mismatch in cosine similarity | Using different embedding models |
| **Poor Retrieval** | Irrelevant chunks returned | Adjust chunk size, check embedding quality |
| **Slow Indexing** | Long wait during abuild_from_list | Use batching, async operations |
| **Empty Results** | `[]` returned from search | Check if database was built successfully |

### Debugging Retrieval

```python
# Check what's in the database
print(f"Number of vectors: {len(vector_db.vectors)}")

# Inspect a retrieved chunk
results = vector_db.search_by_text("test query", k=1)
print(f"Top result: {results[0][0][:100]}...")
print(f"Similarity score: {results[0][1]:.4f}")
```

---

## 9. Debugging Tips

### Verify Embeddings Work
```python
# Two similar sentences should have high similarity
emb1 = model.get_embedding("The cat sat on the mat")
emb2 = model.get_embedding("A feline rested on the rug")
emb3 = model.get_embedding("Python is a programming language")

print(f"Similar: {cosine_similarity(np.array(emb1), np.array(emb2)):.4f}")  # ~0.8+
print(f"Different: {cosine_similarity(np.array(emb1), np.array(emb3)):.4f}")  # ~0.3
```

### Check Chunk Quality
```python
# Print first few chunks
for i, chunk in enumerate(chunks[:3]):
    print(f"--- Chunk {i} ({len(chunk)} chars) ---")
    print(chunk[:200])
```

### Trace the Full Pipeline
```python
# Step by step
print("1. Loading documents...")
docs = loader.load_documents()
print(f"   Loaded {len(docs)} documents")

print("2. Chunking...")
chunks = splitter.split_texts(docs)
print(f"   Created {len(chunks)} chunks")

print("3. Building vector DB...")
vector_db = asyncio.run(vector_db.abuild_from_list(chunks))
print(f"   Indexed {len(vector_db.vectors)} vectors")

print("4. Testing retrieval...")
results = vector_db.search_by_text("test", k=2)
print(f"   Found {len(results)} results")
```

---

## 10. Interview Questions

**Q: What is the difference between dense and sparse retrieval?**

Dense retrieval uses neural network embeddings where most values are non-zero, capturing semantic meaning. Sparse retrieval uses traditional methods like TF-IDF where most values are zero, matching keywords. Dense excels at paraphrases and semantic similarity; sparse excels at exact matches and rare terms.

**Q: Why use cosine similarity instead of Euclidean distance?**

Cosine similarity measures the angle between vectors, making it invariant to magnitude. Two documents about the same topic should be similar regardless of length. Euclidean distance is affected by magnitude, so longer documents would appear more different even if semantically similar.

**Q: How do you choose chunk size?**

Balance precision vs. context: smaller chunks enable more targeted retrieval but may lose context; larger chunks preserve context but reduce precision. Start with 500-1000 characters, tune based on evaluation. Consider document structure - technical docs may need smaller chunks than narrative text.

**Q: What is in-context learning?**

In-context learning is a model's ability to adapt its behavior based on information provided in the prompt, without any weight updates. It's the foundation of RAG - we provide relevant context that the model uses to generate informed responses.

**Q: How would you evaluate a RAG system?**

- **Retrieval**: Precision@k, Recall, MRR - are the right documents retrieved?
- **Generation**: Faithfulness - does the answer use the context? Relevance - does it answer the question?
- **End-to-end**: User satisfaction, task completion rate

---

## 11. Resources & Links

### Official Documentation
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
- [LangChain Vector Stores](https://docs.langchain.com/oss/python/integrations/vectorstores/)
- [PydanticAI RAG Example](https://ai.pydantic.dev/examples/rag/)

### Papers
- [RAG Paper (2020)](https://arxiv.org/abs/2005.11401) - Original RAG architecture
- [GPT-3 Paper (2020)](https://arxiv.org/abs/2005.14165) - In-context learning
- [Sentence-BERT (2019)](https://arxiv.org/abs/1908.10084) - Sentence embeddings

### Benchmarks & Leaderboards
- [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) - Embedding model rankings

### Production Vector Databases
- [pgvector](https://github.com/pgvector/pgvector) - PostgreSQL extension
- [Chroma](https://www.trychroma.com/) - Open-source embedding database
- [Pinecone](https://www.pinecone.io/) - Managed vector database
- [Weaviate](https://weaviate.io/) - Open-source vector search

### Tutorials
- [Illustrated Word2Vec](https://jalammar.github.io/illustrated-word2vec/)
- [Word2Vec TensorFlow Projector](https://projector.tensorflow.org/)

---

## 12. Key Takeaways

1. **RAG is automated in-context learning** - We retrieve context instead of manually writing it

2. **Embeddings capture meaning, not keywords** - Similar concepts cluster in vector space regardless of exact wording

3. **Cosine similarity is the default choice** - Measures direction, not magnitude; works well for normalized embeddings

4. **Chunking matters more than you think** - Balance precision and context; overlap prevents information loss

5. **Start simple, then optimize** - Brute-force search with NumPy is fine for learning; add indexes for scale

6. **Same model for indexing and querying** - Mixing embedding models breaks similarity comparisons

7. **Evaluate retrieval separately from generation** - Poor retrieval can't be fixed by a better LLM

8. **Production RAG is hybrid** - Combine dense vectors with sparse (BM25) for best results

9. **The architecture is the constant** - Tools change; the pattern of embed → store → search → augment → generate persists

10. **Vibe checks first, metrics second** - Manual review catches obvious problems; metrics quantify improvements

---

*Cheatsheet for AIE9 Session 2 - Dense Vector Retrieval*
