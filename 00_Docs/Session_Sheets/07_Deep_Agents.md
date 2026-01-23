# Session 7: Deep Agents

> Build agents that can plan, use subagents, and leverage file systems for complex tasks

---

## Goal

Understand how to build complex agents that operate over longer time horizons using the four key elements of Deep Agents: planning, context management, subagent spawning, and long-term memory.

---

## Learning Outcomes

By the end of this session, you will be able to:

1. **Explain** when to use Deep Agents vs. simple agents or custom LangGraph workflows
2. **Identify** the four key elements that distinguish Deep Agents from simple agents
3. **Implement** task planning with TodoListMiddleware
4. **Use** FilesystemMiddleware to manage agent context effectively
5. **Spawn** subagents for context isolation using the task tool
6. **Configure** persistent memory with LangGraph Store
7. **Create** skill.md files that agents can discover and load dynamically

---

## Tools Introduced

| Tool | Description |
|------|-------------|
| **Deep Agents** | Standalone library for building agents with planning, filesystem, and subagent capabilities |
| **deepagents-cli** | Open source coding assistant that runs in terminal with persistent memory |

---

## Key Concepts

### What are Deep Agents?

Deep Agents are LLM-based systems designed for complex, long-horizon tasks that require more than simple tool-calling loops. They are built on LangGraph and inspired by applications like Claude Code, Deep Research, and Manus.

> **"Deep agents are LLM-based systems that excel at complex, long-horizon tasks by moving beyond simple tool-calling loops into more sophisticated architectures."**
> — LangChain Blog

**When to use Deep Agents:**
- Handle complex, multi-step tasks requiring planning and decomposition
- Manage large amounts of context through file system tools
- Delegate work to specialized subagents for context isolation
- Persist memory across conversations and threads

**When NOT to use Deep Agents:**
- Simple, single-turn tasks → Use `create_agent()`
- Custom workflow logic → Use LangGraph directly

### The Four Elements

Deep Agents are built on four foundational elements:

1. **Detailed System Prompt** - Comprehensive instructions with examples guiding agent behavior
2. **Planning Tool** - A todo list mechanism (`write_todos`) that maintains task focus
3. **Sub-agents** - Spawnable specialized agents for isolated task handling
4. **File System** - Shared workspace for note-taking and memory management

### Middleware Architecture

Deep Agents use a modular middleware architecture. When you create a deep agent with `create_deep_agent`, three middleware components are automatically attached:

- **TodoListMiddleware** - Provides the `write_todos` planning tool
- **FilesystemMiddleware** - Provides file system tools (`ls`, `read_file`, `write_file`, `edit_file`)
- **SubAgentMiddleware** - Provides the `task` tool for spawning subagents

Middleware is composable—you can add as many or as few as needed.

### Context Quarantine with Subagents

> **"Subagents solve the context bloat problem. When agents use tools with large outputs, the context window fills up quickly with intermediate results."**
> — LangChain Documentation

Subagents isolate detailed work—the main agent receives only the final result, keeping its context clean while still going deep on specific subtasks.

### Skills: Dynamic Capability Loading

Skills are folders containing a `SKILL.md` file that agents can discover and load dynamically. This progressive disclosure approach avoids context bloat by loading only metadata initially, then full instructions when needed.

> **"Skills are simply folders containing a SKILL.md file along with any associated files that agents can discover and load dynamically."**
> — LangChain Blog

### Long-term Memory

By default, the filesystem is stored in agent state and is transient to a single thread. You can extend deep agents with long-term memory using a `CompositeBackend` that routes specific paths to persistent storage:

- `/memories/*` → Persistent Store (across threads)
- Other paths → Ephemeral State (single thread)

---

## Recommended Reading

### Required

| Resource | Description |
|----------|-------------|
| [Deep Agents](https://blog.langchain.com/deep-agents/) | Introduction to deep agents and the four key elements |
| [The Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) | Anthropic's approach to building autonomous agents |
| [Doubling down on DeepAgents](https://blog.langchain.com/doubling-down-on-deepagents/) | DeepAgents 0.2 improvements and architectural decisions |
| [Using skills with DeepAgents](https://blog.langchain.com/using-skills-with-deep-agents/) | Dynamic skill loading and SKILL.md format |

### Official Documentation

| Resource | URL |
|----------|-----|
| Deep Agents Overview | https://docs.langchain.com/oss/python/deepagents/overview |
| Deep Agents Middleware | https://docs.langchain.com/oss/python/deepagents/middleware |
| Subagents | https://docs.langchain.com/oss/python/deepagents/subagents |
| Long-term Memory | https://docs.langchain.com/oss/python/deepagents/long-term-memory |
| Deep Agents CLI | https://docs.langchain.com/oss/python/deepagents/cli |
| Skills Architecture | https://docs.langchain.com/oss/python/langchain/multi-agent/skills |

### Code Repository

| Repository | Description |
|------------|-------------|
| [deep-agents-from-scratch](https://github.com/langchain-ai/deep-agents-from-scratch) | Tutorial repository for Deep Agents course |

#### Notebook Progression

The repository contains five notebooks that progressively build toward a production-ready deep agent:

| Notebook | Focus | Concepts Introduced |
|----------|-------|---------------------|
| `0_create_agent.ipynb` | Basic ReAct agent | Baseline agent loop, tool binding, simple tool calling |
| `1_todo.ipynb` | Task planning | `write_todos` tool, TodoListMiddleware, task decomposition |
| `2_files.ipynb` | Virtual filesystem | FilesystemMiddleware, context management, note-taking |
| `3_subagents.ipynb` | Context isolation | SubAgentMiddleware, `task` tool, delegation patterns |
| `4_full_agent.ipynb` | Production agent | All capabilities combined, long-term memory, complete architecture |

> **Recommended order**: Work through notebooks 0→4 sequentially. Each builds on concepts from the previous notebook.

---

## Assignment

**Build an agent that can plan, manage context, delegate, and remember**

### Prerequisites

Complete the tutorial notebooks in order before starting the assignment:

1. **Start with `0_create_agent.ipynb`** — Understand the baseline ReAct agent pattern
2. **Then `1_todo.ipynb`** — Learn how planning changes agent behavior
3. **Then `2_files.ipynb`** — Explore filesystem-based context management
4. **Then `3_subagents.ipynb`** — Observe context isolation in action

These notebooks provide the foundation needed for the main assignment.

### Requirements

1. Create a deep agent using `create_deep_agent`
2. Implement task planning with the `write_todos` tool
3. Use the filesystem to store and retrieve context
4. Spawn at least one subagent to handle a subtask
5. Configure persistent memory for cross-thread state

### Deliverables

- [ ] Working deep agent with all four capabilities
- [ ] Documentation of your agent's planning strategy
- [ ] Demonstration of context quarantine with subagents
- [ ] Evidence of memory persistence across threads

> **Hint**: The `4_full_agent.ipynb` notebook demonstrates the complete architecture. Study how it combines all four elements before building your own.

---

## Advanced Build

**Create a skill.md file that the agent can discover and load dynamically**

### Requirements

1. Create a skills directory structure:
   ```
   ~/.deepagents/agent/skills/
   └── my-skill/
       ├── SKILL.md
       └── resources/
   ```

2. Write a `SKILL.md` file with:
   - YAML frontmatter (name, description, triggers)
   - Detailed instructions in Markdown
   - Example usage patterns

3. Configure your agent to discover and use the skill

4. Demonstrate progressive disclosure (metadata loads first, full content on demand)

### Bonus

- Create multiple skills that work together
- Implement skill-specific tools
- Add skill versioning

---

## Session Flow

### Breakout Room 1 (Tasks 1-5)

**Focus**: Notebooks `0_create_agent.ipynb` through `2_files.ipynb`

- [ ] Install `deepagents` package
- [ ] Work through `0_create_agent.ipynb` — baseline ReAct agent
- [ ] Work through `1_todo.ipynb` — observe how planning changes behavior
- [ ] Work through `2_files.ipynb` — explore filesystem middleware
- [ ] **Activity**: Compare agent behavior with and without the todo list. What changes? Why does planning improve performance on multi-step tasks?

### Breakout Room 2 (Tasks 6-10)

**Focus**: Notebooks `3_subagents.ipynb` and `4_full_agent.ipynb`

- [ ] Work through `3_subagents.ipynb` — context isolation patterns
- [ ] Study `4_full_agent.ipynb` — complete architecture reference
- [ ] Configure subagents for delegation
- [ ] Set up persistent memory with Store
- [ ] **Activity**: Build your own deep agent combining all four elements. How does the agent's architecture handle the complexity tradeoffs between context size and capability?

---

## Connections to Other Sessions

| Session | Connection |
|---------|------------|
| Session 3: The Agent Loop | Deep agents extend the basic agent loop with planning |
| Session 4: Agentic RAG | Deep agents can use RAG as a tool or subagent |
| Session 5: Multi-Agent Systems | Subagent spawning builds on multi-agent patterns |
| Session 6: Agent Memory | Long-term memory extends Session 6 concepts |
| Session 8: Deep Research | Deep research is a specialized deep agent application |

---

*Session Sheet created for AIE9 Session 7: Deep Agents*
*Last updated: January 2026*
