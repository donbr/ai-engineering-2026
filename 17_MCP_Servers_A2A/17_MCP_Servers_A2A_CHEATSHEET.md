# Session 17: MCP Servers & A2A - Cheatsheet

> "MCP is a new standard for connecting AI assistants to the systems where data lives."
> — Anthropic

---

## 1. Quick Reference

### Protocol Comparison Matrix

| Aspect | MCP | A2A | ACP |
|--------|-----|-----|-----|
| **Creator** | Anthropic | Google | IBM |
| **Released** | Nov 2024 | Apr 2025 | 2025 |
| **Focus** | Agent-to-Tool | Agent-to-Agent | Stateful Workflows |
| **Transport** | JSON-RPC (stdio/HTTP) | JSON-RPC over HTTP | REST |
| **Discovery** | Config-based | Agent Cards | Agent Manifests |
| **Governance** | Linux Foundation (AAIF) | Linux Foundation | Linux Foundation |
| **Adoption** | 97M+ SDK downloads | 150+ organizations | Growing |

### When to Use Which

| Scenario | Protocol |
|----------|----------|
| Add database access to agent | **MCP** |
| Agent needs file system tools | **MCP** |
| Two agents collaborate on task | **A2A** |
| Cross-organization agent call | **A2A** |
| Long workflow with checkpoints | **ACP** |
| Tool access + agent collaboration | **MCP + A2A** |

### Key Endpoints

| Protocol | Endpoint | Purpose |
|----------|----------|---------|
| A2A | `/.well-known/agent.json` | Agent discovery |
| A2A | `/message/send` | Synchronous message |
| A2A | `/message/stream` | Streaming response |
| A2A | `/tasks/{id}` | Task status |
| MCP | JSON-RPC via transport | All operations |

---

## 2. Concept Overview

### MCP: Vertical Integration

```
┌─────────────────────────────────────┐
│              AGENT                  │
│                │                    │
│                ▼                    │
│         ┌──────────────┐            │
│         │  MCP CLIENT  │            │
│         └──────┬───────┘            │
│                │ JSON-RPC           │
│                ▼                    │
│         ┌──────────────┐            │
│         │  MCP SERVER  │            │
│         │              │            │
│         │ ┌──────────┐ │            │
│         │ │  Tools   │ │            │
│         │ │Resources │ │            │
│         │ │ Prompts  │ │            │
│         │ └──────────┘ │            │
│         └──────────────┘            │
└─────────────────────────────────────┘
```

**Purpose**: Connect agents to external tools, databases, and APIs.

### A2A: Horizontal Integration

```
┌─────────────────────────────────────┐
│                                     │
│  ┌─────────┐        ┌─────────┐    │
│  │ Agent A │◄──────►│ Agent B │    │
│  └─────────┘        └─────────┘    │
│       │                  │          │
│       ▼                  ▼          │
│  ┌─────────┐        ┌─────────┐    │
│  │ Agent C │◄──────►│ Agent D │    │
│  └─────────┘        └─────────┘    │
│                                     │
└─────────────────────────────────────┘
```

**Purpose**: Enable agents to communicate and collaborate across boundaries.

### Three MCP Primitives

| Primitive | Control | Description |
|-----------|---------|-------------|
| **Tools** | Model | LLM decides when to invoke |
| **Resources** | Application | Host manages access |
| **Prompts** | User | Explicit user selection |

---

## 3. Setup Requirements

### FastMCP Installation

```bash
# Using uv (recommended)
uv add fastmcp

# Using pip
pip install fastmcp
```

### A2A Client Setup (PydanticAI)

```bash
# Using uv
uv add pydantic-ai-slim[a2a]

# Using pip
pip install pydantic-ai-slim[a2a]
```

### Environment Variables

```bash
# .env file
OPENAI_API_KEY=sk-...
MCP_SERVER_PORT=8000
A2A_AUTH_TOKEN=...
```

### Directory Structure

```
my-agent/
├── server.py          # FastMCP server
├── agent_card.json    # A2A discovery
├── tools/
│   ├── __init__.py
│   ├── search.py
│   └── analyze.py
├── tests/
│   └── test_tools.py
└── pyproject.toml
```

---

## 4. Core Concepts

### MCP Server with FastMCP

**Minimal Server Pattern**:
```python
from fastmcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool
def my_tool(param: str) -> str:
    """Tool description becomes schema."""
    return f"Result: {param}"
```

**Resource Pattern**:
```python
@mcp.resource("config://settings")
def get_settings() -> dict:
    """Expose configuration as resource."""
    return {"key": "value"}
```

**Running the Server**:
```python
if __name__ == "__main__":
    mcp.run()  # Default: stdio transport
```

### Agent Card Structure

```json
{
  "name": "research-agent",
  "description": "Searches research papers",
  "url": "https://research.example.com",
  "version": "1.0.0",
  "capabilities": {
    "streaming": true,
    "pushNotifications": false
  },
  "authentication": {
    "type": "bearer"
  },
  "methods": [
    "message/send",
    "message/stream"
  ]
}
```

**Required Fields**:
- `name`: Unique identifier
- `description`: What the agent does
- `url`: Base endpoint
- `methods`: Supported A2A methods

### A2A Message Format

**Request**:
```json
{
  "jsonrpc": "2.0",
  "method": "message/send",
  "params": {
    "message": {
      "role": "user",
      "parts": [{"text": "Analyze this data"}]
    },
    "contextId": "thread-123"
  },
  "id": 1
}
```

**Response (Task)**:
```json
{
  "jsonrpc": "2.0",
  "result": {
    "id": "task-456",
    "status": "completed",
    "result": {
      "parts": [{"text": "Analysis complete..."}]
    }
  },
  "id": 1
}
```

### Task States

| State | Meaning |
|-------|---------|
| `created` | Task accepted, not started |
| `running` | Actively processing |
| `completed` | Success with result |
| `failed` | Error occurred |
| `canceled` | Stopped by client |

---

## 5. Common Patterns

### Pattern 1: FastMCP with Type Hints

```python
from fastmcp import FastMCP
from pydantic import BaseModel

class SearchResult(BaseModel):
    title: str
    url: str
    score: float

mcp = FastMCP("search-server")

@mcp.tool
def search(query: str, limit: int = 5) -> list[SearchResult]:
    """Search documents by query."""
    # Implementation
```

### Pattern 2: A2A Client Call

```python
from pydantic_ai.a2a import A2AClient

async def call_agent(message: str):
    client = A2AClient("https://agent.example.com")
    task = await client.send_message(
        message=message,
        context_id="session-1"
    )
    return task.result
```

### Pattern 3: Protocol Bridge

```python
from pydantic_ai import Agent

agent = Agent("openai:gpt-4o", tools=[...])

# Automatic A2A wrapper
app = agent.to_a2a()
```

### Pattern 4: MCP Router for Modularity

```python
from fastmcp import FastMCP, MCPRouter

router = MCPRouter()

@router.tool
def specialized_tool(x: int) -> int:
    return x * 2

mcp = FastMCP("main")
mcp.include_router(router, prefix="math")
```

---

## 6. Architecture Diagrams

### MCP Server Architecture (ASCII)

```
                    ┌─────────────────┐
                    │   MCP CLIENT    │
                    └────────┬────────┘
                             │
                    JSON-RPC │ (stdio or HTTP)
                             │
                    ┌────────▼────────┐
                    │   MCP SERVER    │
                    │                 │
    ┌───────────────┼─────────────────┼───────────────┐
    │               │                 │               │
    ▼               ▼                 ▼               │
┌───────┐      ┌──────────┐      ┌─────────┐         │
│ TOOLS │      │RESOURCES │      │ PROMPTS │         │
│ Model │      │   App    │      │  User   │         │
│ Ctrl  │      │  Ctrl    │      │  Ctrl   │         │
└───────┘      └──────────┘      └─────────┘         │
                                                      │
    ─────────────────────────────────────────────────┘
                             │
                    ┌────────▼────────┐
                    │ External APIs   │
                    │ Databases       │
                    │ Services        │
                    └─────────────────┘
```

### A2A Discovery Flow (ASCII)

```
┌──────────┐                           ┌──────────┐
│  Client  │                           │  Agent   │
└────┬─────┘                           └────┬─────┘
     │                                      │
     │ GET /.well-known/agent.json          │
     │─────────────────────────────────────►│
     │                                      │
     │◄─────────────────────────────────────│
     │        Agent Card (JSON)             │
     │                                      │
     │ POST /message/send                   │
     │ {message, contextId}                 │
     │─────────────────────────────────────►│
     │                                      │
     │◄─────────────────────────────────────│
     │        Task (completed/running)      │
     │                                      │
```

### Security Layers (ASCII)

```
┌─────────────────────────────────────────────────────┐
│ Layer 5: EXTERNAL API ACCESS                        │
│   Downstream systems honor agent+delegator perms    │
├─────────────────────────────────────────────────────┤
│ Layer 4: TOOL-LEVEL ACCESS                          │
│   Fine-grained permissions per tool                 │
├─────────────────────────────────────────────────────┤
│ Layer 3: MCP SERVER ACCESS                          │
│   Agent authenticates, tool exposure decisions      │
├─────────────────────────────────────────────────────┤
│ Layer 2: DELEGATOR AUTHENTICATION                   │
│   User consent with permission boundaries           │
├─────────────────────────────────────────────────────┤
│ Layer 1: AGENT IDENTITY                             │
│   Distinct, traceable (not shared API keys)         │
└─────────────────────────────────────────────────────┘
```

### Protocol Bridge (ASCII)

```
    External Agent
         │
         │ A2A (message/send)
         ▼
┌─────────────────────────────────────┐
│         A2A BRIDGE LAYER            │
│  ┌────────────────────────────────┐ │
│  │ - Agent Card Discovery         │ │
│  │ - Request Translation          │ │
│  │ - Response Mapping             │ │
│  └────────────────────────────────┘ │
└─────────────────────────────────────┘
         │
         │ MCP (tools/call)
         ▼
┌─────────────────────────────────────┐
│           MCP SERVER                │
│  ┌────────┐ ┌────────┐ ┌────────┐  │
│  │ Tool 1 │ │ Tool 2 │ │ Tool 3 │  │
│  └────────┘ └────────┘ └────────┘  │
└─────────────────────────────────────┘
```

### Production Deployment (ASCII)

```
                   ┌─────────────────┐
                   │  LOAD BALANCER  │
                   └────────┬────────┘
                            │
         ┌──────────────────┼──────────────────┐
         │                  │                  │
         ▼                  ▼                  ▼
   ┌──────────┐       ┌──────────┐       ┌──────────┐
   │ Agent 1  │       │ Agent 2  │       │ Agent 3  │
   │  (A2A)   │       │  (A2A)   │       │  (A2A)   │
   └────┬─────┘       └────┬─────┘       └────┬─────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                  ┌────────▼────────┐
                  │   MCP GATEWAY   │
                  └────────┬────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
  ┌───────────┐      ┌───────────┐      ┌───────────┐
  │MCP Server │      │MCP Server │      │MCP Server │
  │  (Tools)  │      │(Resources)│      │ (Prompts) │
  └───────────┘      └───────────┘      └───────────┘
```

---

## 7. Best Practices

### MCP Server Development

| Practice | Rationale |
|----------|-----------|
| Use type hints | Auto-generates JSON Schema |
| Write docstrings | Becomes tool description |
| Validate inputs | Prevents injection attacks |
| Return structured data | LLM can interpret results |
| Use MCPRouter | Modular organization |

### A2A Integration

| Practice | Rationale |
|----------|-----------|
| Version Agent Cards | Track capability changes |
| Support streaming | Better UX for long tasks |
| Handle task states | Robust error recovery |
| Use contextId | Maintain conversation state |
| Implement timeouts | Prevent hung requests |

### Security

| Practice | Rationale |
|----------|-----------|
| OAuth 2.1 for headless | Proper token management |
| Rotate API keys | Limit exposure window |
| Log all calls | Audit trail |
| Tool-level RBAC | Least privilege |
| Human-in-the-loop | Critical operations |

---

## 8. Common Issues

### Issue: MCP Server Won't Start

**Symptoms**: Server process exits immediately
**Causes**:
- Missing `if __name__ == "__main__":`
- Port already in use
- Import errors in tools

**Fix**:
```python
if __name__ == "__main__":
    mcp.run()
```

### Issue: Tool Schema Not Generated

**Symptoms**: Tool appears but has no parameters
**Causes**:
- Missing type hints
- Non-serializable return types

**Fix**: Add explicit type hints
```python
def tool(x: str) -> str:  # Not just def tool(x):
```

### Issue: A2A Discovery Fails

**Symptoms**: 404 on `/.well-known/agent.json`
**Causes**:
- Agent Card not deployed
- Wrong URL in client

**Fix**: Verify Agent Card location

### Issue: Task Stuck in "running"

**Symptoms**: Task never completes
**Causes**:
- Long-running operation
- Missing await
- Deadlock

**Fix**: Check async patterns, add timeouts

### Issue: Cross-Agent Auth Failure

**Symptoms**: 401/403 from remote agent
**Causes**:
- Token expired
- Wrong auth method
- Missing scope

**Fix**: Verify OAuth flow, check Agent Card auth requirements

---

## 9. Debugging Tips

### MCP Debugging

**Enable Verbose Logging**:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

**Test Tools Directly**:
```python
# Before wrapping in MCP
result = my_tool("test input")
print(result)
```

**Check Schema Generation**:
```python
print(mcp.tools)  # List registered tools
```

### A2A Debugging

**Validate Agent Card**:
```bash
curl https://agent.example.com/.well-known/agent.json | jq
```

**Test Message Send**:
```bash
curl -X POST https://agent.example.com/message/send \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"message/send","params":{"message":{"role":"user","parts":[{"text":"test"}]}},"id":1}'
```

**Check Task Status**:
```bash
curl https://agent.example.com/tasks/{task_id}
```

### Logging Checklist

- [ ] Log all incoming requests
- [ ] Log tool invocations with params
- [ ] Log response times
- [ ] Log errors with context
- [ ] Log authentication events

---

## 10. Interview Questions

### Conceptual Questions

1. **What's the difference between MCP and A2A?**
   - MCP: Agent-to-tool (vertical), within trust boundary
   - A2A: Agent-to-agent (horizontal), across boundaries

2. **When would you use both protocols together?**
   - Agent needs tools (MCP) AND collaborates with other agents (A2A)
   - Example: Research agent with search tools talks to analysis agent

3. **What are the three MCP primitives and their control models?**
   - Tools: Model-controlled (LLM decides)
   - Resources: App-controlled (host decides)
   - Prompts: User-controlled (explicit selection)

4. **How does agent discovery work in A2A?**
   - Agent Card at `/.well-known/agent.json`
   - Describes capabilities, methods, authentication
   - Client negotiates based on supported features

### Scenario Questions

5. **Your agent needs to access a company database. MCP or A2A?**
   - MCP - it's tool access, not agent communication

6. **Two teams have agents that need to collaborate. Approach?**
   - A2A for cross-team communication
   - Each agent has Agent Card
   - Proper authentication between teams

7. **How would you handle a slow remote agent?**
   - Use streaming (`message/stream`)
   - Implement timeouts
   - Handle partial results
   - Consider async patterns

8. **What security considerations for cross-agent calls?**
   - Five security layers
   - OAuth 2.1 / mTLS
   - Tool-level permissions
   - Audit logging
   - Zero trust principles

---

## 11. Resources & Links

### Core Specifications

| Resource | URL |
|----------|-----|
| MCP Specification | [modelcontextprotocol.io/specification/2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25) |
| A2A Protocol | [a2a-protocol.org/latest](https://a2a-protocol.org/latest/) |
| MCP Python SDK | [github.com/modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) |

### Implementation Guides

| Resource | URL |
|----------|-----|
| FastMCP Quickstart | [gofastmcp.com/getting-started/quickstart](https://gofastmcp.com/getting-started/quickstart) |
| FastMCP Tools | [gofastmcp.com/servers/tools](https://gofastmcp.com/servers/tools) |
| PydanticAI A2A | [ai.pydantic.dev/a2a](https://ai.pydantic.dev/a2a/) |
| LangChain MCP | [docs.langchain.com/oss/python/langchain/mcp](https://docs.langchain.com/oss/python/langchain/mcp) |

### Security Resources

| Resource | URL |
|----------|-----|
| OWASP MCP Guide | [genai.owasp.org/resource/cheatsheet-a-practical-guide-for-securely-using-third-party-mcp-servers-1-0](https://genai.owasp.org/resource/cheatsheet-a-practical-guide-for-securely-using-third-party-mcp-servers-1-0/) |
| MCP Security Best Practices | [modelcontextprotocol.io/specification/draft/basic/security_best_practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices) |

### Industry Context

| Resource | URL |
|----------|-----|
| Anthropic MCP Announcement | [anthropic.com/news/model-context-protocol](https://www.anthropic.com/news/model-context-protocol) |
| Linux Foundation AAIF | [linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) |
| A2A Enterprise Guide | [agent2agent.info/blog/implementing-a2a-in-enterprise](https://agent2agent.info/blog/implementing-a2a-in-enterprise/) |

### Example Servers

| Server | Purpose |
|--------|---------|
| [Everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) | Reference/test server |
| [Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) | Web content fetching |
| [Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | Secure file operations |
| [Git](https://github.com/modelcontextprotocol/servers/tree/main/src/git) | Git repository tools |

---

## 12. Key Takeaways

1. **MCP = Vertical**: Connects agents to tools, databases, APIs within trust boundary

2. **A2A = Horizontal**: Enables agent-to-agent communication across organizations

3. **FastMCP for servers**: Decorators + type hints = automatic schema generation

4. **Agent Cards for discovery**: JSON at `/.well-known/agent.json` describes capabilities

5. **Three A2A methods**: `message/send` (sync), `message/stream` (SSE), `tasks/get` (poll)

6. **Task lifecycle matters**: created -> running -> completed/failed/canceled

7. **Five security layers**: Agent identity -> delegator -> MCP server -> tool -> external API

8. **Bridge when needed**: Wrap MCP servers in A2A for cross-agent tool access

9. **Production considerations**: Stateless scaling, monitoring, multi-tenancy, security

---

## Quick Decision Tree

```
Need to add capabilities to your agent?
│
├─► External tool/API/database?
│   └─► Use MCP
│
├─► Collaborate with another agent?
│   │
│   ├─► Same process?
│   │   └─► Direct call
│   │
│   ├─► Same organization?
│   │   └─► A2A (internal)
│   │
│   └─► Cross-organization?
│       └─► A2A (with auth)
│
├─► Stateful workflow with checkpoints?
│   └─► Consider ACP
│
└─► Tools + agent collaboration?
    └─► MCP + A2A together
```

---

*Session 17 Cheatsheet | MCP Servers & A2A | AIE9 Bootcamp*
