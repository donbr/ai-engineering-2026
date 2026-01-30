# 2026 Gemini Architecture

**Purpose**: Depicts the next-generation GM-Google voice assistant architecture using Gemini LLM (2026 era)
**Complexity**: 12 nodes (high-level), 8 nodes (routing)
**View Type**: Logical Architecture

## Overview

This document contains two complementary diagrams showing the modernized architecture. The 2026 system introduces a hybrid edge-cloud approach with Gemini LLM at its core, enabling natural language understanding, agentic tool orchestration, and persistent state management. On-device inference handles simple commands for reduced latency, while complex queries leverage cloud-based Gemini capabilities.

---

## Diagram 1: High-Level Hybrid Architecture

This diagram shows the complete system architecture with edge processing, cloud services, and the agentic tool system.

```mermaid
flowchart TB
    %% Node definitions
    vehicle(["GM Vehicle MY 2015+"])
    edgeInfer{{"On-Device Inference"}}
    edgeOrch[["Edge Orchestration"]]
    cloudOrch[["Cloud Orchestration"]]
    vertexai["Vertex AI"]
    gemini{{"Gemini LLM"}}
    maps[("Google Maps Platform")]
    stt["Speech-to-Text"]
    tts["Text-to-Speech"]
    tools{{"Agentic Tool System"}}
    state[("State Management")]
    human(["Human Advisors"])

    %% Subgraphs
    subgraph VEHICLE["In-Vehicle - Qualcomm Snapdragon"]
        direction TB
        vehicle
        edgeInfer
    end

    subgraph EDGE["Edge Processing"]
        direction TB
        edgeOrch
    end

    subgraph CLOUD["Google Cloud"]
        direction TB
        cloudOrch
        vertexai
        gemini
        maps
        stt
        tts
        tools
        state
    end

    subgraph ESCALATION["Safety Escalation"]
        direction TB
        human
    end

    %% Connections
    vehicle -->|Quick Commands| edgeInfer
    vehicle -->|Complex Queries| cloudOrch
    edgeInfer -->|Local Process| edgeOrch
    cloudOrch -->|Model Hosting| vertexai
    vertexai -->|Inference| gemini
    gemini -->|Function Calls| tools
    tools -.->|POI Data| maps
    gemini -->|Context Write| state
    state -->|Context Read| gemini
    cloudOrch ==>|Safety Escalation| human

    %% Styling
    classDef google fill:#4285F4,stroke:#1a73e8,color:#fff
    classDef gm fill:#003478,stroke:#002255,color:#fff
    classDef edge fill:#34A853,stroke:#1e8e3e,color:#fff
    classDef escalation fill:#EA4335,stroke:#c5221f,color:#fff
    classDef ai fill:#FBBC04,stroke:#f9ab00,color:#000

    class vertexai,maps,stt,tts,cloudOrch google
    class vehicle gm
    class edgeInfer,edgeOrch edge
    class human escalation
    class gemini,tools,state ai
```

### Legend - High-Level Architecture

| Symbol | Meaning |
|--------|---------|
| Blue nodes | Google Cloud infrastructure services |
| Dark blue nodes | GM vehicle components |
| Green nodes | Edge processing layer |
| Yellow nodes | AI/LLM components |
| Red node | Safety escalation path |
| `-->` | Standard data flow |
| `-.->` | API call flow |
| `==>` | Emergency escalation |

---

## Diagram 2: Request Routing Flow

This diagram shows how requests are intelligently routed between edge and cloud processing based on complexity.

```mermaid
flowchart LR
    %% Node definitions
    user(["User Request"])
    router{"Request Router"}
    edge["Edge Processing"]
    cloud["Cloud Processing"]
    basic["Basic Response"]
    complex["Complex Response"]
    merge{"Response Merge"}
    vehicle(["Vehicle Output"])

    %% Connections
    user --> router
    router -->|Simple| edge
    router -->|Complex| cloud
    edge --> basic
    cloud --> complex
    basic --> merge
    complex --> merge
    merge --> vehicle

    %% Styling
    classDef router fill:#FBBC04,stroke:#f9ab00,color:#000
    classDef edge fill:#34A853,stroke:#1e8e3e,color:#fff
    classDef cloud fill:#4285F4,stroke:#1a73e8,color:#fff
    classDef endpoint fill:#003478,stroke:#002255,color:#fff

    class router,merge router
    class edge,basic edge
    class cloud,complex cloud
    class user,vehicle endpoint
```

### Legend - Request Routing

| Symbol | Meaning |
|--------|---------|
| Yellow diamonds | Decision/routing nodes |
| Green rectangles | Edge processing path |
| Blue rectangles | Cloud processing path |
| Dark blue stadiums | Endpoints (user/vehicle) |

---

## Key Components

| Component | Role | Technology |
|-----------|------|------------|
| **On-Device Inference** | Handles simple commands locally | Qualcomm Snapdragon with Gemini Nano |
| **Edge Orchestration** | Manages local processing decisions | Kubernetes on edge infrastructure |
| **Cloud Orchestration** | Routes complex queries to appropriate services | Google Cloud Run |
| **Vertex AI** | Model hosting and inference | Google Vertex AI Platform |
| **Gemini LLM** | Natural language understanding and generation | Gemini 1.5 Pro/Flash |
| **Agentic Tool System** | Dynamic function calling for external services | Google ADK (Agent Development Kit) |
| **State Management** | Persistent conversation context | Firestore with vector embeddings |
| **Maps Platform** | POI search, routing, real-time traffic | Google Maps Platform APIs |

## Routing Decision Criteria

| Query Type | Route | Example |
|------------|-------|---------|
| Simple commands | Edge | "Turn on headlights" |
| Volume/climate control | Edge | "Set temperature to 72" |
| POI search | Cloud | "Find nearest coffee shop" |
| Multi-turn conversation | Cloud | "What about ones with drive-through?" |
| Emergency | Cloud + Human | "I need help, there's been an accident" |

## Performance Improvements

| Metric | 2022 (Dialogflow) | 2026 (Gemini) | Improvement |
|--------|-------------------|---------------|-------------|
| Simple command latency | 800ms | 150ms | 5.3x faster |
| Complex query latency | 1200ms | 600ms | 2x faster |
| Conversation depth | 3 turns | Unlimited | N/A |
| Offline capability | None | Basic commands | New feature |

## Notes

- Hybrid architecture reduces cloud dependency for common operations
- Gemini's context window enables true multi-turn conversations without losing context
- Agentic tools allow dynamic composition of responses from multiple data sources
- State management enables personalization ("You usually prefer drive-through coffee shops")
- Safety escalation now includes automatic crash detection via vehicle sensors
