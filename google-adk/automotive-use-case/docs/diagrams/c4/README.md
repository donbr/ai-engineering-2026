# C4 Layered Architecture Diagrams: Automotive Virtual Assistant

This directory contains three layered architecture diagrams that illustrate the evolution from 2022 Dialogflow to 2026 Google ADK for an automotive virtual assistant use case.

---

## The Layered Architecture Concept

These diagrams follow a modified C4 approach organized by **stability** rather than zoom level:

```
+-------------------------------------------+
|         CONCEPTUAL LAYER (Gray)           |  <-- 100% stable across eras
|    User journeys, business patterns       |
+-------------------------------------------+
              ↓ defines ↓
+-------------------------------------------+
|          LOGICAL LAYER (Blue)             |  <-- Stable interfaces
|    API contracts, tool signatures         |
+-------------------------------------------+
              ↓ implements ↓
+-------------------------------------------+
|         PHYSICAL LAYER (Orange/Green)     |  <-- Where change happens
|    2022 Dialogflow → 2026 ADK             |
+-------------------------------------------+
```

**Key Insight:** Good architecture separates what changes from what stays stable. These diagrams prove that the ADK didn't reinvent automotive virtual assistants - it improved the physical implementation while preserving the conceptual and logical foundations.

---

## The Three Diagrams

### [01_conceptual_layer.md](./01_conceptual_layer.md)
**Color:** All Gray (`#D3D3D3`)

Shows the **era-independent user journey** that is 100% identical between 2022 and 2026:
- User speaks naturally
- System classifies intent (knowledge, service, safety)
- System invokes tools or escalates to humans
- System responds

**Why it matters:** Proves the user experience is timeless - technology changes, patterns don't.

---

### [02_logical_layer.md](./02_logical_layer.md)
**Color:** All Blue (`#4A90D9`)

Shows the **API contracts** that both implementations must honor:
- `check_warranty_status(vin) -> {status, coverage, expiration}`
- `schedule_service_appointment(vin, type, date) -> {booking_id, confirmation}`
- `search_technical_manual(query, model?) -> excerpts`
- `log_safety_escalation(vin, risk, description) -> {ticket_id, status}`

**Why it matters:** Dialogflow webhooks and ADK FunctionTools share identical signatures - backends don't care which framework calls them.

---

### [03_physical_layer.md](./03_physical_layer.md)
**Colors:** Orange (`#FFA500`) for 2022, Green (`#90EE90`) for 2026

Shows **what actually changed** between implementations:
- Routing: Rule-based → LLM-based
- Tool binding: Webhook configs → Python decorators
- Agent composition: Flat → Hierarchical
- Model selection: Single model → Per-agent selection
- Deployment: Cloud-only → Edge + Cloud

**Why it matters:** This is the ONLY layer with significant differences - and it quantifies the business value of migration.

---

## Color Legend

| Color | Hex Code | Meaning | Layer |
|-------|----------|---------|-------|
| **Gray** | `#D3D3D3` | Stable/Unchanged | Conceptual |
| **Blue** | `#4A90D9` | Stable Interface | Logical |
| **Orange** | `#FFA500` | 2022 (Replaced) | Physical |
| **Green** | `#90EE90` | 2026 (New) | Physical |

---

## Visual Narrative

When viewing these three diagrams in sequence, the reader should conclude:

1. **Conceptual Layer:** "The user experience is exactly the same - speak naturally, get answers, safety goes to humans."

2. **Logical Layer:** "The API contracts are identical - `check_warranty_status()` in 2022 looks just like `check_warranty_status()` in 2026."

3. **Physical Layer:** "Oh, HERE'S what changed - better routing, cleaner tool definitions, multi-model support, edge deployment."

---

## Usage

### For Technical Decision-Makers
Use these diagrams to justify ADK migration by showing that:
- Backend systems require ZERO changes
- User experience requires ZERO changes
- Only the conversational AI layer changes
- New capabilities (edge deployment, model selection) provide concrete business value

### For Developers
Use the Logical Layer diagram as a **migration checklist**:
1. Inventory existing webhook signatures
2. Verify each can be implemented as a FunctionTool
3. Map context parameters to state injection
4. Test that backends respond identically

### For Architects
Use the layered approach to evaluate ANY framework migration:
- Does the new framework support the same Conceptual patterns?
- Can it honor existing Logical contracts?
- What Physical improvements does it offer?

---

## Mermaid Rendering

These diagrams use Mermaid.js syntax. To render them:

1. **GitHub:** Markdown files render automatically
2. **VS Code:** Install "Markdown Preview Mermaid Support" extension
3. **Online:** Paste into [mermaid.live](https://mermaid.live)
4. **Documentation tools:** Most modern doc tools (Docusaurus, MkDocs, etc.) support Mermaid

---

## Related Files

- **Plan document:** [../C4_DIAGRAM_PLAN.md](../C4_DIAGRAM_PLAN.md) - Detailed specifications used to create these diagrams
- **Use case overview:** [../README.md](../README.md) - Full automotive virtual assistant documentation

---

## Quick Reference: What Changed vs What Stayed

| Layer | 2022 vs 2026 | Change Percentage |
|-------|--------------|-------------------|
| Conceptual | Identical | 0% |
| Logical | Identical | 0% |
| Physical | Different | 100% |

**Translation:** 2/3 of the architecture is completely stable. Only 1/3 changed, and that change delivers:
- 10x cost reduction (model selection)
- Sub-100ms latency (edge deployment)
- Faster development (auto-generated schemas)
- Better maintainability (hierarchical agents)
