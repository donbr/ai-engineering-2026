# Session 4: Agentic RAG

**Goal**: Look under the hood of agentic RAG and the `create_agent` abstraction

**Learning Outcomes**
- Learn the core constructs of low-level orchestration using LangGraph
- Understand how to set up tracing, view traces, and monitor performance
- Build agents as explicit graphs with full control over state and flow

**New Tools**
- Orchestration: [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)
- Monitoring: [LangSmith Observability](https://docs.langchain.com/langsmith/observability)

## Required Tooling & Account Setup

In addition to the tools we've already learned, in this session you'll need:

1. LangGraph installed: `pip install langgraph>=1.0.0`
2. LangSmith account (created in Session 3)
3. Tracing enabled via environment variables

## Recommended Reading

1. [LangGraph 1.0](https://blog.langchain.com/langchain-langgraph-1dot0/) Release Blog (Oct 2025)
2. [Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph), by LangGraph
3. Additional LangGraph documentation:
   - [Graph API Overview](https://docs.langchain.com/oss/python/langgraph/graph-api)
   - [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
   - [Add Short-Term Memory](https://docs.langchain.com/oss/python/langgraph/add-memory)

# Overview

In Session 3, we learned what an agent is and built one using `create_agent`. But what happens under the hood? How does `create_agent` actually implement the agent loop?

The answer is **LangGraph**.

> "LangGraph is a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents." ~ [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview)

LangGraph gives you explicit control over:
- **State**: What information flows through your agent
- **Nodes**: The discrete steps your agent takes
- **Edges**: How decisions route between steps
- **Persistence**: How state is saved and restored

This session takes you from using high-level abstractions to understanding and building the low-level machinery.

# Why LangGraph?

LangChain's `create_agent` is convenient, but sometimes you need more control:

| Scenario | create_agent | LangGraph |
|----------|--------------|-----------|
| Simple tool-calling agent | Best choice | Overkill |
| Custom state management | Limited | Full control |
| Complex routing logic | Basic | Any pattern |
| Multi-step workflows | Possible | Native support |
| Human-in-the-loop | Middleware | Built-in |
| Debugging complex flows | Harder | Visual graph |

> "LangChain's `create_agent` runs on LangGraph. Use LangChain for a fast start; drop to LangGraph for custom orchestration." ~ [LangGraph v1 Release](https://docs.langchain.com/oss/python/releases/langgraph-v1)

# The Three Pillars of LangGraph

At its core, LangGraph models agent workflows as graphs with three key components:

## 1. State

A shared data structure representing the current snapshot of your application.

```python
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages: Annotated[list, add_messages]
    context: str
    iteration_count: int
```

State is typically defined using `TypedDict` with optional reducers (like `add_messages`) that control how updates are merged.

## 2. Nodes

Functions that encode the logic of your agents. They receive the current state as input and return an updated state.

```python
def call_model(state: State) -> State:
    """Call the LLM with current messages."""
    response = model.invoke(state["messages"])
    return {"messages": [response]}
```

> "Nodes do the work, edges tell what to do next." ~ [Graph API Overview](https://docs.langchain.com/oss/python/langgraph/graph-api)

## 3. Edges

Functions that determine which node to execute next based on the current state.

```python
def should_continue(state: State) -> str:
    """Decide whether to continue or stop."""
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tools"
    return "end"
```

Edges can be:
- **Fixed**: Always go from A to B
- **Conditional**: Route based on state

# Building a Graph

The basic pattern for building a LangGraph agent:

```python
from langgraph.graph import StateGraph, START, END

# 1. Define the graph with state schema
builder = StateGraph(State)

# 2. Add nodes
builder.add_node("agent", call_model)
builder.add_node("tools", call_tools)

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

This creates an explicit representation of the agent loop that Session 3 introduced:

```
START --> agent --> (decision) --> tools --> agent --> ... --> END
                          |
                          +--> END
```

# State Management Deep Dive

## TypedDict Schemas

State schemas define what data flows through your graph:

```python
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]  # Conversation history
    documents: list[Document]                 # Retrieved context
    query: str                                # User question
```

## Reducers

Reducers control how node outputs merge with existing state. The `add_messages` reducer appends new messages rather than replacing:

```python
# Without reducer: state["messages"] = new_messages  (replaces)
# With add_messages: state["messages"].extend(new_messages)  (appends)
```

## Accessing State in Nodes

Every node receives the full state and returns partial updates:

```python
def retrieve_documents(state: AgentState) -> dict:
    """Retrieve relevant documents for the query."""
    query = state["query"]
    docs = retriever.invoke(query)
    return {"documents": docs}  # Only return what changed
```

# Conditional Routing

The power of LangGraph comes from conditional edges. You define routing logic explicitly:

```python
def route_agent(state: AgentState) -> str:
    """Route based on whether tools were called."""
    last_message = state["messages"][-1]

    # If the LLM made tool calls, route to tools node
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"

    # Otherwise, we're done
    return END

# Add conditional edge
builder.add_conditional_edges(
    "agent",
    route_agent,
    {"tools": "tools", END: END}
)
```

## Using Command for Combined State + Routing

LangGraph also supports returning `Command` objects that combine state updates with routing decisions:

```python
from langgraph.graph import Command
from typing import Literal

def agent_node(state: State) -> Command[Literal["tools", "__end__"]]:
    """Agent that returns both state update and routing decision."""
    response = model.invoke(state["messages"])

    if response.tool_calls:
        return Command(
            update={"messages": [response]},
            goto="tools"
        )
    return Command(
        update={"messages": [response]},
        goto=END
    )
```

# Persistence and Checkpointing

LangGraph has a built-in persistence layer through checkpointers:

```python
from langgraph.checkpoint.memory import InMemorySaver

# Create checkpointer
checkpointer = InMemorySaver()

# Compile graph with checkpointer
graph = builder.compile(checkpointer=checkpointer)

# Invoke with thread_id for persistence
config = {"configurable": {"thread_id": "user-123"}}
result = graph.invoke({"messages": [...]}, config)
```

Checkpointing enables:
- **Multi-turn conversations**: State persists across invocations
- **Human-in-the-loop**: Pause, inspect, modify, resume
- **Time travel**: Replay from any checkpoint
- **Fault tolerance**: Recover from failures

> "Checkpoints are saved to a thread, which can be accessed after graph execution." ~ [LangGraph Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)

# LangSmith Observability

LangSmith provides visibility into what your graph is doing:

## Setting Up Tracing

```python
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-key"
os.environ["LANGCHAIN_PROJECT"] = "AIE9-Session4"
```

With tracing enabled, every graph invocation creates a trace showing:
- Each node execution
- State at each step
- LLM calls and responses
- Tool calls and results
- Timing information
- Token counts

## What to Monitor

| Metric | Why It Matters |
|--------|----------------|
| **Latency** | User experience, cost |
| **Token Count** | Cost, context limits |
| **Node Execution Order** | Debugging flow |
| **Tool Usage** | Understanding behavior |
| **Error Rates** | Reliability |

## Viewing Traces

In LangSmith, you can:
1. See the full execution graph
2. Drill into individual nodes
3. View inputs and outputs at each step
4. Compare traces across invocations
5. Identify bottlenecks and failures

# Agentic RAG as a Graph

Now we can implement the agentic RAG pattern explicitly as a graph:

```
START --> classify_query --> (needs_retrieval?)
                |
                +--> retrieve --> generate --> END
                |
                +--> generate --> END
```

The key insight: **retrieval is a conditional step**, not a fixed one. The agent decides whether to retrieve based on the query.

```python
def classify_query(state: AgentState) -> str:
    """Classify whether the query needs retrieval."""
    query = state["messages"][-1].content

    # Use LLM to classify
    classification = classifier.invoke(query)

    if classification == "needs_context":
        return "retrieve"
    return "generate"
```

This gives you explicit control over when retrieval happens, what gets retrieved, and how results are processed.

# Thinking in LangGraph

The mental model for building with LangGraph:

1. **Break the problem into discrete steps (nodes)**
   - What are the distinct operations?
   - What does each step need as input?
   - What does each step produce?

2. **Describe decisions and transitions (edges)**
   - When should we go from A to B?
   - What conditions determine the path?
   - Where are the loops?

3. **Connect through shared state**
   - What information needs to flow between steps?
   - How should updates be merged?
   - What needs to persist?

> "When you build an agent with LangGraph, you will first break it apart into discrete steps called nodes. Then, you will describe the different decisions and transitions from each of your nodes. Finally, you connect nodes together through a shared state that each node can read from and write to." ~ [Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph)

# Key Takeaways

1. **LangGraph is what powers `create_agent`** - understanding it gives you control
2. **Three pillars: State, Nodes, Edges** - the building blocks of any graph
3. **State schemas define data flow** - use TypedDict with optional reducers
4. **Conditional edges enable routing** - the agent decides what to do next
5. **Checkpointing enables persistence** - multi-turn, human-in-the-loop, recovery
6. **LangSmith shows execution** - trace, debug, monitor your graphs
7. **Agentic RAG as explicit graph** - retrieval as conditional routing

# From create_agent to LangGraph

The relationship between LangChain and LangGraph:

| Level | Use Case | Control |
|-------|----------|---------|
| `create_agent` | Quick start, standard patterns | High-level |
| LangGraph | Custom orchestration, complex flows | Low-level |

Start with `create_agent` for simple use cases. Drop to LangGraph when you need:
- Custom state beyond messages
- Complex routing logic
- Multiple workflows
- Fine-grained control

---

Do you have any questions about how to best prepare for Session 4 after reading? Please don't hesitate to provide direct feedback to `greg@aimakerspace.io` or `Dr Greg` on Discord!
