# Session 3 Cheatsheet: The Agent Loop

> Building Production Agents with LangChain 1.0

---

## Quick Reference

| Concept | Definition | Key API/Pattern |
|---------|------------|-----------------|
| Agent | LLM that runs tools in a loop to achieve a goal | `create_agent()` |
| Agent Loop | Model Call → Tool Execution → Repeat | Two-step cycle |
| Runnable | Core abstraction - input → operation → output | `.invoke()`, `.batch()`, `.stream()` |
| LCEL | LangChain Expression Language | `|` (pipe operator) |
| Tool | Function an agent can call | `@tool` decorator |
| Middleware | Hooks into agent execution | `before_model`, `after_model` |
| Agentic RAG | Agent decides when to retrieve | RAG as a tool |

---

## Setup Requirements

### Dependencies
```bash
pip install langchain>=1.0.0 langchain-openai langsmith qdrant-client langchain-qdrant
```

### Environment Variables
```python
import os
os.environ["OPENAI_API_KEY"] = "your-key"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-langsmith-key"
os.environ["LANGCHAIN_PROJECT"] = "AIE9-Session3"
```

---

## 1. What is an Agent?

### Industry Definition
> **"An LLM agent runs tools in a loop to achieve a goal."**
> — Simon Willison [[1]](https://simonwillison.net/2025/Sep/18/agents/)

### Key Characteristics
- **Reason** about what to do next
- **Take actions** by calling tools
- **Observe** the results
- **Iterate** until the task is complete

### Agent vs. Chain
| Chain | Agent |
|-------|-------|
| Fixed sequence | Dynamic decisions |
| Predetermined flow | LLM decides next step |
| No tool selection | Chooses which tools to use |

**Official Docs**: [LangChain Agents](https://docs.langchain.com/oss/python/langchain/agents) [[2]](https://docs.langchain.com/oss/python/langchain/agents)

---

## 2. The Agent Loop

```
┌─────────────────────────────────────────────────────────┐
│                     AGENT LOOP                          │
│                                                         │
│   ┌──────────┐     ┌──────────┐     ┌──────────┐       │
│   │  Model   │ --> │   Tool   │ --> │  Model   │ --> …│
│   │   Call   │     │   Call   │     │   Call   │       │
│   └──────────┘     └──────────┘     └──────────┘       │
│        │                                  │             │
│        v                                  v             │
│   "Use search"                   "Here's the answer"   │
└─────────────────────────────────────────────────────────┘
```

### Two Main Steps
1. **Model Call**: LLM receives current state, decides to:
   - Call a tool (continue loop)
   - Return final answer (exit loop)

2. **Tool Execution**: Tool runs, output added to conversation

3. **Repeat**: Until model has enough info to answer

**Official Docs**: [Agent Loop Architecture](https://docs.langchain.com/oss/python/langchain/agents) [[2]](https://docs.langchain.com/oss/python/langchain/agents)

---

## 3. The Runnable Abstraction

> **"The primary abstraction in the LangChain ecosystem is the Runnable."**

### Universal Interface
Every Runnable follows the same pattern:
- Takes an input
- Performs some operation
- Returns an output

### Core Methods
```python
# Single input
result = runnable.invoke(input)

# Multiple inputs (parallel)
results = runnable.batch([input1, input2, input3])

# Streaming
for chunk in runnable.stream(input):
    print(chunk)

# Async versions
await runnable.ainvoke(input)
await runnable.abatch([input1, input2])
```

### Common Runnable Types
- **Language Models**: `ChatOpenAI`, `ChatAnthropic`
- **Prompt Templates**: `ChatPromptTemplate`
- **Retrievers**: Vector store retrievers
- **Output Parsers**: `StrOutputParser`, `JsonOutputParser`
- **Chains**: Composed Runnables

**Official Docs**: [Runnables Concepts](https://python.langchain.com/docs/concepts/runnables/) [[3]](https://python.langchain.com/docs/concepts/runnables/)

---

## 4. LCEL (LangChain Expression Language)

### The Pipe Operator
LCEL uses `|` to chain Runnables together (like Unix pipes):

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Create components
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}")
])
model = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()

# Chain with LCEL
chain = prompt | model | parser

# Invoke
result = chain.invoke({"question": "What is AI?"})
```

### RAG Chain Example
```python
from langchain_core.runnables import RunnablePassthrough

rag_chain = (
    {"context": retriever, "query": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)
```

**Official Docs**: [LangChain Philosophy](https://docs.langchain.com/oss/python/langchain/philosophy) [[4]](https://docs.langchain.com/oss/python/langchain/philosophy)

---

## 5. ReAct Pattern

### Reasoning + Acting
The **ReAct** (Reasoning and Acting) pattern combines:
- **Chain-of-thought prompting** (reasoning)
- **Action plan generation** (acting)

### From the Original Paper
> "Reasoning traces help the model induce, track and update action plans as well as handle exceptions, while actions allow it to interface with and gather additional information from external sources."
> — Yao et al., 2022 [[5]](https://arxiv.org/abs/2210.03629)

### ReAct in Practice
```
Thought: I need to search for current weather
Action: search_weather("San Francisco")
Observation: 65°F, sunny
Thought: I have the information needed
Action: respond("The weather in SF is 65°F and sunny")
```

**Paper**: [ReAct: Synergizing Reasoning and Acting](https://arxiv.org/abs/2210.03629) [[5]](https://arxiv.org/abs/2210.03629)

---

## 6. Tool Calling

### The `@tool` Decorator
```python
from langchain_core.tools import tool

@tool
def calculate(expression: str) -> str:
    """Evaluate a mathematical expression.

    Args:
        expression: A mathematical expression (e.g., '2 + 2', '10 * 5')
    """
    result = eval(expression, {"__builtins__": {}}, {})
    return f"Result: {result}"

@tool
def get_current_time() -> str:
    """Get the current date and time."""
    from datetime import datetime
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
```

### Why Docstrings Matter
The **docstring IS the tool description** that the LLM sees when deciding which tool to use. Write clear, detailed docstrings that explain:
- What the tool does
- When to use it
- What arguments it accepts

### Tool Structure
```python
@tool
def tool_name(arg1: type, arg2: type = default) -> return_type:
    """One-line description.

    Detailed explanation of when and how to use this tool.

    Args:
        arg1: Description of first argument
        arg2: Description of second argument (optional)

    Returns:
        Description of what is returned
    """
    # Implementation
    return result
```

**Official Docs**: [LangChain Tools](https://docs.langchain.com/oss/python/langchain/tools) [[6]](https://docs.langchain.com/oss/python/langchain/tools)

---

## 7. The `create_agent()` API

### Basic Usage
```python
from langchain.agents import create_agent

agent = create_agent(
    model="gpt-4o",           # Model name or instance
    tools=[tool1, tool2],      # List of tools
    system_prompt="You are a helpful assistant."  # Optional
)

# Invoke the agent
response = agent.invoke({
    "messages": [{"role": "user", "content": "What is 25 * 48?"}]
})

print(response["messages"][-1].content)
```

### Parameters
| Parameter | Type | Description |
|-----------|------|-------------|
| `model` | `str` or `BaseChatModel` | LLM to use |
| `tools` | `List[Tool]` | Available tools |
| `system_prompt` | `str` | System instructions |
| `middleware` | `List[Middleware]` | Execution hooks |

### Streaming Responses
```python
for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "Calculate 15% of 250"}]},
    stream_mode="updates"
):
    for node, values in chunk.items():
        if "messages" in values:
            for msg in values["messages"]:
                print(msg.content)
```

**Official Docs**: [create_agent Reference](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent) [[7]](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent)

---

## 8. Middleware

### What is Middleware?
Middleware hooks into the agent loop at specific points for:
- **Logging**: Track agent behavior
- **Guardrails**: Filter/modify inputs/outputs
- **Rate limiting**: Control API usage
- **Human-in-the-loop**: Pause for approval

### Middleware Architecture
```
┌────────────────────────────────────────────────────┐
│                 MIDDLEWARE HOOKS                    │
│                                                     │
│  ┌──────────────┐              ┌──────────────┐    │
│  │ before_model │ --> MODEL --> │ after_model  │   │
│  └──────────────┘              └──────────────┘    │
│                                                     │
│  ┌───────────────────────────────────────────┐     │
│  │           wrap_model_call                  │    │
│  │     (intercept and modify calls)           │    │
│  └───────────────────────────────────────────┘     │
└────────────────────────────────────────────────────┘
```

### Node-Style Hooks
```python
from langchain.agents.middleware import before_model, after_model

@before_model
def log_before(state, runtime):
    """Called before each model invocation."""
    print(f"Messages: {len(state.get('messages', []))}")
    return None  # Continue without modification

@after_model
def log_after(state, runtime):
    """Called after each model invocation."""
    last_msg = state.get("messages", [])[-1]
    has_tools = hasattr(last_msg, 'tool_calls') and last_msg.tool_calls
    print(f"Tool calls: {has_tools}")
    return None
```

### Built-in Middleware
```python
from langchain.agents.middleware import ModelCallLimitMiddleware

# Prevent runaway agents
call_limiter = ModelCallLimitMiddleware(
    thread_limit=10,    # Max calls per conversation
    run_limit=5,        # Max calls per single run
    exit_behavior="end"
)

agent = create_agent(
    model="gpt-4o",
    tools=tools,
    middleware=[log_before, log_after, call_limiter]
)
```

**Official Docs**: [Middleware Overview](https://docs.langchain.com/oss/python/langchain/middleware/overview) [[8]](https://docs.langchain.com/oss/python/langchain/middleware/overview)

**Custom Middleware**: [Custom Middleware Guide](https://docs.langchain.com/oss/python/langchain/middleware/custom) [[9]](https://docs.langchain.com/oss/python/langchain/middleware/custom)

---

## 9. Traditional RAG vs. Agentic RAG

### Traditional RAG
```
Query → Retrieve → Augment → Generate
```
- Fixed sequence
- Always retrieves
- No decision-making

### Agentic RAG
```
Query → Agent Decides → (Maybe Retrieve) → Generate
```
- Agent controls retrieval
- Can skip retrieval if not needed
- Can retrieve multiple times
- Can use other tools too

### Implementing Agentic RAG
```python
@tool
def search_knowledge_base(query: str) -> str:
    """Search the knowledge base for relevant information.

    Use when the user asks about topics in our documentation.

    Args:
        query: The search query
    """
    results = retriever.invoke(query)
    return "\n".join([doc.page_content for doc in results])

# Agent decides when to use RAG
agent = create_agent(
    model="gpt-4o",
    tools=[search_knowledge_base, calculate, get_time],
    system_prompt="Search the knowledge base for domain questions."
)
```

**Official Docs**: [Retrieval Documentation](https://docs.langchain.com/oss/python/langchain/retrieval) [[10]](https://docs.langchain.com/oss/python/langchain/retrieval)

---

## 10. Qdrant Vector Database

### Key Concepts
| Concept | Description |
|---------|-------------|
| **Collection** | Namespace for vectors (like a table) |
| **Points** | Individual vectors with payloads |
| **Distance** | Similarity metric (cosine, dot, euclidean) |

### Setup
```python
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

# Initialize
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
qdrant_client = QdrantClient(":memory:")  # or URL for production

# Create collection
qdrant_client.create_collection(
    collection_name="my_collection",
    vectors_config=VectorParams(
        size=1536,  # OpenAI embedding dimension
        distance=Distance.COSINE
    )
)

# Create vector store
vector_store = QdrantVectorStore(
    client=qdrant_client,
    collection_name="my_collection",
    embedding=embedding_model
)

# Add documents
vector_store.add_documents(documents)

# Create retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 3})
```

**Official Docs**: [Vector Stores](https://docs.langchain.com/oss/python/integrations/vectorstores/index) [[11]](https://docs.langchain.com/oss/python/integrations/vectorstores/index)

**Qdrant Docs**: [Qdrant Documentation](https://qdrant.tech/documentation/) [[12]](https://qdrant.tech/documentation/)

---

## 11. LangSmith Observability

### What is LangSmith?
> "LangSmith provides tools for developing, debugging, and deploying LLM applications."

### Key Concepts
| Concept | Description |
|---------|-------------|
| **Trace** | Collection of runs (full execution) |
| **Run** | Single unit of work (one LLM call, one tool call) |
| **Project** | Container for traces |

### Enable Tracing
```python
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-api-key"
os.environ["LANGCHAIN_PROJECT"] = "my-project"
```

### Metrics-Driven Development (MDD)
1. **Establish baseline** - Run initial evaluations
2. **Change stuff** - Modify prompts, models, tools
3. **Recalculate metrics** - Compare to baseline

### What to Monitor
- **Token count**: Cost and context usage
- **Latency**: Response times
- **Tool usage**: Which tools are called
- **Error rates**: Failures and retries

**Official Docs**: [LangSmith Observability](https://docs.langchain.com/langsmith/observability) [[13]](https://docs.langchain.com/langsmith/observability)

**Quickstart**: [Observability Quickstart](https://docs.langchain.com/langsmith/observability-quickstart) [[14]](https://docs.langchain.com/langsmith/observability-quickstart)

---

## 12. Context Engineering

### Definition
> **Context engineering** is the practice of building dynamic systems that provide the right information and tools, in the right format, so that an AI application can accomplish a task.

### The 12-Factor Agents (Dex Horthy)
> "Everything that makes agents good is context engineering."

| Factor | Principle |
|--------|-----------|
| 1 | Natural Language to Tool Calls |
| 2 | Own your prompts |
| 3 | Own your context window |
| 4 | Tools are just structured outputs |
| 5 | Unify execution state and business state |
| 6 | Launch/Pause/Resume with simple APIs |
| 7 | Contact humans with tool calls |
| 8 | Own your control flow |
| 9 | Compact errors into context window |
| 10 | Small, focused agents |
| 11 | Trigger from anywhere |
| 12 | Make your agent a stateless reducer |
| 13 | Pre-fetch all the context you might need |

### Context Types
| By Mutability | Description |
|---------------|-------------|
| **Static** | Immutable (user metadata, tools) |
| **Dynamic** | Evolves during execution (conversation history) |

| By Lifetime | Description |
|-------------|-------------|
| **Runtime** | Scoped to single run |
| **Cross-conversation** | Persists across sessions |

**12-Factor Agents**: [GitHub Repository](https://github.com/humanlayer/12-factor-agents) [[15]](https://github.com/humanlayer/12-factor-agents)

**Official Docs**: [Context Engineering](https://docs.langchain.com/oss/python/langchain/context-engineering) [[16]](https://docs.langchain.com/oss/python/langchain/context-engineering)

**Context Overview**: [Context Concepts](https://docs.langchain.com/oss/python/concepts/context) [[17]](https://docs.langchain.com/oss/python/concepts/context)

---

## Code Patterns Reference

### Pattern 1: Basic Agent
```python
from langchain.agents import create_agent
from langchain_core.tools import tool

@tool
def my_tool(input: str) -> str:
    """Tool description."""
    return f"Processed: {input}"

agent = create_agent(
    model="gpt-4o",
    tools=[my_tool],
    system_prompt="You are helpful."
)

response = agent.invoke({"messages": [{"role": "user", "content": "Hello"}]})
```

### Pattern 2: RAG Tool
```python
@tool
def search_docs(query: str) -> str:
    """Search documentation for relevant information."""
    results = retriever.invoke(query)
    return "\n".join([f"[{i+1}]: {d.page_content}" for i, d in enumerate(results)])
```

### Pattern 3: Middleware Logging
```python
from langchain.agents.middleware import before_model

call_count = 0

@before_model
def count_calls(state, runtime):
    global call_count
    call_count += 1
    print(f"Model call #{call_count}")
    return None
```

### Pattern 4: Complete Agentic RAG
```python
from langchain.agents import create_agent
from langchain.agents.middleware import ModelCallLimitMiddleware
from langchain_core.tools import tool
from langchain_qdrant import QdrantVectorStore

# Setup vector store and retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

@tool
def search_knowledge(query: str) -> str:
    """Search knowledge base for information."""
    results = retriever.invoke(query)
    return "\n".join([doc.page_content for doc in results])

# Create agent with middleware
agent = create_agent(
    model="gpt-4o",
    tools=[search_knowledge],
    system_prompt="Answer using the knowledge base when relevant.",
    middleware=[ModelCallLimitMiddleware(run_limit=5)]
)
```

---

## Common Issues & Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| Agent loops forever | No exit condition | Add `ModelCallLimitMiddleware` |
| Wrong tool selected | Poor docstring | Improve tool description |
| Empty retrieval | Bad query | Refine retriever query logic |
| Tracing not working | Missing env vars | Check `LANGCHAIN_TRACING_V2` |
| Tool errors | Missing return | Always return string from tools |

---

## Breakout Room Tasks Summary

### Breakout Room 1 (Tasks 1-5)
- [ ] Install dependencies with `uv sync`
- [ ] Set environment variables (OpenAI, LangSmith)
- [ ] Understand Runnables and LCEL pipe operator
- [ ] Trace through the agent loop conceptually
- [ ] Build first agent with `create_agent()`
- [ ] **Activity**: Create a custom tool

### Breakout Room 2 (Tasks 6-10)
- [ ] Load and chunk documents
- [ ] Set up Qdrant vector database
- [ ] Create RAG tool with retriever
- [ ] Implement logging middleware
- [ ] Build complete Agentic RAG system
- [ ] **Activity**: Enhance the agent

---

## Official Documentation Links

### LangChain Core
- [LangChain Overview](https://docs.langchain.com/oss/python/langchain/overview) [[18]](https://docs.langchain.com/oss/python/langchain/overview)
- [Philosophy](https://docs.langchain.com/oss/python/langchain/philosophy) [[4]](https://docs.langchain.com/oss/python/langchain/philosophy)
- [Component Architecture](https://docs.langchain.com/oss/python/langchain/component-architecture) [[19]](https://docs.langchain.com/oss/python/langchain/component-architecture)

### Agents
- [Agents Documentation](https://docs.langchain.com/oss/python/langchain/agents) [[2]](https://docs.langchain.com/oss/python/langchain/agents)
- [create_agent API Reference](https://reference.langchain.com/python/langchain/agents/) [[7]](https://reference.langchain.com/python/langchain/agents/)

### Tools
- [Tools Documentation](https://docs.langchain.com/oss/python/langchain/tools) [[6]](https://docs.langchain.com/oss/python/langchain/tools)

### Middleware
- [Middleware Overview](https://docs.langchain.com/oss/python/langchain/middleware/overview) [[8]](https://docs.langchain.com/oss/python/langchain/middleware/overview)
- [Custom Middleware](https://docs.langchain.com/oss/python/langchain/middleware/custom) [[9]](https://docs.langchain.com/oss/python/langchain/middleware/custom)
- [Built-in Middleware](https://docs.langchain.com/oss/python/langchain/middleware/built-in) [[20]](https://docs.langchain.com/oss/python/langchain/middleware/built-in)

### Retrieval & RAG
- [Retrieval Documentation](https://docs.langchain.com/oss/python/langchain/retrieval) [[10]](https://docs.langchain.com/oss/python/langchain/retrieval)
- [Vector Stores](https://docs.langchain.com/oss/python/integrations/vectorstores/index) [[11]](https://docs.langchain.com/oss/python/integrations/vectorstores/index)
- [Embedding Models](https://docs.langchain.com/oss/python/integrations/text_embedding/index) [[21]](https://docs.langchain.com/oss/python/integrations/text_embedding/index)

### Context Engineering
- [Context Overview](https://docs.langchain.com/oss/python/concepts/context) [[17]](https://docs.langchain.com/oss/python/concepts/context)
- [Context Engineering in Agents](https://docs.langchain.com/oss/python/langchain/context-engineering) [[16]](https://docs.langchain.com/oss/python/langchain/context-engineering)

### LangSmith
- [LangSmith Home](https://docs.langchain.com/langsmith/home) [[22]](https://docs.langchain.com/langsmith/home)
- [Observability](https://docs.langchain.com/langsmith/observability) [[13]](https://docs.langchain.com/langsmith/observability)
- [Observability Concepts](https://docs.langchain.com/langsmith/observability-concepts) [[23]](https://docs.langchain.com/langsmith/observability-concepts)
- [Observability Quickstart](https://docs.langchain.com/langsmith/observability-quickstart) [[14]](https://docs.langchain.com/langsmith/observability-quickstart)

### LangGraph
- [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview) [[24]](https://docs.langchain.com/oss/python/langgraph/overview)
- [Agentic RAG Tutorial](https://docs.langchain.com/oss/python/langgraph/agentic-rag) [[25]](https://docs.langchain.com/oss/python/langgraph/agentic-rag)

### External Resources
- [Qdrant Documentation](https://qdrant.tech/documentation/) [[12]](https://qdrant.tech/documentation/)
- [12-Factor Agents](https://github.com/humanlayer/12-factor-agents) [[15]](https://github.com/humanlayer/12-factor-agents)
- [ReAct Paper](https://arxiv.org/abs/2210.03629) [[5]](https://arxiv.org/abs/2210.03629)
- [Simon Willison on Agents](https://simonwillison.net/2025/Sep/18/agents/) [[1]](https://simonwillison.net/2025/Sep/18/agents/)
- [LangChain 1.0 Release Blog](https://blog.langchain.com/langchain-langgraph-1dot0/) [[26]](https://blog.langchain.com/langchain-langgraph-1dot0/)

---

## References

1. Willison, Simon. "I think 'agent' may finally have a widely enough agreed upon definition." September 2025. https://simonwillison.net/2025/Sep/18/agents/

2. LangChain Documentation. "Agents." https://docs.langchain.com/oss/python/langchain/agents

3. LangChain Documentation. "Runnables Concepts." https://python.langchain.com/docs/concepts/runnables/

4. LangChain Documentation. "Philosophy." https://docs.langchain.com/oss/python/langchain/philosophy

5. Yao, Shunyu, et al. "ReAct: Synergizing Reasoning and Acting in Language Models." arXiv:2210.03629, October 2022. https://arxiv.org/abs/2210.03629

6. LangChain Documentation. "Tools." https://docs.langchain.com/oss/python/langchain/tools

7. LangChain Reference. "create_agent API." https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent

8. LangChain Documentation. "Middleware Overview." https://docs.langchain.com/oss/python/langchain/middleware/overview

9. LangChain Documentation. "Custom Middleware." https://docs.langchain.com/oss/python/langchain/middleware/custom

10. LangChain Documentation. "Retrieval." https://docs.langchain.com/oss/python/langchain/retrieval

11. LangChain Documentation. "Vector Stores." https://docs.langchain.com/oss/python/integrations/vectorstores/index

12. Qdrant Documentation. https://qdrant.tech/documentation/

13. LangSmith Documentation. "Observability." https://docs.langchain.com/langsmith/observability

14. LangSmith Documentation. "Observability Quickstart." https://docs.langchain.com/langsmith/observability-quickstart

15. HumanLayer. "12-Factor Agents: Patterns of Reliable LLM Applications." https://github.com/humanlayer/12-factor-agents

16. LangChain Documentation. "Context Engineering in Agents." https://docs.langchain.com/oss/python/langchain/context-engineering

17. LangChain Documentation. "Context Overview." https://docs.langchain.com/oss/python/concepts/context

18. LangChain Documentation. "LangChain Overview." https://docs.langchain.com/oss/python/langchain/overview

19. LangChain Documentation. "Component Architecture." https://docs.langchain.com/oss/python/langchain/component-architecture

20. LangChain Documentation. "Built-in Middleware." https://docs.langchain.com/oss/python/langchain/middleware/built-in

21. LangChain Documentation. "Embedding Models." https://docs.langchain.com/oss/python/integrations/text_embedding/index

22. LangSmith Documentation. "Home." https://docs.langchain.com/langsmith/home

23. LangSmith Documentation. "Observability Concepts." https://docs.langchain.com/langsmith/observability-concepts

24. LangChain Documentation. "LangGraph Overview." https://docs.langchain.com/oss/python/langgraph/overview

25. LangChain Documentation. "Build a Custom RAG Agent with LangGraph." https://docs.langchain.com/oss/python/langgraph/agentic-rag

26. LangChain Blog. "LangChain & LangGraph 1.0." October 2025. https://blog.langchain.com/langchain-langgraph-1dot0/

---

*Cheatsheet created for AIE9 Session 3: The Agent Loop*
*Last updated: January 2026*
