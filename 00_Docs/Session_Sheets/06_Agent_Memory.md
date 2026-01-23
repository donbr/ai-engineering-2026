# Session 6: Agent Memory

> **Module**: Complex Agents | **Week**: 3

---

## Goal

Understand how agents remember information across interactions by implementing both short-term (thread-scoped) and long-term (cross-session) memory systems.

---

## Learning Outcomes

By the end of this session, you will be able to:

1. **Differentiate** between short-term and long-term memory in agentic systems and know when to use each
2. **Implement** checkpointers for thread-scoped conversation persistence
3. **Configure** stores with namespaces for cross-session memory
4. **Choose** between hot path and background memory writing strategies based on application requirements
5. **Design** memory architectures that combine checkpointers and stores effectively

---

## Tools Introduced

| Tool | Purpose | Documentation |
|------|---------|---------------|
| **InMemorySaver** | Development checkpointer for short-term memory | [Persistence Guide](https://docs.langchain.com/oss/python/langgraph/persistence) |
| **SqliteSaver** | Local workflow checkpointer | [langgraph-checkpoint-sqlite](https://docs.langchain.com/oss/python/langgraph/persistence) |
| **PostgresSaver** | Production checkpointer | [langgraph-checkpoint-postgres](https://docs.langchain.com/oss/python/langgraph/persistence) |
| **InMemoryStore** | Development store for long-term memory | [Memory Store](https://docs.langchain.com/oss/python/langgraph/persistence) |

---

## Required Tooling & Account Setup

In addition to the tools we've already learned, in this session you'll need:

1. Existing [LangSmith](https://smith.langchain.com/) account (from Session 3)
2. Optional: PostgreSQL for production persistence patterns

---

## Recommended Reading

| Resource | Type | Link |
|----------|------|------|
| Memory Overview | Concepts | [LangChain](https://docs.langchain.com/oss/python/concepts/memory) |
| Short-term Memory | How-to | [LangChain](https://docs.langchain.com/oss/python/langchain/short-term-memory) |
| Long-term Memory | How-to | [LangChain](https://docs.langchain.com/oss/python/langchain/long-term-memory) |
| Add Memory to Agents | Tutorial | [LangGraph](https://docs.langchain.com/oss/python/langgraph/add-memory) |
| Persistence Guide | Reference | [LangGraph](https://docs.langchain.com/oss/python/langgraph/persistence) |
| Context Engineering | Concepts | [LangChain](https://docs.langchain.com/oss/python/langchain/context-engineering) |

---

## LangChain Academy Courses

| Course | Repository | Description |
|--------|------------|-------------|
| Introduction to LangGraph | [langchain-academy](https://github.com/langchain-ai/langchain-academy) | Modules 1-5 including memory and persistence concepts |
| Ambient Agents Project | [agents-from-scratch](https://github.com/langchain-ai/agents-from-scratch) | Email assistant with human-in-the-loop and memory capabilities |
| Long-Term Memory Course | [DeepLearning.AI](https://www.deeplearning.ai/short-courses/long-term-agentic-memory-with-langgraph/) | Free short course on LangGraph memory patterns |

> **Recommended**: Complete the LangChain Academy "Introduction to LangGraph" course Module 4 (Memory & Persistence) before this session for deeper understanding.

---

# Overview

In Session 6, we tackle one of the most important capabilities for production agents: **memory**. Without memory, every conversation starts fresh. With memory, agents can maintain context within conversations, learn user preferences across sessions, and build increasingly personalized experiences.

> "Memory is a system that remembers information about previous interactions." ~ LangChain Documentation

The core **concepts** we'll cover include the distinction between short-term and long-term memory, the role of checkpointers and stores, and the architectural decisions around when and how to write memories. We'll also explore the trade-offs between writing memories during runtime (hot path) versus in background processes.

The core **code** we'll cover includes configuring checkpointers for thread persistence, setting up stores with namespaces for cross-session data, and implementing both hot path memory writes via `Command(update={...})` and background writes via `store.put()`.

---

# What is Agent Memory?

Before diving into implementation, let's establish why memory matters for agents.

Consider a customer service agent. Without memory:
- Every interaction starts from scratch
- Users must repeat their preferences
- The agent cannot learn from past interactions
- Context is lost when conversations span multiple sessions

With memory:
- Conversations can be paused and resumed
- User preferences persist across sessions
- The agent improves through accumulated knowledge
- Multi-turn interactions feel natural and contextual

**Reflection Question**: Think about applications you use daily. Which ones remember your preferences? How does that memory enhance your experience?

---

# Short-Term vs. Long-Term Memory

The LangChain ecosystem provides a clear conceptual framework for agent memory:

> "Short-term memory lets your application remember previous interactions within a single thread or conversation." ~ LangChain Documentation

> "Long-term memory stores user-specific or application-level data across sessions and is shared across conversational threads." ~ LangChain Documentation

```
+----------------------------------------------------------+
|                    MEMORY ARCHITECTURE                    |
+----------------------------------------------------------+
|                                                          |
|  SHORT-TERM MEMORY              LONG-TERM MEMORY         |
|  (Thread-Scoped)                (Cross-Session)          |
|                                                          |
|  +------------------+           +------------------+     |
|  |   Thread 1       |           |                  |     |
|  |   [msg1, msg2]   |           |    STORE         |     |
|  +------------------+           |                  |     |
|           |                     |  namespace_a/    |     |
|           v                     |    key_1: {...}  |     |
|  +------------------+           |    key_2: {...}  |     |
|  |   Thread 2       |           |                  |     |
|  |   [msg1, msg2]   |           |  namespace_b/    |     |
|  +------------------+           |    key_1: {...}  |     |
|           |                     |                  |     |
|           v                     +------------------+     |
|     CHECKPOINTER                        |                |
|  (saves state per thread)         (shared across         |
|                                    all threads)          |
+----------------------------------------------------------+
```

**Key Distinction**:
- **Short-term memory**: Isolated to a single `thread_id`. When you start a new thread, you start fresh.
- **Long-term memory**: Accessible from any thread. Organized by namespaces (like folders) and keys (like filenames).

**Reflection Question**: In a customer support chatbot, what information belongs in short-term memory versus long-term memory?

---

# Checkpointers: The Foundation of Short-Term Memory

> **Critical**: Without a `checkpointer` parameter in `graph.compile()`, your agent has **NO persistent memory at all**. State exists only during execution and is lost when the process ends. This is the most common mistake beginners make.

Checkpointers persist the graph state at each step, enabling conversation continuity within a thread.

## Checkpointer Options

| Checkpointer | Use Case | Persistence |
|--------------|----------|-------------|
| `InMemorySaver` | Development, testing | Lost on restart |
| `SqliteSaver` | Local workflows, prototypes | File-based |
| `PostgresSaver` | Production deployments | Database-backed |

## The Thread ID Pattern

The `thread_id` is the key to short-term memory. Same thread_id = same conversation context.

```
Thread ID: "conversation_123"
+------------------------------------------+
|  Invocation 1                            |
|  User: "Hi, my name is Alice"            |
|  Agent: "Hello Alice! How can I help?"   |
+------------------------------------------+
            |
            v (checkpointer saves state)
+------------------------------------------+
|  Invocation 2                            |
|  User: "What's my name?"                 |
|  Agent: "Your name is Alice!"            |
+------------------------------------------+
```

**Why This Works**: The checkpointer saves the message history after each invocation. When invoked again with the same `thread_id`, the agent retrieves the previous state and continues the conversation.

**Reflection Question**: What happens if you invoke the same agent with a different `thread_id`? What if you want the agent to forget a specific conversation?

---

# Stores: Enabling Long-Term Memory

While checkpointers handle thread-scoped persistence, **stores** enable memory that transcends individual conversations.

## The Namespace Pattern

Stores organize data hierarchically using namespaces:

```
STORE
|
+-- ("user_123", "preferences")
|   +-- "language": {"value": "English"}
|   +-- "timezone": {"value": "PST"}
|
+-- ("user_123", "history")
|   +-- "favorite_topics": {"value": ["AI", "cooking"]}
|
+-- ("user_456", "preferences")
    +-- "language": {"value": "Spanish"}
```

**Key Operations**:
- `store.put(namespace, key, value)` - Save a memory
- `store.get(namespace, key)` - Retrieve a specific memory
- `store.search(namespace, query=...)` - Semantic search within a namespace

**Reflection Question**: How would you design namespaces for a multi-tenant application where each user can have multiple projects?

## Namespace Design Guidance

When designing namespaces, consider these patterns:

| Application Type | Recommended Namespace | Rationale |
|-----------------|----------------------|-----------|
| Single-user app | `(user_id, context_type)` | Simple hierarchy, easy queries |
| Multi-tenant SaaS | `(org_id, project_id, user_id, type)` | Supports org-level and user-level queries |
| Shared knowledge base | `(domain, category, doc_id)` | Organized by topic, not user |

**Design Questions to Ask**:
- Will I need to retrieve ALL memories for a user across different contexts?
- Should different tenants/orgs be completely isolated?
- What queries will I need to run against stored memories?

**Anti-patterns to Avoid**:
- Using random UUIDs as namespace components (makes queries impossible)
- Storing all data in a single flat namespace (defeats hierarchical organization)
- Mixing user preferences with system config in the same namespace

---

# Thread Management

The `thread_id` serves as the conversation identifier, but managing threads effectively requires understanding their lifecycle.

```
+----------------------------------------------------------+
|                   THREAD LIFECYCLE                        |
+----------------------------------------------------------+
|                                                          |
|  1. CREATE          2. CONTINUE        3. BRANCH         |
|                                                          |
|  thread_id: "new"   thread_id: "abc"   thread_id: "xyz"  |
|      |                  |                  |              |
|      v                  v                  v              |
|  [empty state]     [load saved        [fork from         |
|                     state]            checkpoint]        |
|                                                          |
+----------------------------------------------------------+
```

**Common Patterns**:
- **New conversation**: Generate a unique `thread_id` (UUID recommended)
- **Resume conversation**: Use the same `thread_id` from before
- **Branch conversation**: Create new `thread_id` but initialize from existing checkpoint

**Reflection Question**: In a customer support system, when should you create a new thread versus continuing an existing one?

---

# Hot Path Memory: Writing During Runtime

Writing memories during agent execution ("in the hot path") provides immediate availability but adds latency and complexity.

## Using Command for State Updates

Tools can update the agent's state during execution by returning a `Command`:

```
+----------------------------------------------------------+
|                 HOT PATH MEMORY WRITE                     |
+----------------------------------------------------------+
|                                                          |
|  User Input                                              |
|      |                                                   |
|      v                                                   |
|  +------------------+                                    |
|  |  Agent Decides   |                                    |
|  |  to Call Tool    |                                    |
|  +------------------+                                    |
|      |                                                   |
|      v                                                   |
|  +------------------+     +------------------+           |
|  |  Tool Executes   | --> | Return Command   |           |
|  |  Business Logic  |     | update={...}     |           |
|  +------------------+     +------------------+           |
|                               |                          |
|                               v                          |
|                      State Updated                       |
|                      Immediately                         |
|                                                          |
+----------------------------------------------------------+
```

**Advantages**:
- Memories available immediately for subsequent steps
- Users can be notified of memory creation
- Transparent process

**Challenges**:
- Adds latency to agent responses
- Agent must multitask between primary goals and memory management
- May affect quality of both task and memory

**Reflection Question**: For a personal assistant agent, which user preferences should be saved in the hot path versus in the background?

---

# Background Memory: Async Persistence

Writing memories as a separate background process decouples memory management from the primary agent flow.

## Background Memory Pattern

```
+----------------------------------------------------------+
|              BACKGROUND MEMORY WRITE                      |
+----------------------------------------------------------+
|                                                          |
|  Agent Conversation         Background Process           |
|                                                          |
|  User: "Hi!"                                             |
|  Agent: "Hello!"                                         |
|  User: "Remember I like coffee"                          |
|  Agent: "Got it!"                                        |
|       |                                                  |
|       +-------------> Trigger: after N minutes           |
|       |                    or on schedule                |
|       v                        |                         |
|  [Continue chatting]           v                         |
|                         +------------------+             |
|                         | Memory Service   |             |
|                         | Analyzes thread  |             |
|                         | Extracts facts   |             |
|                         | Writes to store  |             |
|                         +------------------+             |
|                                                          |
+----------------------------------------------------------+
```

**Advantages**:
- No latency impact on primary agent
- Dedicated process can be more thorough
- Avoids redundant memory writes for ongoing conversations

**Challenges**:
- Memories not immediately available to other threads
- Requires deciding when to trigger memory formation
- More complex architecture

**Common Triggers**:
- After a set time period (with rescheduling if new events occur)
- On a cron schedule
- Manual trigger by user or application logic

**Reflection Question**: A note-taking agent helps users capture meeting notes. Should it save summaries in the hot path or background? What factors influence this decision?

## Choosing Hot Path vs Background

| Decision Factor | Choose Hot Path | Choose Background |
|----------------|-----------------|-------------------|
| Data needed for next step? | Yes | No |
| Response latency critical? | No | Yes |
| Data consistency required? | Yes | Can tolerate delay |
| User expects confirmation? | Yes | No |

**Examples**:
- **Hot Path**: User authentication status, shopping cart updates, current task context
- **Background**: Preference extraction, conversation summaries, analytics data

---

# Memory Architecture: Dual Pattern

Production agents typically combine both checkpointers and stores:

```
+----------------------------------------------------------+
|             PRODUCTION MEMORY ARCHITECTURE                |
+----------------------------------------------------------+
|                                                          |
|                    create_agent(                         |
|                        model=...,                        |
|                        tools=[...],                      |
|                        checkpointer=PostgresSaver(),     |
|                        store=PostgresStore()             |
|                    )                                     |
|                                                          |
|  +------------------------+  +------------------------+  |
|  |     CHECKPOINTER       |  |        STORE           |  |
|  +------------------------+  +------------------------+  |
|  | - Thread state         |  | - User preferences     |  |
|  | - Message history      |  | - Learned facts        |  |
|  | - Pending tool calls   |  | - Cross-session data   |  |
|  | - Interrupt state      |  | - Semantic searchable  |  |
|  +------------------------+  +------------------------+  |
|           |                            |                 |
|           v                            v                 |
|      Per-Thread                   Per-Namespace          |
|      Isolation                    Organization           |
|                                                          |
+----------------------------------------------------------+
```

**Design Principle**: Use checkpointers for conversation continuity, stores for knowledge persistence.

**Reflection Question**: Your agent needs to remember that a user prefers metric units. Should this go in the checkpointer or the store? Why?

---

# Memory Search: Beyond Key-Value

Modern stores support semantic search via vector embeddings, enabling retrieval based on meaning rather than exact keys.

```
+----------------------------------------------------------+
|                    MEMORY SEARCH                          |
+----------------------------------------------------------+
|                                                          |
|  Query: "What does the user like to drink?"              |
|                                                          |
|  store.search(                                           |
|      namespace=("user_123", "preferences"),              |
|      query="beverage preferences"                        |
|  )                                                       |
|                                                          |
|  Results (ranked by similarity):                         |
|  1. {"fact": "User prefers coffee in the morning"}       |
|  2. {"fact": "User drinks tea in the afternoon"}         |
|  3. {"fact": "User avoids sugary drinks"}                |
|                                                          |
+----------------------------------------------------------+
```

**How It Works**:
1. Store is configured with an embedding function
2. When you `.put()` a memory, it gets embedded
3. When you `.search()`, the query is embedded and compared

**Reflection Question**: When would you use `store.get()` (exact key lookup) versus `store.search()` (semantic search)?

---

# Memory Types: A Conceptual Framework

The LangChain documentation identifies three memory types, aligning with cognitive science concepts:

| Memory Type | Human Analogy | Agent Implementation |
|-------------|---------------|----------------------|
| **Semantic** | Facts and knowledge | Store with extracted facts |
| **Episodic** | Specific experiences | Message history, event logs |
| **Procedural** | How to do things | System prompts, refined instructions |

**Semantic Memory**: "User's name is Alice" - factual knowledge
**Episodic Memory**: "On Tuesday, user asked about weather" - specific events
**Procedural Memory**: "Always respond formally to this user" - learned behaviors

**Reflection Question**: How might an agent update its procedural memory based on user feedback?

---

# Putting It Together

Here's a mental model for designing agent memory:

**Step 1: Identify Memory Requirements**
- What must persist within a conversation? (checkpointer)
- What must persist across conversations? (store)

**Step 2: Choose Write Strategy**
- Is immediate availability critical? (hot path)
- Can memory formation be delayed? (background)

**Step 3: Design Namespace Structure**
- How will you organize long-term memories?
- What scopes make sense? (user, project, organization)

**Step 4: Plan for Search**
- Will you need semantic search?
- Configure embedding function accordingly

---

## Assignment

**Build an agent that leverages both short-term and long-term memory systems.**

### Requirements

1. **Short-term memory**: Agent maintains conversation context using a checkpointer
2. **Long-term memory**: Agent stores and retrieves user preferences across sessions
3. **Memory writing**: Implement at least one method (hot path or background)
4. **Demonstration**: Show the agent remembering information across different thread IDs

### Guiding Questions

- How do you decide what belongs in short-term vs. long-term memory?
- What namespace structure makes sense for your use case?
- How do you handle the case where a memory doesn't exist yet?

### Evaluation Criteria

- Proper separation between checkpointer and store responsibilities
- Effective use of thread_id for conversation isolation
- Meaningful namespace organization for long-term memories
- Clear demonstration of memory persistence

---

## Advanced Build

**Memory-Enhanced Personal Assistant**

Build a personal assistant that:
- Learns user preferences over time (communication style, topics of interest)
- Remembers facts about the user's life (name, job, family)
- Adapts its responses based on accumulated knowledge
- Uses semantic search to find relevant memories

**Bonus Challenges**:
- Implement procedural memory that refines the system prompt based on feedback
- Add memory expiration for time-sensitive information
- Build a memory management interface where users can view/edit their stored data

Reference: [Memory Agent Template](https://github.com/langchain-ai/memory-agent)

---

## Key Takeaways

1. **Memory is foundational** for production agents - without it, every conversation starts fresh

2. **Short-term memory** (checkpointers) handles thread-scoped conversation state; **long-term memory** (stores) persists knowledge across sessions

3. **Thread IDs** are the key to short-term memory - same ID continues the conversation, new ID starts fresh

4. **Namespaces** organize long-term memory hierarchically, enabling structured access and semantic search

5. **Hot path** memory writing provides immediate availability but adds latency; **background** writing eliminates latency but delays availability

6. **Combine both** patterns in production: checkpointer for conversation continuity, store for persistent knowledge

---

*Session 6 | Complex Agents Module | Week 3*
