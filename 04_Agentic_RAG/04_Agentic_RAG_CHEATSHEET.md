# Session 4 Cheatsheet: Agentic RAG

> Low-Level Orchestration with LangGraph

---

## Quick Reference

| Concept | Definition | Key API/Pattern |
|---------|------------|-----------------|
| LangGraph | Low-level orchestration framework | `StateGraph` |
| State | Shared data structure for workflow | `TypedDict` |
| Node | Function that processes state | `builder.add_node()` |
| Edge | Transition between nodes | `builder.add_edge()` |
| Conditional Edge | Routing based on state | `builder.add_conditional_edges()` |
| Checkpointer | Persistence layer | `InMemorySaver` |
| Reducer | Merge strategy for state updates | `Annotated[list, add_messages]` |
| Thread | Conversation/session identifier | `{"configurable": {"thread_id": ...}}` |

---

## Setup Requirements

### Dependencies
```bash
pip install langgraph>=1.0.0 langchain>=1.0.0 langchain-openai langsmith
```

### Environment Variables
```python
import os
os.environ["OPENAI_API_KEY"] = "your-key"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-langsmith-key"
os.environ["LANGCHAIN_PROJECT"] = "AIE9-Session4"
```

---

## 1. LangGraph Overview

### What is LangGraph?
> **"LangGraph is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents."**
> — LangGraph Documentation [[1]](https://docs.langchain.com/oss/python/langgraph/overview)

### LangChain vs LangGraph
| Level | Use Case | Control |
|-------|----------|---------|
| `create_agent` | Quick prototyping | High-level |
| LangGraph | Custom orchestration | Low-level |

### Key Insight
> "LangChain's `create_agent` runs on LangGraph. Use LangChain for a fast start; drop to LangGraph for custom orchestration."
> — LangGraph v1 Release [[2]](https://docs.langchain.com/oss/python/releases/langgraph-v1)

**Official Docs**: [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview) [[1]](https://docs.langchain.com/oss/python/langgraph/overview)

---

## 2. The Three Pillars

### Architecture Diagram
```
┌────────────────────────────────────────────────────────────┐
│                       LANGGRAPH                             │
│                                                             │
│   ┌─────────┐     ┌─────────┐     ┌─────────┐              │
│   │  STATE  │ --> │  NODES  │ --> │  EDGES  │              │
│   │ (data)  │     │ (logic) │     │(routing)│              │
│   └─────────┘     └─────────┘     └─────────┘              │
│        │               │               │                    │
│        v               v               v                    │
│   TypedDict       Functions      Conditional                │
│   + Reducers      + Side effects  + Fixed                  │
└────────────────────────────────────────────────────────────┘
```

### Summary
- **State**: Shared data snapshot
- **Nodes**: Processing functions
- **Edges**: Control flow decisions

> "Nodes do the work, edges tell what to do next."
> — Graph API Overview [[3]](https://docs.langchain.com/oss/python/langgraph/graph-api)

**Official Docs**: [Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api) [[3]](https://docs.langchain.com/oss/python/langgraph/graph-api)

---

## 3. State Definition

### Basic State Schema
```python
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]  # Conversation history
    documents: list                           # Retrieved context
    query: str                                # User question
```

### Understanding Reducers
| Reducer | Behavior | Use Case |
|---------|----------|----------|
| None | Replace value | Simple updates |
| `add_messages` | Append to list | Conversation history |
| Custom | User-defined merge | Complex state |

### How Reducers Work
```python
# Without reducer: Replaces entire value
state["documents"] = new_docs

# With add_messages reducer: Appends
state["messages"] = existing + new_messages
```

### State Update Pattern
```python
def my_node(state: AgentState) -> dict:
    """Return only the fields you want to update."""
    return {"messages": [new_message]}  # Partial update
```

**Official Docs**: [State Schema](https://docs.langchain.com/oss/python/langgraph/state-schema) [[4]](https://docs.langchain.com/oss/python/langgraph/state-schema)

---

## 4. Building Nodes

### Node Function Pattern
```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o")

def call_model(state: AgentState) -> dict:
    """Node that calls the LLM."""
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages": [response]}
```

### Node with Tools
```python
from langchain_core.tools import tool

@tool
def search_docs(query: str) -> str:
    """Search the knowledge base."""
    results = retriever.invoke(query)
    return "\n".join([doc.page_content for doc in results])

# Bind tools to model
model_with_tools = model.bind_tools([search_docs])

def agent_node(state: AgentState) -> dict:
    """Agent node with tool access."""
    response = model_with_tools.invoke(state["messages"])
    return {"messages": [response]}
```

### Tool Execution Node
```python
from langgraph.prebuilt import ToolNode

tools = [search_docs, calculate]
tool_node = ToolNode(tools)
```

**Official Docs**: [ToolNode](https://docs.langchain.com/oss/python/langgraph/prebuilt) [[5]](https://docs.langchain.com/oss/python/langgraph/prebuilt)

---

## 5. Edges and Routing

### Edge Types
| Type | Pattern | Use Case |
|------|---------|----------|
| Fixed | `add_edge(A, B)` | Always A → B |
| Conditional | `add_conditional_edges()` | Route based on state |
| Entry | `add_edge(START, A)` | Graph entry point |
| Exit | `goto=END` | Graph termination |

### Fixed Edges
```python
from langgraph.graph import START, END

builder.add_edge(START, "agent")      # Entry point
builder.add_edge("tools", "agent")    # Tools always go back to agent
```

### Conditional Edges
```python
def should_continue(state: AgentState) -> str:
    """Route based on whether tools were called."""
    last_message = state["messages"][-1]

    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return "end"

builder.add_conditional_edges(
    "agent",                          # Source node
    should_continue,                  # Routing function
    {"tools": "tools", "end": END}   # Mapping
)
```

### Routing Function Pattern
```python
def route_decision(state: AgentState) -> str:
    """
    Routing function must:
    1. Accept state as input
    2. Return a string matching edge map keys
    """
    # Analyze state
    if condition_a:
        return "node_a"
    elif condition_b:
        return "node_b"
    return "default"
```

**Official Docs**: [Conditional Edges](https://docs.langchain.com/oss/python/langgraph/conditional-edges) [[6]](https://docs.langchain.com/oss/python/langgraph/conditional-edges)

---

## 6. Building the Graph

### Complete Graph Pattern
```python
from langgraph.graph import StateGraph, START, END

# 1. Create builder with state schema
builder = StateGraph(AgentState)

# 2. Add nodes
builder.add_node("agent", agent_node)
builder.add_node("tools", tool_node)

# 3. Add edges
builder.add_edge(START, "agent")
builder.add_conditional_edges(
    "agent",
    should_continue,
    {"tools": "tools", "end": END}
)
builder.add_edge("tools", "agent")

# 4. Compile
graph = builder.compile()
```

### Graph Visualization
```python
# Display graph structure (in Jupyter)
from IPython.display import Image, display
display(Image(graph.get_graph().draw_mermaid_png()))
```

### Graph Execution
```python
# Invoke the graph
result = graph.invoke({
    "messages": [{"role": "user", "content": "Hello!"}]
})

# Stream execution
for event in graph.stream({"messages": [...]}):
    print(event)
```

---

## 7. The Command API

### Combined State + Routing
```python
from langgraph.graph import Command
from typing import Literal

def smart_node(state: AgentState) -> Command[Literal["next", "__end__"]]:
    """Return state update AND routing decision."""
    result = process(state)

    if should_continue:
        return Command(
            update={"messages": [result]},
            goto="next"
        )
    return Command(
        update={"messages": [result]},
        goto=END
    )
```

### Benefits of Command
- Single return combines update + routing
- Type hints document valid destinations
- Cleaner than separate routing functions

**Official Docs**: [Command API](https://docs.langchain.com/oss/python/langgraph/use-graph-api) [[7]](https://docs.langchain.com/oss/python/langgraph/use-graph-api)

---

## 8. Checkpointing and Persistence

### Why Checkpointing?
| Capability | Description |
|------------|-------------|
| Multi-turn | Conversations persist across invocations |
| Human-in-the-loop | Pause, inspect, modify, resume |
| Time travel | Replay from any checkpoint |
| Fault tolerance | Recover from failures |

### InMemorySaver (Development)
```python
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)

# Use thread_id for persistence
config = {"configurable": {"thread_id": "user-123"}}
result = graph.invoke({"messages": [...]}, config)
```

### Multi-Turn Conversation
```python
# Turn 1
graph.invoke(
    {"messages": [{"role": "user", "content": "Hi, I'm Alice"}]},
    {"configurable": {"thread_id": "session-1"}}
)

# Turn 2 - Same thread, state persists
graph.invoke(
    {"messages": [{"role": "user", "content": "What's my name?"}]},
    {"configurable": {"thread_id": "session-1"}}
)
# Agent remembers: "Your name is Alice"
```

### Checkpointer Options
| Checkpointer | Use Case |
|--------------|----------|
| `InMemorySaver` | Development, testing |
| `SqliteSaver` | Single-process persistence |
| `PostgresSaver` | Production, multi-process |
| Agent Server | Managed infrastructure |

**Official Docs**: [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) [[8]](https://docs.langchain.com/oss/python/langgraph/persistence)

---

## 9. LangSmith Observability

### Enable Tracing
```python
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-key"
os.environ["LANGCHAIN_PROJECT"] = "my-project"
```

### What Traces Show
```
┌─────────────────────────────────────────────────────────┐
│                    TRACE VIEW                            │
│                                                          │
│  graph.invoke()                                          │
│  ├── agent (node)           [1.2s, 150 tokens]          │
│  │   └── ChatOpenAI.invoke  [1.1s]                      │
│  ├── tools (node)           [0.5s]                      │
│  │   └── search_docs        [0.4s]                      │
│  └── agent (node)           [0.8s, 200 tokens]          │
│      └── ChatOpenAI.invoke  [0.7s]                      │
└─────────────────────────────────────────────────────────┘
```

### Key Metrics
| Metric | Why It Matters |
|--------|----------------|
| Latency | User experience |
| Token count | Cost |
| Node execution order | Debug flow |
| Tool usage | Understand behavior |
| Error rates | Reliability |

### Debugging Tips
1. Check node inputs/outputs in trace
2. Verify routing decisions
3. Inspect state at each step
4. Compare successful vs failed runs

**Official Docs**: [LangSmith Observability](https://docs.langchain.com/langsmith/observability) [[9]](https://docs.langchain.com/langsmith/observability)

---

## 10. Agentic RAG Pattern

### Traditional RAG vs Agentic RAG
```
Traditional:  Query --> Retrieve --> Generate
Agentic:      Query --> (decide) --> [Retrieve?] --> Generate
```

### Agentic RAG Graph
```
┌────────────────────────────────────────────────────────┐
│                   AGENTIC RAG                           │
│                                                         │
│  START --> classify --> (needs context?)                │
│                │                                        │
│                ├──yes──> retrieve --> generate --> END  │
│                │                                        │
│                └──no───> generate --> END               │
└────────────────────────────────────────────────────────┘
```

### Implementation
```python
def classify_query(state: AgentState) -> str:
    """Classify whether retrieval is needed."""
    query = state["messages"][-1].content

    # Simple classification (use LLM in practice)
    if any(word in query.lower() for word in ["what", "how", "explain"]):
        return "retrieve"
    return "generate"

def retrieve_node(state: AgentState) -> dict:
    """Retrieve relevant documents."""
    query = state["messages"][-1].content
    docs = retriever.invoke(query)
    return {"documents": docs}

def generate_node(state: AgentState) -> dict:
    """Generate response with or without context."""
    messages = state["messages"]
    docs = state.get("documents", [])

    if docs:
        context = "\n".join([d.page_content for d in docs])
        messages = messages + [{"role": "system", "content": f"Context: {context}"}]

    response = model.invoke(messages)
    return {"messages": [response]}
```

### Building the RAG Graph
```python
builder = StateGraph(AgentState)

builder.add_node("classify", classify_node)
builder.add_node("retrieve", retrieve_node)
builder.add_node("generate", generate_node)

builder.add_edge(START, "classify")
builder.add_conditional_edges(
    "classify",
    classify_query,
    {"retrieve": "retrieve", "generate": "generate"}
)
builder.add_edge("retrieve", "generate")
builder.add_edge("generate", END)

graph = builder.compile()
```

---

## 11. Thinking in LangGraph

### Design Process
1. **Break into nodes**: What are the discrete steps?
2. **Define transitions**: When do we go from A to B?
3. **Connect via state**: What data flows between steps?

> "When you build an agent with LangGraph, you will first break it apart into discrete steps called nodes."
> — Thinking in LangGraph [[10]](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph)

### Questions to Ask
| Question | Determines |
|----------|-----------|
| What operations are needed? | Nodes |
| What data flows between them? | State schema |
| How do we decide next step? | Edges |
| What conditions change the path? | Conditional routing |
| What needs to persist? | Checkpointing |

### Common Patterns
| Pattern | Structure |
|---------|-----------|
| Simple agent | agent → tools → agent (loop) |
| Agentic RAG | classify → [retrieve] → generate |
| Multi-step | step1 → step2 → step3 → ... |
| Branching | decide → (A or B or C) → merge |

**Official Docs**: [Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph) [[10]](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph)

---

## 12. Code Patterns Reference

### Pattern 1: Basic Agent Graph
```python
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode

builder = StateGraph(AgentState)
builder.add_node("agent", agent_node)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", should_continue)
builder.add_edge("tools", "agent")
graph = builder.compile()
```

### Pattern 2: Graph with Memory
```python
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)

# Invoke with thread
result = graph.invoke(
    {"messages": [...]},
    {"configurable": {"thread_id": "123"}}
)
```

### Pattern 3: Streaming Execution
```python
for event in graph.stream({"messages": [...]}):
    for node_name, node_output in event.items():
        print(f"{node_name}: {node_output}")
```

### Pattern 4: Agentic RAG
```python
class RAGState(TypedDict):
    messages: Annotated[list, add_messages]
    documents: list
    needs_retrieval: bool

def route(state):
    return "retrieve" if state["needs_retrieval"] else "generate"

builder.add_conditional_edges("classify", route)
```

---

## Common Issues & Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| State not updating | Missing reducer | Use `Annotated[list, add_messages]` |
| Graph loops forever | No exit condition | Add conditional edge to END |
| Routing fails | Function returns wrong key | Match routing keys exactly |
| Tracing not working | Env vars not set | Check `LANGCHAIN_TRACING_V2` |
| Memory not persisting | No checkpointer | Add `InMemorySaver()` |
| Wrong thread state | Different thread_id | Use consistent thread_id |

---

## Breakout Room Tasks Summary

### Breakout Room 1 (Tasks 1-5)
- [ ] Install LangGraph dependencies
- [ ] Define a state schema with TypedDict
- [ ] Create a simple node function
- [ ] Build a linear graph (A → B → C)
- [ ] Compile and invoke the graph
- [ ] **Activity**: Add conditional routing

### Breakout Room 2 (Tasks 6-10)
- [ ] Add tools to the agent
- [ ] Implement the tool execution node
- [ ] Create conditional edges for tool routing
- [ ] Enable checkpointing with InMemorySaver
- [ ] Test multi-turn conversation
- [ ] **Activity**: Build Agentic RAG graph

---

## Official Documentation Links

### LangGraph Core
- [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview) [[1]](https://docs.langchain.com/oss/python/langgraph/overview)
- [Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api) [[3]](https://docs.langchain.com/oss/python/langgraph/graph-api)
- [Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph) [[10]](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph)

### State and Nodes
- [State Schema](https://docs.langchain.com/oss/python/langgraph/state-schema) [[4]](https://docs.langchain.com/oss/python/langgraph/state-schema)
- [Prebuilt Components](https://docs.langchain.com/oss/python/langgraph/prebuilt) [[5]](https://docs.langchain.com/oss/python/langgraph/prebuilt)

### Edges and Routing
- [Conditional Edges](https://docs.langchain.com/oss/python/langgraph/conditional-edges) [[6]](https://docs.langchain.com/oss/python/langgraph/conditional-edges)
- [Command API](https://docs.langchain.com/oss/python/langgraph/use-graph-api) [[7]](https://docs.langchain.com/oss/python/langgraph/use-graph-api)

### Persistence
- [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) [[8]](https://docs.langchain.com/oss/python/langgraph/persistence)
- [Add Short-Term Memory](https://docs.langchain.com/oss/python/langgraph/add-memory) [[11]](https://docs.langchain.com/oss/python/langgraph/add-memory)

### Observability
- [LangSmith Observability](https://docs.langchain.com/langsmith/observability) [[9]](https://docs.langchain.com/langsmith/observability)
- [LangSmith Quickstart](https://docs.langchain.com/langsmith/observability-quickstart) [[12]](https://docs.langchain.com/langsmith/observability-quickstart)

### Related
- [LangGraph v1 Release](https://docs.langchain.com/oss/python/releases/langgraph-v1) [[2]](https://docs.langchain.com/oss/python/releases/langgraph-v1)
- [LangChain 1.0 Blog](https://blog.langchain.com/langchain-langgraph-1dot0/) [[13]](https://blog.langchain.com/langchain-langgraph-1dot0/)

---

## References

1. LangChain Documentation. "LangGraph Overview." https://docs.langchain.com/oss/python/langgraph/overview

2. LangChain Documentation. "What's new in LangGraph v1." https://docs.langchain.com/oss/python/releases/langgraph-v1

3. LangChain Documentation. "Graph API overview." https://docs.langchain.com/oss/python/langgraph/graph-api

4. LangChain Documentation. "State Schema." https://docs.langchain.com/oss/python/langgraph/state-schema

5. LangChain Documentation. "Prebuilt Components." https://docs.langchain.com/oss/python/langgraph/prebuilt

6. LangChain Documentation. "Conditional Edges." https://docs.langchain.com/oss/python/langgraph/conditional-edges

7. LangChain Documentation. "Command API." https://docs.langchain.com/oss/python/langgraph/use-graph-api

8. LangChain Documentation. "Persistence." https://docs.langchain.com/oss/python/langgraph/persistence

9. LangSmith Documentation. "Observability." https://docs.langchain.com/langsmith/observability

10. LangChain Documentation. "Thinking in LangGraph." https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph

11. LangChain Documentation. "Add Short-Term Memory." https://docs.langchain.com/oss/python/langgraph/add-memory

12. LangSmith Documentation. "Observability Quickstart." https://docs.langchain.com/langsmith/observability-quickstart

13. LangChain Blog. "LangChain & LangGraph 1.0." October 2025. https://blog.langchain.com/langchain-langgraph-1dot0/

---

*Cheatsheet created for AIE9 Session 4: Agentic RAG*
*Last updated: January 2026*
