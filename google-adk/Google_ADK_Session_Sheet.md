# Google ADK: Agent Development Kit

## Goal

Master Google's Agent Development Kit (ADK) to build production-ready AI agents that can reason, act, and observe to accomplish complex goals.

## Learning Outcomes

By the end of this session, you will be able to:

1. **Explain the core architecture** of AI agents (Model, Tools, Orchestration Layer)
2. **Build single agents** with tools using ADK's code-first approach
3. **Design multi-agent systems** using Sequential, Parallel, and Loop patterns
4. **Implement tool integration** including custom functions, MCP, and AgentTool
5. **Manage agent state** through Sessions, State, and Memory services
6. **Debug agents** using observability tools (logs, traces, metrics)
7. **Evaluate agent quality** with automated evaluation frameworks
8. **Deploy agents** to production using Cloud Run or Agent Engine
9. **Enable agent interoperability** via A2A protocol

## Tools Introduced

| Tool | Purpose |
|------|---------|
| `google-adk` | Core framework for building agents |
| `Agent` | Base class for LLM-powered agents |
| `SequentialAgent` | Fixed-order pipeline execution |
| `ParallelAgent` | Concurrent task execution |
| `LoopAgent` | Iterative refinement cycles |
| `FunctionTool` | Wrap Python functions as tools |
| `AgentTool` | Use agents as tools for other agents |
| `InMemoryRunner` | Local development orchestrator |
| `InMemorySessionService` | Conversation state management |
| `InMemoryMemoryService` | Long-term knowledge persistence |
| `to_a2a()` | Expose agents via A2A protocol |
| `RemoteA2aAgent` | Consume external agents |

## Key Concepts

### 1. What is an AI Agent?

An AI agent is more than an LLM—it's a complete application that reasons, acts, and observes:

```
Prompt → Agent → Thought → Action → Observation → Final Answer
```

**Core Components:**
- **Model** (Brain): The reasoning engine (Gemini, etc.)
- **Tools** (Hands): External capabilities (search, APIs, code execution)
- **Orchestration** (Nervous System): Manages the think-act-observe loop

### 2. The Agentic Problem-Solving Loop

```
┌─────────────────────────────────────────────┐
│            AGENTIC LOOP                     │
├─────────────────────────────────────────────┤
│  1. Get Mission → User provides goal        │
│  2. Scan Scene → Gather context & tools     │
│  3. Think Through → Plan approach           │
│  4. Take Action → Execute tool calls        │
│  5. Observe & Iterate → Process results     │
│         ↓                                   │
│      Loop until mission complete            │
└─────────────────────────────────────────────┘
```

### 3. Taxonomy of Agentic Systems

| Level | Name | Capability |
|-------|------|------------|
| 0 | Core Reasoning | Pure LLM, no tools |
| 1 | Connected Problem-Solver | Uses external tools |
| 2 | Strategic Problem-Solver | Context engineering, multi-step plans |
| 3 | Collaborative Multi-Agent | Team of specialists |
| 4 | Self-Evolving | Creates own tools and agents |

### 4. Multi-Agent Workflow Patterns

**Sequential Agent**: Assembly line—each agent's output feeds the next
- Use when: Order matters, linear pipeline, steps build on each other

**Parallel Agent**: Concurrent execution—independent tasks run simultaneously
- Use when: Tasks are independent, speed matters

**Loop Agent**: Iterative refinement—cycles until condition met
- Use when: Quality improvement needed, feedback loops required

### 5. State Management

```
┌──────────────────────────────────────────────┐
│              STATE SCOPES                    │
├──────────────────────────────────────────────┤
│  Session State → Current conversation        │
│  User State → Persists across sessions       │
│  App State → Shared globally                 │
└──────────────────────────────────────────────┘
```

### 6. Observability Pillars

- **Logs**: What happened at a specific moment
- **Traces**: Why a result occurred (full execution path)
- **Metrics**: How well the agent performs overall

## Recommended Reading

### Official Documentation
- [ADK Documentation](https://google.github.io/adk-docs/) - Primary reference
- [ADK Quickstart for Python](https://google.github.io/adk-docs/get-started/python/)
- [Agents Overview](https://google.github.io/adk-docs/agents/)
- [Tools Overview](https://google.github.io/adk-docs/tools/)

### Whitepapers
- [Introduction to Agents and Agent Architectures](https://www.kaggle.com/whitepaper-agents) - Core concepts
- [Agent Tools & Interoperability with MCP](https://www.kaggle.com/whitepaper-agent-tools) - Tool integration
- [Agent Memory Whitepaper](https://www.kaggle.com/whitepaper-agent-memory) - State management

### Architecture Guides
- [Multi-Agent Design Patterns](https://cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
- [A2A Protocol Specification](https://a2a-protocol.org/)
- [MCP Specification](https://github.com/modelcontextprotocol/)

### Code Resources
- [ADK Python GitHub](https://github.com/google/adk-python)
- [ADK Samples](https://github.com/google/adk-samples) - 1,000+ examples
- [Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack)

## Assignment

### Part 1: Build Your First Agent (Beginner)
Create a simple agent with Google Search that can answer current events questions.

**Questions to consider:**
- What happens when you ask about events after the model's training cutoff?
- How does the agent decide when to use the search tool?

### Part 2: Multi-Agent Content Pipeline (Intermediate)
Design a content creation system using Sequential agents:
1. Research Agent → gathers information
2. Writer Agent → creates draft
3. Editor Agent → refines output

**Questions to consider:**
- How do agents share state between steps?
- What happens if one agent fails mid-pipeline?

### Part 3: Parallel Research System (Advanced)
Build a system that researches multiple topics concurrently using Parallel agents, then aggregates results.

**Questions to consider:**
- When should you use parallel vs sequential execution?
- How do you handle different completion times?

## Advanced Build

### Enterprise Customer Support System

Build a production-ready support system demonstrating all 5 days of learning:

1. **Multi-agent architecture**: Coordinator routes to specialists (billing, technical, general)
2. **Tool integration**: CRM lookup, knowledge base search, ticket creation
3. **Session persistence**: Remember user context across conversations
4. **Memory service**: Learn from resolved tickets
5. **A2A integration**: Connect to external product catalog service
6. **Evaluation**: Quality scoring with LLM-as-judge
7. **Deployment**: Cloud Run with monitoring

**Success Criteria:**
- Handles at least 3 customer intents
- Maintains context across 5+ turns
- Falls back gracefully on unknown queries
- Passes 80% of evaluation scenarios

## Session Structure (5 Days)

| Day | Focus | Key Notebooks |
|-----|-------|---------------|
| 1 | Introduction & Multi-Agent Patterns | `day-1a-from-prompt-to-action`, `day-1b-agent-architectures` |
| 2 | Tools & MCP Integration | `day-2a-agent-tools`, `day-2b-agent-tools-best-practices` |
| 3 | Sessions & Memory | `day-3a-agent-sessions`, `day-3b-agent-memory` |
| 4 | Observability & Evaluation | `day-4a-agent-observability`, `day-4b-agent-evaluation` |
| 5 | A2A & Deployment | `day-5a-agent2agent-communication`, `day-5b-agent-deployment` |

---

*Source: Kaggle 5-Day AI Agents Course with Google ADK*
