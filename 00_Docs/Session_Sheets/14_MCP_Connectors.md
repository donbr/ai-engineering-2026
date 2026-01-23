# Session 14: MCP Connectors

**Goal**: Understand how to use the Model Context Protocol (MCP) to enhance retrieval and extend agent capabilities

**Learning Outcomes**
- Understand the MCP architecture (servers, clients, resources, tools)
- Learn the three core MCP primitives and their control models
- Build MCP clients that connect agents to external data sources
- Integrate MCP tools with LangChain agents for enhanced retrieval
- Evaluate pros and cons of client-side vs server-side MCP

**New Tools**
- Protocol: [Model Context Protocol](https://modelcontextprotocol.io)
- SDK: [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- Framework: [FastMCP](https://gofastmcp.com)
- Adapters: [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters)

## Required Tooling & Account Setup

In addition to the tools we've already learned, in this session you'll need:

1. MCP Python SDK: `pip install mcp>=1.0.0`
2. LangChain MCP Adapters: `pip install langchain-mcp-adapters`
3. FastMCP (optional, for building servers): `pip install fastmcp>=1.0.0`
4. Node.js (for reference server examples): `node --version` (v18+)

## Recommended Reading

1. [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) (Nov 2024)
2. [MCP Specification](https://modelcontextprotocol.io/specification/2025-11-25) - Latest spec with Tasks and OAuth
3. [LangChain MCP Documentation](https://docs.langchain.com/oss/python/langchain/mcp)
4. [FastMCP Welcome Guide](https://gofastmcp.com/getting-started/welcome)
5. [A Year of MCP: From Internal Experiment to Industry Standard](https://www.pento.ai/blog/a-year-of-mcp-2025-review)

---

# Overview

In previous sessions, we learned to build agents with tools and connect them to data sources. But what happens when you need to connect the same agent to multiple data sources? Or when different applications need access to the same data?

The answer is **MCP (Model Context Protocol)**.

> "MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems. Think of MCP like a USB-C port for AI applications."
> ~ [MCP Introduction](https://modelcontextprotocol.io/docs/getting-started/intro)

MCP solves the **M×N integration problem**. Instead of building custom integrations between M applications and N data sources (M×N total), MCP provides a standard protocol that reduces this to M+N implementations.

```
Without MCP:                    With MCP:
App1 ----+                      App1 --+
App2 ----+--- Source1           App2 --+-- MCP -- Source1
App3 ----+--- Source2           App3 --+         Source2
         +--- Source3                            Source3

M×N connections                 M+N connections
```

# Why MCP?

Until recently, every AI integration was bespoke. Claude Desktop talked to one set of APIs, ChatGPT to another, each agent framework had its own patterns. MCP changes this by providing a universal connector layer.

| Approach | Integration Effort | Reusability | Ecosystem |
|----------|-------------------|-------------|-----------|
| Custom integrations | High (per app×source) | Low | None |
| Framework-specific | Medium (per framework) | Within framework | Limited |
| MCP | Low (per source) | Any MCP client | Growing rapidly |

> "The numbers tell the story: 97 million monthly SDK downloads across Python and TypeScript. Over 10,000 active servers. First-class client support in Claude, ChatGPT, Cursor, Gemini, Microsoft Copilot, and Visual Studio Code."
> ~ [A Year of MCP](https://www.pento.ai/blog/a-year-of-mcp-2025-review)

In December 2025, Anthropic donated MCP to the Agentic AI Foundation (AAIF) under the Linux Foundation, with OpenAI, Google, Microsoft, and AWS as founding members.

# The Three Core Primitives

MCP servers expose three types of capabilities with different control models:

| Primitive | Control | Description | Example |
|-----------|---------|-------------|---------|
| **Tools** | Model-controlled | Executable functions | Database queries, API calls |
| **Resources** | Application-controlled | Structured data/context | Files, schemas, configs |
| **Prompts** | User-controlled | Reusable interaction templates | Slash commands, menu options |

The control model is key:
- **Tools**: The LLM decides when to call them (think: function calling)
- **Resources**: The application chooses what context to include
- **Prompts**: The user explicitly invokes them (think: `/search`)

> "Tools in MCP are designed to be model-controlled, meaning that the language model can discover and invoke tools automatically based on its contextual understanding and the user's prompts."
> ~ [MCP Tools Specification](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)

# MCP Architecture

MCP follows a client-host-server architecture built on JSON-RPC 2.0:

```
┌─────────────────────────────────────────────────────────────────┐
│                    APPLICATION HOST                              │
│                                                                  │
│  ┌──────────────────┐                                           │
│  │      Host        │  Manages clients, enforces boundaries     │
│  └────────┬─────────┘                                           │
│           │                                                      │
│  ┌────────┼─────────────────────────────────────┐               │
│  │        │         MCP CLIENTS                  │               │
│  │  ┌─────┴─────┐  ┌───────────┐  ┌───────────┐ │               │
│  │  │  Client 1 │  │  Client 2 │  │  Client 3 │ │               │
│  │  └─────┬─────┘  └─────┬─────┘  └─────┬─────┘ │               │
│  └────────│──────────────│──────────────│───────┘               │
└───────────│──────────────│──────────────│───────────────────────┘
            │ stdio        │ stdio        │ HTTP
            ▼              ▼              ▼
     ┌──────────┐   ┌──────────┐   ┌──────────┐
     │ Server A │   │ Server B │   │ Server C │
     │ (local)  │   │ (local)  │   │ (remote) │
     └────┬─────┘   └────┬─────┘   └────┬─────┘
          ▼              ▼              ▼
       [Files]       [Database]      [APIs]
```

**Key concepts**:
- **Host**: The application process (Claude Desktop, your agent)
- **Client**: Manages connection to one MCP server
- **Server**: Exposes tools, resources, prompts from a data source
- **Transport**: stdio for local servers, Streamable HTTP for remote

> "The Model Context Protocol (MCP) follows a client-host-server architecture where each host can run multiple client instances."
> ~ [MCP Architecture](https://modelcontextprotocol.io/specification/2025-11-25/architecture/index)

# Transport Mechanisms

MCP defines two standard transports:

| Transport | Use Case | Example |
|-----------|----------|---------|
| **stdio** | Local servers, subprocess | Claude Desktop + local tools |
| **Streamable HTTP** | Remote servers, cloud | Production deployments |

**stdio**: Client launches server as subprocess, communicates via stdin/stdout
- Best for local development
- Simple security model (same machine)
- Used by Claude Desktop, Cursor

**Streamable HTTP**: HTTP-based transport with Server-Sent Events
- Best for remote/cloud deployments
- Supports OAuth 2.1 authentication
- Replaced SSE transport in 2025 spec

# LangChain MCP Integration

LangChain provides the `langchain-mcp-adapters` library to use MCP tools in agents:

> "Model Context Protocol (MCP) is an open protocol that standardizes how applications provide tools and context to LLMs. LangChain agents can use tools defined on MCP servers using the langchain-mcp-adapters library."
> ~ [LangChain MCP Documentation](https://docs.langchain.com/oss/python/langchain/mcp)

The key class is `MultiServerMCPClient`, which connects to multiple MCP servers:

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
    tools = await client.get_tools()
    # Use tools with LangGraph agent
```

Each MCP server's tools become available to your agent as normal LangChain tools.

# Building MCP Servers with FastMCP

FastMCP is the leading Python framework for building MCP servers:

> "FastMCP is the standard framework for building MCP applications. The Model Context Protocol (MCP) provides a standardized way to connect LLMs to tools and data, and FastMCP makes it production-ready with clean, Pythonic code."
> ~ [FastMCP Welcome](https://gofastmcp.com/getting-started/welcome)

A minimal FastMCP server looks like this:

```python
from fastmcp import FastMCP

mcp = FastMCP("My Server")

@mcp.tool
def search_docs(query: str) -> str:
    """Search documentation for relevant content."""
    # Implementation here
    return results

if __name__ == "__main__":
    mcp.run()
```

The decorator pattern (`@mcp.tool`, `@mcp.resource`, `@mcp.prompt`) makes it easy to expose capabilities.

# Client-Side vs Server-Side MCP

Understanding when to use MCP as a client vs building your own servers:

| Aspect | Client-Side MCP | Server-Side MCP |
|--------|-----------------|-----------------|
| **When** | Consuming existing servers | Exposing your data/tools |
| **Examples** | Claude Desktop, LangChain agents | Custom data sources |
| **Setup** | Configuration + adapters | FastMCP + implementation |
| **Maintenance** | Update configs | Full lifecycle |

**Client-side pros**:
- Immediate access to ecosystem (10,000+ servers)
- No server development needed
- Configuration-driven

**Client-side cons**:
- Limited to available servers
- Server updates may break clients
- Network dependencies for remote servers

**Server-side pros**:
- Full control over exposed capabilities
- Custom logic and filtering
- Integration with proprietary systems

**Server-side cons**:
- Development and maintenance effort
- Security responsibility
- Deployment infrastructure

# Real-World Example: Life Sciences MCP

The [lifesciences-research](https://github.com/donbr/lifesciences-research) repository demonstrates production MCP patterns for drug discovery:

**Architecture**:
- 12 specialized MCP servers (one per API: HGNC, UniProt, ChEMBL, etc.)
- Gateway server composing all 12 into unified endpoint
- Fuzzy-to-Fact protocol preventing hallucinated mappings

**Key Pattern - Fuzzy-to-Fact**:
```
Phase 1: Fuzzy Discovery
  search_genes("p53") → Ranked candidates with scores

Phase 2: Strict Execution
  get_gene("HGNC:11998") → Full record with cross-references
```

This two-phase pattern ensures agents never hallucinate biological identifiers—they must first search, then use validated IDs.

**Token Budgeting**:
All search tools accept `slim=True` parameter:
- Default (False): Full records (~115-300 tokens/entity)
- Slim (True): Only id, name, score (~20 tokens/entity)

This prevents context window flooding during multi-hop reasoning.

# Security Considerations

MCP introduces new security surfaces. Key concerns from the specification:

| Risk | Description | Mitigation |
|------|-------------|------------|
| Confused Deputy | Proxy server runs unauthorized actions | Validate all requests |
| Prompt Injection | Malicious data triggers unwanted actions | Input sanitization |
| Permission Escalation | Tool access beyond intended scope | Least privilege |
| Credential Exposure | Secrets leaked in logs/errors | Environment-only storage |

> "Clients must carefully evaluate whether an action should proceed, even if an MCP server requests it."
> ~ [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)

**Best practices**:
1. Human-in-the-loop for sensitive actions
2. Input validation on all tool parameters
3. Rate limiting on tool invocations
4. OAuth 2.1 for HTTP transports
5. Audit logging of all MCP interactions

# Key Takeaways

1. **MCP is the USB-C of AI** — universal connector for data sources
2. **Three primitives**: Tools (model), Resources (app), Prompts (user)
3. **Client-host-server architecture** — hosts manage multiple clients
4. **Two transports**: stdio (local), Streamable HTTP (remote)
5. **LangChain integration** — `MultiServerMCPClient` for agents
6. **FastMCP** — Python framework for building servers
7. **Fuzzy-to-Fact pattern** — prevent hallucinated mappings
8. **Security first** — human-in-the-loop, validation, audit

# Assignment

Build an agentic RAG application that retrieves resources via MCP:

1. **Configure MCP client** to connect to at least one MCP server (filesystem, database, or custom)
2. **Build a LangGraph agent** that uses MCP tools for retrieval
3. **Implement conditional retrieval** — agent decides when to call MCP tools
4. **Add observability** — trace MCP tool invocations in LangSmith

**Stretch goals**:
- Build your own FastMCP server exposing custom data
- Implement Fuzzy-to-Fact validation pattern
- Add token budgeting with slim mode

# Advanced Build

Provide tool and data resources through an MCP server:

1. **Design an MCP server** that exposes tools for your domain
2. **Implement resource endpoints** for structured data access
3. **Add prompt templates** for common user workflows
4. **Deploy with Streamable HTTP** transport for remote access
5. **Integrate OAuth 2.1** for secure authentication

This prepares you for Session 15: Agent Servers, where we'll deploy production MCP infrastructure.

---

Do you have any questions about how to best prepare for Session 14 after reading? Please don't hesitate to provide direct feedback to `greg@aimakerspace.io` or `Dr Greg` on Discord!
