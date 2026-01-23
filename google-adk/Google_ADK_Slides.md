# Google ADK: Agent Development Kit
## Slide Deck Specification

---

## Slide 1: Title

**Google ADK: Building Production AI Agents**

*From Prompt to Production with Agent Development Kit*

```
┌─────────────────────────────────────────────────┐
│                                                  │
│          Google Agent Development Kit            │
│                                                  │
│        Build • Deploy • Scale AI Agents          │
│                                                  │
│     ╔═══════════════════════════════════════╗   │
│     ║    Code-First    Multi-Language       ║   │
│     ║    Open Source   Production-Ready     ║   │
│     ╚═══════════════════════════════════════╝   │
│                                                  │
└─────────────────────────────────────────────────┘
```

**Speaker Notes:**
- ADK launched April 2025 at Google Cloud NEXT
- Available in Python, Java, Go, TypeScript
- 14,000+ GitHub stars, millions of downloads
- Code-first approach: treat agent development like software engineering

---

## Slide 2: Learning Objectives

**By the End of This Session**

You will be able to:

1. Explain the core architecture of AI agents
2. Build single agents with tools using ADK
3. Design multi-agent systems with workflow patterns
4. Implement state management for stateful agents
5. Debug agents using observability tools
6. Deploy agents to production

**Key Question:** What transforms an LLM into an Agent?

**Speaker Notes:**
- Focus on concepts before code
- Each objective maps to a course day
- The key question drives all our learning

---

## Slide 3: From LLM to Agent

**What Makes an Agent Different?**

```mermaid
flowchart LR
    subgraph LLM["LLM (Passive)"]
        A[Prompt] --> B[Model] --> C[Text Response]
    end

    subgraph Agent["Agent (Active)"]
        D[Goal] --> E[Think] --> F[Act]
        F --> G[Observe] --> E
        G --> H[Final Answer]
    end

    style Agent fill:#e8f5e9
    style LLM fill:#fff3e0
```

| LLM | Agent |
|-----|-------|
| Generates text | Takes actions |
| Static knowledge | Real-time data |
| Single response | Iterative reasoning |
| Human-guided | Goal-oriented |

**Speaker Notes:**
- LLM: pattern prediction engine
- Agent: complete application with reasoning and action
- The loop is key: think → act → observe → repeat

---

## Slide 4: The Agent Architecture

**Three Core Components**

```mermaid
flowchart TB
    subgraph Agent["AI Agent"]
        M["🧠 MODEL<br/>(Brain)"]
        T["🔧 TOOLS<br/>(Hands)"]
        O["⚡ ORCHESTRATION<br/>(Nervous System)"]

        M <--> O
        T <--> O
    end

    U[User] --> O
    O --> R[Result]
    T --> W[World]

    style M fill:#e1f5fe
    style T fill:#e8f5e9
    style O fill:#fff3e0
```

| Component | Purpose | ADK Implementation |
|-----------|---------|-------------------|
| Model | Reasoning engine | `Gemini()` |
| Tools | External actions | `google_search`, `FunctionTool` |
| Orchestration | Loop management | `Runner`, workflow agents |

**Speaker Notes:**
- Model: the "brain" that reasons
- Tools: the "hands" that interact with the world
- Orchestration: manages the think-act-observe loop

---

## Slide 5: The Agentic Loop

**How Agents Solve Problems**

```mermaid
flowchart TD
    A[1. Get Mission] --> B[2. Scan Scene]
    B --> C[3. Think Through]
    C --> D[4. Take Action]
    D --> E[5. Observe]
    E --> F{Mission<br/>Complete?}
    F -->|No| C
    F -->|Yes| G[Return Result]

    style A fill:#e1f5fe
    style C fill:#fff3e0
    style D fill:#e8f5e9
    style E fill:#fce4ec
```

**Example: "Where is my order #12345?"**

1. **Get Mission:** Answer order status query
2. **Scan Scene:** Available tools, context
3. **Think:** Need to query database, then carrier API
4. **Act:** Call `find_order("12345")`
5. **Observe:** Order found, tracking #ZYX987
6. **Loop:** Call `get_shipping_status("ZYX987")`
7. **Result:** "Your order is Out for Delivery!"

**Speaker Notes:**
- This loop is universal across all agent frameworks
- Agents plan multi-step strategies, not single actions
- Each observation informs the next thought

---

## Slide 6: Taxonomy of Agents

**Five Levels of Agent Capability**

```mermaid
flowchart TB
    L0["Level 0: Core Reasoning<br/>Pure LLM, no tools"]
    L1["Level 1: Connected<br/>Uses external tools"]
    L2["Level 2: Strategic<br/>Multi-step planning"]
    L3["Level 3: Collaborative<br/>Multi-agent teams"]
    L4["Level 4: Self-Evolving<br/>Creates own tools"]

    L0 --> L1 --> L2 --> L3 --> L4

    style L0 fill:#fff3e0
    style L1 fill:#e1f5fe
    style L2 fill:#e8f5e9
    style L3 fill:#fce4ec
    style L4 fill:#f3e5f5
```

| Level | Example |
|-------|---------|
| 0 | "Explain baseball rules" |
| 1 | "What's the weather?" (uses search) |
| 2 | "Find coffee shop halfway between..." |
| 3 | "Launch product with research + marketing" |
| 4 | "Create new monitoring agent on-demand" |

**Speaker Notes:**
- Most production agents are Level 1-3
- Level 4 is cutting-edge research (AlphaEvolve, Co-Scientist)
- Higher levels build on lower capabilities

---

## Slide 7: ADK Design Principles

**Why ADK?**

```
┌─────────────────────────────────────────────────┐
│              ADK DESIGN PRINCIPLES               │
├─────────────────────────────────────────────────┤
│                                                  │
│  ✓ CODE-FIRST: Software engineering patterns    │
│  ✓ OPEN: Works with any model, tool, platform   │
│  ✓ INTEROPERABLE: LangChain, CrewAI, MCP, A2A   │
│  ✓ SCALABLE: Local dev → Production deploy      │
│  ✓ OBSERVABLE: Built-in tracing and debugging   │
│                                                  │
└─────────────────────────────────────────────────┘
```

**Key Differentiators:**
- Betting on model capabilities (not constraining them)
- Best of Google, fully extensible
- Agent as atomic unit, customizable internals

**Speaker Notes:**
- Not "low-code AI sprinkled on workflows"
- Full software engineering: testing, versioning, CI/CD
- Works with existing ecosystems, not locked-in

---

## Slide 8: Your First Agent

**10 Lines to Search the Web**

```python
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.tools import google_search

root_agent = Agent(
    name="helpful_assistant",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction="Use Google Search for current info.",
    tools=[google_search],
)

runner = InMemoryRunner(agent=root_agent)
response = await runner.run_debug("What's new with ADK?")
```

**Result:** Agent searches web, returns current ADK info

**Speaker Notes:**
- Notice: name, model, instruction, tools
- Runner orchestrates the execution
- `run_debug` for prototyping (handles session)

---

## Slide 9: Multi-Agent Patterns

**When One Agent Isn't Enough**

```mermaid
flowchart TD
    subgraph Problem["❌ Monolithic Agent"]
        A["One Agent Does Everything"]
    end

    subgraph Solution["✅ Specialist Team"]
        B["Coordinator"] --> C["Researcher"]
        B --> D["Writer"]
        B --> E["Editor"]
    end

    style Problem fill:#ffcccc
    style Solution fill:#ccffcc
```

**Why Multi-Agent?**
- Simpler individual agents
- Easier to test and debug
- More reliable outcomes
- Parallel execution possible

**Speaker Notes:**
- Monolithic agents: long prompts, hard to debug
- Team of specialists: modular, maintainable
- Mirrors human organizations

---

## Slide 10: Workflow Patterns

**Sequential • Parallel • Loop**

```mermaid
flowchart LR
    subgraph Sequential["Sequential"]
        S1[A] --> S2[B] --> S3[C]
    end

    subgraph Parallel["Parallel"]
        P0[Start] --> P1[A]
        P0 --> P2[B]
        P0 --> P3[C]
        P1 --> P4[End]
        P2 --> P4
        P3 --> P4
    end

    subgraph Loop["Loop"]
        L1[Generate] --> L2[Critique]
        L2 --> L3{Good?}
        L3 -->|No| L1
        L3 -->|Yes| L4[Done]
    end
```

| Pattern | Use When | Example |
|---------|----------|---------|
| Sequential | Order matters | Outline → Write → Edit |
| Parallel | Independent tasks | Research 3 topics |
| Loop | Iterative refinement | Draft → Review → Improve |

**Speaker Notes:**
- Sequential: `SequentialAgent(sub_agents=[...])`
- Parallel: `ParallelAgent(sub_agents=[...])`
- Loop: `LoopAgent(sub_agents=[...], max_iterations=N)`

---

## Slide 11: State Management

**Making Agents Remember**

```mermaid
flowchart TB
    subgraph Scopes["State Scopes"]
        S["Session State<br/>Current conversation"]
        U["User State<br/>Cross-session"]
        A["App State<br/>Global"]
    end

    subgraph Services["Persistence Services"]
        SS["SessionService"]
        MS["MemoryService"]
    end

    S --> SS
    U --> SS
    A --> SS
    SS --> MS

    style S fill:#e1f5fe
    style U fill:#e8f5e9
    style A fill:#fff3e0
```

**Key Mechanisms:**
- `output_key`: Store agent output to state
- `{key}` in instruction: Read from state
- `ToolContext.state`: Access in tools

**Speaker Notes:**
- Session = conversation scratchpad
- User = preferences across sessions
- Memory = long-term knowledge retrieval (RAG)

---

## Slide 12: Tools Deep Dive

**Connecting Agents to the World**

```mermaid
flowchart LR
    A[Agent] --> T{Tool Type}
    T --> B1["Built-in<br/>google_search"]
    T --> B2["Function<br/>FunctionTool()"]
    T --> B3["Agent<br/>AgentTool()"]
    T --> B4["MCP<br/>McpToolset"]

    B1 --> W[World]
    B2 --> W
    B3 --> W
    B4 --> W

    style A fill:#e1f5fe
    style W fill:#e8f5e9
```

**Best Practices:**
- Document thoroughly (helps LLM choose)
- Keep granular (one tool = one action)
- Return structured data (JSON > free text)
- Use type hints (enable validation)

**Speaker Notes:**
- Tools transform static LLM into capable agent
- MCP = Model Context Protocol for standard integration
- AgentTool wraps agents as callable tools

---

## Slide 13: Observability

**Debugging the Non-Deterministic**

```mermaid
flowchart LR
    subgraph Pillars["Three Pillars"]
        L["📝 LOGS<br/>What happened"]
        T["🔗 TRACES<br/>Why it happened"]
        M["📊 METRICS<br/>How well it works"]
    end

    L --> D[Debug]
    T --> D
    M --> D

    style L fill:#e1f5fe
    style T fill:#fff3e0
    style M fill:#e8f5e9
```

**Debugging Flow:**
```
User: "Find quantum computing papers"
Agent: "I cannot help with that"

Without observability: 😭 WHY??
With observability: "Functions: []" ← No tools!
Solution: Add google_search tool
```

**Speaker Notes:**
- Agents fail mysteriously (not predictably)
- Traces show full execution path
- ADK web UI visualizes all three pillars

---

## Slide 14: A2A Protocol

**Agent-to-Agent Communication**

```mermaid
flowchart LR
    subgraph Yours["Your Organization"]
        A["Customer Support<br/>Agent"]
    end

    subgraph External["Vendor"]
        B["Product Catalog<br/>Agent"]
    end

    A -->|A2A| B
    B -->|Response| A
```

**When to Use A2A:**
- Cross-framework (ADK ↔ LangGraph)
- Cross-language (Python ↔ Java)
- Cross-organization (your infra ↔ vendor)

**Implementation:**
```python
# Server: expose agent
app = agent.to_a2a()

# Client: consume remote agent
remote = RemoteA2aAgent(url="https://vendor.com/a2a")
```

**Speaker Notes:**
- A2A = open standard for agent interoperability
- Agent Cards describe capabilities (like API contracts)
- Different from MCP (tools) vs A2A (agent tasks)

---

## Slide 15: Production Deployment

**From Prototype to Production**

```mermaid
flowchart LR
    D["Development<br/>InMemory*"] --> S["Staging<br/>Database*"]
    S --> P["Production<br/>Agent Engine"]

    style D fill:#e1f5fe
    style S fill:#fff3e0
    style P fill:#e8f5e9
```

**Deployment Options:**

| Option | Use Case |
|--------|----------|
| Agent Engine | Fully managed, auto-scaling |
| Cloud Run | Containerized, serverless |
| GKE | Maximum control, multi-cloud |

**Production Checklist:**
- [ ] Replace InMemory with Database services
- [ ] Configure authentication and IAM
- [ ] Enable monitoring and alerting
- [ ] Set up CI/CD evaluation pipeline

**Speaker Notes:**
- Same code, swap services for production
- Evaluation gates deployments (metrics-driven)
- Model Armor for security guardrails

---

## Slide 16: Summary & Next Steps

**Key Takeaways**

```
┌─────────────────────────────────────────────────┐
│           GOOGLE ADK ESSENTIALS                  │
├─────────────────────────────────────────────────┤
│                                                  │
│  1. Agents = LLM + Tools + Orchestration        │
│  2. Think → Act → Observe loop                  │
│  3. Multi-agent > Monolithic                    │
│  4. Sequential • Parallel • Loop patterns       │
│  5. State: Session / User / App scopes          │
│  6. Observability: Logs • Traces • Metrics      │
│  7. A2A for cross-boundary communication        │
│  8. Code-first, production-ready                │
│                                                  │
└─────────────────────────────────────────────────┘
```

**Your Assignment:**
1. Build a single agent with Google Search
2. Create a sequential content pipeline
3. Add parallel research capabilities

**Resources:**
- [google.github.io/adk-docs](https://google.github.io/adk-docs/)
- [github.com/google/adk-samples](https://github.com/google/adk-samples)

**Speaker Notes:**
- Start simple, add complexity incrementally
- Use ADK web UI for debugging
- Join the community: GitHub discussions, Discord

---

## Appendix: Decision Tree

**Choosing the Right Pattern**

```mermaid
flowchart TD
    A{What workflow?} --> B["Fixed Pipeline<br/>(A → B → C)"]
    A --> C["Concurrent Tasks<br/>(A, B, C together)"]
    A --> D["Iterative Refinement<br/>(A ↔ B)"]
    A --> E["Dynamic Decisions<br/>(LLM chooses)"]

    B --> B1["SequentialAgent"]
    C --> C1["ParallelAgent"]
    D --> D1["LoopAgent"]
    E --> E1["Agent with AgentTools"]

    style B1 fill:#fce4ec
    style C1 fill:#e1f5fe
    style D1 fill:#e8f5e9
    style E1 fill:#fff3e0
```

---

*Slides Version: 1.0 | Based on Kaggle 5-Day AI Agents Course with Google ADK*
