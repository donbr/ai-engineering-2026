# AIE9 Code Reference Index

> Comprehensive mapping of repositories to AI Engineering Bootcamp Cohort 9 sessions.

**Last Updated**: 2026-01-22

---

## 2026 Industry-Leading Platforms

The AI Engineering landscape has matured significantly. These are the **production-recommended** frameworks:

| Category | Leading Platform | Why |
|----------|-----------------|-----|
| **Agent Orchestration** | LangGraph | Graph-based state management, production-proven at scale (Klarna, Replit, Elastic) |
| **Multi-Agent** | LangGraph Swarm / OpenAI Agents SDK | Dynamic handoffs, supervisor patterns, native memory |
| **Tool Integration** | MCP (Model Context Protocol) | Industry standard since Dec 2025, adopted by OpenAI, Google, Anthropic |
| **Evaluation** | LangSmith + openevals/agentevals | Native LLM-as-judge, trajectory evaluation, production monitoring |
| **Vector Search** | Qdrant / Chroma | Mature, well-documented, strong LangChain integration |
| **Knowledge Graphs** | Neo4j GraphRAG | Production GraphRAG with LangChain integration |

---

## Session-to-Repository Mapping

| Session | Topic | Primary Repositories |
|---------|-------|----------------------|
| 01 | Vibe Check | openai-cookbook, anthropic-cookbook |
| 02 | Dense Vector Retrieval | langchain, qdrant, chroma |
| 03 | The Agent Loop | langchain-academy, langgraph, 12-factor-agents |
| 04 | Agentic RAG | langchain-academy, langgraph |
| 05 | Multi-Agent Systems | langgraph-swarm-py, openai-agents-python |
| 06 | Agent Memory | memory-agent, langchain-academy, agents-from-scratch |
| 07 | Deep Agents | deep-agents-from-scratch |
| 08 | Deep Research | deep_research_from_scratch, open_deep_research |
| 09 | Synthetic Data Generation | openai-cookbook |
| 10 | Agentic RAG Evaluation | openevals, agentevals, langsmith-sdk, intro-to-langsmith |
| 11 | Advanced Retrievers | neo4j-graphrag-python, qdrant |
| 14 | MCP Connectors | langchain-mcp-adapters, modelcontextprotocol/servers |
| 17 | MCP Servers A2A | modelcontextprotocol/python-sdk, inspector |
| 18 | Guardrails Caching | langchain, langsmith-sdk |

---

## LangChain Ecosystem

### Tutorial Repositories

| Repository | GitHub URL | Description | Sessions |
|------------|------------|-------------|----------|
| **langchain-academy** | [github.com/langchain-ai/langchain-academy](https://github.com/langchain-ai/langchain-academy) | Growing set of modules focused on LangGraph (Modules 0-5). Streaming, agents, memory, persistence. | 3, 4, 6 |
| **agents-from-scratch** | [github.com/langchain-ai/agents-from-scratch](https://github.com/langchain-ai/agents-from-scratch) | Build email assistant with HITL and memory. Agent basics, evaluation, Agent Inbox. | 6 |
| **deep-agents-from-scratch** | [github.com/langchain-ai/deep-agents-from-scratch](https://github.com/langchain-ai/deep-agents-from-scratch) | Five notebooks: ReAct loops, planning tools, context isolation, sub-agent delegation. | 7 |
| **deep_research_from_scratch** | [github.com/langchain-ai/deep_research_from_scratch](https://github.com/langchain-ai/deep_research_from_scratch) | Build deep researcher from scratch. Multi-agent patterns, parallel processing, MCP integration. | 8 |
| **intro-to-langsmith** | [github.com/langchain-ai/intro-to-langsmith](https://github.com/langchain-ai/intro-to-langsmith) | LangSmith Academy: observability, prompt engineering, evaluations, feedback, production monitoring. | 10 |
| **lca-lc-foundations** | [github.com/langchain-ai/lca-lc-foundations](https://github.com/langchain-ai/lca-lc-foundations) | Three modules introducing LangChain's most-used features. Requires Python 3.12-3.14. | 2, 3 |
| **langgraph-101** | [github.com/langchain-ai/langgraph-101](https://github.com/langchain-ai/langgraph-101) | Condensed academy: models, tools, memory, streaming. LG201 for multi-agent patterns. | 3, 5 |
| **langsmith-cookbook** | [github.com/langchain-ai/langsmith-cookbook](https://github.com/langchain-ai/langsmith-cookbook) | Practical recipes for debugging, evaluating, testing, and improving LLM applications. | 10 |
| **learning-langchain** | [github.com/langchain-ai/learning-langchain](https://github.com/langchain-ai/learning-langchain) | Agent evaluation for RAG and SQL, creating datasets. | 10 |

### Agent Libraries

| Repository | GitHub URL | Description | Sessions |
|------------|------------|-------------|----------|
| **langgraph** | [github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Low-level orchestration for stateful agents. Used by Klarna, Replit, Elastic. Memory, streaming. | 3, 4, 5, 6, 7 |
| **langgraph-swarm-py** | [github.com/langchain-ai/langgraph-swarm-py](https://github.com/langchain-ai/langgraph-swarm-py) | Multi-agent swarm with dynamic handoffs based on specializations. | 5 |
| **memory-agent** | [github.com/langchain-ai/memory-agent](https://github.com/langchain-ai/memory-agent) | Chat bot with memory graph Store. Deployable on LangGraph Cloud. | 6 |
| **langchain-mcp-adapters** | [github.com/langchain-ai/langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters) | MCP tools compatible with LangChain/LangGraph. Stdio and HTTP transports. | 14 |
| **open_deep_research** | [github.com/langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) | Production-ready deep research implementation. | 8 |
| **local-deep-researcher** | [github.com/langchain-ai/local-deep-researcher](https://github.com/langchain-ai/local-deep-researcher) | Fully local web research and report writing assistant. | 8 |

### Evaluation Tools

| Repository | GitHub URL | Description | Sessions |
|------------|------------|-------------|----------|
| **openevals** | [github.com/langchain-ai/openevals](https://github.com/langchain-ai/openevals) | Prebuilt evaluators: LLM-as-judge, structured output evaluation, multi-turn simulation. | 10 |
| **agentevals** | [github.com/langchain-ai/agentevals](https://github.com/langchain-ai/agentevals) | Evaluators for agent trajectories. Judge tool selection and action sequences. | 10 |
| **langsmith-sdk** | [github.com/langchain-ai/langsmith-sdk](https://github.com/langchain-ai/langsmith-sdk) | Python/JS SDKs for LangSmith. Debug, evaluate, and monitor LLM apps. | 3, 10 |

### Core Libraries

| Repository | GitHub URL | Description | Sessions |
|------------|------------|-------------|----------|
| **langchain** | [github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Main framework for agents and LLM apps. Core abstractions, chains, integrations. | 2, 3, 4, 18 |
| **langchain-community** | [github.com/langchain-ai/langchain-community](https://github.com/langchain-ai/langchain-community) | Community integrations: vector stores, document loaders, retrievers. | 2, 11 |
| **langchainjs** | [github.com/langchain-ai/langchainjs](https://github.com/langchain-ai/langchainjs) | JavaScript/TypeScript version of LangChain. | - |
| **langserve** | [github.com/langchain-ai/langserve](https://github.com/langchain-ai/langserve) | Deploy runnables and chains as REST APIs. | - |

---

## Anthropic & MCP Ecosystem

### Model Context Protocol (MCP)

| Repository | GitHub URL | Description | Sessions |
|------------|------------|-------------|----------|
| **modelcontextprotocol** | [github.com/modelcontextprotocol/modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol) | MCP specification and documentation. 2025-11-25 latest version. | 14, 17 |
| **servers** | [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Reference implementations and community MCP servers. | 14, 17 |
| **python-sdk** | [github.com/modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | Official Python SDK for MCP servers and clients. | 14, 17 |
| **typescript-sdk** | [github.com/modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | Official TypeScript SDK for MCP. | 14, 17 |
| **inspector** | [github.com/modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector) | Visual testing tool for MCP servers. | 17 |
| **go-sdk** | [github.com/modelcontextprotocol/go-sdk](https://github.com/modelcontextprotocol/go-sdk) | Official Go SDK (with Google). | - |

### Anthropic Resources

| Repository | GitHub URL | Description | Sessions |
|------------|------------|-------------|----------|
| **anthropic-cookbook** | [github.com/anthropics/anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook) | Notebooks/recipes for Claude: RAG, tool use, classification, summarization. | 1 |
| **courses** | [github.com/anthropics/courses](https://github.com/anthropics/courses) | Claude SDK and prompt engineering courses. | 1 |
| **claude-code** | [github.com/anthropics/claude-code](https://github.com/anthropics/claude-code) | Agentic coding tool for terminal, git workflows. | - |
| **claude-agent-sdk-python** | [github.com/anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) | Python SDK for Claude Agent with custom tools. | - |
| **skills** | [github.com/anthropics/skills](https://github.com/anthropics/skills) | Public repository for Agent Skills. | - |

---

## OpenAI Ecosystem

| Repository | GitHub URL | Description | Sessions | Status |
|------------|------------|-------------|----------|--------|
| **openai-agents-python** | [github.com/openai/openai-agents-python](https://github.com/openai/openai-agents-python) | **Production Agents SDK** - official multi-agent framework replacing Swarm. | 5 | Active |
| **evals** | [github.com/openai/evals](https://github.com/openai/evals) | LLM evaluation framework with open benchmark registry. | 10 | Active |
| **simple-evals** | [github.com/openai/simple-evals](https://github.com/openai/simple-evals) | Lightweight evaluation scripts. | 10 | Active |
| **openai-cookbook** | [github.com/openai/openai-cookbook](https://github.com/openai/openai-cookbook) | API guides: prompt engineering, embeddings, RAG, agents, function calling. | 1, 2, 9 | Active |
| **swarm** | [github.com/openai/swarm](https://github.com/openai/swarm) | Educational multi-agent concepts (2024). **Superseded by openai-agents-python.** | - | Archived |

---

## Infrastructure

### Vector Databases

| Repository | GitHub URL | Description | Sessions |
|------------|------------|-------------|----------|
| **qdrant** | [github.com/qdrant/qdrant](https://github.com/qdrant/qdrant) | High-performance vector DB in Rust. Payload filtering, sparse vectors, quantization. | 2, 11 |
| **qdrant-client** | [github.com/qdrant/qdrant-client](https://github.com/qdrant/qdrant-client) | Official Python client. Sync/async, local mode, cloud integration. | 2, 11 |
| **chroma** | [github.com/chroma-core/chroma](https://github.com/chroma-core/chroma) | Open-source embedding database. 25k+ stars, Python/JS support. | 2 |

### Graph Databases

| Repository | GitHub URL | Description | Sessions |
|------------|------------|-------------|----------|
| **neo4j-graphrag-python** | [github.com/neo4j/neo4j-graphrag-python](https://github.com/neo4j/neo4j-graphrag-python) | GraphRAG package for Python. Knowledge graph construction. | 6, 11 |
| **neo4j-graphacademy/courses** | [github.com/neo4j-graphacademy/courses](https://github.com/neo4j-graphacademy/courses) | Graph Databases, Importing Data, Gen-AI RAG workshops. | 11 |
| **genai-workshop-graphrag** | [github.com/neo4j-graphacademy/genai-workshop-graphrag](https://github.com/neo4j-graphacademy/genai-workshop-graphrag) | Mastering RAG with Neo4j GraphRAG Package workshop. | 11 |

---

## MLOps & Orchestration

| Repository | GitHub URL | Description | Sessions |
|------------|------------|-------------|----------|
| **wandb** | [github.com/wandb/wandb](https://github.com/wandb/wandb) | AI developer platform. Experiment tracking, model management. | - |
| **prefect** | [github.com/PrefectHQ/prefect](https://github.com/PrefectHQ/prefect) | Workflow orchestration for data pipelines. 21k+ stars. | - |

---

## Hugging Face

| Repository | GitHub URL | Description | Sessions |
|------------|------------|-------------|----------|
| **transformers** | [github.com/huggingface/transformers](https://github.com/huggingface/transformers) | State-of-the-art ML models. 156k+ stars, 1M+ checkpoints. | 2 |
| **datasets** | [github.com/huggingface/datasets](https://github.com/huggingface/datasets) | Largest hub of ready-to-use datasets. 21k+ stars. | 2, 9 |
| **evaluate** | [github.com/huggingface/evaluate](https://github.com/huggingface/evaluate) | ML evaluation library (see lighteval for LLMs). | 10 |
| **lighteval** | [github.com/huggingface/lighteval](https://github.com/huggingface/lighteval) | All-in-one LLM evaluation toolkit. | 10 |

---

## Community & Reference

| Repository | GitHub URL | Description |
|------------|------------|-------------|
| **12-factor-agents** | [github.com/humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents) | Patterns for reliable LLM applications. |
| **awesome-mcp-servers** | [github.com/punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Curated MCP servers list (7260+ servers). |
| **awesome-mcp-clients** | [github.com/punkpeye/awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients) | Curated MCP clients list. |
| **mcp-debugger** | [github.com/debugmcp/mcp-debugger](https://github.com/debugmcp/mcp-debugger) | LLM-driven step-through debugging via DAP. |
| **gdelt-knowledge-base** | [github.com/donbr/gdelt-knowledge-base](https://github.com/donbr/gdelt-knowledge-base) | Multi-strategy retriever comparison project. |
| **lifesciences-research** | [github.com/donbr/lifesciences-research](https://github.com/donbr/lifesciences-research) | Life sciences MCP server ADR example. |

---

## Structured Index (JSON)

```json
{
  "langchain_ecosystem": {
    "tutorials": [
      {"org": "langchain-ai", "repo": "langchain-academy", "sessions": [3, 4, 6]},
      {"org": "langchain-ai", "repo": "agents-from-scratch", "sessions": [6]},
      {"org": "langchain-ai", "repo": "deep-agents-from-scratch", "sessions": [7]},
      {"org": "langchain-ai", "repo": "deep_research_from_scratch", "sessions": [8]},
      {"org": "langchain-ai", "repo": "intro-to-langsmith", "sessions": [10]},
      {"org": "langchain-ai", "repo": "lca-lc-foundations", "sessions": [2, 3]},
      {"org": "langchain-ai", "repo": "langgraph-101", "sessions": [3, 5]},
      {"org": "langchain-ai", "repo": "langsmith-cookbook", "sessions": [10]},
      {"org": "langchain-ai", "repo": "learning-langchain", "sessions": [10]}
    ],
    "libraries": [
      {"org": "langchain-ai", "repo": "langgraph", "sessions": [3, 4, 5, 6, 7]},
      {"org": "langchain-ai", "repo": "langgraph-swarm-py", "sessions": [5]},
      {"org": "langchain-ai", "repo": "memory-agent", "sessions": [6]},
      {"org": "langchain-ai", "repo": "langchain-mcp-adapters", "sessions": [14]},
      {"org": "langchain-ai", "repo": "open_deep_research", "sessions": [8]},
      {"org": "langchain-ai", "repo": "local-deep-researcher", "sessions": [8]}
    ],
    "evaluation": [
      {"org": "langchain-ai", "repo": "openevals", "sessions": [10]},
      {"org": "langchain-ai", "repo": "agentevals", "sessions": [10]},
      {"org": "langchain-ai", "repo": "langsmith-sdk", "sessions": [3, 10]}
    ],
    "core": [
      {"org": "langchain-ai", "repo": "langchain", "sessions": [2, 3, 4, 18]},
      {"org": "langchain-ai", "repo": "langchain-community", "sessions": [2, 11]}
    ]
  },
  "anthropic_ecosystem": {
    "mcp": [
      {"org": "modelcontextprotocol", "repo": "modelcontextprotocol", "sessions": [14, 17]},
      {"org": "modelcontextprotocol", "repo": "servers", "sessions": [14, 17]},
      {"org": "modelcontextprotocol", "repo": "python-sdk", "sessions": [14, 17]},
      {"org": "modelcontextprotocol", "repo": "typescript-sdk", "sessions": [14, 17]},
      {"org": "modelcontextprotocol", "repo": "inspector", "sessions": [17]}
    ],
    "anthropic": [
      {"org": "anthropics", "repo": "anthropic-cookbook", "sessions": [1]},
      {"org": "anthropics", "repo": "courses", "sessions": [1]}
    ]
  },
  "openai_ecosystem": {
    "agents": [
      {"org": "openai", "repo": "openai-agents-python", "sessions": [5], "status": "active"},
      {"org": "openai", "repo": "swarm", "sessions": [], "status": "archived", "note": "Superseded by openai-agents-python"}
    ],
    "evaluation": [
      {"org": "openai", "repo": "evals", "sessions": [10]},
      {"org": "openai", "repo": "simple-evals", "sessions": [10]}
    ],
    "tutorials": [
      {"org": "openai", "repo": "openai-cookbook", "sessions": [1, 2, 9]}
    ]
  },
  "infrastructure": {
    "vector_databases": [
      {"org": "qdrant", "repo": "qdrant", "sessions": [2, 11]},
      {"org": "qdrant", "repo": "qdrant-client", "sessions": [2, 11]},
      {"org": "chroma-core", "repo": "chroma", "sessions": [2]}
    ],
    "graph_databases": [
      {"org": "neo4j", "repo": "neo4j-graphrag-python", "sessions": [6, 11]},
      {"org": "neo4j-graphacademy", "repo": "courses", "sessions": [11]}
    ]
  },
  "huggingface": {
    "models": [
      {"org": "huggingface", "repo": "transformers", "sessions": [2]}
    ],
    "data": [
      {"org": "huggingface", "repo": "datasets", "sessions": [2, 9]}
    ],
    "evaluation": [
      {"org": "huggingface", "repo": "evaluate", "sessions": [10]},
      {"org": "huggingface", "repo": "lighteval", "sessions": [10]}
    ]
  }
}
```

---

## Key Documentation Links

| Resource | URL |
|----------|-----|
| LangChain Docs | [docs.langchain.com](https://docs.langchain.com) |
| LangGraph Docs | [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph) |
| LangSmith Docs | [docs.smith.langchain.com](https://docs.smith.langchain.com) |
| MCP Specification | [modelcontextprotocol.io/specification/2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25) |
| Anthropic Docs | [docs.anthropic.com](https://docs.anthropic.com) |
| OpenAI Docs | [platform.openai.com/docs](https://platform.openai.com/docs) |
| Qdrant Docs | [qdrant.tech/documentation](https://qdrant.tech/documentation) |
| Neo4j GraphRAG | [neo4j.com/docs/neo4j-graphrag-python](https://neo4j.com/docs/neo4j-graphrag-python/current/) |
| RAGAS Docs | [docs.ragas.io](https://docs.ragas.io) |

---

## Notes

### 2026 Industry Context

- **MCP Standard**: Created by Anthropic Nov 2024, donated to Linux Foundation's Agentic AI Foundation Dec 2025. Now an industry standard adopted by OpenAI, Google DeepMind, and major AI toolmakers.
- **OpenAI Agents SDK** (`openai-agents-python`): Production multi-agent framework. Replaces the educational Swarm project from 2024.
- **LangGraph Dominance**: LangGraph has emerged as the leading open-source agent orchestration framework, used by Klarna, Replit, Elastic.
- **Evaluation Maturity**: `openevals` and `agentevals` are the recommended evaluation tools for LangChain ecosystem. Hugging Face recommends `lighteval` over legacy `evaluate`.
- **LangChain 1.0**: Stable release with Runnable abstraction providing consistent interface across all components.

### Repository Status Guide

| Status | Meaning |
|--------|---------|
| **Active** | Actively maintained, production-ready |
| **Archived** | Superseded or no longer maintained |
| **Educational** | Learning resources, not for production |
| **Experimental** | Cutting-edge but may change |

### Deprecated/Superseded Tools (Do Not Use)
- `openai/swarm` → Use `openai/openai-agents-python`
- `huggingface/evaluate` for LLMs → Use `huggingface/lighteval`
- Legacy LangChain patterns → Use LangChain 1.0 Runnable abstraction
