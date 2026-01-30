# **Automotive Agent Implementation Report**

**To:** System Architect

**From:** Senior ADK Software Engineer

**Date:** January 24, 2026

**Subject:** Implementation Review for Hub-and-Spoke Automotive Support System

## **1\. Executive Summary**

This document details the implementation of the Multi-Agent System (MAS) for the Automotive Support platform. The system has been architected using the **Google Agent Development Kit (ADK) 1.18.0+** standard, employing a "Hub-and-Spoke" routing topology.

The implementation prioritizes safety (Human-in-the-Loop escalation) and latency (tiered model selection), while ensuring robustness through standard ADK resilience patterns.

## **2\. Architectural Implementation**

We successfully implemented the **Hub-and-Spoke** pattern defined in the design deck.

* **The Hub (Root Agent)**: A high-velocity router that holds the session state (VIN) and dispatches user intent.  
* **The Spokes (Specialist Agents)**:  
  1. **Knowledge Specialist**: Deep reasoning agent for technical Q\&A.  
  2. **Service Specialist**: Transactional agent for deterministic API operations.  
  3. **Safety Specialist**: A rigid protocol agent for handling subjective/dangerous user reports.

### **Data Flow & Context Strategy**

We utilized the ADK's LlmAgent capability to pass prompt context dynamically. The Vehicle Identification Number (VIN) is injected into the system instructions of the downstream agents via {vin} placeholders. This ensures that a user does not need to repeat their VIN when switched from the Router to a Specialist.

## **3\. Key Design Decisions**

### **3.1 Tiered Model Selection**

We deliberately split the model architecture to optimize for cost and latency without sacrificing reasoning quality:

* **Root & Service Agents (gemini-3-flash)**: These agents perform classification and simple slot-filling (API parameters). Flash provides the sub-second latency required for the initial "triage" hop.  
* **Knowledge Agent (gemini-3-pro)**: This agent performs RAG synthesis (reading technical manuals and summarizing). We selected "Pro" here because technical accuracy and complex context window utilization are higher priorities than raw speed.

### **3.2 Subjective Safety Analysis (Hard-Coded Heuristics)**

Instead of relying solely on the LLM's general reasoning for safety, we implemented **Prompt Engineering Guardrails** in the Root Agent.

* **Trigger**: Keywords like "knocking", "clunking", "hissing", or "smell".  
* **Action**: These are explicitly defined in the escalation\_tool description to force a route to the Safety Agent.  
* **Rationale**: Subjective audio/sensory analysis is high-risk. We treat these as P0 safety events that bypass standard diagnostic flows.

### **3.3 Resilience Pattern**

We applied google.genai.types.HttpRetryOptions to all model clients. This provides exponential backoff (2s, 4s, 8s) for 429 (Too Many Requests) and 5xx errors, ensuring the agent system creates a stable "dial tone" even during minor API disruptions.

## **4\. Challenges & Mitigations**

During the implementation phase, two critical interaction gaps were identified in the initial spec and resolved:

### **Challenge A: The "Silent Specialist"**

**Issue**: The *Knowledge Specialist* was designed to answer technical questions but lacked an actual interface to retrieve information. It risked hallucinating vehicle specs.

**Resolution**: We implemented the manual\_retrieval\_tool (simulating a Vector Search/RAG lookup). The agent's instructions were updated to *mandate* the use of this tool before generating an answer.

### **Challenge B: The "Dead-End" Escalation**

**Issue**: The *Safety Escalation* agent successfully intercepted dangerous queries but had no mechanism to act on them. It would simply apologize to the user without notifying the business.

**Resolution**: We added a transactional tool, log\_safety\_escalation. This completes the architectural loop by allowing the agent to formally log a "P0\_SAFETY" ticket in the backend, ensuring the Human-in-the-Loop (HITL) protocol is actually triggered.

## **5\. Next Steps**

1. **Unit Testing**: Verify the search\_technical\_manual tool returns consistent results across different car models.  
2. **Integration Testing**: Deploy using adk deploy and test the VIN context persistence when switching from the Root agent to the Service agent.  
3. **RAG Integration**: Replace the mock manual\_retrieval\_tool with a live connector to Vertex AI Search.