# AIE9 Research & Documentation Team: Usage Guide

## Overview

This guide explains how to use the AIE9 research team infrastructure to improve learning materials.

---

## Quick Start

### 1. Full Session Content (Recommended)
```
/session-content
```
Then describe the session: "Create content for Session 4 on Multi-Agent Systems"

This orchestrates the complete 4-phase workflow: Scout → Plan → Generate → Validate

### 2. Create a New Cheatsheet (Standalone)
```
/session-cheatsheet
```
Then describe the session: "Create cheatsheet for Session 4 on Multi-Agent Systems"

### 3. Create Session Slides (Standalone)
```
/session-slides
```
Then describe the session: "Create slides for Session 4 on Multi-Agent Systems"

### 4. Review Student Work
```
/notebook-reviewer
```
Then provide the notebook path to review.

### 5. Run Quality Evaluation
Ask Claude to evaluate materials using the research team agents stored in graphiti.

---

## Available Skills

### Session Content Orchestrator (`/session-content`)

**Triggers:**
- "create session content"
- "develop session materials"
- "full session workflow"

**What it does:**
- **Phase 1 (Scout)**: Runs Gap-Hunter, Benchmarker, Doc-Scout agents in parallel
- **Phase 2 (Plan)**: Creates content plan with 8-10 concepts, diagrams, quotes
- **Phase 3 (Generate)**: Creates Session Sheet → Cheatsheet → Slides sequentially
- **Phase 4 (Validate)**: Runs 100-point quality evaluation on all artifacts

**Outputs:**
- `/00_Docs/Session_Sheets/{NN}_{Name}.md` (Session Sheet)
- `/{NN}_{Name}/{NN}_{Name}_CHEATSHEET.md` (Cheatsheet)
- `/{NN}_{Name}/{NN}_{Name}_Slides.md` (Slides)
- Research artifact in graphiti (`aie9-session-{N}`)
- Content plan in graphiti (`aie9-session-{N}`)
- Quality report in graphiti (`aie9-session-{N}`)

**Key Benefits:**
- Research-first ensures current documentation
- All artifacts share identical concepts, quotes, and diagrams
- Quality gates ensure minimum 80-point score before completion

### Session Cheatsheet (`/session-cheatsheet`)

**Triggers:**
- "create cheatsheet"
- "update session materials"
- "generate quick reference"
- "AIE9 cheatsheet"

**What it does:**
- Creates 12-section standardized cheatsheets
- Uses MCP tools to research current documentation
- Follows teaching philosophy (concepts before code)
- Outputs: `{NN}_{Session_Name}_CHEATSHEET.md`

**MCP Tool Workflow:**
1. `platform-docs` → Broad discovery search
2. `Context7` → Version-accurate verification
3. `docs-langchain` → LangChain specifics
4. `WebFetch` → Verify links work

### Session Slides (`/session-slides`)

**Triggers:**
- "create slides"
- "generate presentation"
- "session slides"

**What it does:**
- Creates 16-slide standardized presentations
- Generates Mermaid diagrams for each concept
- Three sections per slide: Content, Visual, Speaker Notes
- Follows design system (colors, fonts, node styles)
- Outputs: `{NN}_{Session_Name}_Slides.md`

**MCP Tool Workflow:**
1. `platform-docs` → Broad discovery search
2. `Context7` → Version-accurate verification
3. `docs-langchain` → LangChain specifics
4. `WebFetch` → Verify reference URLs

**Optional Export:**
- Use `document-skills:pptx` to convert markdown to .pptx

### Notebook Reviewer (`/notebook-reviewer`)

**Triggers:**
- "review notebook"
- "check submission"
- "grade notebook"

**What it does:**
- Checks structural completeness
- Provides Socratic feedback (no solutions)
- Session-specific validation
- Outputs encouragement-focused review

---

## Research Team Agents

Stored in graphiti `group_id: aie9-research-team`

### Retrieving Agent Prompts

```
Search graphiti for research team agents:
- search_memory_facts(query="research team agent", group_ids=["aie9-research-team"])
- search_nodes(query="Evaluator", group_ids=["aie9-research-team"])
```

### Agent Roster

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| **Feedback-Analyst** | Student confusion patterns | After collecting student feedback |
| **Benchmarker** | Industry standards comparison | Before major curriculum updates |
| **Gap-Hunter** | Missing/stale content | Regular content audits |
| **Evaluator** | Quality scoring (100-pt rubric) | After creating/updating materials |

---

## Common Workflows

### Workflow 0: Full Session Content Pipeline (Recommended)

```
/session-content
"Create content for Session N on [Topic]"

PHASE 1: SCOUT & DISCOVER (Parallel Agents)
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│   Gap-Hunter    │  │   Benchmarker   │  │   Doc-Scout     │
│   (stale/gaps)  │  │ (industry std)  │  │ (current docs)  │
└────────┬────────┘  └────────┬────────┘  └────────┬────────┘
         │                    │                    │
         └────────────────────┼────────────────────┘
                              ▼
                   [Research Artifact → graphiti]

PHASE 2: PLAN & REFINE
- Extract 8-10 core concepts
- Create concept dependency graph
- Design Mermaid diagrams
- Collect industry quotes
- Map to artifact sections
                              ▼
                   [Content Plan → graphiti]

PHASE 3: GENERATE ARTIFACTS (Sequential)
Session Sheet → Cheatsheet → Slides
(Each uses shared concepts/quotes/diagrams)
                              ▼
                   [3 coordinated artifacts]

PHASE 4: VALIDATE
- 100-point rubric per artifact
- Consistency check across artifacts
- Teaching philosophy compliance
- Fix any issues < 80 points
                              ▼
                   [Quality Report → graphiti]

Output: 3 coordinated artifacts with quality scores ≥ 80
```

### Workflow 1: Create New Cheatsheet (Standalone)

```
1. /session-cheatsheet
   "Create cheatsheet for Session N on [Topic]"

2. Claude researches using MCP tools:
   - platform-docs for discovery
   - Context7 for version accuracy
   - docs-langchain for specifics

3. Output: {NN}_{Session_Name}_CHEATSHEET.md

4. Run Evaluator agent for quality score
```

### Workflow 1b: Create Session Slides

```
1. /session-slides
   "Create slides for Session N on [Topic]"

2. Claude researches using MCP tools:
   - platform-docs for discovery
   - Context7 for version accuracy
   - docs-langchain for specifics

3. Output: {NN}_{Session_Name}_Slides.md

4. Optional: /pptx to export to PowerPoint

5. Run Evaluator agent for quality score
```

### Workflow 2: Audit Existing Materials

```
1. Ask: "Run Gap-Hunter on Session 3 materials"

2. Agent cross-references:
   - Current docs vs official documentation
   - Terminology consistency
   - Deprecated APIs

3. Output: Prioritized list of updates needed
```

### Workflow 3: Full Quality Improvement Cycle

```
Phase 1: Analysis (parallel)
├── Feedback-Analyst → confusion patterns
└── Gap-Hunter → content gaps

Phase 2: Benchmarking
└── Benchmarker → industry alignment

Phase 3: Synthesis
└── Generate improvement recommendations

Phase 4: Evaluation
└── Evaluator → 100-point quality score
```

### Workflow 4: Review Student Submission

```
1. /notebook-reviewer

2. Provide notebook path

3. Output:
   - Completion status table
   - What's working well
   - Areas for improvement (Socratic questions)
   - Suggested resources
```

---

## Quality Rubric (100 Points)

| Category | Points | Key Checks |
|----------|--------|------------|
| **Structure** | 25 | Quick ref table, setup, concepts, patterns, issues |
| **Teaching** | 25 | Concepts before code, minimal examples, Socratic |
| **Completeness** | 25 | All topics, 15+ references, diagrams, tables |
| **Quality** | 25 | Links work, syntax valid, terms consistent |

### Score Interpretation
- **90-100**: Ready for student use
- **80-89**: Minor improvements needed
- **70-79**: Several areas need attention
- **60-69**: Significant gaps present
- **Below 60**: Major revision required

---

## MCP Tool Reference

### Documentation Research
| Tool | Purpose | Example |
|------|---------|---------|
| `platform-docs` | Broad search | `search_docs(query="agents", source="LangChain")` |
| `Context7` | Version-accurate | `query-docs(libraryId="/langchain/docs", query="tools")` |
| `docs-langchain` | LangChain specific | `SearchDocsByLangChain(query="middleware")` |

### Memory Storage
| Tool | Purpose |
|------|---------|
| `graphiti-docker` | Local dev knowledge graph |
| `graphiti-aura` | Production knowledge graph |

### Key Group IDs
- `aie9-research-team` - Agent prompts, rubric, orchestrator
- `aie9-session-{N}` - Session-specific data

---

## Example Commands

### Create Cheatsheet
```
Create a cheatsheet for Session 5 covering LangGraph workflows
```

### Run Specific Agent
```
Using the Gap-Hunter agent from graphiti, scan the Session 2
materials for deprecated APIs and terminology inconsistencies
```

### Quality Evaluation
```
Evaluate the Session 3 cheatsheet against the 100-point rubric.
Score each category and provide specific recommendations.
```

### Review Notebook
```
Review the student notebook at 02_Dense_Vector_Retrieval/homework.ipynb
using Socratic feedback
```

### Search Agent Prompts
```
Search graphiti for the Evaluator agent prompt template
```

---

## Teaching Philosophy Reminders

**DO:**
- Lead with concepts, then code
- Keep code to 1-3 lines (max 15)
- Ask Socratic questions
- Point out issues without fixing
- Link to official documentation

**DON'T:**
- Provide copy-paste solutions
- Write complete code for exercises
- Skip conceptual explanations
- Exceed code length limits

---

## File Locations

| Resource | Path |
|----------|------|
| **Session Content Orchestrator** | `~/.claude/skills/session-content/SKILL.md` |
| Research Artifact Schema | `~/.claude/skills/session-content/references/research-artifact-schema.json` |
| Content Plan Schema | `~/.claude/skills/session-content/references/content-plan-schema.json` |
| Quality Report Schema | `~/.claude/skills/session-content/references/quality-report-schema.json` |
| Session Cheatsheet Skill | `~/.claude/skills/session-cheatsheet/SKILL.md` |
| Cheatsheet Template | `~/.claude/skills/session-cheatsheet/references/cheatsheet-template.md` |
| Session Slides Skill | `~/.claude/skills/session-slides/SKILL.md` |
| Slides Template | `~/.claude/skills/session-slides/references/slide-template.md` |
| Notebook Reviewer Skill | `~/.claude/skills/notebook-reviewer/SKILL.md` |
| Project Instructions | `/home/donbr/AIE9/AIE9/CLAUDE.md` |
| Reference Cheatsheet | `/home/donbr/AIE9/AIE9/03_The_Agent_Loop/03_The_Agent_Loop_CHEATSHEET.md` |
| Reference Slides | `/home/donbr/AIE9/AIE9/03_The_Agent_Loop/03_The_Agent_Loop_Slides.md` |

---

## Verification

To verify the system is working:

1. **Skills loaded**: Check `/session-content`, `/session-cheatsheet`, `/session-slides`, and `/notebook-reviewer` appear in available skills
2. **Graphiti connected**: Run `get_status()` on graphiti-docker
3. **Agents retrievable**: Search for "Evaluator" in `aie9-research-team` group
4. **Templates exist**: Read the cheatsheet-template.md and slide-template.md files
5. **Schemas valid**: Read the JSON schema files in `~/.claude/skills/session-content/references/`

---

*Last updated: January 2026*
