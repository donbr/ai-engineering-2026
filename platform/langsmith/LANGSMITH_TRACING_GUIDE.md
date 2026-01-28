# LangSmith Tracing & Telemetry for Multi-Agent Systems

> Understanding how spans are created and what data is captured in the multi-agent wellness application

## Trace Hierarchy Concepts

```
┌─────────────────────────────────────────────────────────────────────┐
│                           TRACE                                     │
│  (One complete request/response cycle with a unique trace_id)       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    ROOT SPAN (Parent Run)                    │   │
│  │  run_type: "chain"                                          │   │
│  │  name: "RunnableSequence" or "supervisor_graph"             │   │
│  └─────────────────────┬───────────────────────────────────────┘   │
│                        │                                            │
│         ┌──────────────┼──────────────┐                            │
│         │              │              │                            │
│         ▼              ▼              ▼                            │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐                      │
│  │ CHILD SPAN │ │ CHILD SPAN │ │ CHILD SPAN │                      │
│  │ run_type:  │ │ run_type:  │ │ run_type:  │                      │
│  │ "chain"    │ │ "llm"      │ │ "tool"     │                      │
│  │ (node)     │ │ (GPT call) │ │ (search)   │                      │
│  └────────────┘ └────────────┘ └────────────┘                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## What's Captured in a Single Span (Run)

### Core Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | UUID | Unique identifier for this span |
| `name` | string | Human-readable label (e.g., "supervisor_node", "ChatOpenAI") |
| `run_type` | enum | One of: `"chain"`, `"llm"`, `"tool"`, `"retriever"`, `"embedding"` |
| `trace_id` | UUID | Links all spans in the same request |
| `parent_run_id` | UUID | Immediate parent span |
| `dotted_order` | string | Hierarchical path (e.g., "1.2.1" for nested position) |

### Execution Data

| Field | Type | Description |
|-------|------|-------------|
| `inputs` | dict | Data provided to this operation |
| `outputs` | dict | Results from this operation |
| `start_time` | datetime | When execution began |
| `end_time` | datetime | When execution completed |
| `status` | string | `"success"`, `"error"`, or `"pending"` |
| `error` | string | Error message if failed |

### LLM-Specific Fields (when `run_type="llm"`)

| Field | Type | Description |
|-------|------|-------------|
| `prompt_tokens` | int | Tokens in the prompt |
| `completion_tokens` | int | Tokens generated |
| `total_tokens` | int | Sum of prompt + completion |
| `total_cost` | float | Estimated cost in USD |
| `first_token_time` | datetime | When streaming began (if applicable) |

### Metadata

| Field | Type | Description |
|-------|------|-------------|
| `tags` | list[str] | Labels for filtering (e.g., ["production", "wellness"]) |
| `metadata` | dict | Custom key-value pairs |
| `extra` | dict | Additional framework-specific data |

---

## Span Creation in the Multi-Agent Application

### Analysis of `multi_agent_applications.py`

Below is a breakdown of which code creates individual spans:

### 1. **Graph Invocation** → Root Chain Span

```python
# Line 484-490
response = supervisor_graph.invoke(
    {"messages": [HumanMessage(content="What exercises can help with lower back pain?")]}
)
```

**Creates:**
- **1 Root Span** (`run_type: "chain"`)
  - `name`: "RunnableSequence" or graph name
  - `inputs`: `{"messages": [HumanMessage(...)]}`
  - `outputs`: Final state with all messages

---

### 2. **Supervisor Node** → Chain + LLM Spans

```python
# Line 364-380 - supervisor_node function
def supervisor_node(state: SupervisorState):
    prompt_value = supervisor_prompt.invoke({"question": user_question})  # Chain span
    result = routing_llm.invoke(prompt_value)  # LLM span (GPT-5.2)
    return {"next": result.next}
```

**Creates:**
- **1 Chain Span** (`run_type: "chain"`)
  - `name`: "supervisor" (node name)
  - `inputs`: Current state
  - `outputs`: `{"next": "exercise"}`

- **1 LLM Span** (`run_type: "llm"`) - nested inside
  - `name`: "ChatOpenAI" (GPT-5.2)
  - `inputs`: Formatted prompt messages
  - `outputs`: `RouterOutput` structured response
  - Token counts and costs

---

### 3. **Specialist Agent Nodes** → Chain + LLM + Tool Spans

```python
# Line 389-408 - create_agent_node wrapper
def agent_node(state: SupervisorState):
    result = agent.invoke({"messages": state["messages"]})  # Triggers multiple spans
    return {"messages": [response_with_name]}
```

Each specialist (exercise, nutrition, sleep, stress) creates:

**Creates:**
- **1 Chain Span** (`run_type: "chain"`)
  - `name`: "exercise" / "nutrition" / "sleep" / "stress"

- **1+ LLM Spans** (`run_type: "llm"`) - nested inside
  - `name`: "ChatOpenAI" (GPT-4o-mini)
  - May have multiple if agent reasons through tool use

- **1+ Tool Spans** (`run_type: "tool"`) - nested inside
  - `name`: "search_exercise_info" / "search_nutrition_info" / etc.
  - `inputs`: Query string
  - `outputs`: Retrieved documents

---

### 4. **RAG Tool Execution** → Tool + Retriever + Embedding Spans

```python
# Line 230-240 - search_exercise_info tool
@tool
def search_exercise_info(query: str) -> str:
    results = retriever.invoke(f"exercise fitness workout {query}")  # Multiple spans
    return "\n\n".join([f"[Source {i+1}]: {doc.page_content}" ...])
```

**Creates:**
- **1 Tool Span** (`run_type: "tool"`)
  - `name`: "search_exercise_info"
  - `inputs`: `{"query": "lower back pain"}`
  - `outputs`: Formatted document string

- **1 Retriever Span** (`run_type: "retriever"`) - nested inside
  - `name`: "QdrantRetriever"
  - `inputs`: Augmented query
  - `outputs`: List of Document objects

- **1 Embedding Span** (`run_type: "embedding"`) - nested inside
  - `name`: "OpenAIEmbeddings"
  - `inputs`: Query text
  - `outputs`: Vector embedding

---

### 5. **Tavily Web Search** → Tool Span

```python
# Line 556-568 - search_web_current tool
@tool
def search_web_current(query: str) -> str:
    response = tavily_search.invoke(query)  # External API call
    return "\n\n".join(formatted)
```

**Creates:**
- **1 Tool Span** (`run_type: "tool"`)
  - `name`: "search_web_current"
  - `inputs`: `{"query": "latest research..."}`
  - `outputs`: Formatted web results

---

## Complete Trace Example: Supervisor Pattern Query

For the query: `"What exercises can help with lower back pain?"`

```
TRACE: abc123-...
│
├─ [chain] supervisor_graph.invoke
│   ├─ inputs: {"messages": [HumanMessage("What exercises...")]}
│   ├─ outputs: {"messages": [...], "next": "exercise"}
│   │
│   ├─ [chain] supervisor_node
│   │   ├─ [llm] ChatOpenAI (GPT-5.2)
│   │   │   ├─ inputs: {"messages": [SystemMessage, HumanMessage]}
│   │   │   ├─ outputs: RouterOutput(next="exercise", reasoning="...")
│   │   │   ├─ tokens: {prompt: 150, completion: 25, total: 175}
│   │   │   └─ cost: $0.0021
│   │   └─ outputs: {"next": "exercise"}
│   │
│   └─ [chain] exercise_node
│       ├─ [chain] create_agent (GPT-4o-mini)
│       │   ├─ [llm] ChatOpenAI
│       │   │   ├─ inputs: {"messages": [...]}
│       │   │   ├─ outputs: ToolCall(search_exercise_info)
│       │   │   └─ tokens: {prompt: 200, completion: 30}
│       │   │
│       │   ├─ [tool] search_exercise_info
│       │   │   ├─ inputs: {"query": "lower back pain"}
│       │   │   ├─ [retriever] QdrantRetriever
│       │   │   │   ├─ [embedding] OpenAIEmbeddings
│       │   │   │   │   └─ inputs: "exercise fitness workout lower back pain"
│       │   │   │   └─ outputs: [Document, Document, Document]
│       │   │   └─ outputs: "[Source 1]: ... [Source 2]: ..."
│       │   │
│       │   └─ [llm] ChatOpenAI (final response)
│       │       ├─ inputs: {"messages": [...with tool results...]}
│       │       └─ outputs: "Based on the wellness guide..."
│       │
│       └─ outputs: {"messages": [AIMessage("[EXERCISE SPECIALIST]...")]}
```

---

## Handoff Pattern: Additional Spans

For the handoff pattern (Task 5), additional spans are created:

```python
# Line 800-836 - create_handoff_node
def node(state: HandoffState):
    result = agent.invoke({"messages": state["messages"]})
    # Check for handoff...
    if "HANDOFF:" in msg.content:
        return {"current_agent": target, "transfer_count": state["transfer_count"] + 1}
```

**Additional Spans per Handoff:**
- **1 Chain Span** per agent visited
- **1+ LLM Spans** per agent (may decide to handoff or respond)
- **Tool Spans** if agents search before handing off

---

## Key Insights for Students

### 1. **Span Granularity**

| Operation | Spans Created |
|-----------|---------------|
| Graph invoke | 1 (root chain) |
| Node execution | 1 chain + nested children |
| LLM call | 1 llm |
| Tool call | 1 tool + nested operations |
| RAG retrieval | 1 retriever + 1 embedding |

### 2. **Cost Attribution**

LangSmith tracks costs at the LLM span level:
- **GPT-5.2** (supervisor): Higher cost per routing decision
- **GPT-4o-mini** (specialists): Lower cost per response
- View aggregated costs per trace or per project

### 3. **Debugging with Spans**

In LangSmith UI, you can:
- **Expand** each span to see inputs/outputs
- **Filter** by `run_type` (e.g., show only `llm` spans)
- **Search** by metadata/tags
- **Compare** traces to identify performance regressions

### 4. **What Creates SEPARATE Traces**

Each of these creates a **new trace** (separate trace_id):
- Each `graph.invoke()` call
- Missing parent context in async code
- Thread pool executor without manual context propagation

---

## Trace Filtering Examples

### Find all LLM calls in a project

```python
from langsmith import Client

client = Client()
llm_runs = client.list_runs(
    project_name="AIE9 - Multi-Agent Applications",
    run_type="llm",
    select=["name", "total_tokens", "total_cost"]
)
```

### Find expensive traces

```python
expensive_runs = client.list_runs(
    project_name="AIE9 - Multi-Agent Applications",
    filter='gt(total_cost, 0.01)',  # > $0.01
)
```

### Find traces with handoffs

```python
handoff_traces = client.list_runs(
    project_name="AIE9 - Multi-Agent Applications",
    filter='has(outputs, "HANDOFF")',
)
```

---

## Resources

- [LangSmith Run Data Format](https://docs.langchain.com/langsmith/run-data-format)
- [Trace with LangGraph](https://docs.langchain.com/langsmith/trace-with-langgraph)
- [Observability Concepts](https://docs.langchain.com/langsmith/observability-concepts)
- [Troubleshoot Trace Nesting](https://docs.langchain.com/langsmith/nest-traces)

---

## Understanding Trace Architecture

### Key Insight: Separate Traces Are BY DESIGN

When you observe multiple traces in LangSmith, this is **not necessarily a problem**—it's often the **intended architecture**.

### Terminology Clarification

| Term | Definition | Scope |
|------|------------|-------|
| **Run (Span)** | A single unit of work (LLM call, tool call, node execution) | Within a trace |
| **Trace** | One complete input→output cycle (one `graph.invoke()` call) | Single request |
| **Thread** | A sequence of related traces (multi-turn conversation) | Across multiple requests |

### The Designed Behavior

```
┌─────────────────────────────────────────────────────────────────────┐
│                         THREAD (Conversation)                       │
│                    thread_id: "wellness-session-1"                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐     │
│  │   TRACE #1      │  │   TRACE #2      │  │   TRACE #3      │     │
│  │  (Turn 1)       │  │  (Turn 2)       │  │  (Turn 3)       │     │
│  │                 │  │                 │  │                 │     │
│  │ graph.invoke()  │  │ graph.invoke()  │  │ graph.invoke()  │     │
│  │      │          │  │      │          │  │      │          │     │
│  │ ┌────┴────┐     │  │ ┌────┴────┐     │  │ ┌────┴────┐     │     │
│  │ │supervisor│    │  │ │supervisor│    │  │ │supervisor│    │     │
│  │ └────┬────┘     │  │ └────┬────┘     │  │ └────┬────┘     │     │
│  │      │          │  │      │          │  │      │          │     │
│  │ ┌────┴────┐     │  │ ┌────┴────┐     │  │ ┌────┴────┐     │     │
│  │ │exercise │     │  │ │nutrition│     │  │ │  sleep  │     │     │
│  │ │  agent  │     │  │ │  agent  │     │  │ │  agent  │     │     │
│  │ └─────────┘     │  │ └─────────┘     │  │ └─────────┘     │     │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

Each TRACE is separate (different trace_id).
All TRACES share the same thread_id → grouped in Thread view.
```

### What Creates ONE Trace

Each `graph.invoke()` call creates ONE trace containing:
- Root run (the graph execution)
- Nested child runs (nodes, LLM calls, tools)

```python
# This creates ONE trace with nested runs
response = supervisor_graph.invoke(
    {"messages": [HumanMessage(content="What exercises help?")]}
)
```

### What Creates SEPARATE Traces (By Design)

Multiple `graph.invoke()` calls = Multiple traces:

```python
# Trace #1
response1 = supervisor_with_memory.invoke(
    {"messages": [HumanMessage(content="Morning routine?")]},
    config={"configurable": {"thread_id": "session-1"}}
)

# Trace #2 (separate, but same thread)
response2 = supervisor_with_memory.invoke(
    {"messages": [HumanMessage(content="What about diet?")]},
    config={"configurable": {"thread_id": "session-1"}}  # Same thread_id
)
```

---

## When Runs Become Orphaned (Actual Issue)

There IS a distinction between:
1. **Expected separate traces** (multiple invokes) - BY DESIGN
2. **Orphaned runs within a single invoke** - Context propagation issue

Orphaned runs happen when context propagation fails:

### Cause 1: Asyncio in Python < 3.11

```python
# Python < 3.11 doesn't propagate contextvars in asyncio.create_task()
nest_asyncio.apply()  # May interfere with context propagation
```

### Cause 2: ThreadPoolExecutor / Parallel Execution

```python
# contextvars start EMPTY in new threads
from concurrent.futures import ThreadPoolExecutor

# BAD: Loses trace context
with ThreadPoolExecutor() as executor:
    executor.map(some_function, items)
```

### Cause 3: Callback Manager Not Inherited

When invoking an agent inside a node without passing config:

```python
# May not inherit the parent's callbacks
result = agent.invoke({"messages": state["messages"]})
```

---

## What Students Will See in LangSmith

### Expected (Unified Trace)
```
Trace abc123
├── supervisor_graph.invoke
│   ├── supervisor_node
│   │   └── ChatOpenAI (GPT-5.2)
│   └── exercise_node
│       ├── create_agent
│       │   ├── ChatOpenAI (GPT-4o-mini)
│       │   └── search_exercise_info
│       └── response
```

### Actual (Split Traces - The Problem)
```
Trace abc123 (Graph)
└── supervisor_graph.invoke
    └── supervisor_node

Trace def456 (Orphaned LLM Call)
└── ChatOpenAI (GPT-5.2)

Trace ghi789 (Orphaned Agent)
└── create_agent
    ├── ChatOpenAI (GPT-4o-mini)
    └── search_exercise_info
```

---

## Solutions for Orphaned Runs

### Fix 1: Pass Config Explicitly

```python
from langchain_core.runnables import RunnableConfig

def agent_node(state: SupervisorState, config: RunnableConfig):
    # Explicitly pass config to preserve tracing context
    result = agent.invoke({"messages": state["messages"]}, config=config)
    return {"messages": [response_with_name]}
```

### Fix 2: Use `@traceable` with Parent Context

```python
from langsmith import traceable
from langsmith.run_helpers import get_current_run_tree

@traceable
def agent_node(state: SupervisorState):
    run_tree = get_current_run_tree()
    result = agent.invoke(
        {"messages": state["messages"]},
        langsmith_extra={"parent": run_tree}
    )
    return {"messages": [response_with_name]}
```

### Fix 3: Use ContextThreadPoolExecutor

```python
from langsmith.run_helpers import ContextThreadPoolExecutor

with ContextThreadPoolExecutor() as executor:
    executor.map(some_function, items)  # Context propagates
```

---

## Diagnostic: Reasoning About Trace Patterns

### Decision Tree

```
Observing multiple traces in LangSmith?
           │
           ▼
Did you call graph.invoke() multiple times?
           │
    ┌──────┴──────┐
    │ YES         │ NO
    │             │
    ▼             ▼
EXPECTED!     Did ONE invoke produce
Use thread_id  multiple root traces?
to group them        │
              ┌──────┴──────┐
              │ YES         │ NO
              │             │
              ▼             ▼
         ISSUE:        Everything
         Orphaned      is working
         runs          correctly!
         (context
         propagation
         failure)
```

### Quick Reference

| Scenario | Expected Traces | Root Runs per Trace |
|----------|-----------------|---------------------|
| Single question | 1 | 1 (graph.invoke) |
| Multi-turn (2 turns) | 2 | 1 each |
| Single with orphan bug | 2+ | Multiple (problem!) |

### Diagnostic Code

```python
from langsmith import Client
from datetime import datetime, timedelta

client = Client()

# Get all traces in a time window
traces = list(client.list_runs(
    project_name="AIE9 - Multi-Agent Applications",
    is_root=True,  # Only root traces
    start_time=datetime.now() - timedelta(minutes=5),
))

print(f"Root traces in last 5 minutes: {len(traces)}")

# If you invoked the graph once but see multiple root traces, you have split traces
for trace in traces:
    print(f"  - {trace.name}: {trace.id}")
