# GM OnStar Architecture Evolution: Dialogflow to Gemini

This document provides architectural diagrams illustrating the evolution of GM's OnStar conversational AI system from Dialogflow (2022) to Gemini (2026).

---

## Diagram 1: 2022 Dialogflow Architecture

This diagram shows the original OnStar Interactive Virtual Assistant architecture using Google Cloud Dialogflow. All AI processing occurs server-side, enabling backward compatibility with vehicles from 2015 onwards.

```mermaid
flowchart TB
    subgraph Vehicle["GM Vehicle (2015+)"]
        TCU["Telematic Control Unit (TCU)"]
        MIC["Microphone"]
        SPK["Speaker"]
        BTN["OnStar Blue Button"]

        BTN --> TCU
        MIC --> TCU
        TCU --> SPK
    end

    subgraph OnStarBackend["OnStar Backend Infrastructure"]
        DC1["Data Center<br/>(Auburn Hills, MI)"]
        DC2["Data Center<br/>(Plano, TX)"]
        VEHCOM["VehCom System<br/>(Vehicle Communications)"]
        TELEPHONY["Telephony<br/>Integration"]
        ROUTING["Routing Logic"]

        VEHCOM --> DC1
        VEHCOM --> DC2
        DC1 --> ROUTING
        DC2 --> ROUTING
        ROUTING --> TELEPHONY
    end

    subgraph GoogleCloud["Google Cloud Services"]
        STT["Speech-to-Text API"]
        DIALOGFLOW["Dialogflow CX<br/>(NLU Engine)"]
        TTS["Text-to-Speech<br/>(WaveNet)"]
        INTENTS["Intent Recognition"]
        ENTITIES["Entity Extraction"]
        WEBHOOKS["Webhooks<br/>(Backend APIs)"]

        STT --> DIALOGFLOW
        DIALOGFLOW --> INTENTS
        DIALOGFLOW --> ENTITIES
        INTENTS --> WEBHOOKS
        ENTITIES --> WEBHOOKS
        WEBHOOKS --> TTS
    end

    subgraph HumanAdvisors["Human OnStar Advisors"]
        EMERGENCY["Emergency Services<br/>Specialists"]
        SUPPORT["Customer Support<br/>Representatives"]
    end

    TCU -->|"Audio Stream"| VEHCOM
    VEHCOM -->|"Audio"| STT
    TTS -->|"Audio Response"| VEHCOM
    VEHCOM -->|"Response"| TCU

    ROUTING -->|"Emergency Detection<br/>(accident, help, crash)"| TELEPHONY
    TELEPHONY -->|"Route to Human"| EMERGENCY
    TELEPHONY --> SUPPORT

    style Vehicle fill:#e1f5fe,stroke:#01579b
    style OnStarBackend fill:#fff3e0,stroke:#e65100
    style GoogleCloud fill:#e8f5e9,stroke:#2e7d32
    style HumanAdvisors fill:#fce4ec,stroke:#880e4f
```

### Key Architectural Characteristics (2022)

| Aspect | Implementation |
|--------|----------------|
| **Processing Model** | 100% Cloud-based |
| **NLU Engine** | Dialogflow CX with predefined intents |
| **Voice Synthesis** | Google WaveNet for natural voice |
| **Intent Matching** | Keyword and phrase-based classification |
| **Human Escalation** | Emergency keyword detection triggers routing |
| **Vehicle Requirements** | No hardware upgrades needed (MY 2015+) |

---

## Diagram 2: 2026 Gemini Hybrid Architecture

This diagram shows the evolved architecture with Gemini AI, featuring hybrid edge-cloud processing. Simple commands are handled on-device for low latency, while complex queries leverage cloud-based Gemini models.

```mermaid
flowchart TB
    subgraph Vehicle["GM Vehicle with Hybrid Processing"]
        subgraph EdgeCompute["On-Device Processing (Qualcomm Snapdragon)"]
            LOCALAI["Local AI Inference"]
            SAFETY["Safety-Critical<br/>Functions"]
            CACHE["Response Cache"]
        end

        TCU["Telematic Control Unit"]
        MIC["Microphone Array"]
        SPK["Premium Audio System"]
        SENSORS["Vehicle Sensors<br/>(CAN Bus Data)"]

        MIC --> TCU
        SENSORS --> TCU
        TCU --> EdgeCompute
        EdgeCompute --> SPK
    end

    subgraph CloudDecision["Query Complexity<br/>Router"]
        SIMPLE["Simple Commands<br/>(Climate, Locks, Lights)"]
        COMPLEX["Complex Queries<br/>(Multi-turn, Context-aware)"]
    end

    subgraph GoogleCloud["Google Cloud (Vertex AI)"]
        GEMINI["Gemini Models<br/>(LLM Inference)"]
        MAPS["Google Maps Platform<br/>(250M+ POIs)"]
        CONTEXT["Conversation<br/>Memory"]
        MULTIMODAL["Multimodal<br/>Processing"]

        GEMINI --> CONTEXT
        GEMINI --> MULTIMODAL
        MAPS --> GEMINI
    end

    subgraph Capabilities["New Gemini Capabilities"]
        NATURAL["Natural Language<br/>(No rigid syntax)"]
        MEMORY["Multi-turn<br/>Conversation Memory"]
        ACCENT["Improved Accent<br/>Recognition"]
        EXPLAIN["Vehicle Feature<br/>Explanations"]
    end

    subgraph SafetyEscalation["Safety Escalation"]
        ONSTAR["OnStar Emergency<br/>Response Center"]
        FIRSTRESPONDERS["First Responders<br/>(911 Integration)"]
    end

    TCU --> CloudDecision

    CloudDecision -->|"Latency < 100ms"| SIMPLE
    SIMPLE --> LOCALAI
    LOCALAI -->|"Immediate Response"| SPK

    CloudDecision -->|"Context Required"| COMPLEX
    COMPLEX -->|"Cloud Route"| GEMINI
    GEMINI -->|"Rich Response"| TCU

    GEMINI --> Capabilities

    SAFETY -->|"Emergency Detection"| ONSTAR
    ONSTAR --> FIRSTRESPONDERS

    style Vehicle fill:#e3f2fd,stroke:#1565c0
    style EdgeCompute fill:#fff9c4,stroke:#f9a825
    style GoogleCloud fill:#e8f5e9,stroke:#2e7d32
    style Capabilities fill:#f3e5f5,stroke:#7b1fa2
    style SafetyEscalation fill:#ffebee,stroke:#c62828
```

### Hybrid Processing Decision Matrix

| Query Type | Processing Location | Latency Target | Example |
|------------|---------------------|----------------|---------|
| Climate Control | Edge (On-device) | < 100ms | "Set temperature to 72" |
| Door Locks | Edge (On-device) | < 100ms | "Lock all doors" |
| Multi-turn Dialog | Cloud (Gemini) | < 2s | "Find a restaurant... Italian... with outdoor seating" |
| Feature Explanation | Cloud (Gemini) | < 2s | "How does one-pedal driving work?" |
| Navigation | Cloud (Maps + Gemini) | < 3s | "Navigate to the nearest charging station" |
| Emergency | Edge + Cloud | Immediate | "I've been in an accident" |

---

## Diagram 3: Side-by-Side Evolution Comparison

This diagram provides a direct comparison of the architectural components and their evolution from Dialogflow (2022) to Gemini ADK (2026).

```mermaid
flowchart LR
    subgraph Dialogflow2022["2022: Dialogflow CX Architecture"]
        direction TB

        DF_INTENT["Intent Classification<br/>━━━━━━━━━━━━━━━<br/>Dialogflow CX<br/>• Predefined intents<br/>• Keyword matching<br/>• Rigid syntax required"]

        DF_TOOL["Tool Calling<br/>━━━━━━━━━━━━━━━<br/>Webhooks<br/>• HTTP endpoints<br/>• Static integrations<br/>• Manual configuration"]

        DF_PROCESS["Processing Model<br/>━━━━━━━━━━━━━━━<br/>Cloud-Only<br/>• All processing remote<br/>• Network dependent<br/>• Higher latency"]

        DF_HANDOFF["Human Handoff<br/>━━━━━━━━━━━━━━━<br/>Emergency Keywords<br/>• 'accident', 'help', 'crash'<br/>• Binary escalation<br/>• No context transfer"]

        DF_INTENT --> DF_TOOL
        DF_TOOL --> DF_PROCESS
        DF_PROCESS --> DF_HANDOFF
    end

    subgraph Evolution["Evolution"]
        direction TB
        E1["Intent Classification<br/>────────────────>"]
        E2["Tool Calling<br/>────────────────>"]
        E3["Processing<br/>────────────────>"]
        E4["Human Handoff<br/>────────────────>"]
    end

    subgraph Gemini2026["2026: Gemini ADK Architecture"]
        direction TB

        GEM_INTENT["Intent Classification<br/>━━━━━━━━━━━━━━━<br/>LlmAgent (Root Coordinator)<br/>• Natural language understanding<br/>• Context-aware routing<br/>• Flexible interpretation"]

        GEM_TOOL["Tool Calling<br/>━━━━━━━━━━━━━━━<br/>FunctionTool<br/>• Type-safe functions<br/>• Dynamic tool selection<br/>• Agent orchestration"]

        GEM_PROCESS["Processing Model<br/>━━━━━━━━━━━━━━━<br/>Hybrid Edge-Cloud<br/>• On-device for simple tasks<br/>• Cloud for complex queries<br/>• Adaptive routing"]

        GEM_HANDOFF["Human Handoff<br/>━━━━━━━━━━━━━━━<br/>Safety Escalation Agent<br/>• Semantic understanding<br/>• Context preservation<br/>• Intelligent handoff"]

        GEM_INTENT --> GEM_TOOL
        GEM_TOOL --> GEM_PROCESS
        GEM_PROCESS --> GEM_HANDOFF
    end

    DF_INTENT ~~~ E1
    DF_TOOL ~~~ E2
    DF_PROCESS ~~~ E3
    DF_HANDOFF ~~~ E4

    E1 ~~~ GEM_INTENT
    E2 ~~~ GEM_TOOL
    E3 ~~~ GEM_PROCESS
    E4 ~~~ GEM_HANDOFF

    style Dialogflow2022 fill:#fff3e0,stroke:#e65100
    style Evolution fill:#e0e0e0,stroke:#616161
    style Gemini2026 fill:#e8f5e9,stroke:#2e7d32
```

### Detailed Component Comparison

| Component | Dialogflow CX (2022) | Gemini ADK (2026) | Key Improvement |
|-----------|---------------------|-------------------|-----------------|
| **Intent Classification** | Dialogflow CX | LlmAgent (Root Coordinator) | No rigid syntax; natural conversation |
| **NLU Model** | Intent-based matching | Gemini LLM | Contextual understanding, multi-turn memory |
| **Tool Calling** | Webhooks (HTTP) | FunctionTool | Type-safe, agent-orchestrated |
| **Processing Location** | Cloud-only | Hybrid edge-cloud | Reduced latency, offline capability |
| **Human Handoff** | Emergency keyword detection | Safety Escalation Agent | Semantic understanding with context |
| **Accent Handling** | Limited | Advanced | Improved recognition across dialects |
| **Conversation Memory** | Session-based | Persistent context | Cross-session continuity |
| **Vehicle Data Access** | Limited | Full CAN bus integration | Rich vehicle state awareness |

### ADK Pattern Mapping

```mermaid
flowchart TB
    subgraph ADKMapping["Google ADK Pattern Mapping"]
        direction LR

        subgraph Agents["Agent Types"]
            ROOT["LlmAgent<br/>(Root Coordinator)"]
            NAV["Navigation Agent"]
            VEHICLE["Vehicle Control Agent"]
            SAFETY["Safety Escalation Agent"]
            INFO["Information Agent"]
        end

        subgraph Tools["FunctionTools"]
            CLIMATE["set_climate()"]
            LOCKS["control_locks()"]
            ROUTE["calculate_route()"]
            POI["find_poi()"]
            ESCALATE["escalate_to_human()"]
        end

        subgraph Callbacks["Callbacks & Hooks"]
            BEFORE["before_agent_callback<br/>(Safety check)"]
            AFTER["after_agent_callback<br/>(Logging)"]
        end

        ROOT --> NAV
        ROOT --> VEHICLE
        ROOT --> SAFETY
        ROOT --> INFO

        NAV --> ROUTE
        NAV --> POI
        VEHICLE --> CLIMATE
        VEHICLE --> LOCKS
        SAFETY --> ESCALATE

        BEFORE --> ROOT
        ROOT --> AFTER
    end

    style Agents fill:#e3f2fd,stroke:#1565c0
    style Tools fill:#fff9c4,stroke:#f9a825
    style Callbacks fill:#f3e5f5,stroke:#7b1fa2
```

---

## Summary

The evolution from Dialogflow to Gemini represents a fundamental shift in automotive conversational AI:

1. **From Intent-Based to LLM-Based**: Moving from rigid keyword matching to flexible natural language understanding
2. **From Cloud-Only to Hybrid**: Distributing processing between edge and cloud for optimal latency and capability
3. **From Webhooks to Agents**: Transitioning from static HTTP integrations to dynamic, orchestrated agent systems
4. **From Binary Escalation to Intelligent Handoff**: Enabling context-preserving transfers to human specialists

This architectural evolution enables GM to deliver a more natural, responsive, and capable in-vehicle assistant while maintaining backward compatibility with vehicles dating back to model year 2015.

---

*Diagrams created: January 2026*
*Based on research from GM and Google Cloud partnership announcements*
