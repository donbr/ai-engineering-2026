# Session 3: The Agent Loop

> Building Production Agents with LangChain 1.0

---

## Goal

Understand the foundational agent architecture and build production-ready agents using LangChain's `create_agent()` API with tools, middleware, and vector-based retrieval.

---

## Learning Outcomes

By the end of this session, you will be able to:

1. **Define** what an "agent" is and explain the agent loop architecture
2. **Describe** the Runnable abstraction and compose chains using LCEL
3. **Create** tools with the `@tool` decorator and meaningful docstrings
4. **Build** agents using `create_agent()` with middleware for logging and guardrails
5. **Implement** Agentic RAG where the agent controls when to retrieve
6. **Configure** LangSmith tracing to observe agent behavior

---

## Tools Introduced

| Tool | Purpose |
|------|---------|
| `create_agent()` | Production-ready agent builder in LangChain 1.0 |
| `@tool` decorator | Convert Python functions to agent-callable tools |
| Middleware hooks | `before_model`, `after_model` for agent control |
| `QdrantVectorStore` | Vector database for semantic retrieval |
| LangSmith | Observability and tracing for LLM applications |

---

## Key Concepts

### 1. What is an Agent?

> **"An LLM agent runs tools in a loop to achieve a goal."**
> — Simon Willison, September 2025

An agent is more than just an LLM. It combines a language model with **tools** and runs them in a **loop** until the task is complete. The key characteristics are:

- **Reason** about what to do next
- **Act** by calling tools
- **Observe** the results
- **Iterate** until the goal is achieved

This distinguishes agents from simple chains, which follow a fixed sequence of steps.

**Reference**: [Simon Willison on Agents](https://simonwillison.net/2025/Sep/18/agents/)

---

### 2. The Agent Loop

The agent loop is the core execution pattern:

```
┌─────────────────────────────────────────────────────────┐
│                     AGENT LOOP                          │
│                                                         │
│   ┌──────────┐     ┌──────────┐     ┌──────────┐       │
│   │  Model   │ --> │   Tool   │ --> │  Model   │ --> … │
│   │   Call   │     │ Execution│     │   Call   │       │
│   └──────────┘     └──────────┘     └──────────┘       │
│        │                                  │             │
│        v                                  v             │
│   "Use search"                   "Here's the answer"   │
└─────────────────────────────────────────────────────────┘
```

**Two main steps:**
1. **Model Call**: LLM receives state, decides to call a tool or return an answer
2. **Tool Execution**: Selected tool runs, result added to conversation

The loop continues until the model decides it has enough information.

**Reference**: [LangChain Agents Documentation](https://docs.langchain.com/oss/python/langchain/agents)

---

### 3. The Runnable Abstraction

> **"The primary abstraction in the LangChain ecosystem is the Runnable."**

Every LangChain component follows the same interface:
- Takes an **input**
- Performs an **operation**
- Returns an **output**

**Core methods:**
- `invoke(input)` — Process single input
- `batch([inputs])` — Process multiple inputs in parallel
- `stream(input)` — Stream output chunks

**Common Runnable types:**
- Language models (`ChatOpenAI`, `ChatAnthropic`)
- Prompt templates (`ChatPromptTemplate`)
- Retrievers (vector store retrievers)
- Output parsers (`StrOutputParser`)

**Reference**: [Runnables Concepts](https://python.langchain.com/docs/concepts/runnables/)

---

### 4. LCEL (LangChain Expression Language)

LCEL uses the pipe operator (`|`) to chain Runnables together, similar to Unix pipes:

```
prompt | model | parser
```

Output flows from left to right. This creates composable, readable chains.

**Key insight**: Because everything is a Runnable with the same interface, any component can be chained with any other component.

**Reference**: [LangChain Philosophy](https://docs.langchain.com/oss/python/langchain/philosophy)

---

### 5. The ReAct Pattern

**ReAct** (Reasoning and Acting) interleaves chain-of-thought reasoning with action execution:

> "Reasoning traces help the model induce, track and update action plans as well as handle exceptions, while actions allow it to interface with and gather additional information from external sources."
> — Yao et al., 2022

The pattern:
1. **Thought**: Reason about what to do
2. **Action**: Execute a tool
3. **Observation**: See the result
4. **Repeat**: Continue until task complete

**Reference**: [ReAct Paper](https://arxiv.org/abs/2210.03629)

---

### 6. Tool Calling

Tools are Python functions that agents can call. The `@tool` decorator converts functions into agent-callable tools.

**Critical insight**: The docstring becomes the tool description that the LLM uses to decide which tool to call. Write clear, detailed docstrings that explain:
- What the tool does
- When to use it
- What arguments it accepts

**Reference**: [LangChain Tools](https://docs.langchain.com/oss/python/langchain/tools)

---

### 7. The `create_agent()` API

`create_agent()` is the standard way to build agents in LangChain 1.0. It provides:
- Simpler interface than lower-level APIs
- Middleware support for customization
- Built on LangGraph for production reliability

**Key parameters:**
| Parameter | Description |
|-----------|-------------|
| `model` | LLM to use (string or model instance) |
| `tools` | List of tools the agent can call |
| `system_prompt` | System-level instructions |
| `middleware` | List of middleware hooks |

**Reference**: [create_agent API Reference](https://reference.langchain.com/python/langchain/agents/)

---

### 8. Middleware

Middleware hooks into the agent loop at specific points for:
- **Logging**: Track what the agent does
- **Guardrails**: Filter or modify inputs/outputs
- **Rate limiting**: Control API usage
- **Human-in-the-loop**: Pause for approval

**Available hooks:**
- `beforeAgent` — Before agent starts
- `beforeModel` — Before each LLM call
- `afterModel` — After each LLM response
- `afterAgent` — After agent completes

**Built-in middleware:**
- `ToolCallLimitMiddleware` — Prevent runaway agents
- `HumanInTheLoopMiddleware` — Require human approval
- `SummarizationMiddleware` — Summarize long conversations

**Reference**: [Middleware Overview](https://docs.langchain.com/oss/python/langchain/middleware/overview)

---

### 9. Traditional RAG vs. Agentic RAG

**Traditional RAG**: Fixed pipeline
```
Query → Always Retrieve → Augment → Generate
```

**Agentic RAG**: Agent controls retrieval
```
Query → Agent Decides → (Maybe Retrieve) → Generate
```

**Benefits of Agentic RAG:**
- Skip retrieval when not needed
- Retrieve multiple times if necessary
- Combine retrieval with other tools
- More flexible and often more efficient

**Reference**: [LangChain Retrieval](https://docs.langchain.com/oss/python/langchain/retrieval)

---

### 10. LangSmith Observability

LangSmith provides visibility into agent execution:

**Key concepts:**
| Concept | Description |
|---------|-------------|
| **Trace** | Full execution path (collection of runs) |
| **Run** | Single operation (one LLM call, one tool call) |
| **Project** | Container for organizing traces |

**What to monitor:**
- Token usage and cost
- Latency and response times
- Tool call patterns
- Error rates and failures

**Reference**: [LangSmith Observability](https://docs.langchain.com/langsmith/observability)

---

## Context Engineering

> **"Everything that makes agents good is context engineering."**
> — Dex Horthy

Context engineering is the practice of providing the right information, in the right format, at the right time. Key principles from the **12-Factor Agents** manifesto:

1. Natural Language to Tool Calls
2. Own your prompts
3. Own your context window
4. Tools are structured outputs
5. Small, focused agents

**Reference**: [12-Factor Agents](https://github.com/humanlayer/12-factor-agents)

---

## Recommended Reading

### Essential
- [LangChain Agents Documentation](https://docs.langchain.com/oss/python/langchain/agents) — Official agents guide
- [LangChain 1.0 Release Notes](https://docs.langchain.com/oss/python/releases/langchain-v1) — What's new in v1
- [ReAct Paper](https://arxiv.org/abs/2210.03629) — Original reasoning + acting research

### Concepts
- [Runnables Concepts](https://python.langchain.com/docs/concepts/runnables/) — Understanding the core abstraction
- [LangChain Philosophy](https://docs.langchain.com/oss/python/langchain/philosophy) — Design principles

### Tools & Middleware
- [Tools Documentation](https://docs.langchain.com/oss/python/langchain/tools) — Creating tools
- [Middleware Overview](https://docs.langchain.com/oss/python/langchain/middleware/overview) — Customizing agents
- [Built-in Middleware](https://docs.langchain.com/oss/python/langchain/middleware/built-in) — Ready-to-use middleware

### Observability
- [LangSmith Observability](https://docs.langchain.com/langsmith/observability) — Tracing and monitoring
- [Observability Quickstart](https://docs.langchain.com/langsmith/observability-quickstart) — Getting started

### Vector Stores
- [Qdrant Documentation](https://qdrant.tech/documentation/) — Vector database
- [LangChain Vector Stores](https://docs.langchain.com/oss/python/integrations/vectorstores/index) — Integration guide

### Industry Perspectives
- [Simon Willison on Agents](https://simonwillison.net/2025/Sep/18/agents/) — Industry definition
- [12-Factor Agents](https://github.com/humanlayer/12-factor-agents) — Production agent patterns

---

## Assignment

### Part 1: Build Your First Agent
1. Set up the development environment with required dependencies
2. Create a simple agent using `create_agent()` with basic tools
3. Observe the agent loop in action using LangSmith traces

### Part 2: Create Custom Tools
1. Define at least two custom tools with the `@tool` decorator
2. Write clear docstrings that help the LLM choose the right tool
3. Test tool selection with different queries

### Part 3: Implement Agentic RAG
1. Set up Qdrant as your vector database
2. Create a retrieval tool that searches your knowledge base
3. Build an agent that decides when to use retrieval

### Part 4: Add Middleware
1. Implement logging middleware to track agent behavior
2. Add `ToolCallLimitMiddleware` to prevent runaway loops
3. Observe the middleware effects in LangSmith

### Deliverable
Record a Loom video (5-10 minutes) walking through your implementation. Explain:
- How the agent loop works in your application
- Why you designed your tools the way you did
- What you learned from observing the LangSmith traces

---

## Advanced Build

Extend your Agentic RAG system with these challenges:

### Multi-Tool Agent
Create an agent with 3+ tools that can:
- Search your knowledge base
- Perform calculations
- Look up current information (weather, time, etc.)

### Conversation Memory
Add conversation history so the agent can reference previous exchanges.

### Custom Middleware
Build a custom middleware that:
- Logs token usage for cost tracking
- Implements a simple content filter
- Tracks tool call patterns for optimization

### Production Hardening
- Add error handling for failed tool calls
- Implement graceful degradation when tools are unavailable
- Set up alerts for anomalous agent behavior

---

## Quick Reference

### Environment Setup
```bash
pip install langchain>=1.0.0 langchain-openai langsmith qdrant-client langchain-qdrant
```

### Environment Variables
```
OPENAI_API_KEY=your-key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your-langsmith-key
LANGCHAIN_PROJECT=AIE9-Session3
```

### Basic Agent Pattern
```python
from langchain.agents import create_agent
from langchain_core.tools import tool

@tool
def my_tool(input: str) -> str:
    """Tool description for LLM."""
    return f"Result: {input}"

agent = create_agent(
    model="gpt-4o",
    tools=[my_tool],
    system_prompt="You are helpful."
)

response = agent.invoke({
    "messages": [{"role": "user", "content": "Hello"}]
})
```

---

*Session Sheet for AIE9 Session 3: The Agent Loop*
*Last updated: January 2026*
