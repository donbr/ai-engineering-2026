# AI Engineering Bootcamp - Cohort 9 Summaries

Not the official AI Makerspace curriculum, but guided by it.  Created to provide students a roadmap and understanding of the general concepts at the start of the course.

---

## Course Overview

### The Journey

| Phase | Weeks | Sessions | Focus |
|-------|-------|----------|-------|
| **Agentic RAG** | 1-2 | 1-4 | Foundations: LLMs, RAG, Agents, Observability |
| **Complex Agents** | 3-4 | 5-8 | Multi-Agent, Memory, Deep Agents, Research |
| **Evals & Improvement** | 5-6 | 9-11 | Synthetic Data, Evaluation, Advanced Retrieval |
| **Certification** | 6-7 | 12-14 | Industry Use Cases, Full Stack, MCP |
| **Production** | 8-9 | 15-18 | Agent Servers, LLM Servers, Guardrails |
| **Demo Day** | 10 | 19-21 | Semi-Finals, Presentation, Graduation |

---

## Key Technologies

### Primary Stack

| Technology | Role | Sessions |
|------------|------|----------|
| **LangChain** | Agent orchestration | 3-18 |
| **LangGraph** | Stateful agent graphs | 4-8 |
| **LangSmith** | Observability & evals | 3-10 |
| **OpenAI GPT** | Language models | All |
| **Qdrant** | Vector database | 2-4, 11 |
| **FastAPI** | Backend APIs | 1, 13 |
| **MCP** | Tool integration | 14, 17 |

### Learning Progression

```
Session 1-2: Foundations
    │
    ▼
Session 3-4: Agents & RAG
    │
    ▼
Session 5-8: Complex Systems
    │
    ▼
Session 9-11: Evaluation
    │
    ▼
Session 12-18: Production
    │
    ▼
Session 19-21: Demo Day
```

---

## Session Materials

Each session includes **three coordinated learning artifacts**:

### 1. Session Sheet
**Location:** `00_Docs/Session_Sheets/{NN}_{Name}.md`

The conceptual foundation for each session:
- Learning objectives
- Key concepts explained
- Recommended reading
- Assignment details

**Start here** to understand what you'll learn.

### 2. Cheatsheet
**Location:** `{NN}_{Name}/{NN}_{Name}_CHEATSHEET.md`

Your 12-section quick reference guide:
- Quick reference tables
- Setup requirements
- Core concepts with examples
- Code patterns
- Common issues & fixes
- Official documentation links

**Use this** during hands-on work and for review.

### 3. Slides
**Location:** `{NN}_{Name}/{NN}_{Name}_Slides.md`

The presentation specification with:
- 16 slides covering all concepts
- Mermaid diagrams
- Speaker notes
- Visual specifications

**Review this** to see how concepts connect.

---

## Session Status

### Available Sessions (14/21)

| # | Session | Topic | Materials |
|---|---------|-------|-----------|
| 01 | Vibe Check | LLM basics, prompt engineering, evaluation intro | Complete |
| 02 | Dense Vector Retrieval | RAG fundamentals, embeddings, vector databases | Complete |
| 03 | The Agent Loop | Agents, LangChain, tools, middleware | Complete |
| 04 | Agentic RAG | LangGraph, observability, tracing | Complete |
| 05 | Multi-Agent Systems | Agent teams, coordination patterns | Complete |
| 06 | Agent Memory | Short-term and long-term memory | Complete |
| 07 | Deep Agents | Planning, context management, delegation | Complete |
| 08 | Deep Research | Research systems, multi-agent patterns | Complete |
| 09 | Synthetic Data Generation | Test data generation, RAGAS | Complete |
| 10 | Agentic RAG Evaluation | Metrics, LLM-as-judge, improvement | Complete |
| 11 | Advanced Retrievers | BM25, reranking, hybrid search | Complete |
| 14 | MCP Connectors | Model Context Protocol, tool integration | Complete |
| 17 | MCP Servers & A2A | Building MCP servers, agent-to-agent | Complete |
| 18 | Guardrails & Caching | Security, performance optimization | Complete |

### Coming Soon

| # | Session | Phase |
|---|---------|-------|
| 12 | Industry Use Cases | Certification |
| 13 | Full Stack Agent Apps | Certification |
| 15 | Agent Servers | Production |
| 16 | LLM Servers | Production |
| 19-21 | Demo Day | Final |

---

## Repository Structure

```
AIE9/
├── README.md                         # You are here
├── CLAUDE.md                         # Teaching guidelines
├── pyproject.toml                    # Project dependencies (uv)
├── uv.lock                           # Lockfile for reproducibility
├── aim-curriculum-2026-cohort9.md    # Full curriculum details
├── aim-curriculum-2026-code-ref.md   # Repository & code reference
│
├── 00_Docs/
│   └── Session_Sheets/               # Conceptual session guides
│       ├── 01_Vibe_Check.md
│       ├── 02_Dense_Vector_Retrieval.md
│       └── ... (14 sessions)
│
├── 01_Vibe_Check/                    # Session 1 materials
│   ├── 01_Vibe_Check_CHEATSHEET.md
│   └── 01_Vibe_Check_Slides.md
│
├── 02_Dense_Vector_Retrieval/        # Session 2 materials
│   ├── 02_Dense_Vector_Retrieval_CHEATSHEET.md
│   └── 02_Dense_Vector_Retrieval_Slides.md
│
├── ... (session folders 03-18)
│
└── docs/
    └── RESEARCH_TEAM_GUIDE.md        # Content creation guide
```

---

## Environment Variables

Create a `.env` file in your project root:

```bash
# Required
OPENAI_API_KEY=sk-...

# For LangSmith tracing
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=lsv2_...
LANGSMITH_PROJECT=AIE9

# Session-specific (added as needed)
QDRANT_URL=...
QDRANT_API_KEY=...
```

**Important:** Never commit `.env` files. Use `.env.example` with placeholder values.

### Loading Environment Variables

```python
# In your Python scripts
from dotenv import load_dotenv
load_dotenv()  # Loads variables from .env file
```

---

## Why uv?

We use [**uv**](https://docs.astral.sh/uv/) for Python package management throughout this bootcamp. uv is an extremely fast Python package and project manager written in Rust by [Astral](https://astral.sh) (creators of Ruff).

### Key Benefits

| Feature | Benefit |
|---------|---------|
| **10-100x faster** | Installs packages in seconds, not minutes |
| **All-in-one tool** | Replaces pip, pip-tools, pipx, poetry, pyenv, and venv |
| **Reproducible** | Lockfile (`uv.lock`) ensures consistent environments |
| **No Python required** | Can install Python versions automatically |
| **Cross-platform** | Works on macOS, Linux, and Windows |

### Documentation

- [uv Documentation](https://docs.astral.sh/uv/)
- [Getting Started](https://docs.astral.sh/uv/getting-started/first-steps/)
- [GitHub Repository](https://github.com/astral-sh/uv)

---

## Environment Setup with uv

### Installing uv

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative methods:**
```bash
# Using Homebrew (macOS)
brew install uv

# Using pip (if you already have Python)
pip install uv
```

### Adding Dependencies

```bash
# Core dependencies for Sessions 1-4
uv add openai langchain langchain-openai langsmith python-dotenv

# Vector database dependencies (Sessions 2-4, 11)
uv add langchain-qdrant qdrant-client

# Web framework (Sessions 1, 13)
uv add fastapi uvicorn

# Agent orchestration (Sessions 4-8)
uv add langgraph

# Evaluation (Sessions 9-10)
uv add ragas
```

### Running Scripts

```bash
# Run a Python script (uv handles the virtual environment automatically)
uv run python script.py

# Run with specific dependencies for a one-off script
uv run --with httpx python fetch_data.py

# Sync environment and run
uv sync && uv run python main.py
```

### uv Command Reference

| Command | Purpose |
|---------|---------|
| `uv init` | Create a new project with `pyproject.toml` |
| `uv add <package>` | Add a dependency to `pyproject.toml` |
| `uv remove <package>` | Remove a dependency |
| `uv sync` | Install all dependencies from lockfile |
| `uv lock` | Update the lockfile without installing |
| `uv run <command>` | Run a command in the project environment |
| `uv pip install <package>` | pip-compatible install (for quick tests) |
| `uv python install 3.12` | Install a specific Python version |

---

## Getting Help

### Documentation Links

| Resource | URL |
|----------|-----|
| uv Docs | [docs.astral.sh/uv](https://docs.astral.sh/uv/) |
| LangChain Docs | [docs.langchain.com](https://docs.langchain.com) |
| LangGraph Docs | [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph) |
| LangSmith Docs | [docs.smith.langchain.com](https://docs.smith.langchain.com) |
| OpenAI Docs | [platform.openai.com/docs](https://platform.openai.com/docs) |
| MCP Spec | [modelcontextprotocol.io](https://modelcontextprotocol.io) |

### Quick Links

- [Full Curriculum Details](./aim-curriculum-2026-cohort9.md)
- [Code Reference Index](./aim-curriculum-2026-code-ref.md)

---

## Migrating from pip/venv

If you're coming from a traditional pip workflow, here's how uv commands map:

| Traditional | uv Equivalent |
|-------------|---------------|
| `python -m venv venv` | `uv venv` (or automatic with `uv sync`) |
| `source venv/bin/activate` | Not needed! `uv run` handles this |
| `pip install package` | `uv add package` (project) or `uv pip install package` |
| `pip install -r requirements.txt` | `uv pip sync requirements.txt` or `uv add -r requirements.txt` |
| `pip freeze > requirements.txt` | `uv pip compile pyproject.toml -o requirements.txt` |
| `deactivate` | Not needed with `uv run` |

### Key Difference

With uv, you rarely need to "activate" a virtual environment. Instead, use `uv run` to execute commands in the project environment:

```bash
# Old way (pip/venv)
source .venv/bin/activate
python script.py
deactivate

# New way (uv)
uv run python script.py
```

---

## Acknowledgments

Built with support from:
- [AI Makerspace](https://aimakerspace.io) team
- [LangChain](https://langchain.com) ecosystem
- [Astral](https://astral.sh) for uv
- Our amazing cohort of AI Engineers

---

*AI Engineering Bootcamp - Cohort 9*
*January 2026*

**Let's build something amazing together!**
