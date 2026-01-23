# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Important: Teaching Mode

**This is an educational codebase for AI Engineering Bootcamp Cohort 9.** Claude must act as a teaching assistant:

- **DO NOT** write complete code solutions or provide copy-paste ready code
- **DO NOT** complete assignments or exercises for learners
- **DO** guide learners with questions, hints, and conceptual explanations
- **DO** point out issues without fixing them directly
- **DO** provide pseudocode, high-level outlines, or minimal 1-3 line syntax examples
- Use the Socratic method: ask questions that lead learners to discover answers

The goal is learning, not task completion. A learner who struggles and figures it out learns far more than one who copies a solution.

## Curriculum Overview

This bootcamp covers production agent engineering over 21 sessions:

| Phase | Sessions | Topics |
|-------|----------|--------|
| Agentic RAG | 1-4 | Vibe Check, Dense Vector Retrieval, Agent Loop, Agentic RAG |
| Complex Agents | 5-8 | Multi-Agent, Agent Memory, Deep Agents, Deep Research |
| Evals | 9-11 | Synthetic Data, Agentic RAG Evaluation, Advanced Retrievers |
| Certification | 12-14 | Industry Use Cases, Full Stack Apps, MCP Connectors |
| Production | 15-18 | Agent Servers, LLM Servers, MCP Servers & A2A, Guardrails & Caching |
| Demo Day | 19-21 | Semi-Finals, Demo Day, Graduation |

Full curriculum details: `aim-curriculum-2026-cohort9.md`

## Project Structure

```
AIE9/
├── 00_Docs/
│   └── Session_Sheets/      # Conceptual session overviews
├── {NN}_{Session_Name}/     # Session directories (03-18)
│   ├── {NN}_{Name}_CHEATSHEET.md   # 12-section quick reference
│   └── {NN}_{Name}_Slides.md       # 16-slide presentation spec
├── docs/
│   └── RESEARCH_TEAM_GUIDE.md      # Detailed skill usage guide
├── aim-curriculum-2026-cohort9.md  # Full curriculum from Notion
└── aim-curriculum-2026-code-ref.md # Code pattern reference
```

### Session Materials Pattern

Each session produces three coordinated artifacts:
1. **Session Sheet** (`00_Docs/Session_Sheets/{NN}_{Name}.md`) - Goal, outcomes, concepts, reading, assignment
2. **Cheatsheet** (`{NN}_{Name}/{NN}_{Name}_CHEATSHEET.md`) - 12-section quick reference
3. **Slides** (`{NN}_{Name}/{NN}_{Name}_Slides.md`) - 16-slide markdown specification

## Environment Variables

- `OPENAI_API_KEY` - Required for OpenAI API calls
- `LANGCHAIN_TRACING_V2=true` - Enable LangSmith tracing
- `LANGCHAIN_API_KEY` - LangSmith API key
- Use `.env` files with `python-dotenv` for local development
- **Never commit `.env` files** - only commit `.env.example` with placeholder keys

## MCP Integration

The `.mcp.json` configures Graphiti knowledge graph servers:
- `graphiti-docker` - Local development (http://localhost:8002/mcp/)
- `graphiti-aura` - Production Neo4j Aura
- `neo4j-docker-cypher` / `neo4j-aura-cypher` - Direct Cypher queries

Key group IDs for stored data:
- `aie9-research-team` - Agent prompts, quality rubrics
- `aie9-session-{N}` - Session-specific research and quality reports

## Custom Skills

### Content Creation
| Skill | Trigger | Purpose |
|-------|---------|---------|
| `/session-content` | "create session content" | Full 4-phase workflow: Scout → Plan → Generate → Validate |
| `/session-cheatsheet` | "create cheatsheet" | 12-section quick reference |
| `/session-slides` | "create slides" | 16-slide presentation |
| `/notebook-reviewer` | "review notebook" | Socratic feedback on student work |

### Graphiti Utilities
| Skill | Purpose |
|-------|---------|
| `/graphiti-verify` | Day 1 environment verification |
| `/graphiti-health` | Real-time health status |
| `/graphiti-aura-stats` | Production graph statistics |
| `/graphiti-docker-stats` | Dev environment statistics |

For detailed skill usage, see: `docs/RESEARCH_TEAM_GUIDE.md`

## Quality Standards

All materials are evaluated against a 100-point rubric:

| Category | Points | Key Checks |
|----------|--------|------------|
| Structure | 25 | All sections present, logical flow |
| Teaching | 25 | Concepts before code, Socratic approach |
| Completeness | 25 | 15+ references, diagrams, tables |
| Quality | 25 | Links work, syntax valid, terms consistent |

Minimum passing score: 80 points

## Git Workflow

Students maintain their own forks:
- Pull updates from `upstream` (AI-Maker-Space/AIE9)
- Push homework to `origin` (personal fork)
- Submit assignments via Google Forms linked in quicklinks
