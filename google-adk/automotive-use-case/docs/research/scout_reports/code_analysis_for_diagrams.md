# Code Analysis for Diagram Generation

**Source Files Analyzed:**
- `automotive-tools.py` - Tool definitions and mock implementations
- `automotive-agent.py` - Agent hierarchy and routing logic

---

## CONCEPTUAL LAYER (Stable Across Eras)

These high-level interaction patterns exist regardless of implementation technology (2022 Dialogflow or 2026 ADK):

### Core Interaction Patterns

| Pattern | Description | Era-Independent? |
|---------|-------------|------------------|
| User Intent Recognition | User speaks natural language request | Yes |
| Request Classification | System categorizes intent (knowledge, service, safety) | Yes |
| Tool Invocation | System calls backend APIs to fulfill request | Yes |
| Response Synthesis | System generates human-readable response | Yes |
| Safety Escalation | Human specialist notified for critical issues | Yes |

### User Journey Flows

```
Standard Flow:
  User Request → Intent Classification → Specialist Routing → Tool Execution → Response

Safety Flow:
  User Describes Symptom → Safety Detection → Human Escalation → Ticket Created → Acknowledgment
```

### Key Conceptual Entities

1. **User** - Vehicle owner seeking assistance
2. **Vehicle** - Identified by VIN, has warranty status
3. **Appointment** - Service booking with date/type
4. **Technical Manual** - Knowledge base for vehicle specifications
5. **Safety Ticket** - Escalation record for human review

---

## LOGICAL LAYER (API Interfaces)

These tool interfaces represent the contract between the conversational layer and backend systems. They would exist in BOTH Dialogflow webhooks (2022) and ADK FunctionTools (2026).

### Tool Interface Specifications

#### 1. check_warranty_status

```
INPUT:
  - vin: str (17-character Vehicle Identification Number)

OUTPUT:
  - vin: str
  - warranty_status: str ("Active" | "Expired")
  - coverage_plan: str
  - expiration_date: str (YYYY-MM-DD)
  - error?: str (if VIN not found)

PURPOSE: Determine coverage before scheduling paid services
```

#### 2. schedule_service_appointment

```
INPUT:
  - vin: str
  - service_type: str ("Oil Change" | "Diagnostic" | "Tire Rotation" | ...)
  - preferred_date: str (YYYY-MM-DD format)

OUTPUT:
  - booking_id: str (format: BK-{last4vin}-{timestamp})
  - status: str ("Confirmed")
  - service_type: str
  - scheduled_date: str
  - message: str
  - error?: str (if date invalid)

PURPOSE: Create service appointments in dealership system
```

#### 3. search_technical_manual

```
INPUT:
  - query: str (user's technical question)
  - car_model: str (optional, defaults to "Generic Model")

OUTPUT:
  - str (relevant excerpts from manual)

PURPOSE: RAG-style retrieval for how-to questions, warning lights, specifications
```

#### 4. log_safety_escalation

```
INPUT:
  - vin: str
  - risk_assessment: str (brief summary, e.g., "Engine Knock detected")
  - customer_description: str (verbatim user input)

OUTPUT:
  - ticket_id: str (format: SAFE-{4digit})
  - status: str ("ESCALATED_TO_HUMAN")
  - priority: str ("P0_SAFETY")
  - message: str

PURPOSE: Human-in-the-Loop escalation for subjective safety symptoms
```

### Interface Mapping: Dialogflow vs ADK

| Dialogflow (2022) | ADK (2026) | Same Interface? |
|-------------------|------------|-----------------|
| Fulfillment Webhook | FunctionTool | Yes (same I/O) |
| Intent Detection | LlmAgent routing | Same purpose |
| Context Parameters | State injection `{vin}` | Same data flow |
| Fallback Intent | AgentTool description routing | Similar concept |

---

## PHYSICAL LAYER (2026 ADK Implementation Details)

These are specific to the Google ADK (Agent Development Kit) architecture:

### ADK-Specific Components

#### 1. FunctionTool Wrappers

```python
# Tools are wrapped for LLM schema generation
warranty_tool = FunctionTool(check_warranty_status)
scheduling_tool = FunctionTool(schedule_service_appointment)
manual_retrieval_tool = FunctionTool(search_technical_manual)
escalation_tool_function = FunctionTool(log_safety_escalation)
```

**Purpose:** ADK uses these wrappers to:
- Extract function signatures
- Generate JSON schemas for the LLM
- Enable automatic parameter binding

#### 2. LlmAgent Specialists

| Agent | Model | Tools | Purpose |
|-------|-------|-------|---------|
| `knowledge_specialist` | gemini-3-pro | manual_retrieval_tool | Technical Q&A |
| `service_specialist` | gemini-3-flash | warranty_tool, scheduling_tool | Transactions |
| `safety_escalation` | gemini-3-flash | escalation_tool_function | Human handoff |
| `automotive_root` | gemini-3-flash | AgentTools (routing) | Central dispatcher |

#### 3. AgentTool Routing

```python
# Agents are wrapped as tools for the root agent
knowledge_tool = AgentTool(agent=knowledge_agent, description="...")
service_tool = AgentTool(agent=service_agent, description="...")
escalation_tool = AgentTool(agent=human_handoff_agent, description="...")
```

**Routing Logic (from descriptions):**
- Knowledge: "questions about how the car works, technical specs, features"
- Service: "warranty status, booking appointments, service records"
- Escalation: "CRITICAL: knocking, clunking, hissing, burning smell, vibration"

#### 4. State Injection Pattern

```python
# VIN passed through system prompt templates
system_prompt="...The current VIN is: {vin}"

# Initial state set at runtime
initial_state={"vin": "VIN123456789"}
```

**Flow:** Root Agent maintains `{vin}` in session context, passed to specialists via prompt templates.

#### 5. Model Selection Strategy

| Model | Use Case | Rationale |
|-------|----------|-----------|
| `gemini-3-flash` | Root routing, service, escalation | Speed, cost efficiency |
| `gemini-3-pro` | Knowledge synthesis | Complex reasoning, quality |

#### 6. Resilience Configuration

```python
RETRY_POLICY = HttpRetryOptions(
    max_retries=5,
    backoff_factor=2.0,  # Exponential: 2s, 4s, 8s...
    status_codes=[429, 500, 502, 503, 504]
)
```

#### 7. Runtime Infrastructure

```python
server = AdkWebServer(
    agent=root_agent,
    initial_state={"vin": "VIN123456789"}
)
server.start(port=8080)
```

---

## DIAGRAM EXTRACTION SUMMARY

### For Conceptual Diagram (Era-Independent)

```
Entities: User, Vehicle, Appointment, Manual, SafetyTicket
Flows:
  1. User → System → Response (happy path)
  2. User → Safety Detection → Human Escalation (safety path)
```

### For Logical Diagram (Interface-Level)

```
Interfaces:
  - check_warranty_status(vin) → warranty_info
  - schedule_service_appointment(vin, type, date) → booking
  - search_technical_manual(query, model) → excerpts
  - log_safety_escalation(vin, risk, description) → ticket

Routing:
  - Intent → {knowledge | service | safety} specialist
```

### For Physical Diagram (ADK-Specific)

```
Components:
  - FunctionTool wrappers
  - LlmAgent instances (with model selection)
  - AgentTool routing layer
  - AdkWebServer runtime
  - State injection ({vin})
  - HttpRetryOptions resilience
```

---

## KEY INSIGHTS FOR TEACHING

1. **Layered Architecture Stability**: The conceptual and logical layers remain stable across technology generations. A student learning Dialogflow patterns in 2022 would recognize the same patterns in ADK 2026.

2. **Interface Preservation**: The four tool interfaces (warranty, scheduling, manual search, escalation) would have identical signatures whether implemented as Dialogflow webhooks or ADK FunctionTools.

3. **Implementation Flexibility**: Only the physical layer changes - how tools are wrapped, how routing is declared, what models are used. This demonstrates the value of clean interface design.

4. **Safety-First Routing**: Both eras would need explicit safety escalation paths. The ADK makes this declarative through AgentTool descriptions marked "CRITICAL".
