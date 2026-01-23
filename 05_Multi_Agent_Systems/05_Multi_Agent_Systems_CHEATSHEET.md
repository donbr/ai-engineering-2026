# Session 5 Cheatsheet: Multi-Agent Systems

> Building Coordinated Agent Architectures with LangGraph

---

## Quick Reference

| Concept | Definition | Key API/Pattern |
|---------|------------|-----------------|
| Multi-Agent | Multiple specialized agents coordinating on tasks | `create_swarm()` |
| Supervisor | Central agent directing worker agents | Supervisor pattern |
| Router | Classify input → route to specialist | Router pattern |
| Swarm | Agents hand off control dynamically | `create_handoff_tool()` |
| Shared State | TypedDict schema shared across agents | `class State(TypedDict)` |
| Handoff Tool | Transfers control between agents | `create_handoff_tool()` |
| Checkpointer | Short-term memory for conversation state | `InMemorySaver()` |
| Store | Long-term memory across sessions | `InMemoryStore()` |

---

## Setup Requirements

### Dependencies
```bash
pip install langchain>=1.0.0 langchain-openai langgraph langgraph-swarm
```

### Environment Variables
```python
import os
os.environ["OPENAI_API_KEY"] = "your-key"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-langsmith-key"
os.environ["LANGCHAIN_PROJECT"] = "AIE9-Session5"
```

---

## 1. When to Use Multi-Agent Systems

### Industry Definition
> **"Multi-agent systems coordinate specialized components to tackle complex workflows. However, not every complex task requires this approach."**
> — LangChain Team [[1]](https://docs.langchain.com/oss/python/langchain/multi-agent/index)

### Decision Framework
| Single Agent | Multi-Agent |
|--------------|-------------|
| One knowledge domain | Multiple domains |
| Tools share context | Tools need different prompts |
| < 10 related tools | Domain-specific toolsets |
| Simple workflow | Complex coordination needed |

### Key Question
**"Could one agent with dynamic tools solve this?"**
- If yes → single agent
- If no → consider multi-agent

**Official Docs**: [Multi-agent Overview](https://docs.langchain.com/oss/python/langchain/multi-agent/index) [[1]](https://docs.langchain.com/oss/python/langchain/multi-agent/index)

---

## 2. Supervisor Pattern

### Industry Definition
> **"The supervisor pattern is a multi-agent architecture where a central supervisor agent coordinates specialized worker agents."**
> — LangChain Team [[2]](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents-personal-assistant)

### Architecture
```
┌────────────────────────────────────────────────────────┐
│                   SUPERVISOR PATTERN                    │
│                                                         │
│                  ┌──────────────┐                      │
│                  │  Supervisor  │                      │
│                  └──────┬───────┘                      │
│                         │                              │
│            ┌────────────┼────────────┐                │
│            ▼            ▼            ▼                │
│      ┌──────────┐ ┌──────────┐ ┌──────────┐         │
│      │ Calendar │ │  Email   │ │  Search  │         │
│      │  Agent   │ │  Agent   │ │  Agent   │         │
│      └──────────┘ └──────────┘ └──────────┘         │
│                                                         │
│  - Supervisor understands overall workflow             │
│  - Workers have specialized prompts & tools            │
│  - Results flow back through supervisor                │
└────────────────────────────────────────────────────────┘
```

### When to Use
- Tasks requiring **different types of expertise**
- Need for **central coordination**
- Workers have **fundamentally different responsibilities**

**Official Docs**: [Supervisor Tutorial](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents-personal-assistant) [[2]](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents-personal-assistant)

---

## 3. Router Pattern

### Industry Definition
> **"The router pattern excels when your organization's knowledge lives across distinct verticals—separate knowledge domains that each require their own agent."**
> — LangChain Team [[3]](https://docs.langchain.com/oss/python/langchain/multi-agent/router-knowledge-base)

### Architecture
```
┌────────────────────────────────────────────────────────┐
│                    ROUTER PATTERN                       │
│                                                         │
│   ┌───────┐    ┌──────────┐                           │
│   │ Query │───▶│ Classify │                           │
│   └───────┘    └────┬─────┘                           │
│                     │                                   │
│         ┌───────────┼───────────┐                     │
│         ▼           ▼           ▼                     │
│   ┌──────────┐ ┌──────────┐ ┌──────────┐            │
│   │  GitHub  │ │  Notion  │ │  Slack   │            │
│   │  Agent   │ │  Agent   │ │  Agent   │            │
│   └────┬─────┘ └────┬─────┘ └────┬─────┘            │
│        │            │            │                    │
│        └────────────┼────────────┘                    │
│                     ▼                                   │
│              ┌────────────┐                            │
│              │ Synthesize │───▶ Combined Answer       │
│              └────────────┘                            │
└────────────────────────────────────────────────────────┘
```

### When to Use
- Knowledge across **distinct verticals**
- Queries that span **multiple sources**
- Need to **synthesize** results from specialists

**Official Docs**: [Router Tutorial](https://docs.langchain.com/oss/python/langchain/multi-agent/router-knowledge-base) [[3]](https://docs.langchain.com/oss/python/langchain/multi-agent/router-knowledge-base)

---

## 4. Swarm Pattern

### Industry Definition
> **"A library for creating swarm-style multi-agent systems where specialized agents dynamically hand off control."**
> — LangChain Team [[4]](https://github.com/langchain-ai/langgraph-swarm-py)

### Architecture
```
┌────────────────────────────────────────────────────────┐
│                    SWARM PATTERN                        │
│                                                         │
│     ┌─────────┐          ┌─────────┐                  │
│     │  Alice  │◀────────▶│   Bob   │                  │
│     │ (math)  │  handoff │(pirate) │                  │
│     └────┬────┘          └────┬────┘                  │
│          │                    │                        │
│          │    Dynamic         │                        │
│          │    Control         │                        │
│          │    Transfer        │                        │
│          ▼                    ▼                        │
│     ┌─────────────────────────────────────────┐       │
│     │          Shared State + Memory          │       │
│     │   - active_agent tracked automatically  │       │
│     │   - conversation history preserved      │       │
│     └─────────────────────────────────────────┘       │
└────────────────────────────────────────────────────────┘
```

### Key Characteristics
- **No central coordinator** — agents hand off directly
- **Context preserved** across handoffs
- **Active agent** tracked in state

**Official Docs**: [LangGraph Swarm](https://github.com/langchain-ai/langgraph-swarm-py) [[4]](https://github.com/langchain-ai/langgraph-swarm-py)

---

## 5. Shared State Management

### State Schema
```
┌────────────────────────────────────────────────────────┐
│                   SHARED STATE                          │
│                                                         │
│   class State(TypedDict):                              │
│       messages: list[AnyMessage]     # Conversation    │
│       active_agent: str              # Current agent   │
│       classification: dict | None    # Route info      │
│       results: list[str] | None      # Agent outputs   │
│                                                         │
│              ┌────────────────┐                        │
│              │     State      │                        │
│              └───────┬────────┘                        │
│           ┌──────────┼──────────┐                     │
│           ▼          ▼          ▼                     │
│       ┌──────┐  ┌──────┐  ┌──────┐                   │
│       │Agent │  │Agent │  │Agent │                   │
│       │  A   │  │  B   │  │  C   │                   │
│       └──────┘  └──────┘  └──────┘                   │
│                                                         │
│   All agents read/update the SAME state object         │
└────────────────────────────────────────────────────────┘
```

### Key Principles
- **Store raw data, not formatted text** — allows flexibility in prompts
- **Use `Annotated` for list updates** — `operator.add` for appending
- **Nodes update state** — return dict with changed keys

**Official Docs**: [Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api) [[5]](https://docs.langchain.com/oss/python/langgraph/graph-api)

---

## 6. Handoff Tools

### Creating Handoff Tools
```
┌────────────────────────────────────────────────────────┐
│                   HANDOFF TOOLS                         │
│                                                         │
│   transfer_to_bob = create_handoff_tool(               │
│       agent_name="Bob",                                 │
│       description="Transfer to Bob, the pirate"        │
│   )                                                     │
│                                                         │
│   ┌─────────┐   transfer_to_bob()   ┌─────────┐       │
│   │  Alice  │ ──────────────────────▶│   Bob   │       │
│   └─────────┘                        └─────────┘       │
│                                                         │
│   - Agent calls handoff tool like any other tool       │
│   - Control transfers to target agent                  │
│   - Conversation context preserved                     │
└────────────────────────────────────────────────────────┘
```

### Best Practices
- **Descriptive names** — help agent decide when to hand off
- **Clear descriptions** — explain what target agent does
- **Two-way handoffs** — allow return to original agent

**Official Docs**: [LangGraph Swarm](https://github.com/langchain-ai/langgraph-swarm-py) [[4]](https://github.com/langchain-ai/langgraph-swarm-py)

---

## 7. Memory in Multi-Agent Systems

### Memory Types
```
┌────────────────────────────────────────────────────────┐
│                    MEMORY TYPES                         │
│                                                         │
│   ┌──────────────────────────────────────────────┐    │
│   │              SHORT-TERM MEMORY               │    │
│   │                                              │    │
│   │   checkpointer = InMemorySaver()            │    │
│   │                                              │    │
│   │   - Maintains conversation state            │    │
│   │   - Tracks active agent                     │    │
│   │   - Persists within thread_id               │    │
│   └──────────────────────────────────────────────┘    │
│                                                         │
│   ┌──────────────────────────────────────────────┐    │
│   │              LONG-TERM MEMORY                │    │
│   │                                              │    │
│   │   store = InMemoryStore()                   │    │
│   │                                              │    │
│   │   - Persists across sessions                │    │
│   │   - Shared data between threads             │    │
│   │   - User preferences, history               │    │
│   └──────────────────────────────────────────────┘    │
│                                                         │
│   app = workflow.compile(                              │
│       checkpointer=checkpointer,  # Required          │
│       store=store                 # Optional          │
│   )                                                     │
└────────────────────────────────────────────────────────┘
```

### Key Insight
> **"Short-term memory is crucial for maintaining conversation state between turns."**
> — LangChain Team [[4]](https://github.com/langchain-ai/langgraph-swarm-py)

**Official Docs**: [Memory Overview](https://docs.langchain.com/oss/python/concepts/memory) [[6]](https://docs.langchain.com/oss/python/concepts/memory)

---

## 8. Human-in-the-Loop

### Interrupt and Resume Pattern
```
┌────────────────────────────────────────────────────────┐
│                HUMAN-IN-THE-LOOP                        │
│                                                         │
│   ┌─────────┐                                          │
│   │ Agent   │                                          │
│   │ Action  │                                          │
│   └────┬────┘                                          │
│        │                                                │
│        ▼                                                │
│   ┌─────────────────┐                                  │
│   │ Requires        │                                  │
│   │ Approval?       │                                  │
│   └────────┬────────┘                                  │
│            │                                            │
│      ┌─────┴─────┐                                     │
│      ▼           ▼                                     │
│   ┌──────┐  ┌──────────┐                              │
│   │  No  │  │   Yes    │                              │
│   └──┬───┘  └────┬─────┘                              │
│      │           │                                     │
│      │           ▼                                     │
│      │     ┌───────────┐                              │
│      │     │ Interrupt │                              │
│      │     └─────┬─────┘                              │
│      │           ▼                                     │
│      │     ┌───────────┐                              │
│      │     │  Human    │                              │
│      │     │  Review   │                              │
│      │     └─────┬─────┘                              │
│      │           │                                     │
│      │     ┌─────┴─────┐                              │
│      │     ▼           ▼                              │
│      │  Approve     Reject                            │
│      │     │           │                              │
│      │     ▼           ▼                              │
│      │  Execute     Cancel                            │
│      │     │           │                              │
│      └─────┴───────────┘                              │
└────────────────────────────────────────────────────────┘
```

### Resume After Approval
```python
human_response = Command(resume={"approved": True})
result = app.invoke(human_response, config)
```

**Official Docs**: [Human-in-the-Loop](https://docs.langchain.com/oss/python/deepagents/human-in-the-loop) [[7]](https://docs.langchain.com/oss/python/deepagents/human-in-the-loop)

---

## 9. Debugging Multi-Agent Systems

### Observability with LangSmith
```
┌────────────────────────────────────────────────────────┐
│                    OBSERVABILITY                        │
│                                                         │
│   os.environ["LANGCHAIN_TRACING_V2"] = "true"          │
│   os.environ["LANGCHAIN_API_KEY"] = "your-key"         │
│                                                         │
│   ┌──────────────────────────────────────────────┐    │
│   │                 LangSmith                    │    │
│   │                                              │    │
│   │   Traces ─────▶ See each agent's actions    │    │
│   │   Graph  ─────▶ Visualize agent flow        │    │
│   │   Metrics ────▶ Token usage, latency        │    │
│   │   Errors ─────▶ Debug handoff failures      │    │
│   └──────────────────────────────────────────────┘    │
└────────────────────────────────────────────────────────┘
```

### Common Issues
| Issue | Cause | Solution |
|-------|-------|----------|
| Lost context | Missing checkpointer | Add `InMemorySaver()` |
| Wrong agent | Bad handoff description | Improve tool description |
| State mismatch | Type error | Check TypedDict schema |
| Infinite loop | No exit condition | Add termination logic |

**Official Docs**: [LangSmith](https://docs.langchain.com/langsmith) [[8]](https://docs.langchain.com/langsmith)

---

## 10. Common Patterns

### Pattern 1: Supervisor with Workers
```python
supervisor = create_agent(
    model,
    workers=[calendar_agent, email_agent],
    system_prompt="You coordinate calendar and email tasks."
)
```

### Pattern 2: Router with Synthesis
```python
route = classifier.invoke(query)
results = [agents[r].invoke(query) for r in route.domains]
answer = synthesizer.invoke(results)
```

### Pattern 3: Swarm with Memory
```python
workflow = create_swarm([alice, bob])
app = workflow.compile(checkpointer=InMemorySaver())
```

---

## 11. Interview Questions

1. **When would you choose multi-agent over a single agent?**
   - Multiple knowledge domains requiring different prompts
   - Complex coordination between specialized tasks

2. **What's the difference between supervisor and router patterns?**
   - Supervisor: central coordinator, sequential worker calls
   - Router: parallel specialist queries, synthesized results

3. **How do handoff tools work in swarm systems?**
   - Agent calls handoff tool → control transfers → context preserved

4. **Why is a checkpointer required for multi-turn swarm conversations?**
   - Tracks active agent between invocations
   - Maintains conversation history

---

## 12. Resources & Links

| # | Resource | Type | Link |
|---|----------|------|------|
| 1 | Multi-agent Overview | Docs | [LangChain](https://docs.langchain.com/oss/python/langchain/multi-agent/index) |
| 2 | Supervisor Tutorial | Tutorial | [LangChain](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents-personal-assistant) |
| 3 | Router Tutorial | Tutorial | [LangChain](https://docs.langchain.com/oss/python/langchain/multi-agent/router-knowledge-base) |
| 4 | LangGraph Swarm | GitHub | [GitHub](https://github.com/langchain-ai/langgraph-swarm-py) |
| 5 | Graph API | Docs | [LangGraph](https://docs.langchain.com/oss/python/langgraph/graph-api) |
| 6 | Memory Overview | Docs | [LangGraph](https://docs.langchain.com/oss/python/concepts/memory) |
| 7 | Human-in-the-Loop | Docs | [LangGraph](https://docs.langchain.com/oss/python/deepagents/human-in-the-loop) |
| 8 | LangSmith | Docs | [LangSmith](https://docs.langchain.com/langsmith) |
| 9 | LangGraph Overview | Docs | [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) |
| 10 | Don't Build Multi-Agents | Paper | [Cognition](https://cognition.ai/blog/dont-build-multi-agents) |
| 11 | Thinking in LangGraph | Tutorial | [LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph) |
| 12 | Graph API | Docs | [LangGraph](https://docs.langchain.com/oss/python/langgraph/graph-api) |
| 13 | AutoGen Integration | Tutorial | [LangSmith](https://docs.langchain.com/langsmith/autogen-integration) |
| 14 | LangSmith Deployment | Docs | [LangSmith](https://docs.langchain.com/langsmith/components) |
| 15 | Workflows & Agents | Tutorial | [LangGraph](https://docs.langchain.com/oss/python/langgraph/workflows-agents) |

---

## Key Takeaways

1. **Not everything needs multi-agent** — single agent with dynamic tools often works
2. **Supervisor** for coordinated expertise, **Router** for parallel specialists, **Swarm** for dynamic handoffs
3. **Shared state** via TypedDict schemas enables inter-agent communication
4. **Checkpointer is required** for multi-turn conversations in swarms
5. **Human-in-the-loop** for sensitive actions (emails, purchases)
6. **LangSmith** for debugging complex multi-agent interactions

---

*Session 5 Cheatsheet | Multi-Agent Systems | Complex Agents Module*
