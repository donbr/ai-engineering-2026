# Session 5: Multi-Agent Systems

> **Module**: Complex Agents | **Week**: 3

---

## Goal

Build multi-agent systems that coordinate specialized workers to solve complex tasks using supervisor, router, and swarm patterns.

---

## Learning Outcomes

By the end of this session, you will be able to:

1. **Explain** when multi-agent systems are appropriate versus single agents with dynamic tools
2. **Implement** the supervisor pattern with specialized worker agents
3. **Design** router architectures that classify and direct queries to domain specialists
4. **Create** handoff tools that transfer control between agents in swarm systems
5. **Manage** shared state across multi-agent workflows using TypedDict schemas

---

## Tools Introduced

| Tool | Purpose | Documentation |
|------|---------|---------------|
| **LangGraph 1.x** | Low-level orchestration framework for stateful agents | [LangGraph Docs](https://docs.langchain.com/oss/python/langgraph/overview) |
| **LangGraph Swarm** | Swarm-style multi-agent handoff library | [GitHub](https://github.com/langchain-ai/langgraph-swarm-py) |
| **LangSmith** | Observability and debugging for agent systems | [LangSmith Docs](https://docs.langchain.com/langsmith) |

---

## Key Concepts

### 1. When to Use Multi-Agent Systems

> **"Multi-agent systems coordinate specialized components to tackle complex workflows. However, not every complex task requires this approach."**
> — LangChain Team

**Decision Framework:**
- Single agent with 10+ tools often suffices for single-domain tasks
- Multi-agent when tools require **different prompts or expertise**
- Multi-agent when task spans **multiple knowledge domains**

### 2. Supervisor Pattern

A central supervisor coordinates specialized worker agents:

```
┌─────────────────────────────────────────────┐
│              SUPERVISOR PATTERN              │
│                                              │
│         ┌──────────────┐                    │
│         │  Supervisor  │                    │
│         └──────┬───────┘                    │
│                │                             │
│       ┌────────┼────────┐                   │
│       ▼        ▼        ▼                   │
│   ┌───────┐ ┌───────┐ ┌───────┐           │
│   │Worker │ │Worker │ │Worker │           │
│   │   A   │ │   B   │ │   C   │           │
│   └───────┘ └───────┘ └───────┘           │
└─────────────────────────────────────────────┘
```

**Use when**: Tasks require different types of expertise with central coordination.

### 3. Router Pattern

A routing step classifies input and directs to specialists:

```
┌─────────────────────────────────────────────┐
│               ROUTER PATTERN                 │
│                                              │
│   Query → [Classify] → Agent A ─┐           │
│                      → Agent B ─┼→ Synthesize │
│                      → Agent C ─┘           │
└─────────────────────────────────────────────┘
```

**Use when**: Knowledge lives across distinct verticals (GitHub, Notion, Slack).

### 4. Swarm Pattern

Agents dynamically hand off control using handoff tools:

```
┌─────────────────────────────────────────────┐
│                SWARM PATTERN                 │
│                                              │
│   Alice ←──handoff──→ Bob                   │
│     │                   │                    │
│     └───────────────────┘                   │
│         dynamic control                      │
└─────────────────────────────────────────────┘
```

**Use when**: Agents need to transfer control based on conversation flow.

### 5. Shared State & Memory

Multi-agent systems share state through TypedDict schemas:

- **Short-term memory**: Checkpointer maintains conversation state
- **Long-term memory**: Store persists data across sessions

### 6. Human-in-the-Loop

Interrupt and resume patterns for sensitive actions:

- Pause before sending emails, making purchases
- Human reviews, approves, edits, or rejects
- Agent resumes with decision

---

## Recommended Reading

| Resource | Type | Link |
|----------|------|------|
| Multi-agent Overview | Documentation | [LangChain](https://docs.langchain.com/oss/python/langchain/multi-agent/index) |
| LangGraph Overview | Documentation | [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) |
| Supervisor Pattern Tutorial | Tutorial | [LangChain](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents-personal-assistant) |
| Router Pattern Tutorial | Tutorial | [LangChain](https://docs.langchain.com/oss/python/langchain/multi-agent/router-knowledge-base) |
| LangGraph Swarm | Documentation | [GitHub](https://github.com/langchain-ai/langgraph-swarm-py) |
| "Don't Build Multi-Agents" | Paper | [Cognition](https://cognition.ai/blog/dont-build-multi-agents) |
| Graph API Overview | Documentation | [LangGraph](https://docs.langchain.com/oss/python/langgraph/graph-api) |
| Human-in-the-Loop Guide | Documentation | [LangGraph](https://docs.langchain.com/oss/python/deepagents/human-in-the-loop) |
| Memory Overview | Documentation | [LangGraph](https://docs.langchain.com/oss/python/concepts/memory) |
| Thinking in LangGraph | Tutorial | [LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph) |

---

## Assignment

**Build a multi-agent application that generates reports using multiple specialized teams.**

### Deliverables

1. **Supervisor agent** coordinating at least 2 worker agents
2. **Shared state schema** for inter-agent communication
3. **Human-in-the-loop approval** for final report

### Evaluation Criteria

- Proper separation of concerns between agents
- Effective use of handoff mechanisms
- State management across agent boundaries

---

## Advanced Build

**Customer Support Swarm**

Build a customer support system with flight and hotel booking agents that hand off based on user needs:

- Dynamic handoff between booking specialists
- Shared reservation state
- Memory persistence across conversations

Reference: [LangGraph Swarm Examples](https://github.com/langchain-ai/langgraph-swarm-py/blob/main/examples/)

---

*Session 5 | Complex Agents Module | Week 3*
