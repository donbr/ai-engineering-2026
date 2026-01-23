# Session 7: Deep Agents

## Slide Deck for AIE9 Bootcamp

---

## Slide 1: Title

### Content
# Deep Agents
## Building Agents for Complex, Long-Horizon Tasks

**Session 7 | AI Engineering Bootcamp Cohort 9**

### Visual
```mermaid
graph LR
    subgraph "Deep Agent"
        A[Planning] --> B[Context]
        B --> C[Delegation]
        C --> D[Memory]
    end
    style A fill:#e1f5fe
    style B fill:#fff3e0
    style C fill:#e8f5e9
    style D fill:#fce4ec
```

### Speaker Notes
Welcome to Session 7 on Deep Agents. Today we'll learn how to build agents that can handle complex, multi-step tasks over longer time horizons. This builds on everything we've learned about agents, multi-agent systems, and memory.

---

## Slide 2: Learning Objectives

### Content
## By the End of This Session

1. **Explain** when to use Deep Agents vs. simple agents
2. **Identify** the four key elements of Deep Agents
3. **Implement** task planning with TodoListMiddleware
4. **Use** FilesystemMiddleware for context management
5. **Spawn** subagents for context isolation
6. **Configure** persistent memory with LangGraph Store
7. **Create** skill.md files for dynamic capability loading

### Visual
```mermaid
graph TB
    A[Simple Agent] --> B{Complex Task?}
    B -->|No| A
    B -->|Yes| C[Deep Agent]
    C --> D[Plan]
    C --> E[Context]
    C --> F[Delegate]
    C --> G[Remember]
    style C fill:#e8f5e9
```

### Speaker Notes
These are our learning objectives. Notice we're building on Session 3 (Agent Loop), Session 5 (Multi-Agent), and Session 6 (Memory). Deep Agents integrate all these concepts into a cohesive framework.

---

## Slide 3: What are Deep Agents?

### Content
## Beyond Simple Tool-Calling Loops

> "Deep agents are LLM-based systems that excel at complex, long-horizon tasks by moving beyond simple tool-calling loops into more sophisticated architectures."
> — LangChain Blog

**Built on LangGraph, inspired by:**
- Claude Code (Anthropic)
- Deep Research (OpenAI)
- Manus (startup)

### Visual
```mermaid
graph LR
    subgraph "Simple Agent"
        A1[Query] --> B1[LLM]
        B1 --> C1[Tool]
        C1 --> B1
        B1 --> D1[Response]
    end

    subgraph "Deep Agent"
        A2[Complex Task] --> B2[Plan]
        B2 --> C2[Execute]
        C2 --> D2[Delegate]
        D2 --> E2[Remember]
        E2 --> C2
        C2 --> F2[Complete]
    end

    style B2 fill:#e1f5fe
    style C2 fill:#fff3e0
    style D2 fill:#e8f5e9
    style E2 fill:#fce4ec
```

### Speaker Notes
The key insight is that simple agents work great for simple tasks, but complex tasks need more sophisticated approaches. Deep agents add planning, context management, delegation, and memory to handle longer time horizons.

---

## Slide 4: When to Use What

### Content
## Agent Selection Decision Tree

| Scenario | Solution |
|----------|----------|
| Simple, single-turn task | `create_agent()` |
| Custom workflow logic needed | LangGraph (build from scratch) |
| Complex, multi-step, long-running | `create_deep_agent()` |

### Visual
```mermaid
flowchart TD
    A[New Task] --> B{Simple?}
    B -->|Yes| C[create_agent]
    B -->|No| D{Custom<br/>Workflow?}
    D -->|Yes| E[LangGraph]
    D -->|No| F{Long-running<br/>Complex?}
    F -->|Yes| G[Deep Agent]
    F -->|No| C

    style C fill:#e1f5fe
    style E fill:#fff3e0
    style G fill:#e8f5e9
```

### Speaker Notes
This is the decision framework. Simple tasks: use create_agent. Need custom control flow: use LangGraph directly. Complex, long-running tasks with planning needs: use Deep Agents. Deep Agents is built on LangGraph, so it's not either/or—it's about picking the right level of abstraction.

---

## Slide 5: The Four Elements

### Content
## Foundational Architecture

1. **Detailed System Prompt** - Instructions with examples
2. **Planning Tool** - `write_todos` for task decomposition
3. **Sub-agents** - Spawn specialized agents
4. **File System** - Context management & memory

### Visual
```mermaid
graph TB
    subgraph "Deep Agent Architecture"
        A[System Prompt<br/>Detailed Instructions] --> E[Agent Core]
        B[Planning Tool<br/>write_todos] --> E
        C[Sub-agents<br/>task tool] --> E
        D[File System<br/>Context Store] --> E
    end

    style A fill:#e1f5fe
    style B fill:#fff3e0
    style C fill:#e8f5e9
    style D fill:#fce4ec
    style E fill:#f5f5f5
```

### Speaker Notes
These four elements are what distinguish deep agents from simple agents. Each one solves a specific problem: system prompts guide behavior, planning maintains focus, subagents handle context bloat, and the filesystem stores data. Let's explore each one. (Notebook reference: `0_create_agent.ipynb` establishes the baseline agent architecture.)

---

## Slide 6: Planning and Task Decomposition

### Content
## TodoListMiddleware

**The `write_todos` tool enables:**
- Break complex tasks into steps
- Track progress through execution
- Adapt plans as new information emerges

**Key Insight:** The todo list is a "no-op" tool—it doesn't execute actions but provides **context engineering** that helps maintain focus.

### Visual
```mermaid
graph LR
    A[Complex Task] --> B[Break Down]
    B --> C[Step 1]
    B --> D[Step 2]
    B --> E[Step 3]

    C --> F{Done?}
    F -->|No| C
    F -->|Yes| D

    D --> G{Done?}
    G -->|No| D
    G -->|Yes| E

    E --> H[Complete]

    style B fill:#e1f5fe
    style H fill:#e8f5e9
```

### Speaker Notes
The planning tool is interesting because it's essentially a "no-op"—it doesn't do anything functional. But by forcing the agent to articulate its plan, we provide context engineering that keeps the agent focused across long tasks. This is similar to how humans use todo lists. (Notebook reference: `1_todo.ipynb` implements the TodoListMiddleware and `write_todos` tool.)

---

## Slide 7: Context Management with Filesystem

### Content
## FilesystemMiddleware

> "The key design principle behind the Claude Agent SDK is to give your agents a computer, allowing them to work like humans do."
> — Anthropic Engineering

**Available Tools:**
| Tool | Purpose |
|------|---------|
| `ls` | List files |
| `read_file` | Read contents |
| `write_file` | Store data |
| `edit_file` | Modify existing |

### Visual
```mermaid
graph TB
    A[Large Tool Result] --> B{Context<br/>Overflow?}
    B -->|Yes| C[write_file]
    C --> D[Virtual Filesystem]
    B -->|No| E[Keep in Context]

    F[Need Data] --> G[read_file]
    G --> D
    D --> H[Retrieved Data]

    style C fill:#fff3e0
    style G fill:#fff3e0
    style D fill:#e8f5e9
```

### Speaker Notes
The filesystem is how agents manage context overflow. When tools return large results, instead of keeping everything in the context window, the agent can write data to files and read it back when needed. This mimics how humans use notes and documents. (Notebook reference: `2_files.ipynb` implements the FilesystemMiddleware with virtual file operations.)

---

## Slide 8: Subagent Spawning

### Content
## SubAgentMiddleware & Context Quarantine

> "Subagents solve the context bloat problem. When agents use tools with large outputs, the context window fills up quickly with intermediate results."
> — LangChain Docs

**The `task` tool spawns isolated agents** that:
- Work with their own context
- Return only summarized results
- Keep main agent's context clean

### Visual
```mermaid
graph TB
    subgraph Main["Main Agent (Clean Context)"]
        A[High-level Task]
    end

    A --> B[task tool]

    subgraph Sub["Subagent (Isolated Context)"]
        B --> C[Web Searches]
        B --> D[File Reads]
        B --> E[API Calls]
        C --> F[Intermediate Data]
        D --> F
        E --> F
    end

    F --> G[Summarized Result]
    G --> Main

    style Main fill:#e1f5fe
    style Sub fill:#fff3e0
    style G fill:#e8f5e9
```

### Speaker Notes
This is context quarantine. The subagent does all the messy work—web searches, file reads, API calls—and accumulates lots of intermediate data. But only the summarized result comes back to the main agent. This keeps the main agent's context clean and focused. (Notebook reference: `3_subagents.ipynb` implements the SubAgentMiddleware and `task` tool for context isolation.)

---

## Slide 9: Long-term Memory

### Content
## Persistent Storage Across Threads

**Default behavior:** Filesystem is transient (single thread)

**With CompositeBackend:**
- `/memories/*` → Persistent Store (across threads)
- Other paths → Ephemeral State (single thread)

**Store Options:**
- InMemoryStore (dev)
- Redis Store (prod)
- Custom backends (databases)

### Visual
```mermaid
graph LR
    A[Deep Agent] --> B{Path Router}

    B -->|/memories/*| C[Store Backend]
    B -->|other| D[State Backend]

    C --> E[(Persistent<br/>across threads)]
    D --> F[(Ephemeral<br/>single thread)]

    style C fill:#e8f5e9
    style D fill:#fff3e0
    style E fill:#e8f5e9
    style F fill:#fce4ec
```

### Speaker Notes
By default, the filesystem is stored in agent state and lost when the thread ends. But you can configure a CompositeBackend that routes certain paths to persistent storage. This enables agents to remember things across conversations—like user preferences or learned patterns.

---

## Slide 10: Middleware Architecture

### Content
## Modular, Composable Design

```python
from deepagents import create_deep_agent

# Automatically attaches:
# - TodoListMiddleware
# - FilesystemMiddleware
# - SubAgentMiddleware

agent = create_deep_agent(model="gpt-4o")
```

**Middleware is composable**—add/remove as needed.

### Visual
```mermaid
graph LR
    A[create_deep_agent] --> B[TodoList<br/>Middleware]
    A --> C[Filesystem<br/>Middleware]
    A --> D[SubAgent<br/>Middleware]

    B --> E[Agent Tools]
    C --> E
    D --> E

    E --> F[Deep Agent]

    style B fill:#e1f5fe
    style C fill:#fff3e0
    style D fill:#e8f5e9
    style F fill:#fce4ec
```

### Speaker Notes
The middleware architecture is what makes Deep Agents modular. When you call create_deep_agent, it automatically attaches the three core middleware components. But you can customize this—add your own middleware or remove ones you don't need.

---

## Slide 11: Skills: Dynamic Capability Loading

### Content
## Progressive Disclosure for Capabilities

> "Skills are simply folders containing a SKILL.md file along with any associated files that agents can discover and load dynamically."
> — LangChain Blog

**Structure:**
```
~/.deepagents/agent/skills/
└── my-skill/
    ├── SKILL.md
    └── resources/
```

### Visual
```mermaid
sequenceDiagram
    participant A as Agent
    participant S as Skills Directory
    participant M as SKILL.md

    A->>S: Discover skills
    S-->>A: Skill metadata only
    Note over A: Context cost: Minimal

    A->>A: Match trigger
    A->>M: Load full instructions
    M-->>A: Complete skill content
    Note over A: Context cost: Only when needed

    A->>A: Execute skill
```

### Speaker Notes
Skills use progressive disclosure. The agent first sees only metadata—name and triggers. When a user request matches a trigger, the agent loads the full SKILL.md instructions. This keeps context lean until capabilities are actually needed.

---

## Slide 12: The Deep Agents CLI

### Content
## Terminal-Based Agent Assistant

**Capabilities:**
- File operations (read, write, edit)
- Shell execution (tests, builds, git)
- Web search (Tavily integration)
- HTTP requests (API calls)
- Task planning (todos)
- Memory (cross-session)
- Human-in-the-loop (approvals)

```bash
pip install deepagents-cli
deepagents
```

### Visual
```mermaid
graph TB
    A[User] --> B[deepagents CLI]

    B --> C[File Ops]
    B --> D[Shell]
    B --> E[Web]
    B --> F[Memory]
    B --> G[Skills]

    C --> H[Project Files]
    D --> I[Terminal]
    E --> J[Internet]
    F --> K[(Store)]
    G --> L[~/.deepagents/skills]

    style B fill:#e8f5e9
```

### Speaker Notes
The Deep Agents CLI is a ready-to-use implementation of all these concepts. It's like having Claude Code but built on LangGraph with customizable skills. You can extend it with your own skills and configure its behavior.

---

## Slide 13: Production Patterns

### Content
## Deploying Deep Agents

**Backend Selection:**
| Environment | Recommended |
|-------------|-------------|
| Development | InMemoryStore |
| Testing | SQLite Store |
| Production | Redis / PostgreSQL |

**Token Management (DeepAgents 0.2):**
- Large tool result eviction
- Conversation summarization
- Dangling tool call repair

### Visual
```mermaid
graph TB
    subgraph "Production Stack"
        A[Deep Agent] --> B[Token Manager]
        B --> C[Backend Router]

        C --> D[(Redis Store)]
        C --> E[(PostgreSQL)]

        B --> F[Eviction Policy]
        B --> G[Summarization]
    end

    style D fill:#e8f5e9
    style E fill:#e8f5e9
```

### Speaker Notes
In production, you need proper backends for persistence and token management strategies to handle long-running tasks. DeepAgents 0.2 added automatic eviction of large tool results and conversation summarization to manage context limits.

---

## Slide 14: Demo - Building a Deep Agent

### Content
## Live Implementation: deep-agents-from-scratch

| Notebook | Concept | Builds On |
|----------|---------|-----------|
| `0_create_agent.ipynb` | Basic ReAct agent (baseline) | — |
| `1_todo.ipynb` | Task planning with `write_todos` | Notebook 0 |
| `2_files.ipynb` | Virtual filesystem operations | Notebook 1 |
| `3_subagents.ipynb` | Context isolation through delegation | Notebook 2 |
| `4_full_agent.ipynb` | Full production research agent | All previous |

### Visual
```mermaid
graph LR
    A[0_create_agent] --> B[1_todo]
    B --> C[2_files]
    C --> D[3_subagents]
    D --> E[4_full_agent]

    A:::baseline
    B:::planning
    C:::context
    D:::delegation
    E:::complete

    classDef baseline fill:#e1f5fe
    classDef planning fill:#fff3e0
    classDef context fill:#e8f5e9
    classDef delegation fill:#fce4ec
    classDef complete fill:#c8e6c9
```

### Speaker Notes
The demo follows the deep-agents-from-scratch repository notebooks. Each notebook builds incrementally: start with a basic ReAct agent (0), add planning (1), add filesystem (2), add subagents (3), then see everything combined in a production research agent (4). This mirrors how you'd build a real deep agent.

---

## Slide 15: Summary

### Content
## Key Takeaways

1. **Deep Agents** = Planning + Context + Delegation + Memory
2. **Four Elements**: System prompt, todos, subagents, filesystem
3. **Context Quarantine** solves context bloat via subagents
4. **Skills** enable progressive disclosure of capabilities
5. **Production** requires proper backends and token management

**Remember:** Use Deep Agents when tasks are complex and long-running. For simple tasks, `create_agent()` is still the right choice.

### Visual
```mermaid
graph TB
    A[Deep Agents] --> B[When to Use]
    A --> C[Four Elements]
    A --> D[Key Patterns]

    B --> B1[Complex Tasks]
    B --> B2[Long Horizons]
    B --> B3[Context Heavy]

    C --> C1[Planning]
    C --> C2[Filesystem]
    C --> C3[Subagents]
    C --> C4[Memory]

    D --> D1[Context Quarantine]
    D --> D2[Progressive Disclosure]
    D --> D3[Middleware Composition]

    style A fill:#e8f5e9
```

### Speaker Notes
To summarize: Deep Agents extend the agent loop with planning, context management, delegation, and memory. The four elements work together to handle complex, long-running tasks. Use the right tool for the job—simple tasks don't need deep agents. (Notebook reference: `4_full_agent.ipynb` combines all concepts into a production-ready research agent.)

---

## Slide 16: Resources & Q&A

### Content
## Learn More

**Documentation:**
- [Deep Agents Overview](https://docs.langchain.com/oss/python/deepagents/overview)
- [Middleware](https://docs.langchain.com/oss/python/deepagents/middleware)
- [Subagents](https://docs.langchain.com/oss/python/deepagents/subagents)
- [Skills](https://docs.langchain.com/oss/python/langchain/multi-agent/skills)

**Blog Posts:**
- [Deep Agents](https://blog.langchain.com/deep-agents/)
- [Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)

**Hands-On Notebooks:**
```
deep-agents-from-scratch/
├── 0_create_agent.ipynb   # Basic ReAct agent (baseline)
├── 1_todo.ipynb           # Task planning with write_todos
├── 2_files.ipynb          # Virtual filesystem operations
├── 3_subagents.ipynb      # Context isolation through delegation
└── 4_full_agent.ipynb     # Full production research agent
```
- [deep-agents-from-scratch](https://github.com/langchain-ai/deep-agents-from-scratch)

## Questions?

### Visual
```mermaid
graph LR
    A[Questions] --> B[Docs]
    A --> C[Blogs]
    A --> D[GitHub]
    A --> E[Notebooks]

    D --> D1[0_create_agent]
    D --> D2[1_todo]
    D --> D3[2_files]
    D --> D4[3_subagents]
    D --> D5[4_full_agent]

    style A fill:#e1f5fe
    style E fill:#e8f5e9
    style D fill:#fff3e0
```

### Speaker Notes
The deep-agents-from-scratch repository provides hands-on notebooks that mirror this session's concepts. Work through them in order: baseline agent (0), then add planning (1), filesystem (2), subagents (3), and finally see the complete production agent (4). Each notebook builds on the previous one. Now, let's open it up for questions.

---

## Design System

### Colors
- Input/Query nodes: `#e1f5fe` (light blue)
- Processing/Model nodes: `#fff3e0` (light orange)
- Tool/Action nodes: `#e8f5e9` (light green)
- Output/Result nodes: `#fce4ec` (light pink)
- Neutral: `#f5f5f5` (light gray)

### Typography
- Titles: Bold, large
- Body: Regular
- Code: Monospace
- Quotes: Italic with attribution

### Diagram Conventions
- Flow: Left-to-right or top-to-bottom
- Subgraphs for grouped concepts
- Consistent node shapes per type

---

*Slides created for AIE9 Session 7: Deep Agents*
*Last updated: January 2026*
