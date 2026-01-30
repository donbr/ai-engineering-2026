# ADR-001: Migrate from Dialogflow to Google ADK

## Status

Accepted

## Context

The 2022 OnStar IVA implementation used Dialogflow CX for intent-based natural language understanding. With the 2025-2026 GM-Google partnership expansion and the introduction of Google's Agent Development Kit (ADK), a fundamental architectural shift became possible.

Key drivers:
- Dialogflow's intent-matching limitations for complex multi-turn conversations
- Availability of Gemini models with native function calling
- ADK's support for hierarchical multi-agent orchestration
- Need for hybrid edge-cloud processing for latency-sensitive commands

## Decision

Adopt Google ADK as the primary framework for the automotive virtual assistant, replacing Dialogflow CX for new development while maintaining backward compatibility during transition.

Key architectural changes:
1. **Replace intent classification** with LLM-based semantic understanding
2. **Implement Hub-and-Spoke pattern** with Root Coordinator + Specialist agents
3. **Use tiered model selection** (Gemini Flash for routing, Pro for complex reasoning)
4. **Enable hybrid processing** with edge inference for safety-critical commands

## Consequences

### Positive
- More natural, context-aware conversations without rigid intent boundaries
- Flexible tool orchestration through native function calling
- Better handling of ambiguous or multi-intent queries
- Easier addition of new capabilities via tools vs. new intents

### Negative
- Higher compute costs for LLM inference vs. intent classification
- Requires model versioning and prompt engineering expertise
- Less deterministic behavior compared to rule-based intents
- Longer initial response latency for complex queries

### Neutral
- Existing vehicle API integrations remain unchanged
- Backend service contracts preserved (OnStar APIs)
- Training data can be repurposed for evaluation benchmarks

## Alternatives Considered

| Alternative | Pros | Cons | Why Not Chosen |
|-------------|------|------|----------------|
| Upgrade Dialogflow CX | Existing expertise, lower risk | Limited by intent paradigm | Doesn't solve core limitations |
| LangChain/LangGraph | Popular, well-documented | Not Google-native, extra integration | ADK provides tighter Vertex AI integration |
| Custom orchestration | Full control | High development cost | ADK provides production-ready patterns |

## References

- [PROVENANCE_ANALYSIS.md](../research/provenance/PROVENANCE_ANALYSIS.md)
- [GM_Google_Gemini_Partnership_Research.md](../research/partnerships/GM_Google_Gemini_Partnership_Research.md)
- [Google ADK Documentation](https://google.github.io/adk-docs/)
