# Automotive ADK Provenance Research: Next Steps

## Session Handoff Document
**Date**: 2026-01-24
**Status**: Initial research complete, architecture analysis pending

---

## Research Completed This Session

### Documents Created

| File | Description |
|------|-------------|
| `RESEARCH_TEAM_DESIGN.md` | Multi-agent research team architecture |
| `PROVENANCE_ANALYSIS.md` | Initial provenance conclusions |
| `GM_OnStar_IVA_Dialogflow_Research.md` | 2022 IVA with Dialogflow architecture |
| `GM_Google_Gemini_Partnership_Research.md` | 2025-2026 Gemini integration timeline |
| `OnStar_API_Research_Summary.md` | API evolution from 2012-2026 |

### Key Findings

1. **GM-Google partnership** started 2019, OnStar IVA launched 2022 with Dialogflow
2. **1M+ inquiries/month** handled by the IVA in U.S. and Canada
3. **Server-side processing** enables backward compatibility to 2015 vehicles
4. **Hybrid edge-cloud** architecture announced for Gemini (2025-2026)
5. **January 2026** - New OnStar API tiers + FTC settlement on data sharing
6. **No public repos** - implementation is entirely proprietary

### Stored in Graphiti

**Group ID**: `automotive-adk-provenance-2026`
- Initial findings episode
- API pattern analysis episode
- Provenance summary episode

---

## Next Research Phase: Architecture Diagrams

### Objective

Create visual architecture comparisons showing the evolution from Dialogflow to Gemini agentic systems, emphasizing that the **conceptual patterns remain stable** while **compute location has shifted**.

### Research Questions

1. What changed in the routing architecture between 2022 and 2026?
2. Where are lightweight models now running (edge vs cloud)?
3. How do the tool-wrapping patterns compare to ADK FunctionTool?
4. What remains constant? (VIN handling, intent routing, human handoff)

### Deliverable 1: Architecture Diagram Comparison

Create side-by-side diagrams:

**Diagram A: 2022 Dialogflow Architecture**
```
Vehicle → OnStar Backend → Google Cloud Dialogflow → Response
                ↓
         Human Advisors (escalation)
```

Components to show:
- TCU (in-vehicle telematic control unit)
- OnStar data centers (Auburn Hills, Plano)
- Dialogflow intent recognition
- Speech-to-Text / Text-to-Speech (WaveNet)
- Human advisor routing for emergencies

**Diagram B: 2026 Gemini Hybrid Architecture**
```
Vehicle (edge models) → Google Cloud Gemini → Response
         ↓                      ↓
   Quick commands        Complex queries
```

Components to show:
- On-device inference (Qualcomm Snapdragon)
- Cloud inference (Vertex AI)
- Hybrid orchestration layer
- Agentic tool calls vs Dialogflow intents

### Deliverable 2: Pattern Mapping Table

| Pattern | Dialogflow 2022 | Gemini ADK 2026 | Notes |
|---------|-----------------|-----------------|-------|
| Intent Classification | Dialogflow CX | Root Coordinator (LlmAgent) | More flexible |
| Tool Calling | Webhooks | FunctionTool | Same concept |
| State Management | Session parameters | User/Session scope | Formalized |
| Human Handoff | Emergency keyword detection | Safety Escalation Agent | Same pattern |
| VIN Context | Session variables | State injection ({vin}) | Same pattern |

### Deliverable 3: "What's Really Changed" Summary

Write a 1-page analysis answering:
- What's genuinely new in the agentic approach?
- What's just rebranding of existing patterns?
- Where does GenAI add real value vs hype?

---

## Research Tasks for Next Session

### Task 1: Source Official Architecture Diagrams

**Objective**: Find any published architecture diagrams from GM, Google, or partners.

**Search targets**:
- Google Cloud automotive solution pages
- GM investor presentations (check for tech slides)
- Qualcomm Snapdragon Digital Chassis documentation
- Volvo EX90 reference architecture (uses same components)

**Expected output**: Links to official diagrams or descriptions detailed enough to reconstruct

### Task 2: Compare Dialogflow CX to ADK Patterns

**Objective**: Map Dialogflow CX concepts to ADK equivalents.

**Research**:
- Dialogflow CX: Flows, Pages, Intents, Entities, Webhooks
- ADK: LlmAgent, SequentialAgent, FunctionTool, AgentTool, State

**Expected output**: Concept mapping table with code examples

### Task 3: Validate API Pattern Claims

**Objective**: Confirm whether the automotive example's API patterns match OnStar APIs.

**Specific checks**:
- Does OnStar have a direct warranty API? (Research says no - portal only)
- Does OnStar have direct appointment booking? (Research says no - dealer contact)
- Are the example APIs idealized or based on actual endpoints?

**Expected output**: API comparison table with citations

### Task 4: Create Mermaid Architecture Diagrams

**Objective**: Produce publishable diagrams for the automotive use case folder.

**Diagrams to create**:
1. 2022 Dialogflow flow (based on researched architecture)
2. 2026 Gemini hybrid flow (based on researched architecture)
3. Side-by-side comparison highlighting changes

**Format**: Mermaid.js syntax for easy rendering

---

## Quality Evaluation

### Research Quality Rubric (100 Points)

Each deliverable should be evaluated against these criteria:

| Category | Points | Criteria |
|----------|--------|----------|
| **Completeness** | 25 | All research questions answered; no gaps |
| **Accuracy** | 25 | Claims verified against sources; version-current |
| **Sources** | 25 | 10+ authoritative citations; links work |
| **Actionability** | 25 | Clear next steps; practical not theoretical |

### Quality Check Process

After each deliverable is produced:

1. **Self-evaluate**: Score against the rubric
2. **Verify sources**: Confirm all links work, versions are current
3. **Cross-reference**: Check claims against official documentation
4. **Report score**: "This deliverable scores X/100 because..."

### Minimum Quality Threshold

- **90-100**: Publish-ready
- **80-89**: Minor improvements needed (list them)
- **70-79**: Significant gaps (specify what's missing)
- **Below 70**: Requires rework

---

## How to Continue This Research

### Option A: Resume with Research Agents

```
Continue the automotive ADK provenance research. The previous session
completed initial research (see NEXT_RESEARCH_PLAN.md).

Focus on Task 1: Source official architecture diagrams.
Search Google Cloud automotive pages and Qualcomm documentation.
```

### Option B: Create Deliverables Directly

```
Create the architecture comparison diagrams for the GM-Google
automotive evolution. Use the research in:
- GM_OnStar_IVA_Dialogflow_Research.md
- GM_Google_Gemini_Partnership_Research.md

Output Mermaid diagrams showing 2022 vs 2026 architecture.
```

### Option C: Deep Dive on Specific Topic

```
Deep dive into [specific topic from research]:
- Dialogflow CX to ADK pattern mapping
- OnStar API validation against example
- Edge vs cloud inference tradeoffs
```

---

## Context for Future Session

### User Background

- Has direct experience with GM API modernization work
- Familiar with Dialogflow and intent-based systems
- Teaching AIE9 bootcamp on agent engineering
- Interested in provenance: where did this example come from?

### Key Insight from Discussion

> "Conceptually not a lot has changed. With lighter weight agents being able
> to be in the car, that provides key value."

The research should validate this hypothesis - that agentic AI in automotive is evolutionary, not revolutionary, building on Dialogflow patterns with improved NLU and edge deployment.

---

## Files to Read First (Next Session)

1. This file: `NEXT_RESEARCH_PLAN.md`
2. `PROVENANCE_ANALYSIS.md` - Main conclusions
3. `GM_OnStar_IVA_Dialogflow_Research.md` - 2022 architecture details
4. `GM_Google_Gemini_Partnership_Research.md` - 2026 evolution
5. `Automotive Agent Design with ADK.md` - Original example being analyzed

---

---

## Starting Prompt for Next Session

Copy and paste this to start the next session:

```
Read and follow the research plan at:
/home/donbr/AIE9/AIE9/google-adk/automotive-use-case/NEXT_RESEARCH_PLAN.md

Before proceeding, confirm:
1. You've read the NEXT_RESEARCH_PLAN.md handoff document
2. You've noted the files to read first (section at bottom of plan)
3. You understand the quality rubric (100-point scoring)
4. You're ready to continue the automotive ADK provenance research

Then ask me:
- Which of the four research tasks should we focus on?
- Should we run tasks in parallel or sequentially?
- What depth level: survey, practical, or deep?
- What output format do you prefer for deliverables?
```

---

*Plan created: 2026-01-24*
*Ready for handoff to next session*
