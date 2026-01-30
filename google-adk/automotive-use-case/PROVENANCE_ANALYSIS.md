# Automotive ADK Example - Provenance Analysis

## Research Date: 2026-01-24

## Executive Summary

This document traces the likely origins of the automotive multi-agent ADK example by analyzing its components, test scenarios, and comparing them to known Google partnerships and industry APIs.

**Primary Hypothesis**: The example represents a reference architecture influenced by Google's partnership with GM (OnStar) and other automotive OEMs, evolved from Dialogflow-era intent classification patterns into modern ADK agentic patterns.

---

## Test Scenarios Identified

The automotive example includes six core test scenarios that map to the agent architecture:

| # | Scenario | User Query Example | Target Agent | Backend |
|---|----------|-------------------|--------------|---------|
| 1 | Tire Pressure | "What is the optimal tire pressure for my car?" | Knowledge Agent | RAG - Owner's Manual |
| 2 | Warranty Check | "Is my transmission still under warranty?" | Service Agent | Warranty API + VIN |
| 3 | Appointment Booking | "I need to get my oil changed" | Service Agent | Scheduling API |
| 4 | Safety Escalation | "I hear a knocking sound when I brake" | Safety Agent | Human Handoff |
| 5 | Maintenance Schedule | "When should I change my transmission fluid?" | Knowledge Agent | RAG - Maintenance Docs |
| 6 | General Technical | "How do I pair my phone with Bluetooth?" | Knowledge Agent | RAG - Owner's Manual |

### Scenario-to-Agent Mapping

```
User Query
    │
    ▼
┌─────────────────┐
│ Root Coordinator │ (Gemini 3 Pro - Intent Classification)
└────────┬────────┘
         │
    ┌────┴────┬─────────────┐
    ▼         ▼             ▼
Technical  Transactional  Safety
   │           │            │
   ▼           ▼            ▼
Knowledge   Service      Human
 Agent       Agent       Handoff
   │           │            │
   ▼           ▼            ▼
  RAG      APIs/DBs       CRM
```

---

## Component Analysis for Provenance

### 1. VIN Lookup Pattern

**In Example**: 17-character VIN validation, VIN passed via session state, used for warranty and vehicle identification.

**Industry Match**:
- OnStar API uses VIN as primary vehicle identifier
- Standard automotive pattern across all OEMs
- VIN validation regex (`^[A-HJ-NPR-Z0-9]{17}$`) is industry standard

**Provenance Signal**: Generic - used by all automotive systems

### 2. Warranty Check API

**In Example**:
```python
def check_warranty_status(vin: str) -> Dict[str, Any]:
    # Returns: vin, warranty_status, coverage_plan, expiration_date
```

**Industry Match**:
- OnStar: Warranty info via My Account portal, not direct API
- GM: Warranty Tracker in account dashboard
- Smartcar: Provides warranty data for some makes

**Provenance Signal**: The example's direct warranty API is *idealized* - real OEM implementations typically require portal access. Suggests this is a reference architecture rather than production integration.

### 3. Service Scheduling API

**In Example**:
```python
def schedule_service_appointment(vin: str, service_type: str, preferred_date: str):
    # Direct booking with confirmation
```

**Industry Match**:
- OnStar: Form submission prompts dealer contact
- GM Support: "Schedule Service" links to dealer
- Most OEMs: Indirect scheduling through dealer network

**Provenance Signal**: Direct booking API is aspirational. Real-world implementations have dealer intermediation. This pattern may come from consulting firm requirements documents.

### 4. RAG Document Sources

**In Example**:
- Owner's Manuals (PDF - multi-column, tables, warning boxes)
- Maintenance Schedules (varied formats)
- Technical specifications
- Web content (HTML)
- Markdown documentation

**Industry Match**:
- GM: Owner's manuals as PDF downloads
- OnStar IVA: Answers from "vehicle data caches"
- Google Automotive AI Agent: "Technical information from the automaker's vehicle data caches"

**Provenance Signal**: Strong match to how OEMs structure documentation. Layout-aware parsing requirement matches complexity of real automotive manuals.

### 5. Safety Escalation Pattern

**In Example**:
- Trigger on subjective symptoms (sounds, smells)
- Log P0_SAFETY ticket
- Human-in-the-loop handoff

**Industry Match**:
- OnStar: Emergency services routing
- GM Dialogflow: Detects emergency phrases, routes to human
- Industry standard: Liability requires human handoff for diagnostics

**Provenance Signal**: This is a liability-driven pattern universal to automotive support. The formalization as an agent pattern is consistent with ADK best practices.

---

## Google Partnership Analysis

### GM-Google Partnership (Strongest Signal)

| Timeline | Development |
|----------|-------------|
| 2022 | OnStar Interactive Virtual Assistant (IVA) launched with Dialogflow |
| 2023 | GM announces ChatGPT integration for owner's manual queries |
| 2023 | GM and Google Cloud expand partnership for conversational generative AI |
| 2025 | GM vehicles get Gemini integration via Android Auto |
| 2026 | OnStar API plans consolidated (January 2026) |

**Key Evidence**:
- OnStar IVA handles 1M+ inquiries/month using Dialogflow
- Dialogflow trained on GM's technical documentation
- Pattern evolution: Dialogflow intent → Vertex AI Agent Builder → ADK agents

### Other OEM Partnerships

| OEM | Partnership Details | Relevance |
|-----|-------------------|-----------|
| **Mercedes-Benz** | First to ship Automotive AI Agent in MBUX (2025 CLA) | Production deployment |
| **Renault** | EV charger data scientist agent demo at Cloud Next 2025 | ADK showcase |
| **Volkswagen** | myVW AI assistant demo at Cloud Next 2025 | Concept alignment |
| **Qualcomm** | Partnership (Sep 2025) for automotive agentic AI | Infrastructure layer |

---

## Technology Evolution Map

```
2016: Dialogflow (intent classification, slot filling)
       │
       ▼
2020: Dialogflow CX (complex flows, state management)
       │
       ▼
2022: Contact Center AI (CCAI) + automotive deployments
       │
       ▼
2023: Vertex AI Agent Builder (LLM + data stores)
       │
       ▼
2025: Agent Development Kit (code-first, multi-agent)
       │
       ▼
2025: Automotive AI Agent (OEM-specific tuning)
```

**Insight**: The automotive example bridges the Dialogflow paradigm (intent classification, deterministic slot filling) with the ADK paradigm (LLM routing, agentic tools). It represents conceptual evolution, not greenfield design.

---

## Provenance Conclusion

### Most Likely Origin

**Google-OEM Collaborative Reference Architecture**

Evidence:
1. Patterns match OnStar IVA capabilities evolved for ADK
2. No matching sample in official ADK-samples repo (suggests internal origin)
3. Level of detail consistent with Google documentation standards
4. Test scenarios match real automotive support workflows
5. Idealized APIs (vs. real OEM constraints) suggest reference architecture

### Contributing Influences

| Source | Contribution | Confidence |
|--------|--------------|------------|
| GM/OnStar partnership | API patterns, VIN handling, warranty flow | High |
| Google ADK team | Architecture patterns, Gemini tiering | High |
| Dialogflow heritage | Intent classification, slot filling | High |
| Consulting firm input | Requirements formalization, idealized APIs | Medium |
| Automotive industry standards | VIN format, safety escalation | High |

### Open Questions

1. Was this created for Google Cloud Next 2025 as a demo?
2. Is there an internal Google "automotive reference implementation"?
3. Did a consulting firm (Accenture, Deloitte, Slalom) formalize OEM requirements?

---

## Next Research Steps

1. [ ] Search Google Cloud Next 2025 session recordings for automotive ADK demos
2. [ ] Check Accenture/Deloitte automotive AI practice publications
3. [ ] Look for GM engineering blog posts about OnStar modernization
4. [ ] Search automotive tech conference proceedings (CES 2025, Auto Shanghai)
5. [ ] Check LinkedIn for Google ADK team posts about automotive

---

## Appendix: RAG Implementation Considerations

The Knowledge Agent's RAG pipeline requires special handling for automotive documentation:

### Document Types

| Type | Format | Challenges | Recommended Loader |
|------|--------|------------|-------------------|
| Owner's Manual | PDF | Multi-column, tables, warning boxes | Vertex AI Layout Parser / Docling |
| Maintenance Schedule | PDF/HTML | Matrix tables (miles × components) | Table-preserving extraction |
| Technical Specs | Markdown | Header hierarchies, nested content | MarkdownHeaderTextSplitter |
| Web Content | HTML | Dynamic content, navigation noise | BeautifulSoup + content extraction |

### Chunking Strategy

1. **PDF Documents**: Chunk by logical block (complete thought), not character count
2. **Tables**: Preserve as structured data, not flattened text
3. **Markdown**: Use header-based splitting with contextual inheritance
4. **Metadata**: Always include parent headers in chunk metadata

### Retrieval Strategies

- **Naive retrieval**: Fast but misses context
- **BM25**: Good for keyword matching (part numbers, codes)
- **Semantic search**: Best for natural language queries
- **Parent-child retrieval**: Good for specification lookups
- **Ensemble**: Combine BM25 + semantic for best coverage

---

## Data Stored in Graphiti

- **Group ID**: `automotive-adk-provenance-2026`
- **Episodes**: Initial findings, API pattern analysis

---

*Generated by Research Team Agent - 2026-01-24*
