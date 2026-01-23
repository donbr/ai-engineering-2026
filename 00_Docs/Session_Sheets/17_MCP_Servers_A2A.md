# Session 17: MCP Servers & A2A

> "MCP is a new standard for connecting AI assistants to the systems where data lives, including content repositories, business tools, and development environments."
> — Anthropic, Model Context Protocol Announcement

## Goal

Build and deploy MCP servers that expose custom tools while understanding the A2A (Agent-to-Agent) protocol for cross-agent communication in distributed systems.

## Learning Outcomes

By the end of this session, you will be able to:

1. **Compare protocols**: Distinguish between MCP (agent-to-tool), A2A (agent-to-agent), and ACP (stateful workflows) and identify appropriate use cases
2. **Build MCP servers**: Implement an MCP server using FastMCP with custom tools, resources, and prompts
3. **Create Agent Cards**: Design capability manifests for agent discovery in A2A ecosystems
4. **Handle A2A messaging**: Implement synchronous and streaming message patterns with proper task lifecycle management
5. **Apply security patterns**: Implement OAuth 2.1, mTLS, and zero-trust principles for cross-agent authentication
6. **Bridge protocols**: Connect MCP servers to A2A endpoints for cross-agent tool accessibility
7. **Design for production**: Plan scalable agent infrastructure with monitoring and multi-tenancy

## Tools Introduced

| Tool | Purpose | Documentation |
|------|---------|---------------|
| **FastMCP** | Python framework for MCP server development | [gofastmcp.com](https://gofastmcp.com) |
| **MCP Python SDK** | Official Anthropic MCP implementation | [modelcontextprotocol.io](https://modelcontextprotocol.io) |
| **A2A Protocol** | Google's agent-to-agent communication standard | [a2a-protocol.org](https://a2a-protocol.org) |
| **Agent Cards** | JSON manifests for agent discovery | Part of A2A specification |

---

## Key Concepts

### 1. Protocol Landscape

The agentic ecosystem has converged on three complementary protocols, each solving a different integration challenge:

```
┌─────────────────────────────────────────────────────────────────┐
│                    PROTOCOL LANDSCAPE                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   MCP (Anthropic)              A2A (Google)                     │
│   ┌─────────────┐              ┌─────────────┐                  │
│   │   Agent     │              │   Agent A   │                  │
│   │      │      │              │      │      │                  │
│   │      ▼      │              │      ▼      │                  │
│   │   Tools     │              │   Agent B   │                  │
│   │  Resources  │              │   Agent C   │                  │
│   │  Prompts    │              │   Agent D   │                  │
│   └─────────────┘              └─────────────┘                  │
│                                                                  │
│   VERTICAL                     HORIZONTAL                        │
│   Agent-to-Tool                Agent-to-Agent                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Protocol Comparison**:

| Aspect | MCP | A2A | ACP (IBM) |
|--------|-----|-----|-----------|
| **Focus** | Tool integration | Agent collaboration | Stateful workflows |
| **Communication** | JSON-RPC 2.0 | JSON-RPC over HTTP | REST |
| **Discovery** | Config-based | Agent Cards | Agent Manifests |
| **State** | Single-server | Task lifecycle | Built-in memory |
| **Best For** | Extending capabilities | Cross-domain agents | Enterprise HITL |

**When to use which?**
- Use **MCP** when your agent needs to access external tools, databases, or APIs
- Use **A2A** when agents need to collaborate across organizational or security boundaries
- Use **both** when building production multi-agent systems with external integrations

---

### 2. MCP Server Architecture

MCP servers expose capabilities via three primitives, each with different control semantics:

```
┌─────────────────────────────────────────────────────────────────┐
│                    MCP SERVER ARCHITECTURE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                    ┌─────────────────┐                          │
│                    │   MCP Server    │                          │
│                    │                 │                          │
│   ┌────────────────┼─────────────────┼────────────────┐        │
│   │                │                 │                │        │
│   ▼                ▼                 ▼                │        │
│ ┌──────┐      ┌──────────┐      ┌─────────┐          │        │
│ │Tools │      │Resources │      │ Prompts │          │        │
│ │      │      │          │      │         │          │        │
│ │MODEL │      │   APP    │      │  USER   │          │        │
│ │CTRL  │      │  CTRL    │      │  CTRL   │          │        │
│ └──────┘      └──────────┘      └─────────┘          │        │
│                                                       │        │
│   ┌───────────────────────────────────────────────────┘        │
│   │                                                             │
│   ▼                                                             │
│ ┌──────────────────────────────────────────────┐               │
│ │              TRANSPORT LAYER                  │               │
│ │  ┌─────────────┐    ┌────────────────────┐   │               │
│ │  │   stdio     │    │ Streamable HTTP    │   │               │
│ │  │  (local)    │    │   (production)     │   │               │
│ │  └─────────────┘    └────────────────────┘   │               │
│ └──────────────────────────────────────────────┘               │
└─────────────────────────────────────────────────────────────────┘
```

**Control Models**:
- **Tools** (Model-controlled): LLM decides when to invoke based on context
- **Resources** (Application-controlled): Host application manages access
- **Prompts** (User-controlled): Explicit user selection required

**Transport Selection**:
- **stdio**: Local development, subprocess communication, fastest latency
- **Streamable HTTP**: Production deployments, remote access, OAuth support

---

### 3. FastMCP Framework

FastMCP provides a Pythonic interface for building MCP servers with automatic schema generation from type hints.

**Core Pattern**:
```python
from fastmcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool
def search_docs(query: str, limit: int = 5) -> list[str]:
    """Search documentation for relevant content."""
    # Implementation here
```

**Key Features**:
- Decorators generate JSON Schema from function signatures
- Docstrings become tool descriptions
- Type hints drive parameter validation
- MCPRouter for modular organization

**Running the Server**:
```python
if __name__ == "__main__":
    mcp.run()
```

---

### 4. Agent Cards

> "A2A is an open protocol created by Google for secure agent-to-agent communication and collaboration... empowering developers to build agents that seamlessly interoperate."
> — Linux Foundation, A2A Announcement

Agent Cards are JSON manifests that describe an agent's capabilities for discovery:

```json
{
  "name": "research-agent",
  "description": "Searches and analyzes research papers",
  "url": "https://research.example.com",
  "version": "1.0.0",
  "capabilities": {
    "streaming": true,
    "pushNotifications": false
  },
  "authentication": {
    "type": "bearer",
    "scheme": "OAuth2"
  },
  "methods": ["message/send", "message/stream", "tasks/get"]
}
```

**Discovery Flow**:
1. Client requests `/.well-known/agent.json`
2. Agent Card describes capabilities and authentication
3. Client negotiates based on supported methods
4. Communication begins with appropriate method

**Required Fields**:
- `name`: Unique identifier
- `description`: Human-readable purpose
- `url`: Base endpoint for communication
- `methods`: Supported A2A methods

---

### 5. A2A Protocol Methods

A2A defines three methods for agent communication:

| Method | Pattern | Use Case |
|--------|---------|----------|
| `message/send` | Synchronous | Simple request/response |
| `message/stream` | SSE streaming | Long-running, partial results |
| `tasks/get` | Polling | Check status of async tasks |

**Message Structure**:
```
┌─────────────────────────────────────────────────────────────────┐
│                    A2A MESSAGE LIFECYCLE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Client                                Server                    │
│    │                                      │                      │
│    │───── message/send ──────────────────▶│                      │
│    │      {role: "user",                  │                      │
│    │       parts: [{text: "..."}]}        │                      │
│    │                                      │                      │
│    │◀───── Task (completed) ─────────────│                      │
│    │      {status: "completed",           │                      │
│    │       result: {parts: [...]}}        │                      │
│                                                                  │
│  ─────────── OR (streaming) ──────────────                      │
│                                                                  │
│    │───── message/stream ────────────────▶│                      │
│    │                                      │                      │
│    │◀───── SSE: partial result ──────────│                      │
│    │◀───── SSE: partial result ──────────│                      │
│    │◀───── SSE: final result ────────────│                      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Key Concepts**:
- `contextId`: Thread identifier (maps to LangGraph `thread_id`)
- `parts`: Message content (text or data)
- `Task`: Represents ongoing operation with status

---

### 6. Task Lifecycle

A2A tasks progress through defined states:

```
┌─────────────────────────────────────────────────────────────────┐
│                    TASK STATE MACHINE                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                      ┌──────────┐                               │
│                      │ created  │                               │
│                      └────┬─────┘                               │
│                           │                                      │
│                           ▼                                      │
│                      ┌──────────┐                               │
│            ┌────────│ running  │────────┐                       │
│            │         └────┬─────┘        │                       │
│            │              │              │                       │
│            ▼              ▼              ▼                       │
│      ┌──────────┐  ┌──────────┐  ┌───────────┐                  │
│      │ canceled │  │completed │  │  failed   │                  │
│      └──────────┘  └──────────┘  └───────────┘                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**State Definitions**:
- **created**: Task accepted, not yet processing
- **running**: Actively processing
- **completed**: Successfully finished with result
- **failed**: Error occurred (check error field)
- **canceled**: Stopped by client request

**Error Handling Pattern**:
```python
task = await agent.send_message(message)
match task.status:
    case "completed":
        return task.result
    case "failed":
        raise AgentError(task.error)
    case "canceled":
        log.info("Task was canceled")
```

---

### 7. Cross-Agent Security

> "Tool poisoning attacks are a specialized form of prompt injection where malicious instructions are tucked away in the tool descriptions themselves."
> — Invariant Labs

**Five Security Layers**:

```
┌─────────────────────────────────────────────────────────────────┐
│                    SECURITY LAYERS                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Layer 5: External API Access                                   │
│     └── Downstream systems honor agent + delegator permissions  │
│                                                                  │
│  Layer 4: Tool-Level Access                                     │
│     └── Fine-grained permissions per tool invocation            │
│                                                                  │
│  Layer 3: MCP Server Access                                     │
│     └── Agent authenticates to server, tool exposure decisions  │
│                                                                  │
│  Layer 2: Delegator Authentication                              │
│     └── User consent with explicit permission boundaries        │
│                                                                  │
│  Layer 1: Agent Identity                                        │
│     └── Distinct, traceable identity (not shared API keys)      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Key Security Patterns**:

| Pattern | Implementation |
|---------|----------------|
| **Authentication** | OAuth 2.1, mTLS, JWT with rotation |
| **Authorization** | RBAC/ABAC policies, tool-level permissions |
| **Zero Trust** | Continuously verify, no implicit trust |
| **Human-in-the-Loop** | Approval gates for sensitive actions |
| **Audit** | Log all cross-agent interactions |

**Attack Vectors to Mitigate**:
- Tool poisoning (malicious descriptions)
- Cross-tool data exfiltration
- Prompt injection via MCP
- Resource theft (quota exhaustion)

---

### 8. Protocol Bridging

Connecting MCP servers to A2A endpoints enables cross-agent tool accessibility:

```
┌─────────────────────────────────────────────────────────────────┐
│                    PROTOCOL BRIDGE                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  External Agent                                                  │
│       │                                                          │
│       ▼  A2A (message/send)                                     │
│  ┌─────────────────────────────────────────┐                    │
│  │           A2A Bridge Layer              │                    │
│  │  ┌───────────────────────────────────┐  │                    │
│  │  │    Agent Card Discovery           │  │                    │
│  │  │    Request Translation            │  │                    │
│  │  │    Response Mapping               │  │                    │
│  │  └───────────────────────────────────┘  │                    │
│  └─────────────────────────────────────────┘                    │
│       │                                                          │
│       ▼  MCP (tools/call)                                       │
│  ┌─────────────────────────────────────────┐                    │
│  │           MCP Server                    │                    │
│  │  ┌─────┐  ┌─────┐  ┌─────┐             │                    │
│  │  │Tool1│  │Tool2│  │Tool3│             │                    │
│  │  └─────┘  └─────┘  └─────┘             │                    │
│  └─────────────────────────────────────────┘                    │
│       │                                                          │
│       ▼                                                          │
│  External Services                                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Bridge Responsibilities**:
- Expose MCP tools as A2A capabilities in Agent Card
- Translate A2A messages to MCP tool calls
- Map MCP responses to A2A task results
- Handle authentication across both protocols

**PydanticAI Pattern**:
```python
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o", tools=[...])
app = agent.to_a2a()  # Automatic A2A wrapper
```

---

### 9. Production Patterns

> "Use MCP when you need fast, stateless tool execution. Use A2A when you need complex, stateful orchestration. Use both when building production systems."
> — PlexObject

**Production Architecture**:

```
┌─────────────────────────────────────────────────────────────────┐
│                    PRODUCTION DEPLOYMENT                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                   ┌──────────────────┐                          │
│                   │  Load Balancer   │                          │
│                   └────────┬─────────┘                          │
│                            │                                     │
│         ┌──────────────────┼──────────────────┐                 │
│         ▼                  ▼                  ▼                 │
│  ┌────────────┐    ┌────────────┐    ┌────────────┐            │
│  │  Agent 1   │    │  Agent 2   │    │  Agent 3   │            │
│  │  (A2A)     │    │  (A2A)     │    │  (A2A)     │            │
│  └─────┬──────┘    └─────┬──────┘    └─────┬──────┘            │
│        │                 │                 │                    │
│        └─────────────────┼─────────────────┘                    │
│                          ▼                                      │
│               ┌──────────────────┐                              │
│               │   MCP Gateway    │                              │
│               └────────┬─────────┘                              │
│                        │                                        │
│         ┌──────────────┼──────────────┐                        │
│         ▼              ▼              ▼                        │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐                  │
│  │ MCP Server │ │ MCP Server │ │ MCP Server │                  │
│  │  (Tools)   │ │(Resources) │ │ (Prompts)  │                  │
│  └────────────┘ └────────────┘ └────────────┘                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Scaling Considerations**:
- Horizontal scaling with stateless agents
- Connection pooling for MCP servers
- Async processing for long-running tasks
- Circuit breakers for external dependencies

**Monitoring Requirements**:
- Task lifecycle metrics (created, running, completed, failed)
- Latency histograms per agent and tool
- Authentication failure rates
- Cross-agent call graphs

**Multi-Tenancy**:
- PostgreSQL row-level security for isolation
- Namespace tool contexts per server
- Tenant-specific Agent Cards

---

## Security Considerations

### Checklist for Production Deployment

- [ ] OAuth 2.1 with client credentials flow for headless agents
- [ ] mTLS between agents in same trust domain
- [ ] API key rotation with secrets manager
- [ ] RBAC policies at tool level
- [ ] Audit logging for all cross-agent calls
- [ ] Rate limiting per agent identity
- [ ] Input validation on all tool parameters
- [ ] Human-in-the-loop for sensitive operations

### OWASP Guidance

The [OWASP GenAI Security Project](https://genai.owasp.org/resource/cheatsheet-a-practical-guide-for-securely-using-third-party-mcp-servers-1-0/) provides comprehensive frameworks for MCP security.

---

## Key Takeaways

1. **MCP = Vertical, A2A = Horizontal**: MCP connects agents to tools; A2A connects agents to agents
2. **FastMCP simplifies servers**: Decorators + type hints = automatic schema generation
3. **Agent Cards enable discovery**: JSON manifests at well-known endpoints
4. **Three A2A methods**: send (sync), stream (SSE), tasks/get (polling)
5. **Task lifecycle matters**: Track states for error handling and cancellation
6. **Security is layered**: Five layers from agent identity to external APIs
7. **Bridge when needed**: Wrap MCP servers in A2A for cross-agent access
8. **Design for production**: Stateless scaling, monitoring, multi-tenancy
9. **Both protocols together**: MCP for tools, A2A for collaboration

---

## Recommended Reading

### Core Specifications
- [MCP Specification (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25) - Official protocol reference
- [A2A Protocol](https://a2a-protocol.org/latest/) - Google's agent communication standard
- [FastMCP Documentation](https://gofastmcp.com) - Python server framework

### Implementation Guides
- [FastMCP Quickstart](https://gofastmcp.com/getting-started/quickstart) - Build your first server
- [PydanticAI A2A](https://ai.pydantic.dev/a2a/) - A2A integration patterns
- [LangChain MCP Adapters](https://docs.langchain.com/oss/python/langchain/mcp) - LangChain integration

### Security Resources
- [OWASP MCP Security Guide](https://genai.owasp.org/resource/cheatsheet-a-practical-guide-for-securely-using-third-party-mcp-servers-1-0/) - Security best practices
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices) - Official security guidance

### Industry Context
- [Anthropic MCP Announcement](https://www.anthropic.com/news/model-context-protocol) - Why MCP was created
- [Linux Foundation AAIF](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) - Governance structure
- [A Year of MCP Review](https://www.pento.ai/blog/a-year-of-mcp-2025-review) - Industry adoption

---

## Assignment

### Build: MCP Server with A2A Bridge

Create an MCP server that:
1. Exposes at least 3 custom tools using FastMCP
2. Includes proper type hints and docstrings
3. Runs on Streamable HTTP transport
4. Has an Agent Card for discovery

**Stretch Goals**:
- Implement OAuth 2.1 authentication
- Add tool-level authorization
- Create monitoring dashboards
- Test with a second agent via A2A

### Questions to Consider

1. What would happen if your MCP server becomes unavailable? How would dependent agents handle this?
2. How would you version your Agent Card when adding new capabilities?
3. What security considerations apply when bridging MCP to A2A?
4. How would you test cross-agent communication in isolation?

---

## Advanced Build

Design a multi-agent research system where:

1. **Coordinator Agent** (A2A): Receives research queries, delegates to specialists
2. **Search Agent** (A2A + MCP): Uses search tools via MCP, exposes via A2A
3. **Analysis Agent** (A2A + MCP): Uses analysis tools, exposes summaries
4. **Report Agent** (A2A): Combines results, produces final output

Consider:
- Agent Card design for each specialist
- Error handling when specialists fail
- Security between agents
- Monitoring and observability

---

## Session Connections

| Related Session | Connection |
|-----------------|------------|
| Session 5: Multi-Agent Systems | Local orchestration patterns (supervisor, router, swarm) |
| Session 7: Deep Agents | Subagent spawning evolves into A2A for remote agents |
| Session 14: MCP Connectors | Client-side MCP becomes foundation for server-side |
| Session 15: Agent Servers | Deployment patterns apply to MCP servers |
| Session 18: Guardrails | Security patterns extend to cross-agent validation |
