# GM-Google Automotive Architecture Diagrams

This directory contains Mermaid diagrams documenting the evolution of GM's OnStar voice assistant architecture from the 2022 Dialogflow-based system to the 2026 Gemini-powered agentic architecture.

## Diagram Index

| File | Purpose | Diagram Type |
|------|---------|--------------|
| [01_architecture_2022_dialogflow.md](01_architecture_2022_dialogflow.md) | 2022 Dialogflow-era architecture | Flowchart (TB) |
| [02_architecture_2026_gemini.md](02_architecture_2026_gemini.md) | 2026 Gemini-era architecture (2 diagrams) | Flowchart (TB, LR) |
| [03_evolution_comparison.md](03_evolution_comparison.md) | Side-by-side comparison with delta analysis | Flowchart (LR) + Tables |
| [04_agentic_tool_flow.md](04_agentic_tool_flow.md) | Detailed tool orchestration sequence | Sequence Diagram |

## Quick Links

### By Era

- **2022 Architecture**: [01_architecture_2022_dialogflow.md](01_architecture_2022_dialogflow.md)
- **2026 Architecture**: [02_architecture_2026_gemini.md](02_architecture_2026_gemini.md)

### By View Type

- **Logical Architecture**: Diagrams 01, 02
- **Comparative Analysis**: Diagram 03
- **Behavioral/Sequence**: Diagram 04

## Color Coding

All diagrams use a consistent color scheme:

| Color | Hex | Meaning |
|-------|-----|---------|
| Google Blue | `#4285F4` | Google Cloud services |
| GM Blue | `#003478` | GM/OnStar components |
| Green | `#34A853` | Edge processing |
| Yellow | `#FBBC04` | AI/LLM components |
| Red | `#EA4335` | Human escalation paths |

## Viewing the Diagrams

### GitHub

GitHub natively renders Mermaid diagrams in markdown files. Simply click on any `.md` file to view the rendered diagrams.

### Local Preview

1. **VS Code**: Install the "Markdown Preview Mermaid Support" extension
2. **Mermaid Live Editor**: Copy diagram code to [mermaid.live](https://mermaid.live)
3. **Command Line**: Use `mmdc` (Mermaid CLI) to export as PNG/SVG

### Export Commands

```bash
# Install Mermaid CLI
npm install -g @mermaid-js/mermaid-cli

# Export specific diagram to PNG
mmdc -i 01_architecture_2022_dialogflow.md -o 01_architecture_2022_dialogflow.png

# Export all diagrams
for f in *.md; do mmdc -i "$f" -o "${f%.md}.png"; done
```

## Diagram Complexity Summary

| Diagram | Nodes | Edges | Status |
|---------|-------|-------|--------|
| 01 (2022 Dialogflow) | 10 | 9 | Within limits |
| 02A (2026 High-Level) | 12 | 10 | Within limits |
| 02B (Request Routing) | 8 | 8 | Within limits |
| 03 (Comparison) | 14 | 13 | Within limits |
| 04 (Sequence) | 6 | 11 | Within limits |

All diagrams are designed to render correctly without hitting Mermaid complexity limits (50 nodes, 100 edges).

## Related Documentation

- [DIAGRAM_PLAN_V2.md](../DIAGRAM_PLAN_V2.md) - Original planning document with specifications
- [GM_GOOGLE_PARTNERSHIP_TIMELINE.md](../GM_GOOGLE_PARTNERSHIP_TIMELINE.md) - Partnership history and context

## Updates

- **2026-01-24**: Initial diagram set created
  - 01: 2022 Dialogflow architecture
  - 02: 2026 Gemini architecture (high-level + routing)
  - 03: Evolution comparison with delta table
  - 04: Agentic tool flow sequence diagram
