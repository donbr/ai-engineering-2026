# Complexity Analysis Scout Report

**Analyst**: Complexity Scout
**Date**: 2026-01-24
**Research Scope**: GM-Google automotive architecture evolution (2022-2026)

---

## 2022 COMPONENTS (Dialogflow Era)

### Entities (10 total)
1. **GM Vehicle** (MY 2015+)
2. **TCU** (Telematic Control Unit)
3. **OnStar Blue Button**
4. **OnStar Backend** (Auburn Hills, MI / Plano, TX data centers)
5. **Google Cloud Dialogflow CX**
6. **Speech-to-Text Service**
7. **Text-to-Speech (WaveNet)**
8. **Intent Recognition Engine**
9. **Webhook Handler** (external API calls)
10. **Human OnStar Advisors**

### Relationships (8 total)
1. Vehicle --> TCU (voice capture)
2. TCU --> OnStar Backend (audio stream)
3. OnStar Backend --> Speech-to-Text (conversion)
4. Speech-to-Text --> Dialogflow CX (intent matching)
5. Dialogflow CX --> Webhook (external queries)
6. Dialogflow CX --> Text-to-Speech (response)
7. Text-to-Speech --> Vehicle (audio playback)
8. Dialogflow CX --> Human Advisors (emergency escalation)

---

## 2026 COMPONENTS (Gemini Era)

### Entities (12 total)
1. **GM Vehicle** (MY 2015+)
2. **On-Device Inference** (Qualcomm Snapdragon)
3. **Edge Orchestration Layer**
4. **Cloud Orchestration Layer**
5. **Google Cloud Vertex AI**
6. **Gemini LLM**
7. **Google Maps Platform**
8. **Speech-to-Text Service**
9. **Text-to-Speech Service**
10. **Agentic Tool System** (FunctionTool equivalents)
11. **State Management** (user/session scope)
12. **Human OnStar Advisors**

### Relationships (10 total)
1. Vehicle --> Edge Inference (quick commands)
2. Vehicle --> Cloud (complex queries)
3. Edge Inference --> Edge Orchestration (local processing)
4. Cloud --> Vertex AI (model hosting)
5. Vertex AI --> Gemini (inference)
6. Gemini --> Tool System (function calls)
7. Tool System --> Google Maps (POI data)
8. Gemini --> State Management (context retention)
9. State Management --> Gemini (multi-turn memory)
10. Cloud --> Human Advisors (safety escalation)

---

## DELTA ANALYSIS

### What Changed
| Aspect | 2022 | 2026 | Impact |
|--------|------|------|--------|
| **Processing Location** | Cloud-only | Hybrid edge-cloud | Lower latency for basic commands |
| **Language Understanding** | Intent-based | LLM-based | Flexible natural language |
| **Context Handling** | Session parameters | Multi-turn memory | Richer conversations |
| **Tool Invocation** | Webhooks | Agentic tools | More dynamic orchestration |
| **Entity Count** | 10 | 12 | +20% complexity |
| **Relationship Count** | 8 | 10 | +25% complexity |

### What Stayed the Same
1. **Vehicle connectivity**: TCU/OnStar as entry point
2. **Human handoff**: Emergency escalation pattern preserved
3. **Server-side AI**: Complex processing remains cloud-based
4. **Backward compatibility**: MY 2015+ vehicles still supported
5. **Speech pipeline**: STT/TTS bookends the flow

---

## RECOMMENDED STRUCTURE

### Diagram Count: 3 diagrams in 2 files

**File 1: `architecture_2022_dialogflow.md`**
- Single flowchart diagram
- 10 entities, 8 relationships
- Estimated complexity: Simple (single linear flow with one branch)

**File 2: `architecture_2026_gemini.md`**
- Two diagrams:
  1. **High-level hybrid view**: Edge vs cloud routing (swimlane)
  2. **Detailed agentic flow**: Tool orchestration pattern
- 12 entities, 10 relationships
- Estimated complexity: Medium (parallel paths, state loops)

### Rationale
- 2022 architecture is straightforward enough for a single diagram
- 2026 architecture requires splitting into layers to avoid overwhelming complexity
- Separate files enable standalone viewing and side-by-side comparison

### Alternative: Single Comparison File
If side-by-side comparison is preferred, create one file with:
- Diagram 1: 2022 Dialogflow flow (left)
- Diagram 2: 2026 Gemini flow (right)
- Table: Delta summary between diagrams

---

*Report complete. Ready for diagram generation phase.*
