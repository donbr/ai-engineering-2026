# Session 7 Cheatsheet: Deep Agents

> Build agents that can plan, use subagents, and leverage file systems for complex tasks

---

## Quick Reference

| Concept | Definition | Key API/Pattern |
|---------|------------|-----------------|
| Deep Agent | Agent for complex, long-horizon tasks | `create_deep_agent()` |
| Four Elements | System prompt, planning, subagents, filesystem | Middleware stack |
| TodoListMiddleware | Task planning and decomposition | `write_todos` tool |
| FilesystemMiddleware | Context offloading to virtual files | `ls`, `read_file`, `write_file`, `edit_file` |
| SubAgentMiddleware | Spawn isolated agents for subtasks | `task` tool |
| Context Quarantine | Isolate subagent work from main context | Subagent result summarization |
| Skills | Dynamic capability loading | `SKILL.md` files |
| Long-term Memory | Persistent storage across threads | `CompositeBackend` + `Store` |

---

## Setup Requirements

### Dependencies
```bash
pip install deepagents langchain langgraph langsmith
```

### Environment Variables
```python
import os
os.environ["OPENAI_API_KEY"] = "your-key"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-langsmith-key"
os.environ["LANGCHAIN_PROJECT"] = "AIE9-Session7"
```

### CLI Installation
```bash
pip install deepagents-cli
deepagents --help
```

---

## Tutorial Notebooks

The [deep-agents-from-scratch](https://github.com/langchain-ai/deep-agents-from-scratch) repository provides hands-on tutorials that progressively build a complete deep agent system.

### Notebook Overview

| Notebook | Title | Concepts Covered | Section |
|----------|-------|------------------|---------|
| `0_create_agent.ipynb` | Basic ReAct Agent | Baseline agent, tool calling, ReAct loop | Section 1 |
| `1_todo.ipynb` | Task Planning | `write_todos` tool, task decomposition | Section 3 |
| `2_files.ipynb` | Virtual Filesystem | `ls`, `read_file`, `write_file`, context offloading | Section 4 |
| `3_subagents.ipynb` | Subagent Delegation | Context isolation, `task` tool, result summarization | Section 5 |
| `4_full_agent.ipynb` | Full Research Agent | Complete integration, production patterns | Section 10 |

### Learning Path

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TUTORIAL PROGRESSION                              │
│                                                                     │
│   0_create_agent.ipynb                                              │
│   (Baseline ReAct)                                                  │
│        │                                                            │
│        v                                                            │
│   1_todo.ipynb           2_files.ipynb                              │
│   (Planning)             (Filesystem)                               │
│        │                      │                                     │
│        └──────────┬───────────┘                                     │
│                   │                                                 │
│                   v                                                 │
│            3_subagents.ipynb                                        │
│            (Context Isolation)                                      │
│                   │                                                 │
│                   v                                                 │
│            4_full_agent.ipynb                                       │
│            (Production Agent)                                       │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Notebook URLs

- [0_create_agent.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/0_create_agent.ipynb) - Start here for baseline understanding
- [1_todo.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/1_todo.ipynb) - Add planning capabilities
- [2_files.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/2_files.ipynb) - Add virtual filesystem
- [3_subagents.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/3_subagents.ipynb) - Add delegation
- [4_full_agent.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/4_full_agent.ipynb) - Complete production agent

---

## 1. What are Deep Agents?

**Tutorial**: Start with [0_create_agent.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/0_create_agent.ipynb) to build a baseline ReAct agent before adding deep agent capabilities.

### Industry Definition
> **"Deep agents are LLM-based systems that excel at complex, long-horizon tasks by moving beyond simple tool-calling loops into more sophisticated architectures."**
> — LangChain Blog [[1]](https://blog.langchain.com/deep-agents/)

### Key Characteristics
- **Plan** over longer time horizons
- **Manage** large amounts of context
- **Delegate** work to specialized subagents
- **Persist** memory across conversations

### Inspiration
Built on LangGraph, inspired by:
- Claude Code (Anthropic)
- Deep Research (OpenAI)
- Manus (startup)

### When to Use What

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AGENT SELECTION DECISION                         │
│                                                                     │
│   Simple task?                                                      │
│       YES → create_agent()                                          │
│       NO  ↓                                                         │
│                                                                     │
│   Custom workflow logic needed?                                     │
│       YES → LangGraph (build from scratch)                          │
│       NO  ↓                                                         │
│                                                                     │
│   Complex, multi-step, long-running?                                │
│       YES → Deep Agents (create_deep_agent)                         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Official Docs**: [Deep Agents Overview](https://docs.langchain.com/oss/python/deepagents/overview) [[2]](https://docs.langchain.com/oss/python/deepagents/overview)

---

## 2. The Four Elements

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    FOUR ELEMENTS OF DEEP AGENTS                      │
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐                          │
│  │  1. DETAILED    │  │  2. PLANNING    │                          │
│  │  SYSTEM PROMPT  │  │     TOOL        │                          │
│  │  (Instructions  │  │  (write_todos)  │                          │
│  │   with examples)│  │                 │                          │
│  └─────────────────┘  └─────────────────┘                          │
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐                          │
│  │  3. SUB-AGENTS  │  │  4. FILE SYSTEM │                          │
│  │  (task tool for │  │  (Context mgmt  │                          │
│  │   delegation)   │  │   & memory)     │                          │
│  └─────────────────┘  └─────────────────┘                          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Why Each Element Matters

| Element | Problem Solved | Mechanism | Tutorial Notebook |
|---------|---------------|-----------|-------------------|
| System Prompt | Behavior guidance | Detailed instructions + examples | `0_create_agent.ipynb` |
| Planning Tool | Task focus | No-op tool for context engineering | `1_todo.ipynb` |
| Sub-agents | Context bloat | Isolated execution, summarized results | `3_subagents.ipynb` |
| File System | Context overflow | Offload data to virtual filesystem | `2_files.ipynb` |

**Blog Post**: [Deep Agents](https://blog.langchain.com/deep-agents/) [[1]](https://blog.langchain.com/deep-agents/)

---

## 3. Planning and Task Decomposition

**Tutorial**: See [1_todo.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/1_todo.ipynb) for implementing the `write_todos` planning tool.

### The TodoListMiddleware

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PLANNING WORKFLOW                                 │
│                                                                     │
│   ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐ │
│   │  Break   │ --> │ Execute  │ --> │  Check   │ --> │  Adapt   │ │
│   │  Down    │     │   Step   │     │ Progress │     │   Plan   │ │
│   └──────────┘     └──────────┘     └──────────┘     └──────────┘ │
│        │                                                    │       │
│        └────────────────────────────────────────────────────┘       │
│                         (Repeat until done)                         │
└─────────────────────────────────────────────────────────────────────┘
```

### Built-in Tool
```python
# write_todos is automatically available
# Agent uses it to track task progress
```

### Why Planning Matters
The todo list is a "no-op" tool—it doesn't execute actions but provides **context engineering** that helps the agent maintain focus across long tasks.

**Official Docs**: [Deep Agents Middleware](https://docs.langchain.com/oss/python/deepagents/middleware) [[3]](https://docs.langchain.com/oss/python/deepagents/middleware)

---

## 4. Context Management with Filesystem

**Tutorial**: See [2_files.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/2_files.ipynb) for implementing virtual filesystem operations.

### The FilesystemMiddleware

> **"The key design principle behind the Claude Agent SDK is to give your agents a computer, allowing them to work like humans do."**
> — Anthropic Engineering [[4]](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)

### Available Tools

| Tool | Purpose |
|------|---------|
| `ls` | List files in directory |
| `read_file` | Read file contents |
| `write_file` | Write content to file |
| `edit_file` | Modify existing file |

### Context Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CONTEXT MANAGEMENT FLOW                           │
│                                                                     │
│   Large Tool Result                                                 │
│        │                                                            │
│        v                                                            │
│   ┌──────────┐     ┌──────────┐     ┌──────────┐                   │
│   │ Receive  │ --> │  Store   │ --> │ Retrieve │ --> Use           │
│   │  Data    │     │  in File │     │  As Needed│                   │
│   └──────────┘     └──────────┘     └──────────┘                   │
│                                                                     │
│   (Prevents context window overflow)                                │
└─────────────────────────────────────────────────────────────────────┘
```

### Use Cases
- Store intermediate results
- Cache expensive computations
- Maintain notes across long sessions
- Share data between main agent and subagents

---

## 5. Subagent Spawning

**Tutorial**: See [3_subagents.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/3_subagents.ipynb) for implementing context isolation through delegation.

### The SubAgentMiddleware

> **"Subagents solve the context bloat problem. When agents use tools with large outputs, the context window fills up quickly with intermediate results."**
> — LangChain Docs [[5]](https://docs.langchain.com/oss/python/deepagents/subagents)

### Context Quarantine Pattern

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CONTEXT QUARANTINE                                │
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │                     MAIN AGENT                               │  │
│   │   Context: Clean, focused on high-level task                 │  │
│   │                                                              │  │
│   │        │ task("research X")                                  │  │
│   │        v                                                     │  │
│   │   ┌─────────────────┐                                        │  │
│   │   │    SUBAGENT     │ <-- Isolated context                   │  │
│   │   │                 │                                        │  │
│   │   │ - Web searches  │                                        │  │
│   │   │ - File reads    │                                        │  │
│   │   │ - API calls     │                                        │  │
│   │   │                 │                                        │  │
│   │   └────────┬────────┘                                        │  │
│   │            │                                                 │  │
│   │            v                                                 │  │
│   │   [Summarized Result] <-- Only final output returns          │  │
│   │                                                              │  │
│   └─────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

### Subagent Types

| Type | Purpose |
|------|---------|
| Research | Information gathering (web, databases) |
| Code | Programming tasks (isolated execution) |
| General | Flexible subtask handling |

### Benefits
- Main agent stays focused
- Large intermediate data stays isolated
- Specialized instructions per subagent
- Parallel execution possible

**Official Docs**: [Subagents](https://docs.langchain.com/oss/python/deepagents/subagents) [[5]](https://docs.langchain.com/oss/python/deepagents/subagents)

---

## 6. Long-term Memory

### Memory Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    MEMORY ROUTING                                    │
│                                                                     │
│   Deep Agent                                                        │
│        │                                                            │
│        v                                                            │
│   ┌──────────────────┐                                              │
│   │   Path Router    │                                              │
│   └────────┬─────────┘                                              │
│            │                                                        │
│     ┌──────┴──────┐                                                 │
│     │             │                                                 │
│     v             v                                                 │
│ /memories/*    other paths                                          │
│     │             │                                                 │
│     v             v                                                 │
│ ┌─────────┐  ┌─────────┐                                            │
│ │  Store  │  │  State  │                                            │
│ │ Backend │  │ Backend │                                            │
│ └────┬────┘  └────┬────┘                                            │
│      │            │                                                 │
│      v            v                                                 │
│ Persistent   Ephemeral                                              │
│ (across      (single                                                │
│  threads)     thread)                                               │
└─────────────────────────────────────────────────────────────────────┘
```

### Store Options

| Backend | Persistence | Use Case |
|---------|-------------|----------|
| State Backend | Single thread | Default, transient |
| InMemoryStore | Cross-thread | Development |
| Redis Store | Cross-thread | Production |
| Custom Backend | Configurable | Database integration |

### CompositeBackend
Routes different paths to different storage:
- `/memories/*` → Persistent (Store)
- Everything else → Ephemeral (State)

**Official Docs**: [Long-term Memory](https://docs.langchain.com/oss/python/deepagents/long-term-memory) [[6]](https://docs.langchain.com/oss/python/deepagents/long-term-memory)

---

## 7. The Middleware Architecture

### Composition Model

```
┌─────────────────────────────────────────────────────────────────────┐
│                    MIDDLEWARE COMPOSITION                            │
│                                                                     │
│   create_deep_agent()                                               │
│        │                                                            │
│        ├──────────────────┬──────────────────┐                      │
│        │                  │                  │                      │
│        v                  v                  v                      │
│   ┌──────────┐      ┌──────────┐      ┌──────────┐                 │
│   │ TodoList │      │Filesystem│      │ SubAgent │                 │
│   │Middleware│      │Middleware│      │Middleware│                 │
│   └────┬─────┘      └────┬─────┘      └────┬─────┘                 │
│        │                  │                  │                      │
│        └──────────────────┼──────────────────┘                      │
│                           │                                         │
│                           v                                         │
│                    ┌──────────────┐                                 │
│                    │ Agent Tools  │                                 │
│                    └──────────────┘                                 │
│                                                                     │
│   (Middleware is composable - add/remove as needed)                 │
└─────────────────────────────────────────────────────────────────────┘
```

### Each Middleware Provides

| Middleware | Tools Added | Tutorial Notebook |
|------------|-------------|-------------------|
| TodoListMiddleware | `write_todos` | `1_todo.ipynb` |
| FilesystemMiddleware | `ls`, `read_file`, `write_file`, `edit_file` | `2_files.ipynb` |
| SubAgentMiddleware | `task` | `3_subagents.ipynb` |

### Customization
You can use any middleware independently or create custom middleware for specific needs.

---

## 8. Skills: Dynamic Capability Loading

### What are Skills?

> **"Skills are simply folders containing a SKILL.md file along with any associated files that agents can discover and load dynamically."**
> — LangChain Blog [[7]](https://blog.langchain.com/using-skills-with-deep-agents/)

### Skill Structure

```
~/.deepagents/agent/skills/
└── my-skill/
    ├── SKILL.md          # Skill definition
    └── resources/        # Associated files
        ├── template.txt
        └── data.json
```

### SKILL.md Format

```markdown
---
name: my-skill
description: Brief description
triggers:
  - "keyword1"
  - "keyword2"
---

# My Skill

Detailed instructions for the agent...

## Examples

Example usage patterns...
```

### Progressive Disclosure

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PROGRESSIVE DISCLOSURE                            │
│                                                                     │
│   1. DISCOVER                                                       │
│      Agent sees skill metadata (name, triggers)                     │
│      Context cost: Minimal                                          │
│             │                                                       │
│             v                                                       │
│   2. MATCH TRIGGER                                                  │
│      User request matches skill trigger                             │
│             │                                                       │
│             v                                                       │
│   3. LOAD FULL INSTRUCTIONS                                         │
│      Agent reads complete SKILL.md                                  │
│      Context cost: Only when needed                                 │
│             │                                                       │
│             v                                                       │
│   4. EXECUTE                                                        │
│      Agent follows skill instructions                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Benefits
- **Token efficiency**: Only load what's needed
- **Reduced cognitive load**: Atomic, focused capabilities
- **Team distribution**: Different teams maintain different skills
- **Lightweight composition**: Skills don't conflict

**Blog Post**: [Using skills with DeepAgents](https://blog.langchain.com/using-skills-with-deep-agents/) [[7]](https://blog.langchain.com/using-skills-with-deep-agents/)

---

## 9. The Deep Agents CLI

### Key Capabilities

| Capability | Description |
|------------|-------------|
| File operations | Read, write, edit files |
| Shell execution | Run tests, build, manage deps |
| Web search | Up-to-date information (requires Tavily) |
| HTTP requests | API calls and integrations |
| Task planning | Todo system for tracking |
| Memory | Store/retrieve across sessions |
| Human-in-the-loop | Approval controls |

### Usage

```bash
# Start CLI
deepagents

# List available skills
deepagents skills list

# Run with specific skill
deepagents --skill web-research
```

### Configuration
```
~/.deepagents/
├── agent/
│   ├── skills/        # Skill definitions
│   └── config.yaml    # CLI configuration
└── memories/          # Persistent storage
```

**Official Docs**: [Deep Agents CLI](https://docs.langchain.com/oss/python/deepagents/cli) [[8]](https://docs.langchain.com/oss/python/deepagents/cli)

---

## 10. Production Patterns

**Tutorial**: See [4_full_agent.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/4_full_agent.ipynb) for a complete production-ready research agent integrating all capabilities.

### Backend Configuration

| Environment | Recommended Backend |
|-------------|---------------------|
| Development | InMemoryStore |
| Testing | SQLite Store |
| Production | Redis / PostgreSQL |

### Token Management

**DeepAgents 0.2 Improvements:**
- Large tool result eviction
- Conversation summarization
- Dangling tool call repair

### Error Handling

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ERROR RECOVERY PATTERNS                           │
│                                                                     │
│   Tool Failure                                                      │
│        │                                                            │
│        v                                                            │
│   ┌──────────┐     ┌──────────┐     ┌──────────┐                   │
│   │  Retry   │ --> │  Fallback│ --> │  Escalate│                   │
│   │  (3x)    │     │  Tool    │     │  to Human│                   │
│   └──────────┘     └──────────┘     └──────────┘                   │
│                                                                     │
│   Context Overflow                                                  │
│        │                                                            │
│        v                                                            │
│   ┌──────────┐     ┌──────────┐                                    │
│   │ Evict    │ --> │Summarize │                                    │
│   │ Old Data │     │ Context  │                                    │
│   └──────────┘     └──────────┘                                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Blog Post**: [Doubling down on DeepAgents](https://blog.langchain.com/doubling-down-on-deepagents/) [[9]](https://blog.langchain.com/doubling-down-on-deepagents/)

---

## Code Patterns Reference

### Pattern 1: Basic Deep Agent
```python
from deepagents import create_deep_agent

agent = create_deep_agent(
    model="gpt-4o",
    system_prompt="You are a helpful coding assistant."
)
```

### Pattern 2: With Custom Subagents
```python
from deepagents import create_deep_agent

research_agent = create_deep_agent(
    model="gpt-4o",
    system_prompt="You research topics thoroughly."
)

agent = create_deep_agent(
    model="gpt-4o",
    subagents={"research": research_agent}
)
```

### Pattern 3: With Persistent Memory
```python
from langgraph.store.memory import InMemoryStore

store = InMemoryStore()

agent = create_deep_agent(
    model="gpt-4o",
    store=store
)
```

---

## Common Issues & Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| Context overflow | Too much data in context | Use filesystem to offload |
| Subagent not returning | Task too vague | Improve task description |
| Memory not persisting | Wrong backend | Use CompositeBackend with Store |
| Skills not loading | Wrong path | Check `~/.deepagents/agent/skills/` |
| Slow execution | Too many subagent calls | Batch related work |
| Planning loops | Unclear goals | Improve system prompt |

---

## Breakout Room Tasks Summary

### Breakout Room 1 (Tasks 1-5)
- [ ] Install deepagents package
- [ ] Create first deep agent with `create_deep_agent`
  - **Notebook**: Start with [0_create_agent.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/0_create_agent.ipynb) for baseline ReAct agent
- [ ] Explore built-in tools (todos, filesystem)
  - **Notebook**: [1_todo.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/1_todo.ipynb) for planning
  - **Notebook**: [2_files.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/2_files.ipynb) for filesystem
- [ ] Understand middleware architecture
- [ ] **Activity**: Implement planning for multi-step task

### Breakout Room 2 (Tasks 6-10)
- [ ] Configure subagents for delegation
  - **Notebook**: [3_subagents.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/3_subagents.ipynb) for context isolation
- [ ] Implement context quarantine pattern
- [ ] Set up persistent memory with Store
- [ ] Create a skill.md file
- [ ] **Activity**: Build complete deep agent with all capabilities
  - **Notebook**: [4_full_agent.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/4_full_agent.ipynb) for full production agent

---

## Official Documentation Links

### Deep Agents
- [Deep Agents Overview](https://docs.langchain.com/oss/python/deepagents/overview) [[2]](https://docs.langchain.com/oss/python/deepagents/overview)
- [Middleware](https://docs.langchain.com/oss/python/deepagents/middleware) [[3]](https://docs.langchain.com/oss/python/deepagents/middleware)
- [Subagents](https://docs.langchain.com/oss/python/deepagents/subagents) [[5]](https://docs.langchain.com/oss/python/deepagents/subagents)
- [Long-term Memory](https://docs.langchain.com/oss/python/deepagents/long-term-memory) [[6]](https://docs.langchain.com/oss/python/deepagents/long-term-memory)
- [Deep Agents CLI](https://docs.langchain.com/oss/python/deepagents/cli) [[8]](https://docs.langchain.com/oss/python/deepagents/cli)
- [Customization](https://docs.langchain.com/oss/python/deepagents/customization) [[10]](https://docs.langchain.com/oss/python/deepagents/customization)

### Skills
- [Skills Architecture](https://docs.langchain.com/oss/python/langchain/multi-agent/skills) [[11]](https://docs.langchain.com/oss/python/langchain/multi-agent/skills)
- [SQL Assistant with Skills](https://docs.langchain.com/oss/python/langchain/multi-agent/skills-sql-assistant) [[12]](https://docs.langchain.com/oss/python/langchain/multi-agent/skills-sql-assistant)

### LangGraph Memory
- [Add Memory](https://docs.langchain.com/oss/python/langgraph/add-memory) [[13]](https://docs.langchain.com/oss/python/langgraph/add-memory)
- [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) [[14]](https://docs.langchain.com/oss/python/langgraph/persistence)

### Blog Posts
- [Deep Agents](https://blog.langchain.com/deep-agents/) [[1]](https://blog.langchain.com/deep-agents/)
- [Using skills with DeepAgents](https://blog.langchain.com/using-skills-with-deep-agents/) [[7]](https://blog.langchain.com/using-skills-with-deep-agents/)
- [Doubling down on DeepAgents](https://blog.langchain.com/doubling-down-on-deepagents/) [[9]](https://blog.langchain.com/doubling-down-on-deepagents/)

### External Resources
- [Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) [[4]](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
- [deep-agents-from-scratch](https://github.com/langchain-ai/deep-agents-from-scratch) [[15]](https://github.com/langchain-ai/deep-agents-from-scratch)

### Tutorial Notebooks
- [0_create_agent.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/0_create_agent.ipynb) - Basic ReAct agent (baseline) [[16]](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/0_create_agent.ipynb)
- [1_todo.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/1_todo.ipynb) - Task planning with write_todos [[17]](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/1_todo.ipynb)
- [2_files.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/2_files.ipynb) - Virtual filesystem operations [[18]](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/2_files.ipynb)
- [3_subagents.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/3_subagents.ipynb) - Context isolation through delegation [[19]](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/3_subagents.ipynb)
- [4_full_agent.ipynb](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/4_full_agent.ipynb) - Full production research agent [[20]](https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/4_full_agent.ipynb)

---

## References

1. LangChain Blog. "Deep Agents." July 2025. https://blog.langchain.com/deep-agents/

2. LangChain Documentation. "Deep Agents Overview." https://docs.langchain.com/oss/python/deepagents/overview

3. LangChain Documentation. "Deep Agents Middleware." https://docs.langchain.com/oss/python/deepagents/middleware

4. Anthropic Engineering. "Building Agents with the Claude Agent SDK." September 2025. https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk

5. LangChain Documentation. "Subagents." https://docs.langchain.com/oss/python/deepagents/subagents

6. LangChain Documentation. "Long-term Memory." https://docs.langchain.com/oss/python/deepagents/long-term-memory

7. LangChain Blog. "Using skills with DeepAgents." November 2025. https://blog.langchain.com/using-skills-with-deep-agents/

8. LangChain Documentation. "Deep Agents CLI." https://docs.langchain.com/oss/python/deepagents/cli

9. LangChain Blog. "Doubling down on DeepAgents." October 2025. https://blog.langchain.com/doubling-down-on-deepagents/

10. LangChain Documentation. "Customize Deep Agents." https://docs.langchain.com/oss/python/deepagents/customization

11. LangChain Documentation. "Skills." https://docs.langchain.com/oss/python/langchain/multi-agent/skills

12. LangChain Documentation. "Build a SQL assistant with on-demand skills." https://docs.langchain.com/oss/python/langchain/multi-agent/skills-sql-assistant

13. LangChain Documentation. "Add Memory." https://docs.langchain.com/oss/python/langgraph/add-memory

14. LangChain Documentation. "Persistence." https://docs.langchain.com/oss/python/langgraph/persistence

15. LangChain GitHub. "deep-agents-from-scratch." https://github.com/langchain-ai/deep-agents-from-scratch

16. LangChain GitHub. "0_create_agent.ipynb - Basic ReAct Agent." https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/0_create_agent.ipynb

17. LangChain GitHub. "1_todo.ipynb - Task Planning." https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/1_todo.ipynb

18. LangChain GitHub. "2_files.ipynb - Virtual Filesystem." https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/2_files.ipynb

19. LangChain GitHub. "3_subagents.ipynb - Subagent Delegation." https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/3_subagents.ipynb

20. LangChain GitHub. "4_full_agent.ipynb - Full Production Agent." https://github.com/langchain-ai/deep-agents-from-scratch/blob/main/4_full_agent.ipynb

---

*Cheatsheet created for AIE9 Session 7: Deep Agents*
*Last updated: January 2026*
