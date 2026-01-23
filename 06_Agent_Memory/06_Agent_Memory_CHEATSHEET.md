# Session 6 Cheatsheet: Agent Memory

> Building Memory-Enabled Agents with LangGraph

---

## Quick Reference

| Concept | Definition | Key API/Pattern |
|---------|------------|-----------------|
| Short-Term Memory | Thread-scoped conversation history | `checkpointer` + `thread_id` |
| Long-Term Memory | Cross-thread persistent storage | `store` + namespaces |
| Checkpointer | Persists state at each graph step | `InMemorySaver`, `SqliteSaver`, `PostgresSaver` |
| Store | JSON document storage with namespaces | `InMemoryStore` |
| Thread Management | Identifies unique conversations | `config["configurable"]["thread_id"]` |
| Hot Path Memory | State updates during runtime | `Command(update={...})` |
| Background Memory | Async persistence outside main loop | `store.put()` |
| Memory Architecture | Dual persistence pattern | `checkpointer` + `store` |
| Memory Search | Semantic retrieval via embeddings | `store.search(query=...)` |

---

## Setup Requirements

### Dependencies
```bash
pip install langgraph>=0.2.0 langchain-openai langsmith
pip install langgraph-checkpoint-sqlite   # For SQLite persistence
pip install langgraph-checkpoint-postgres # For production Postgres
```

### Environment Variables
```python
import os
os.environ["OPENAI_API_KEY"] = "your-key"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-langsmith-key"
os.environ["LANGCHAIN_PROJECT"] = "AIE9-Session6"
```

---

## 1. Short-Term Memory

### Definition
> **"Short-term memory lets your application remember previous interactions within a single thread or conversation."**
> -- LangGraph Docs [[1]](https://docs.langchain.com/oss/python/concepts/memory)

### Key Characteristics
- **Thread-scoped**: Each `thread_id` maintains separate history
- **Automatic**: Updates at every graph step
- **Persistent**: Survives application restarts (with proper checkpointer)
- **Sequential**: Messages ordered by conversation flow

### Short-Term Memory Flow
```
┌─────────────────────────────────────────────────────────────┐
│               SHORT-TERM MEMORY (THREAD-SCOPED)             │
│                                                             │
│   Thread "abc-123"                                          │
│   ┌──────────┐   ┌──────────┐   ┌──────────┐              │
│   │ Message 1│-->│ Message 2│-->│ Message 3│-->...        │
│   │  "Hi!"   │   │ "Hello!" │   │ "How...?"│              │
│   └──────────┘   └──────────┘   └──────────┘              │
│        │              │              │                     │
│        v              v              v                     │
│   [Checkpointer saves state after each step]              │
└─────────────────────────────────────────────────────────────┘
```

### Basic Pattern
```python
from langgraph.checkpoint.memory import InMemorySaver
checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)
```

> **Critical**: Without `checkpointer` in `compile()`, state is lost when execution ends. This is the #1 beginner mistake.

**Official Docs**: [Short-Term Memory](https://docs.langchain.com/oss/python/langchain/short-term-memory) [[2]](https://docs.langchain.com/oss/python/langchain/short-term-memory)

---

## 2. Long-Term Memory

### Definition
> **"Long-term memory stores user-specific or application-level data across sessions and is shared across conversational threads."**
> -- LangGraph Docs [[1]](https://docs.langchain.com/oss/python/concepts/memory)

### Key Characteristics
- **Cross-thread**: Accessible from any conversation
- **Namespace-organized**: Hierarchical storage structure
- **JSON documents**: Flexible data format
- **User-scoped**: Often organized by user ID

### Long-Term Memory Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    LONG-TERM MEMORY (STORE)                 │
│                                                             │
│   Namespace: ("user_123", "preferences")                    │
│   ┌────────────────────────────────────────────┐           │
│   │  Key: "food"     -> {"value": "pizza"}     │           │
│   │  Key: "language" -> {"value": "english"}   │           │
│   │  Key: "theme"    -> {"value": "dark"}      │           │
│   └────────────────────────────────────────────┘           │
│                                                             │
│   Namespace: ("user_123", "memories")                       │
│   ┌────────────────────────────────────────────┐           │
│   │  Key: "mem_001"  -> {"text": "Likes jazz"} │           │
│   │  Key: "mem_002"  -> {"text": "Has a dog"}  │           │
│   └────────────────────────────────────────────┘           │
│                                                             │
│   [Accessible from ANY thread for user_123]                │
└─────────────────────────────────────────────────────────────┘
```

### Store Operations
| Operation | Method | Description |
|-----------|--------|-------------|
| Create | `store.put(namespace, key, value)` | Add/update memory |
| Read | `store.get(namespace, key)` | Retrieve by key |
| Search | `store.search(namespace, query=...)` | Semantic search |
| Delete | `store.delete(namespace, key)` | Remove memory |

**Official Docs**: [Long-Term Memory](https://docs.langchain.com/oss/python/langchain/long-term-memory) [[3]](https://docs.langchain.com/oss/python/langchain/long-term-memory)

---

## 3. Checkpointers

### Overview
> **"Memory is a system that remembers information about previous interactions."**
> -- LangGraph Docs [[1]](https://docs.langchain.com/oss/python/concepts/memory)

### Checkpointer Types

| Checkpointer | Package | Use Case |
|--------------|---------|----------|
| `InMemorySaver` | `langgraph-checkpoint` | Development/testing |
| `SqliteSaver` | `langgraph-checkpoint-sqlite` | Local persistence |
| `PostgresSaver` | `langgraph-checkpoint-postgres` | Production |

### Checkpointer Selection Guide
```
┌─────────────────────────────────────────────────────────────┐
│                  CHOOSING A CHECKPOINTER                    │
│                                                             │
│   Development?                                              │
│        │                                                    │
│        ├── Yes ──> InMemorySaver (fast, no setup)          │
│        │                                                    │
│        └── No ──> Need local persistence?                   │
│                        │                                    │
│                        ├── Yes ──> SqliteSaver             │
│                        │                                    │
│                        └── No ──> PostgresSaver (prod)     │
└─────────────────────────────────────────────────────────────┘
```

### Usage Patterns
```python
# In-memory (development)
from langgraph.checkpoint.memory import InMemorySaver
checkpointer = InMemorySaver()

# SQLite (local persistence)
from langgraph.checkpoint.sqlite import SqliteSaver
checkpointer = SqliteSaver.from_conn_string("./memory.db")

# Postgres (production)
from langgraph.checkpoint.postgres import PostgresSaver
checkpointer = PostgresSaver.from_conn_string(connection_string)
```

**Official Docs**: [Checkpointer Libraries](https://docs.langchain.com/oss/python/langgraph/persistence) [[4]](https://docs.langchain.com/oss/python/langgraph/persistence)

---

## 4. Stores

### Store Architecture
Stores organize memories as JSON documents under hierarchical namespaces.

### Namespace Structure
```
┌─────────────────────────────────────────────────────────────┐
│                    STORE NAMESPACE HIERARCHY                │
│                                                             │
│   store.put(                                                │
│       namespace = ("user_id", "context"),  <-- Tuple       │
│       key = "memory_id",                   <-- String      │
│       value = {"data": ...}                <-- JSON Dict   │
│   )                                                         │
│                                                             │
│   Conceptual Path: /user_id/context/memory_id              │
│                                                             │
│   Examples:                                                 │
│   - ("user_123", "preferences") / "theme"                  │
│   - ("org_456", "policies") / "refund_policy"              │
│   - ("app", "config") / "feature_flags"                    │
└─────────────────────────────────────────────────────────────┘
```

### Namespace Design Patterns
| App Type | Namespace Pattern | Rationale |
|----------|------------------|-----------|
| Single-user | `(user_id, context)` | Simple hierarchy |
| Multi-tenant | `(org_id, user_id, type)` | Org-level isolation |
| Knowledge base | `(domain, category)` | Topic-organized |

### InMemoryStore Setup
```python
from langgraph.store.memory import InMemoryStore

store = InMemoryStore()
graph = builder.compile(store=store)
```

### Store with Semantic Search
```python
from langchain.embeddings import init_embeddings
store = InMemoryStore(
    index={"embed": init_embeddings("openai:text-embedding-3-small"), "dims": 1536}
)
```

**Official Docs**: [Memory Store](https://docs.langchain.com/oss/python/langgraph/persistence) [[4]](https://docs.langchain.com/oss/python/langgraph/persistence)

---

## 5. Thread Management

### Thread as Conversation Identifier
Each `thread_id` represents a unique conversation context.

### Thread Isolation Pattern
```
┌─────────────────────────────────────────────────────────────┐
│                    THREAD ISOLATION                          │
│                                                             │
│   User: Alice                                               │
│   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │
│   │ Thread: t1  │  │ Thread: t2  │  │ Thread: t3  │       │
│   │ "Pizza app" │  │ "Weather"   │  │ "Calendar"  │       │
│   │ [isolated]  │  │ [isolated]  │  │ [isolated]  │       │
│   └─────────────┘  └─────────────┘  └─────────────┘       │
│         │                │                │                │
│         └────────────────┼────────────────┘                │
│                          v                                  │
│              Long-Term Store (shared)                       │
│              Namespace: ("alice", "preferences")            │
└─────────────────────────────────────────────────────────────┘
```

### Thread Configuration
```python
config = {"configurable": {"thread_id": "conversation-123"}}
response = graph.invoke({"messages": [...]}, config)
```

### Multi-User Pattern
```python
config = {
    "configurable": {
        "thread_id": "conv-abc",
        "user_id": "user_123"    # For long-term memory namespace
    }
}
```

**Official Docs**: [Add Memory](https://docs.langchain.com/oss/python/langgraph/add-memory) [[5]](https://docs.langchain.com/oss/python/langgraph/add-memory)

---

## 6. Hot Path Memory

### Definition
Memory updates that occur during graph execution as part of the main processing flow.

### Hot Path Flow
```
┌─────────────────────────────────────────────────────────────┐
│                    HOT PATH MEMORY                          │
│                                                             │
│   Input --> Node A --> Node B --> Output                    │
│               │           │                                 │
│               v           v                                 │
│         [State Update] [State Update]                       │
│               │           │                                 │
│               └─────┬─────┘                                 │
│                     v                                       │
│              Checkpointer                                   │
│          (saves after each step)                            │
└─────────────────────────────────────────────────────────────┘
```

### Command Pattern for State Updates
```python
from langgraph.graph import Command

def my_node(state):
    return Command(
        update={"counter": state["counter"] + 1},  # State update
        goto="next_node"                            # Control flow
    )
```

### Use Cases
- Conversation history accumulation
- Intermediate computation results
- Real-time state tracking
- Tool call results

**Official Docs**: [Command Updates](https://docs.langchain.com/oss/python/langgraph/use-graph-api) [[6]](https://docs.langchain.com/oss/python/langgraph/use-graph-api)

---

## 7. Background Memory

### Definition
Memory persistence that occurs asynchronously, outside the critical path of request processing.

### Background vs Hot Path
```
┌─────────────────────────────────────────────────────────────┐
│             HOT PATH vs BACKGROUND MEMORY                   │
│                                                             │
│   HOT PATH (synchronous):                                   │
│   Request --> Process --> State Update --> Response         │
│                              │                              │
│                         [blocking]                          │
│                                                             │
│   BACKGROUND (asynchronous):                                │
│   Request --> Process --> Response                          │
│                  │                                          │
│                  └──> [async] store.put() ──> Store        │
│                         [non-blocking]                      │
└─────────────────────────────────────────────────────────────┘
```

### Background Store Operations
```python
def update_memory(state, config, *, store):
    user_id = config["configurable"]["user_id"]
    namespace = (user_id, "memories")
    memory_id = str(uuid.uuid4())

    # Background write - doesn't block response
    store.put(namespace, memory_id, {"memory": extracted_fact})
```

### Use Cases
- User preference learning
- Fact extraction from conversations
- Analytics and logging
- Cross-session insights

**Official Docs**: [Memory Store Operations](https://docs.langchain.com/oss/python/langgraph/persistence) [[4]](https://docs.langchain.com/oss/python/langgraph/persistence)

---

## 8. Memory Architecture

### Dual Pattern: Checkpointer + Store

```
┌─────────────────────────────────────────────────────────────┐
│              COMPLETE MEMORY ARCHITECTURE                   │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐  │
│   │                    CHECKPOINTER                      │  │
│   │              (Short-Term Memory)                     │  │
│   │                                                      │  │
│   │   Thread A ──> [msg1, msg2, msg3, ...]             │  │
│   │   Thread B ──> [msg1, msg2, ...]                   │  │
│   │   Thread C ──> [msg1, ...]                         │  │
│   └─────────────────────────────────────────────────────┘  │
│                          │                                  │
│                          │ compile(checkpointer, store)     │
│                          │                                  │
│   ┌─────────────────────────────────────────────────────┐  │
│   │                      STORE                           │  │
│   │               (Long-Term Memory)                     │  │
│   │                                                      │  │
│   │   User Prefs ──> {theme: dark, lang: en}           │  │
│   │   User Facts ──> [likes pizza, has dog]            │  │
│   │   App Config ──> {features: [...]}                 │  │
│   └─────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Complete Setup Pattern
```python
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore

checkpointer = InMemorySaver()
store = InMemoryStore()

graph = builder.compile(
    checkpointer=checkpointer,  # Short-term
    store=store                  # Long-term
)
```

### When to Use Each

| Need | Use | Reason |
|------|-----|--------|
| Conversation history | Checkpointer | Thread-scoped, automatic |
| User preferences | Store | Cross-thread, persistent |
| Session state | Checkpointer | Tied to conversation |
| Learned facts | Store | Available everywhere |

**Official Docs**: [Persistence Guide](https://docs.langchain.com/oss/python/langgraph/persistence) [[4]](https://docs.langchain.com/oss/python/langgraph/persistence)

---

## 9. Memory Search

### Semantic Search Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                  SEMANTIC MEMORY SEARCH                     │
│                                                             │
│   Query: "I'm hungry"                                       │
│            │                                                │
│            v                                                │
│   ┌──────────────┐                                         │
│   │  Embedding   │ ──> [0.12, 0.87, 0.34, ...]            │
│   │    Model     │                                         │
│   └──────────────┘                                         │
│            │                                                │
│            v                                                │
│   ┌──────────────────────────────────────────────┐        │
│   │              Vector Index                     │        │
│   │  "I love pizza"    [0.11, 0.89, 0.32] ✓ 0.97│        │
│   │  "I am a plumber"  [0.45, 0.12, 0.78]   0.23│        │
│   │  "Coffee is great" [0.33, 0.67, 0.45]   0.41│        │
│   └──────────────────────────────────────────────┘        │
│            │                                                │
│            v                                                │
│   Result: "I love pizza" (highest similarity)              │
└─────────────────────────────────────────────────────────────┘
```

### Enable Semantic Search
```python
from langchain.embeddings import init_embeddings
from langgraph.store.memory import InMemoryStore

embeddings = init_embeddings("openai:text-embedding-3-small")
store = InMemoryStore(
    index={"embed": embeddings, "dims": 1536}
)
```

### Search Operations
```python
# Store memories
store.put(("user_123", "memories"), "1", {"text": "I love pizza"})
store.put(("user_123", "memories"), "2", {"text": "I am a plumber"})

# Semantic search
items = store.search(
    ("user_123", "memories"),
    query="I'm hungry",
    limit=1
)
# Returns: "I love pizza" (semantically related to hunger)
```

### Semantic Search Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| No results returned | Namespace mismatch | Verify exact namespace tuple matches between `put()` and `search()` |
| Wrong results | Low embedding dims | Use minimum 1536 dims for text-embedding-3-small |
| Empty results | Missing index config | Ensure `index={"embed": ..., "dims": ...}` in store init |
| Slow searches | Large namespace | Add namespace partitioning or use external vector DB |
| API errors | Missing API key | Set `OPENAI_API_KEY` environment variable |

> **Common Mistake**: Using `store.get()` for semantic lookup. Use `store.search()` for similarity-based retrieval; `get()` only works with exact key matches.

**Official Docs**: [Semantic Search](https://docs.langchain.com/oss/python/langgraph/add-memory) [[5]](https://docs.langchain.com/oss/python/langgraph/add-memory)

---

## 10. Memory Lifecycle

### CRUD Operations Flow
```
┌─────────────────────────────────────────────────────────────┐
│                   MEMORY LIFECYCLE                          │
│                                                             │
│   CREATE                                                    │
│   store.put(namespace, key, {"data": "value"})             │
│        │                                                    │
│        v                                                    │
│   ┌──────────┐                                             │
│   │  STORE   │ ◄─────────────────────────────┐            │
│   └──────────┘                               │            │
│        │                                      │            │
│        v                                      │            │
│   READ                              UPDATE    │            │
│   store.get(namespace, key)         store.put(namespace,  │
│   store.search(namespace, query)    key, {"new": "data"}) │
│        │                                      │            │
│        v                                      │            │
│   DELETE                                                   │
│   store.delete(namespace, key)                             │
└─────────────────────────────────────────────────────────────┘
```

### Lifecycle Operations Table

| Operation | Method | Returns |
|-----------|--------|---------|
| Create | `store.put(ns, key, value)` | None |
| Read (exact) | `store.get(ns, key)` | Item or None |
| Read (search) | `store.search(ns, query=...)` | List[Item] |
| Update | `store.put(ns, key, new_value)` | None (overwrites) |
| Delete | `store.delete(ns, key)` | None |

### Access in Nodes
```python
def my_node(state, config, *, store):
    user_id = config["configurable"]["user_id"]
    namespace = (user_id, "preferences")

    # Read
    item = store.get(namespace, "settings")

    # Update
    store.put(namespace, "settings", {"theme": "dark"})
```

---

## 11. Common Misconceptions

### Misconception vs Reality

| Misconception | Reality |
|---------------|---------|
| "Checkpointer stores long-term memory" | Checkpointer is thread-scoped; use Store for cross-thread |
| "Memory persists without a checkpointer" | In-memory state is lost; need checkpointer for persistence |
| "All threads share the same messages" | Each thread_id has isolated message history |
| "Store and checkpointer are interchangeable" | Different purposes: Store for data, Checkpointer for state |
| "InMemorySaver persists to disk" | InMemory = RAM only; use SqliteSaver for disk |

### Thread vs Store Scope
```
┌─────────────────────────────────────────────────────────────┐
│                    SCOPE COMPARISON                         │
│                                                             │
│   CHECKPOINTER (Thread-Scoped):                            │
│   ┌─────────┐  ┌─────────┐  ┌─────────┐                   │
│   │Thread A │  │Thread B │  │Thread C │  <-- Isolated     │
│   │[msgs]   │  │[msgs]   │  │[msgs]   │                   │
│   └─────────┘  └─────────┘  └─────────┘                   │
│                                                             │
│   STORE (User/App-Scoped):                                 │
│   ┌─────────────────────────────────────────┐              │
│   │        Shared across ALL threads         │ <-- Global │
│   │  User preferences, learned facts, etc.   │              │
│   └─────────────────────────────────────────┘              │
└─────────────────────────────────────────────────────────────┘
```

---

## 12. Assignment Reference

### Session 6 Homework Checklist
- [ ] Implement short-term memory with InMemorySaver
- [ ] Add long-term memory store with namespaces
- [ ] Configure thread management with unique IDs
- [ ] Implement semantic search for memory retrieval
- [ ] Test memory persistence across conversations
- [ ] Experiment with different checkpointer backends

### Key Concepts to Demonstrate
1. Thread isolation (separate conversations)
2. Cross-thread memory sharing (user preferences)
3. Semantic search for relevant memories
4. Proper namespace organization

---

## Code Patterns Reference

### Pattern 1: Basic Memory Setup
```python
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore

checkpointer = InMemorySaver()
store = InMemoryStore()
graph = builder.compile(checkpointer=checkpointer, store=store)
```

### Pattern 2: Thread Configuration
```python
config = {"configurable": {"thread_id": "user-session-123", "user_id": "alice"}}
response = graph.invoke({"messages": [{"role": "user", "content": "Hi"}]}, config)
```

### Pattern 3: Store Operations in Node
```python
def memory_node(state, config, *, store):
    user_id = config["configurable"]["user_id"]
    items = store.search((user_id, "memories"), query=state["messages"][-1].content)
    return {"context": [item.value for item in items]}
```

### Pattern 4: Semantic Search Setup
```python
from langchain.embeddings import init_embeddings
store = InMemoryStore(
    index={"embed": init_embeddings("openai:text-embedding-3-small"), "dims": 1536}
)
```

---

## Common Issues & Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| Memory lost between runs | Using InMemorySaver | Switch to SqliteSaver or PostgresSaver |
| Messages shared across threads | Same thread_id used | Use unique thread_id per conversation |
| Store.get returns None | Wrong namespace or key | Check namespace tuple and key string |
| Semantic search fails | No index configured | Add `index` config to InMemoryStore |
| State not persisting | Missing checkpointer | Add `checkpointer=` in compile() |
| Cross-thread data not found | Using checkpointer instead of store | Use store.put() for shared data |

---

## Breakout Room Tasks Summary

### Breakout Room 1 (Tasks 1-5)
- [ ] Set up environment with dependencies
- [ ] Create graph with InMemorySaver checkpointer
- [ ] Test multi-turn conversation with thread_id
- [ ] Verify thread isolation with different thread_ids
- [ ] **Activity**: Implement basic short-term memory

### Breakout Room 2 (Tasks 6-10)
- [ ] Add InMemoryStore for long-term memory
- [ ] Implement namespace structure for users
- [ ] Create memory read/write operations in nodes
- [ ] Enable semantic search with embeddings
- [ ] **Activity**: Build complete memory architecture

---

## Official Documentation Links

### Memory Concepts
- [Memory Overview](https://docs.langchain.com/oss/python/concepts/memory) [[1]](https://docs.langchain.com/oss/python/concepts/memory)
- [Short-Term Memory](https://docs.langchain.com/oss/python/langchain/short-term-memory) [[2]](https://docs.langchain.com/oss/python/langchain/short-term-memory)
- [Long-Term Memory](https://docs.langchain.com/oss/python/langchain/long-term-memory) [[3]](https://docs.langchain.com/oss/python/langchain/long-term-memory)

### LangGraph Persistence
- [Persistence Guide](https://docs.langchain.com/oss/python/langgraph/persistence) [[4]](https://docs.langchain.com/oss/python/langgraph/persistence)
- [Add Memory Guide](https://docs.langchain.com/oss/python/langgraph/add-memory) [[5]](https://docs.langchain.com/oss/python/langgraph/add-memory)
- [Command API](https://docs.langchain.com/oss/python/langgraph/use-graph-api) [[6]](https://docs.langchain.com/oss/python/langgraph/use-graph-api)

### Context Engineering
- [Dynamic Runtime Context](https://docs.langchain.com/oss/python/concepts/context) [[7]](https://docs.langchain.com/oss/python/concepts/context)

### Embedding & Search
- [Embedding Models](https://docs.langchain.com/oss/python/integrations/text_embedding/index) [[8]](https://docs.langchain.com/oss/python/integrations/text_embedding/index)

### LangSmith
- [LangSmith Observability](https://docs.langchain.com/langsmith/observability) [[9]](https://docs.langchain.com/langsmith/observability)

### LangChain Academy Courses
- [Introduction to LangGraph](https://github.com/langchain-ai/langchain-academy) - Modules 1-5 including memory and persistence [[10]](https://github.com/langchain-ai/langchain-academy)
- [Ambient Agents Project](https://github.com/langchain-ai/agents-from-scratch) - Email assistant with memory capabilities [[11]](https://github.com/langchain-ai/agents-from-scratch)
- [Long-Term Memory Course](https://www.deeplearning.ai/short-courses/long-term-agentic-memory-with-langgraph/) - DeepLearning.AI free course [[12]](https://www.deeplearning.ai/short-courses/long-term-agentic-memory-with-langgraph/)

---

## References

1. LangGraph Documentation. "Memory Overview." https://docs.langchain.com/oss/python/concepts/memory

2. LangChain Documentation. "Short-Term Memory." https://docs.langchain.com/oss/python/langchain/short-term-memory

3. LangChain Documentation. "Long-Term Memory." https://docs.langchain.com/oss/python/langchain/long-term-memory

4. LangGraph Documentation. "Persistence Guide." https://docs.langchain.com/oss/python/langgraph/persistence

5. LangGraph Documentation. "Add Memory Guide." https://docs.langchain.com/oss/python/langgraph/add-memory

6. LangGraph Documentation. "Command API." https://docs.langchain.com/oss/python/langgraph/use-graph-api

7. LangGraph Documentation. "Dynamic Runtime Context." https://docs.langchain.com/oss/python/concepts/context

8. LangChain Documentation. "Embedding Models." https://docs.langchain.com/oss/python/integrations/text_embedding/index

9. LangSmith Documentation. "Observability." https://docs.langchain.com/langsmith/observability

10. LangChain Academy. "Introduction to LangGraph." https://github.com/langchain-ai/langchain-academy

11. LangChain Academy. "Agents from Scratch - Ambient Agents Project." https://github.com/langchain-ai/agents-from-scratch

12. DeepLearning.AI. "Long-Term Agentic Memory with LangGraph." https://www.deeplearning.ai/short-courses/long-term-agentic-memory-with-langgraph/

---

*Cheatsheet created for AIE9 Session 6: Agent Memory*
*Last updated: January 2026*
