# Session 14 Cheatsheet: MCP Connectors

> Connecting AI Applications to External Systems with the Model Context Protocol

---

## Quick Reference

| Concept | Definition | Key API/Pattern |
|---------|------------|-----------------|
| MCP | Open protocol for AI-to-data connections | JSON-RPC 2.0 |
| Server | Exposes tools, resources, prompts | `FastMCP("name")` |
| Client | Connects to MCP servers | `MultiServerMCPClient({...})` |
| Tool | Model-controlled executable function | `@mcp.tool` |
| Resource | Application-controlled data/context | `@mcp.resource` |
| Prompt | User-controlled interaction template | `@mcp.prompt` |
| Transport | Communication layer (stdio/HTTP) | `command` or `url` |
| Host | Application managing MCP clients | Claude Desktop, LangGraph |

---

## Setup Requirements

### Dependencies
```bash
pip install mcp>=1.0.0 langchain-mcp-adapters fastmcp>=1.0.0
pip install langgraph langchain-openai langsmith
```

### Environment Variables
```python
import os
os.environ["OPENAI_API_KEY"] = "your-key"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-langsmith-key"
os.environ["LANGCHAIN_PROJECT"] = "AIE9-Session14"
```

---

## 1. MCP Overview

### What is MCP?
> **"MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems. Think of MCP like a USB-C port for AI applications."**
> — MCP Introduction [[1]](https://modelcontextprotocol.io/docs/getting-started/intro)

### The M×N Problem
```
┌────────────────────────────────────────────────────────────────┐
│  WITHOUT MCP                    WITH MCP                        │
│                                                                 │
│  App1 ────┐                    App1 ──┐                        │
│  App2 ────┼──── Source1        App2 ──┼── MCP ── Source1       │
│  App3 ────┼──── Source2        App3 ──┘         Source2        │
│           └──── Source3                          Source3        │
│                                                                 │
│  M×N connections               M+N connections                  │
└────────────────────────────────────────────────────────────────┘
```

### Key Insight
> "The numbers tell the story: 97 million monthly SDK downloads. Over 10,000 active servers. First-class client support in Claude, ChatGPT, Cursor, Gemini, Microsoft Copilot, and VS Code."
> — A Year of MCP [[2]](https://www.pento.ai/blog/a-year-of-mcp-2025-review)

**Official Docs**: [MCP Introduction](https://modelcontextprotocol.io/docs/getting-started/intro) [[1]](https://modelcontextprotocol.io/docs/getting-started/intro)

---

## 2. The Three Core Primitives

### Control Model Diagram
```
┌────────────────────────────────────────────────────────────────┐
│                    MCP PRIMITIVES                               │
│                                                                 │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│   │    TOOLS     │  │  RESOURCES   │  │   PROMPTS    │        │
│   │              │  │              │  │              │        │
│   │  Model       │  │  Application │  │    User      │        │
│   │  Controlled  │  │  Controlled  │  │  Controlled  │        │
│   │              │  │              │  │              │        │
│   │  Functions   │  │  Data/Docs   │  │  Templates   │        │
│   └──────────────┘  └──────────────┘  └──────────────┘        │
│                                                                 │
│  LLM decides      App chooses        User invokes              │
│  when to call     what to include    explicitly                │
└────────────────────────────────────────────────────────────────┘
```

### Primitives Comparison
| Primitive | Control | Discovery | Example |
|-----------|---------|-----------|---------|
| **Tools** | Model | Listed at init | `search_database(query)` |
| **Resources** | Application | URI patterns | `file://docs/api.md` |
| **Prompts** | User | Slash commands | `/summarize [topic]` |

### Key Quote
> "Tools in MCP are designed to be model-controlled, meaning that the language model can discover and invoke tools automatically based on its contextual understanding."
> — MCP Tools Specification [[3]](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)

**Official Docs**: [MCP Primitives](https://modelcontextprotocol.io/specification/2025-11-25) [[3]](https://modelcontextprotocol.io/specification/2025-11-25)

---

## 3. MCP Architecture

### Client-Host-Server Model
```
┌─────────────────────────────────────────────────────────────┐
│                APPLICATION HOST PROCESS                      │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │                      HOST                               │ │
│  │  (Manages clients, enforces security boundaries)       │ │
│  └───────────┬──────────────┬──────────────┬──────────────┘ │
│              │              │              │                 │
│        ┌─────┴─────┐  ┌─────┴─────┐  ┌─────┴─────┐         │
│        │ Client 1  │  │ Client 2  │  │ Client 3  │         │
│        └─────┬─────┘  └─────┬─────┘  └─────┬─────┘         │
└──────────────│──────────────│──────────────│────────────────┘
               │ stdio        │ stdio        │ HTTP
               ▼              ▼              ▼
        ┌──────────┐   ┌──────────┐   ┌──────────┐
        │ Server A │   │ Server B │   │ Server C │
        │ (Files)  │   │   (DB)   │   │  (API)   │
        └──────────┘   └──────────┘   └──────────┘
```

### Architecture Components
| Component | Role | Example |
|-----------|------|---------|
| Host | Application process | Claude Desktop, LangGraph app |
| Client | Server connection manager | One client per server |
| Server | Capability provider | Filesystem, database |
| Transport | Communication layer | stdio, Streamable HTTP |

### Key Quote
> "The Model Context Protocol (MCP) follows a client-host-server architecture where each host can run multiple client instances."
> — MCP Architecture [[4]](https://modelcontextprotocol.io/specification/2025-11-25/architecture/index)

**Official Docs**: [MCP Architecture](https://modelcontextprotocol.io/specification/2025-11-25/architecture/index) [[4]](https://modelcontextprotocol.io/specification/2025-11-25/architecture/index)

---

## 4. Transport Mechanisms

### Transport Comparison
| Transport | Protocol | Use Case | Auth |
|-----------|----------|----------|------|
| **stdio** | stdin/stdout | Local servers | Environment vars |
| **Streamable HTTP** | HTTP + SSE | Remote servers | OAuth 2.1 |

### stdio Transport (Local)
```python
# Client launches server as subprocess
{
    "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/data"]
    }
}
```

### Streamable HTTP Transport (Remote)
```python
# Client connects to remote server
{
    "remote-api": {
        "transport": "streamable_http",
        "url": "https://mcp.example.com/mcp",
        "headers": {"Authorization": f"Bearer {token}"}
    }
}
```

### Lifecycle Phases
```
┌────────────────────────────────────────────────────────────┐
│                   MCP LIFECYCLE                             │
│                                                             │
│  1. INITIALIZATION    2. OPERATION    3. SHUTDOWN          │
│  ┌─────────────┐      ┌───────────┐   ┌───────────┐       │
│  │ Capability  │  --> │ JSON-RPC  │-->│ Graceful  │       │
│  │ Negotiation │      │ Messages  │   │ Terminate │       │
│  └─────────────┘      └───────────┘   └───────────┘       │
└────────────────────────────────────────────────────────────┘
```

**Official Docs**: [MCP Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports) [[5]](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)

---

## 5. Building MCP Servers with FastMCP

### What is FastMCP?
> **"FastMCP is the standard framework for building MCP applications. The Model Context Protocol (MCP) provides a standardized way to connect LLMs to tools and data, and FastMCP makes it production-ready."**
> — FastMCP Welcome [[6]](https://gofastmcp.com/getting-started/welcome)

### Minimal Server Pattern
```python
from fastmcp import FastMCP

mcp = FastMCP("My Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

### Adding Resources
```python
@mcp.resource("config://app-settings")
def get_config() -> str:
    """Application configuration."""
    return '{"theme": "dark", "version": "1.0"}'
```

### Adding Prompts
```python
@mcp.prompt
def summarize(topic: str) -> str:
    """Generate a summarization prompt."""
    return f"Please summarize the following topic: {topic}"
```

### FastMCP Decorator Reference
| Decorator | Primitive | Control |
|-----------|-----------|---------|
| `@mcp.tool` | Tool | Model |
| `@mcp.resource` | Resource | Application |
| `@mcp.prompt` | Prompt | User |

**Official Docs**: [FastMCP Documentation](https://gofastmcp.com) [[6]](https://gofastmcp.com)

---

## 6. LangChain MCP Integration

### MultiServerMCPClient Pattern
```python
from langchain_mcp_adapters.client import MultiServerMCPClient

async with MultiServerMCPClient({
    "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/data"]
    },
    "database": {
        "command": "python",
        "args": ["-m", "my_db_server"]
    }
}) as client:
    # Get all tools from all servers
    tools = await client.get_tools()

    # Use with LangGraph agent
    agent = create_react_agent(model, tools)
```

### Key Quote
> "Model Context Protocol (MCP) is an open protocol that standardizes how applications provide tools and context to LLMs. LangChain agents can use tools defined on MCP servers."
> — LangChain MCP Documentation [[7]](https://docs.langchain.com/oss/python/langchain/mcp)

### Stateless vs Stateful Sessions
| Mode | Behavior | Use Case |
|------|----------|----------|
| Stateless | Fresh session per invocation | Simple queries |
| Stateful | Persistent session | Multi-step workflows |

```python
# Stateful session example
async with client.session("filesystem") as session:
    # Multiple calls share context
    await session.call_tool("list_files", {"path": "/"})
    await session.call_tool("read_file", {"path": "/doc.md"})
```

**Official Docs**: [LangChain MCP](https://docs.langchain.com/oss/python/langchain/mcp) [[7]](https://docs.langchain.com/oss/python/langchain/mcp)

---

## 7. Agentic RAG with MCP

### Architecture Pattern
```
┌────────────────────────────────────────────────────────────────┐
│                   AGENTIC RAG + MCP                             │
│                                                                 │
│  Query --> Agent --> (needs context?) --> MCP Server            │
│               │               │                │                │
│               │               │                ▼                │
│               │               │         ┌──────────┐           │
│               │               │         │ Database │           │
│               │               │         │   Files  │           │
│               │               │         │   APIs   │           │
│               │               │         └──────────┘           │
│               │               │                │                │
│               │               └── retrieve ────┘                │
│               ▼                                                 │
│           Generate Response                                     │
└────────────────────────────────────────────────────────────────┘
```

### LangGraph Implementation
```python
from langgraph.graph import StateGraph, START, END
from langchain_mcp_adapters.client import MultiServerMCPClient

class RAGState(TypedDict):
    messages: Annotated[list, add_messages]
    documents: list
    needs_retrieval: bool

async def retrieve_via_mcp(state: RAGState) -> dict:
    """Use MCP tools for retrieval."""
    async with MultiServerMCPClient(mcp_config) as client:
        tools = await client.get_tools()
        search_tool = next(t for t in tools if "search" in t.name)
        results = await search_tool.ainvoke({"query": state["query"]})
    return {"documents": results}

builder = StateGraph(RAGState)
builder.add_node("retrieve", retrieve_via_mcp)
builder.add_node("generate", generate_response)
builder.add_conditional_edges("agent", route_decision)
```

---

## 8. Fuzzy-to-Fact Pattern

### The Problem: Hallucinated Identifiers
Agents often guess or hallucinate entity identifiers, leading to invalid API calls:
```
Agent: "Query gene BRCA1..."
API: Error - "BRCA1" is not a valid HGNC CURIE
```

### The Solution: Two-Phase Validation
```
┌────────────────────────────────────────────────────────────────┐
│               FUZZY-TO-FACT PROTOCOL                            │
│                                                                 │
│  PHASE 1: FUZZY DISCOVERY                                      │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  search_genes("p53")                                     │  │
│  │  → Ranked candidates with similarity scores              │  │
│  │  → [{"id": "HGNC:11998", "name": "TP53", "score": 0.95}] │  │
│  └─────────────────────────────────────────────────────────┘  │
│                           │                                     │
│                           ▼                                     │
│  PHASE 2: STRICT EXECUTION                                     │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │  get_gene("HGNC:11998")                                  │  │
│  │  → Full record with cross-references                     │  │
│  │  → Guaranteed valid identifier                           │  │
│  └─────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────┘
```

### Error Envelope Pattern
```python
class ErrorEnvelope(BaseModel):
    success: bool = False
    error: ErrorDetail

class ErrorDetail(BaseModel):
    code: str           # "UNRESOLVED_ENTITY"
    message: str        # Human-readable error
    recovery_hint: str  # "Call search_genes first"
    invalid_input: str  # The bad input that was passed
```

### Implementation
```python
@mcp.tool
def get_gene(hgnc_id: str) -> GeneRecord:
    """Get gene by HGNC CURIE. Requires valid ID from search_genes."""
    if not hgnc_id.startswith("HGNC:"):
        return ErrorEnvelope.unresolved_entity(
            hgnc_id,
            "Call search_genes to resolve the identifier first."
        )
    return fetch_gene_record(hgnc_id)
```

**Source**: [lifesciences-research ADR-001](https://github.com/donbr/lifesciences-research) [[8]](https://github.com/donbr/lifesciences-research)

---

## 9. Token Budgeting with Slim Mode

### The Problem: Context Window Flooding
Full entity records flood the context window during multi-hop reasoning:
- Full record: ~115-300 tokens per entity
- 10 entities × 4 hops = 4,000-12,000 tokens wasted

### The Solution: Slim Mode
```python
@mcp.tool
def search_genes(query: str, slim: bool = False) -> list:
    """Search genes with optional slim mode for token efficiency."""
    results = api.search(query)

    if slim:
        # ~20 tokens per entity
        return [{"id": r.id, "name": r.name, "score": r.score}
                for r in results]
    else:
        # ~115-300 tokens per entity
        return [r.full_record() for r in results]
```

### Token Comparison
| Mode | Tokens/Entity | Use Case |
|------|---------------|----------|
| Full | 115-300 | Final retrieval, display |
| Slim | ~20 | Multi-hop reasoning, scanning |

### Null Handling Policy
```python
# BAD: Wastes tokens
{"hgnc": "HGNC:1100", "ensembl": null, "uniprot": null}

# GOOD: Omit null keys entirely
{"hgnc": "HGNC:1100"}
```

---

## 10. Security Best Practices

### Security Risks
| Risk | Description | Mitigation |
|------|-------------|------------|
| Confused Deputy | Proxy executes unintended actions | Validate all requests |
| Prompt Injection | Malicious data triggers actions | Input sanitization |
| Permission Escalation | Beyond intended scope | Least privilege |
| Credential Exposure | Secrets in logs/errors | Environment-only storage |

### Security Checklist
```
┌────────────────────────────────────────────────────────────────┐
│              MCP SECURITY CHECKLIST                             │
│                                                                 │
│  □ Human-in-the-loop for sensitive actions                    │
│  □ Input validation on all tool parameters                    │
│  □ Rate limiting on tool invocations                          │
│  □ OAuth 2.1 for HTTP transports                              │
│  □ Audit logging of all MCP interactions                      │
│  □ Environment variables for secrets (never hardcode)         │
│  □ Least privilege: expose only necessary tools               │
│  □ Structured error responses (no stack traces)               │
└────────────────────────────────────────────────────────────────┘
```

### Key Quote
> "Clients must carefully evaluate whether an action should proceed, even if an MCP server requests it."
> — MCP Security Best Practices [[9]](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)

**Official Docs**: [MCP Security](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) [[9]](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)

---

## 11. Client-Side vs Server-Side MCP

### Decision Matrix
| Factor | Client-Side | Server-Side |
|--------|-------------|-------------|
| **Role** | Consume existing servers | Build new servers |
| **Setup** | Config + adapters | FastMCP + implementation |
| **Ecosystem** | 10,000+ servers | Custom data sources |
| **Maintenance** | Update configs | Full lifecycle |
| **Control** | Limited to server capabilities | Full control |

### When to Use Client-Side
- Quick integration with existing MCP servers
- Leveraging community-built capabilities
- Prototyping agent workflows

### When to Build Server-Side
- Exposing proprietary data sources
- Custom validation logic (Fuzzy-to-Fact)
- Domain-specific token optimization

### Gateway Composition Pattern
```python
# Compose multiple servers into one endpoint
mcp = FastMCP("Gateway")

mcp.mount(hgnc_mcp, prefix="hgnc", tool_names={
    "search_genes": "hgnc_search_genes"
})
mcp.mount(uniprot_mcp, prefix="uniprot", tool_names={
    "search_proteins": "uniprot_search_proteins"
})
```

---

## 12. Common Issues & Debugging

### Troubleshooting Table
| Issue | Cause | Fix |
|-------|-------|-----|
| Server not found | Wrong command/path | Verify `command` and `args` |
| Connection timeout | Server crashed | Check server logs |
| Tool not available | Capability mismatch | Verify tool registration |
| Auth failure | Missing/expired token | Refresh OAuth token |
| Rate limited | Too many requests | Implement backoff |
| Invalid response | Schema mismatch | Check return types |

### Debugging with LangSmith
```python
# Enable tracing to see MCP interactions
os.environ["LANGCHAIN_TRACING_V2"] = "true"
```

### Common Patterns
```python
# Pattern: Check server health before use
async with MultiServerMCPClient(config) as client:
    try:
        tools = await client.get_tools()
        if not tools:
            raise ValueError("No tools available")
    except Exception as e:
        logger.error(f"MCP connection failed: {e}")
```

### Error Recovery Pattern
```python
@mcp.tool
def robust_search(query: str) -> SearchResult | ErrorEnvelope:
    """Search with structured error handling."""
    try:
        return perform_search(query)
    except RateLimitError:
        return ErrorEnvelope.rate_limited("Retry after 5 seconds")
    except ValueError as e:
        return ErrorEnvelope.invalid_input(str(e))
```

---

## Code Patterns Reference

### Pattern 1: Basic MCP Client
```python
from langchain_mcp_adapters.client import MultiServerMCPClient

async with MultiServerMCPClient({
    "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/data"]
    }
}) as client:
    tools = await client.get_tools()
```

### Pattern 2: FastMCP Server with All Primitives
```python
from fastmcp import FastMCP

mcp = FastMCP("Full Server")

@mcp.tool
def search(query: str) -> list:
    """Search the database."""
    return db.search(query)

@mcp.resource("config://settings")
def get_settings() -> str:
    """Application settings."""
    return json.dumps(config)

@mcp.prompt
def analyze(topic: str) -> str:
    """Generate analysis prompt."""
    return f"Analyze {topic} in depth."
```

### Pattern 3: LangGraph + MCP Agent
```python
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.client import MultiServerMCPClient

async def build_agent():
    async with MultiServerMCPClient(mcp_config) as client:
        tools = await client.get_tools()
        agent = create_react_agent(model, tools)
        return agent
```

### Pattern 4: Claude Desktop Configuration
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/me"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {"GITHUB_TOKEN": "your-token"}
    }
  }
}
```

---

## Breakout Room Tasks Summary

### Breakout Room 1 (Tasks 1-5)
- [ ] Install MCP dependencies (mcp, langchain-mcp-adapters)
- [ ] Configure MultiServerMCPClient with one server
- [ ] List available tools from the server
- [ ] Invoke a tool and examine the response
- [ ] Integrate tools with a simple LangGraph agent
- [ ] **Activity**: Add conditional retrieval logic

### Breakout Room 2 (Tasks 6-10)
- [ ] Build a FastMCP server with one tool
- [ ] Add a resource endpoint to the server
- [ ] Test the server with Claude Desktop or client
- [ ] Implement Fuzzy-to-Fact validation
- [ ] Add slim mode for token efficiency
- [ ] **Activity**: Deploy server for agentic RAG

---

## Official Documentation Links

### MCP Core
- [MCP Introduction](https://modelcontextprotocol.io/docs/getting-started/intro) [[1]](https://modelcontextprotocol.io/docs/getting-started/intro)
- [MCP Specification (2025-11-25)](https://modelcontextprotocol.io/specification/2025-11-25) [[3]](https://modelcontextprotocol.io/specification/2025-11-25)
- [MCP Architecture](https://modelcontextprotocol.io/specification/2025-11-25/architecture/index) [[4]](https://modelcontextprotocol.io/specification/2025-11-25/architecture/index)
- [MCP Transports](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports) [[5]](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)

### Tools and Primitives
- [MCP Tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools) [[3]](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)
- [MCP Resources](https://modelcontextprotocol.io/specification/2025-11-25/server/resources) [[10]](https://modelcontextprotocol.io/specification/2025-11-25/server/resources)
- [MCP Prompts](https://modelcontextprotocol.io/specification/2025-11-25/server/prompts) [[11]](https://modelcontextprotocol.io/specification/2025-11-25/server/prompts)

### SDKs and Frameworks
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) [[12]](https://github.com/modelcontextprotocol/python-sdk)
- [FastMCP Documentation](https://gofastmcp.com) [[6]](https://gofastmcp.com)
- [LangChain MCP Adapters](https://docs.langchain.com/oss/python/langchain/mcp) [[7]](https://docs.langchain.com/oss/python/langchain/mcp)

### Security and Authorization
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) [[9]](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [MCP Authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) [[13]](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)

### Examples
- [lifesciences-research](https://github.com/donbr/lifesciences-research) [[8]](https://github.com/donbr/lifesciences-research)
- [MCP Example Servers](https://modelcontextprotocol.io/examples) [[14]](https://modelcontextprotocol.io/examples)

---

## References

1. Model Context Protocol. "Introduction to MCP." https://modelcontextprotocol.io/docs/getting-started/intro

2. Pento. "A Year of MCP: From Internal Experiment to Industry Standard." https://www.pento.ai/blog/a-year-of-mcp-2025-review

3. Model Context Protocol. "MCP Specification - Tools." https://modelcontextprotocol.io/specification/2025-11-25/server/tools

4. Model Context Protocol. "MCP Architecture." https://modelcontextprotocol.io/specification/2025-11-25/architecture/index

5. Model Context Protocol. "MCP Transports." https://modelcontextprotocol.io/specification/2025-11-25/basic/transports

6. FastMCP. "Getting Started." https://gofastmcp.com/getting-started/welcome

7. LangChain Documentation. "MCP Integration." https://docs.langchain.com/oss/python/langchain/mcp

8. donbr. "lifesciences-research." https://github.com/donbr/lifesciences-research

9. Model Context Protocol. "Security Best Practices." https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices

10. Model Context Protocol. "MCP Resources." https://modelcontextprotocol.io/specification/2025-11-25/server/resources

11. Model Context Protocol. "MCP Prompts." https://modelcontextprotocol.io/specification/2025-11-25/server/prompts

12. GitHub. "MCP Python SDK." https://github.com/modelcontextprotocol/python-sdk

13. Model Context Protocol. "Authorization." https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization

14. Model Context Protocol. "Example Servers." https://modelcontextprotocol.io/examples

---

*Cheatsheet created for AIE9 Session 14: MCP Connectors*
*Last updated: January 2026*
