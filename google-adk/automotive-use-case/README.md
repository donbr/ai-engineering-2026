# Automotive AI Agent Use Case

Research and implementation of an automotive virtual assistant using Google's Agent Development Kit (ADK), based on the GM OnStar IVA evolution from Dialogflow (2022) to Gemini (2026).

## Quick Navigation

| Section | Description |
|---------|-------------|
| [Core Documents](#core-documents) | Start here - the 5 essential documents |
| [docs/](#documentation-structure) | All documentation |
| [src/](#source-code) | Prototype implementation |

## Core Documents

These 5 documents capture the essential design and approach:

1. **[PROVENANCE_ANALYSIS.md](docs/research/provenance/PROVENANCE_ANALYSIS.md)** - Origin story and evolution analysis
2. **[Automotive Agent Design with ADK.md](src/prototype/Automotive%20Agent%20Design%20with%20ADK.md)** - Technical specification
3. **[ARCHITECTURE_DIAGRAMS.md](docs/design/ARCHITECTURE_DIAGRAMS.md)** - Visual architecture comparison
4. **[DIAGRAM_PLAN_V2.md](docs/design/DIAGRAM_PLAN_V2.md)** - Diagram specifications and blueprints
5. **[Implementation_Report.md](src/prototype/Implementation_Report.md)** - Challenges and lessons learned

## Recommended Reading Order

### For Architects (Understanding the Design)
1. PROVENANCE_ANALYSIS.md (context)
2. Automotive Agent Design with ADK.md (spec)
3. ARCHITECTURE_DIAGRAMS.md (visual)
4. Implementation_Report.md (reality check)

### For Developers (Building It)
1. Automotive Agent Design with ADK.md (spec)
2. automotive-agent.py (code)
3. Implementation_Report.md (gotchas)
4. DIAGRAM_PLAN_V2.md (reference)

### For Research Continuity
1. NEXT_RESEARCH_PLAN.md (where we left off)
2. PROVENANCE_ANALYSIS.md (what we found)
3. Scout reports (methodology)

## Documentation Structure

```
docs/
├── adr/                    # Architecture Decision Records
│   ├── 000-template.md
│   └── 001-dialogflow-to-adk-migration.md
├── design/                 # Design documents and RFCs
│   ├── ARCHITECTURE_DIAGRAMS.md
│   ├── C4_DIAGRAM_PLAN.md
│   ├── DIAGRAM_PLAN_V2.md
│   ├── NEXT_RESEARCH_PLAN.md
│   ├── RESEARCH_TEAM_DESIGN.md
│   └── rfc-template.md
├── diagrams/               # Visual documentation
│   ├── README.md           # Diagram index and rendering guide
│   ├── architecture/       # Static structure diagrams
│   ├── c4/                 # C4 model layered views
│   └── sequences/          # Behavioral flow diagrams
├── research/               # Research findings
│   ├── partnerships/       # GM-Google partnership analysis
│   ├── provenance/         # Origin and evolution tracking
│   └── scout_reports/      # Initial research sweeps
└── validation/             # Quality and validation reports
```

## Source Code

```
src/
└── prototype/
    ├── Automotive Agent Design with ADK.md  # Technical specification
    ├── Implementation_Report.md              # Implementation review
    ├── automotive-agent.py                   # ADK agent implementation
    └── automotive-tools.py                   # Tool definitions
```

## Key Architecture Concepts

### Hub-and-Spoke Pattern
- **Root Coordinator**: Routes requests to specialists
- **Vehicle Control Specialist**: Start/stop, locks, climate
- **Navigation Specialist**: Destinations, routes, POI
- **Information Specialist**: Manuals, warranty, FAQs

### Tiered Model Selection
| Task Type | Model | Rationale |
|-----------|-------|-----------|
| Intent routing | Gemini Flash | Low latency, cost-effective |
| Complex reasoning | Gemini Pro | Higher accuracy for nuanced queries |
| Safety-critical | Edge inference | Guaranteed latency, offline capable |

### Evolution Timeline
- **2022**: Dialogflow CX + Cloud Functions (intent-based)
- **2025-2026**: Gemini + ADK (LLM-native, agentic)

## Quality Standards

All documents are evaluated against a 100-point rubric:

| Category | Points | Focus |
|----------|--------|-------|
| Structure | 25 | All sections present, logical flow |
| Accuracy | 25 | Claims verified, sources cited |
| Completeness | 25 | No gaps, 10+ sources |
| Actionability | 25 | Clear next steps, practical examples |

Minimum passing score: 80 points

## Templates

Use these templates for new documentation:
- [ADR Template](docs/adr/000-template.md) - Architecture decisions
- [RFC Template](docs/design/rfc-template.md) - Design proposals
- [Scout Report Template](docs/research/scout_reports/000-template.md) - Research findings

## Known Gaps

Documented in [NEXT_RESEARCH_PLAN.md](docs/design/NEXT_RESEARCH_PLAN.md):
- [ ] Complete `automotive-tools.py` implementation
- [ ] RAG chunking and retrieval strategy
- [ ] Test suite and evaluation framework
- [ ] Deployment guide
- [ ] Edge inference implementation details
