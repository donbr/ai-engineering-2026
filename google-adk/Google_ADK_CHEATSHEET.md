# Google ADK Cheatsheet

## 1. Quick Reference

```
pip install google-adk                    # Install ADK
adk create my-agent --model gemini-2.5-flash  # Create new agent
adk web                                   # Start dev UI
adk run                                   # Run agent CLI
```

**Core Imports:**
```python
from google.adk.agents import Agent, SequentialAgent, ParallelAgent, LoopAgent
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search, AgentTool, FunctionTool
from google.adk.sessions import InMemorySessionService
```

---

## 2. Concept Overview

### What Makes an Agent?

| Component | Role | ADK Equivalent |
|-----------|------|----------------|
| Model (Brain) | Reasoning engine | `Gemini()` model |
| Tools (Hands) | External actions | `google_search`, `FunctionTool` |
| Orchestration | Loop management | `Runner`, workflow agents |
| Memory | State persistence | `SessionService`, `MemoryService` |

### The Agentic Loop

```
┌────────────────────────────────────────┐
│  1. GET MISSION → Receive user goal   │
│  2. SCAN SCENE → Gather context       │
│  3. THINK → Plan next action          │
│  4. ACT → Execute tool call           │
│  5. OBSERVE → Process result          │
│         ↓ Loop until done             │
└────────────────────────────────────────┘
```

---

## 3. Setup Requirements

**Environment Variables:**
```bash
export GOOGLE_API_KEY="your-api-key"
# OR for Vertex AI:
export GOOGLE_CLOUD_PROJECT="your-project"
export GOOGLE_CLOUD_LOCATION="us-central1"
```

**Project Structure:**
```
my-agent/
├── __init__.py          # Package marker
├── agent.py             # Agent definition (root_agent)
└── .env                 # Environment variables
```

**Minimum agent.py:**
```python
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini

root_agent = Agent(
    name="my_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction="You are a helpful assistant.",
)
```

---

## 4. Core Concepts

### Agent Types

| Type | Use Case | Key Property |
|------|----------|--------------|
| `Agent` | LLM-driven decisions | `tools=[]` |
| `SequentialAgent` | Fixed pipeline | `sub_agents=[]` |
| `ParallelAgent` | Concurrent tasks | `sub_agents=[]` |
| `LoopAgent` | Iterative refinement | `max_iterations` |

### State Scopes

| Scope | Key Format | Persistence |
|-------|------------|-------------|
| Session | `"key"` | Current conversation |
| User | `"user:key"` | Across sessions for user |
| App | `"app:key"` | Global across all users |

### Tool Types

| Type | Purpose | Example |
|------|---------|---------|
| Built-in | Pre-integrated | `google_search` |
| FunctionTool | Wrap Python | `FunctionTool(my_func)` |
| AgentTool | Agent as tool | `AgentTool(sub_agent)` |
| MCP | External servers | `McpToolset.from_server()` |

---

## 5. Common Patterns

### Basic Agent with Tool

```python
from google.adk.agents import Agent
from google.adk.tools import google_search

agent = Agent(
    name="search_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction="Search for current information when asked.",
    tools=[google_search],
)
```

### Custom Function Tool

```python
def get_weather(city: str) -> str:
    """Get weather for a city."""
    return f"Weather in {city}: Sunny, 72°F"

agent = Agent(
    name="weather_agent",
    tools=[FunctionTool(get_weather)],
)
```

### Sequential Pipeline

```python
research = Agent(name="researcher", output_key="findings")
writer = Agent(
    name="writer",
    instruction="Write based on: {findings}",
    output_key="draft"
)
editor = Agent(
    name="editor",
    instruction="Edit: {draft}",
    output_key="final"
)

pipeline = SequentialAgent(
    name="content_pipeline",
    sub_agents=[research, writer, editor],
)
```

### Parallel Execution

```python
tech = Agent(name="tech_researcher", output_key="tech_data")
health = Agent(name="health_researcher", output_key="health_data")
finance = Agent(name="finance_researcher", output_key="finance_data")

aggregator = Agent(
    instruction="Combine: {tech_data}, {health_data}, {finance_data}"
)

system = SequentialAgent(
    sub_agents=[
        ParallelAgent(sub_agents=[tech, health, finance]),
        aggregator,
    ]
)
```

### Loop with Exit Condition

```python
def exit_loop():
    """Call when task is complete."""
    return {"status": "done"}

refiner = Agent(
    name="refiner",
    instruction="If critique says APPROVED, call exit_loop. Else improve.",
    tools=[FunctionTool(exit_loop)],
)

loop = LoopAgent(
    sub_agents=[critic, refiner],
    max_iterations=3,
)
```

---

## 6. Architecture Diagrams

### Single Agent Architecture

```
┌──────────────────────────────────────────┐
│               AGENT                       │
├──────────────────────────────────────────┤
│  ┌─────────────┐   ┌─────────────┐      │
│  │   Model     │   │   Tools     │      │
│  │  (Gemini)   │   │ (Search,    │      │
│  │             │   │  Functions) │      │
│  └──────┬──────┘   └──────┬──────┘      │
│         │                 │              │
│         └────────┬────────┘              │
│                  ▼                       │
│         ┌────────────────┐               │
│         │  Orchestration │               │
│         │    (Runner)    │               │
│         └────────────────┘               │
└──────────────────────────────────────────┘
```

### Multi-Agent System

```
┌─────────────────────────────────────────────────────┐
│              ROOT COORDINATOR                        │
├─────────────────────────────────────────────────────┤
│                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────┐ │
│  │  Research    │  │   Writer     │  │  Editor   │ │
│  │  Agent       │→→│   Agent      │→→│  Agent    │ │
│  │              │  │              │  │           │ │
│  └──────────────┘  └──────────────┘  └───────────┘ │
│         │                 │                │        │
│         └─────────────────┼────────────────┘        │
│                           ▼                         │
│                  ┌────────────────┐                 │
│                  │ Shared State   │                 │
│                  │ (output_key)   │                 │
│                  └────────────────┘                 │
└─────────────────────────────────────────────────────┘
```

### A2A Communication

```
┌───────────────────┐         ┌───────────────────┐
│  Your Agent       │         │  External Agent   │
│  (Consumer)       │  A2A    │  (Server)         │
│                   │ ─────→  │                   │
│  RemoteA2aAgent   │ ←─────  │  to_a2a()         │
└───────────────────┘         └───────────────────┘
```

---

## 7. Best Practices

### Tool Design

- **Document thoroughly**: Descriptions help LLM choose correctly
- **Keep granular**: One tool = one action
- **Design concise output**: Minimize token usage
- **Use type hints**: Enable proper validation
- **Return structured data**: JSON over free text

### Agent Design

- **Start simple**: Single agent, then add complexity
- **Decompose specialists**: Don't overload one agent
- **Use output_key**: Share state between agents
- **Set max_iterations**: Prevent infinite loops
- **Include guardrails**: Validate inputs/outputs

### Memory Management

- **Session for conversation**: Short-term context
- **User state for preferences**: Cross-session persistence
- **App state sparingly**: Only truly global data
- **Use MemoryService**: Long-term knowledge retrieval

---

## 8. Common Issues

| Issue | Symptom | Solution |
|-------|---------|----------|
| 429 Rate Limit | Too many requests | Add retry config, slow down |
| Tool not called | Agent ignores tool | Improve instruction, check tool docs |
| Context overflow | Long conversations | Use context compaction |
| State not persisting | Data lost | Check session_id consistency |
| Agent loops forever | No termination | Add exit conditions, max_iterations |
| MCP connection fails | Server not found | Verify server running, check URL |

---

## 9. Debugging Tips

### Enable Logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Use ADK Web UI

```bash
adk web --port 8000
# Access at http://localhost:8000
# View traces, tool calls, responses
```

### Inspect Session State

```python
session = await session_service.get_session(
    app_name="my-app",
    user_id="user-1",
    session_id="session-1"
)
print(session.state)
```

### Check Tool Availability

```python
# In agent definition, verify tools list
print(f"Agent has {len(agent.tools)} tools")
for tool in agent.tools:
    print(f"  - {tool.name}")
```

---

## 10. Interview Questions

1. **What distinguishes an AI agent from a standard LLM?**
   - Agent can reason, take actions via tools, and observe results
   - LLM just generates text from static knowledge

2. **When would you use SequentialAgent vs ParallelAgent?**
   - Sequential: Steps depend on each other (pipeline)
   - Parallel: Independent tasks (concurrent research)

3. **How do agents share state in ADK?**
   - Via `output_key` parameter storing to session state
   - Next agent accesses with `{key}` in instruction template

4. **What is the A2A protocol used for?**
   - Cross-framework, cross-language, cross-organization agent communication
   - Enables agent interoperability over networks

5. **How do you prevent an agent from looping forever?**
   - Set `max_iterations` on LoopAgent
   - Create explicit exit_loop function tool
   - Add termination conditions in critic agent

---

## 11. Resources & Links

### Official Documentation
- [ADK Docs](https://google.github.io/adk-docs/)
- [ADK GitHub](https://github.com/google/adk-python)
- [ADK Samples](https://github.com/google/adk-samples)

### Google Cloud
- [Vertex AI Agent Engine](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview)
- [Cloud Run Deployment](https://codelabs.developers.google.com/deploy-manage-observe-adk-cloud-run)

### Protocols
- [A2A Protocol](https://a2a-protocol.org/)
- [MCP Specification](https://github.com/modelcontextprotocol/)

### Whitepapers
- [Introduction to Agents](https://www.kaggle.com/whitepaper-agents)
- [Agent Tools & MCP](https://www.kaggle.com/whitepaper-agent-tools)
- [Agent Memory](https://www.kaggle.com/whitepaper-agent-memory)

---

## 12. Key Takeaways

1. **Agents = LLMs + Tools + Orchestration** in a think-act-observe loop

2. **ADK is code-first**: Design patterns from software engineering apply

3. **Multi-agent > Monolithic**: Specialized agents collaborate better

4. **State has scopes**: Session (conversation), User (persistence), App (global)

5. **Three workflow patterns**: Sequential (pipeline), Parallel (concurrent), Loop (iterative)

6. **Observability is critical**: Logs, traces, metrics for debugging

7. **A2A for interop**: Cross-framework, cross-organization communication

8. **Start simple**: One agent, one tool, then add complexity

9. **Evaluation matters**: LLM-as-judge for quality scoring

10. **Production needs services**: Session persistence, memory, deployment infrastructure

---

*Cheatsheet Version: 1.0 | Based on Kaggle 5-Day AI Agents Course*
