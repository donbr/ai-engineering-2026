# **Architecting the Cognitive Vehicle: A Comprehensive Specification for Agentic Automotive Support Systems**

## **1\. Executive Summary and Strategic Architecture**

The automotive industry has transitioned from a hardware-centric manufacturing model to a software-defined ecosystem. As vehicles evolve into always-connected platforms, the support infrastructure serving owners and technicians must undergo a parallel transformation. Traditional support mechanisms—static owner’s manuals, decision-tree chatbots, and scripted call centers—are buckling under the weight of increasing vehicle complexity. The modern automotive consumer expects immediate, context-aware, and technically accurate resolution to queries ranging from infotainment configuration to complex mechanical diagnostics.

This report articulates the technical specification for a next-generation **Automotive Support System** architected on the **Google Agent Development Kit (ADK)**. Unlike previous generations of "stateless" AI assistants, this system leverages a **Multi-Agent System (MAS)** architecture.1 By decomposing the cognitive load across specialized agents—specifically a **KnowledgeAgent** for technical retrieval, a **ServiceAgent** for transactional execution, and a **HumanHandoffAgent** for safety escalation—the system achieves a balance of reliability, safety, and scalability that monolithic Large Language Models (LLMs) cannot provide.

Central to this design is the strategic application of the **Gemini 3** model family. Adhering to the rigorous cognitive requirements of automotive diagnostics, the architecture mandates **Gemini 3 Pro** for the high-reasoning tasks of Intent Classification and Complex RAG synthesis, ensuring that nuanced user queries are correctly interpreted and grounded in technical fact.2 Conversely, **Gemini 3 Flash** is deployed for high-volume, low-latency routing and deterministic tool execution, optimizing the economic profile of the system without compromising performance.2

Furthermore, this specification integrates the **Agent-to-Agent (A2A) Protocol**, a standardized interoperability layer that allows this support system to exist not as a silo, but as a collaborative node within a broader ecosystem of OEM, dealer, and third-party services.4 By strictly defining state horizons—persistent vehicle data in **User Scope** and ephemeral dialogue context in **Session Scope**—the architecture ensures data hygiene and hyper-personalization.

The following sections provide an exhaustive technical blueprint, detailing the ingestion pipelines for heterogeneous documentation, the cryptographic and schema definitions for API interactions, and the orchestration logic required to deploy this system at an enterprise scale.

## ---

**2\. The Paradigm Shift: From Monolithic LLMs to Agentic Workflows**

### **2.1 Limitations of Monolithic Architectures in Safety-Critical Domains**

The initial wave of Generative AI adoption in customer support relied heavily on monolithic architectures. In these systems, a single LLM instance—prompted with a massive system instruction—was responsible for every aspect of the interaction. This "God Model" approach required the LLM to simultaneously act as a greeter, a technical manual reader, a warranty database querist, and a safety compliance officer.

While functional for casual conversation, monolithic architectures exhibit severe failure modes in the automotive domain:

1. **Context Drift:** As a conversation elongates, the model's attention mechanism struggles to retain the specific constraints of the prompt against the accumulating noise of the dialogue history.  
2. **Tool Hallucination:** A model optimized for creative fluency often invents API parameters or confidentially states incorrect warranty terms when the actual data is unavailable.  
3. **Latency Bottlenecks:** Routing a simple query like "Book an oil change" through a massive reasoning model introduces unnecessary latency and cost.  
4. **Debugging Complexity:** When a monolithic agent fails, isolating the error is nearly impossible. Did it fail because of the retrieval context, the prompt instruction, or the model's inherent bias?

As noted in foundational analysis of agent systems, reliability in AI comes from **decentralization and specialization**.1 Just as modern software engineering rejects monolithic codebases in favor of microservices, modern AI architecture demands a Multi-Agent System (MAS).

### **2.2 The Google Agent Development Kit (ADK) Proposition**

The Google ADK facilitates this transition by providing the primitives necessary to treat agents as software components. It moves development from "prompt engineering" to "cognitive architecture."

**Key ADK Primitives Utilized:**

* **SequentialAgent:** Enforces linear, deterministic workflows (e.g., Ingest ![][image1] Validate ![][image1] Summarize).1  
* **Router:** Dynamically selects the best downstream agent based on semantic intent.6  
* **State Management:** Provides structured scopes (User, Session) to manage context persistence, a feature often absent in raw API integrations.1

The ADK allows us to bind specific models to specific roles. We leverage this to assign **Gemini 3 Pro** to the Root Coordinator for superior intent classification, while using lighter models for simpler downstream tasks. This heterogeneous model strategy is the cornerstone of cost-effective, high-performance agent design.

## ---

**3\. System Topology and Orchestration Logic**

The proposed architecture is a hierarchical tree structure governed by a Root Coordinator. This creates a "Hub and Spoke" model where the Root acts as the intelligent dispatcher, and the leaf nodes act as functional specialists.

### **3.1 Architectural Diagram**

The following Mermaid.js visualization details the agent hierarchy, the model assignments, and the flow of persistent vs. ephemeral state data.

Code snippet

graph TD  
    %% Core Nodes  
    User((End User))  
    Root  
      
    %% Specialist Agents  
    subgraph Specialist\_Team  
        direction TB  
        KA  
        SA  
        HH  
    end

    %% Data Scopes  
    subgraph Data\_Scopes  
        US  
        SS  
    end

    %% External Systems  
    subgraph Infrastructure \[External Infrastructure\]  
        VDB  
        APIs  
        CRM\[Human Console\<br/\>Live Agent Platform\]  
    end

    %% Routing Logic  
    User \--\>|Natural Language Query| Root  
    Root \--\>|Intent: Technical/Spec| KA  
    Root \--\>|Intent: Transactional| SA  
    Root \--\>|Intent: Ambiguous/Unsafe| HH

    %% State Interaction  
    Root \-.-\>|Read/Write| SS  
    SA \-.-\>|Read| US  
    SA \-.-\>|Write| SS  
    KA \-.-\>|Read| US  
    KA \-.-\>|Read| SS

    %% Backend Connections  
    KA \<--\>|Retrieval| VDB  
    SA \<--\>|HTTP/REST| APIs  
    HH \--\>|A2A Handoff| CRM

### **3.2 The Root Coordinator: The Cognitive Cortex**

The **Root Coordinator** is the most critical component of the system. It does not answer questions; it understands them. In accordance with the requirement to use **Gemini 3 Pro** for high-reasoning tasks like "Intent Classification" 7, this agent is powered by the most capable model available.

**Why Gemini 3 Pro for the Root?**

User queries in the automotive domain are frequently multi-faceted or ambiguous.

* *Query:* "My car is making a sound like a penny in a dryer, and I think I'm due for service anyway. Is that covered?"  
* *Analysis:* This query contains three distinct intents:  
  1. Diagnostic (Sound analysis) ![][image1] Human Handoff.  
  2. Maintenance (Service due) ![][image1] Service Agent.  
  3. Warranty (Coverage check) ![][image1] Service Agent.

A lightweight model might latch onto "service" and route immediately to the booking API, ignoring the potentially dangerous mechanical noise. **Gemini 3 Pro** possesses the reasoning depth to recognize the *primary* risk (the noise) and prioritize the **HumanHandoffAgent**, or to decompose the query into sub-tasks (investigate noise first, then check warranty).

**Routing Logic Table:**

| Semantic Intent | Definition | Target Agent | Model Justification |
| :---- | :---- | :---- | :---- |
| **Technical / Specification** | Requests for static facts, fluid capacities, operating procedures, or maintenance intervals. | KnowledgeAgent | Requires complex synthesis of manual data. |
| **Transactional / Action** | Requests to change state (book appointment) or query dynamic databases (warranty status). | ServiceAgent | Task is deterministic; routing can be handled by Flash, but Root classification uses Pro. |
| **Diagnostic / Subjective** | Descriptions of sensory inputs (sounds, smells), accident reports, or emergency indicators. | HumanHandoffAgent | Safety-critical; requires immediate escalation. |

### **3.3 The Agent-to-Agent (A2A) Protocol Layer**

The architecture is not designed in a vacuum. It utilizes the **Agent-to-Agent (A2A) Protocol** to facilitate communication between the Root and its specialists, and potentially between this system and external partners.4

**Implementation Details:**

* **Agent Cards:** Each specialist (Knowledge, Service, Handoff) publishes an "Agent Card"—a JSON manifest describing its capabilities, input schema, and supported interaction modes.5  
* **Standardization:** Unlike proprietary function calling, A2A provides a universal standard. If the dealership changes its scheduling provider to a third-party AI scheduler, the ServiceAgent can simply swap the target Agent Card without rewriting the Root Coordinator's logic.5  
* **Interoperability:** This future-proofs the system. An insurance company's agent could eventually query this Automotive Support Agent via A2A to verify vehicle specs during a claim, authenticated via the protocol's security layer.9

## ---

**4\. The Knowledge Agent: Advanced RAG and Layout-Aware Ingestion**

The **KnowledgeAgent** answers the "What" and "How" questions. It is backed by a **Retrieval-Augmented Generation (RAG)** pipeline. However, standard RAG implementations often fail in the automotive domain due to the complex formatting of Owner's Manuals.

### **4.1 The Challenge of Automotive Documentation**

Automotive manuals are not linear text. They are highly visual documents containing:

* **Multi-column layouts:** Text flows from the bottom of column A to the top of column B, interrupting linear parsing.  
* **Warning Boxes:** Important safety information is often placed in sidebars or colored boxes that break the narrative flow.  
* **Complex Tables:** Maintenance schedules are massive matrices of "Miles" vs. "Components" vs. "Driving Conditions."  
* **Markdown Hierarchies:** Digital versions often exist as deeply nested Markdown files.

A naive ingestion strategy (e.g., "split every 1000 characters") destroys this structure. A chunk might contain the header "Engine Oil" but cut off before the specific viscosity table, or worse, blend it with the "Transmission Fluid" section from the next column.10

### **4.2 Specification: Layout-Aware PDF Ingestion**

To satisfy the requirement for a "layout-aware ingestion strategy," we mandate the use of the **Vertex AI Layout Parser** or a comparable tool like **Docling**.11

**The Pipeline:**

1. **Optical Layout Analysis (OLA):** Before text extraction, the document is processed by a computer vision model that identifies geometric regions: Header, Paragraph, Table, Image, Sidebar.  
2. **Structure-Preserving Extraction:**  
   * **Text:** Extracted within the identified blocks, respecting reading order (column-wise, not just left-to-right).  
   * **Tables:** Tables are not flattened to text. They are extracted as structural objects (HTML \<table\> or Markdown tables). This preserves the row/column associations.12  
   * **Metadata Tagging:** Each extracted chunk is tagged with its parent headers. A paragraph about "5W-30" is not just stored as "5W-30"; it is stored with metadata {"Section": "Maintenance", "Subsection": "Fluids", "Component": "Engine Oil"}.  
3. **Visual Chunking:** Instead of splitting by character count, we split by **Logical Block**. A chunk represents a complete thought (e.g., a full warning box, a complete table row context).10

**Performance Impact:** Research on "Layout-Aware Document Retrieval" (LAD-RAG) demonstrates that this approach can improve retrieval recall by over 20% compared to baseline text splitters and achieve near-perfect recall on complex document queries.14 This is non-negotiable for safety-critical automotive data.

### **4.3 Specification: Structured Markdown Splitting**

For documentation already in Markdown (e.g., digital service guides), we utilize **Header-Based Splitting**.15

**The Algorithm:** We utilize a parser similar to LangChain's MarkdownHeaderTextSplitter 17, but enhanced with **Contextual Inheritance**.

* **Mechanism:** The splitter traverses the Markdown Abstract Syntax Tree (AST).  
* **Aggregation:** Content is grouped by the deepest header level (e.g., \#\#\#).  
* **Path Injection:** Crucially, the parent headers are prepended to the chunk content.

  * ### ***Source:***     **Maintenance**     **Severe Driving**     **Oil Change**     **Replace every 3,000 miles.**

  * *Generated Chunk:* Maintenance \> Severe Driving \> Oil Change: Replace every 3,000 miles.  
* **Reasoning:** When the vector database retrieves this chunk, the LLM immediately knows it applies to "Severe Driving" conditions, preventing it from advising a normal user to change oil unnecessarily often.15

### **4.4 Synthesis Model: Gemini 3 Pro**

Once relevant chunks are retrieved, the **KnowledgeAgent** utilizes **Gemini 3 Pro** for synthesis.

* **Role:** Complex RAG Synthesis.  
* **Capability:** Gemini 3 Pro's large context window allows it to ingest multiple conflicting manual sections (e.g., one for the 2.0L engine, one for the 2.5L engine) and reason over them to ask the user: *"Which engine do you have?"* before answering. A lesser model might simply hallucinate an answer based on the first chunk it sees.1

## ---

**5\. The Service Agent: Tooling, State, and Determinism**

The **ServiceAgent** is the system's "hands." It handles deterministic tasks like warranty checks and appointment scheduling.

### **5.1 Model Selection: Gemini 3 Flash**

In accordance with the directive to use **Gemini 3 Flash** for low-latency, high-volume tasks 2, this agent utilizes the Flash model.

* **Justification:** Service tasks are structurally rigid. The agent does not need to philosophize about warranties; it needs to extract a VIN, format a JSON payload, and parse the response. Flash is faster and significantly cheaper for these high-throughput operations.

### **5.2 Tool Definitions and Schemas**

The ServiceAgent operates using **ADK Tool Definitions**. These tools are interfaces to external APIs.

#### **5.2.1 Warranty API Tool**

**Function:** Checks coverage status.

**Dependency:** user.state\['vin'\].

**JSON Schema:**

JSON

{  
  "name": "check\_warranty",  
  "description": "Retrieves warranty status from the OEM database.",  
  "parameters": {  
    "type": "object",  
    "properties": {  
      "vin": {  
        "type": "string",  
        "description": "17-character Vehicle Identification Number",  
        "pattern": "^{17}$"  
      }  
    },  
    "required": \["vin"\]  
  }  
}

*Design Note:* The regex pattern ensures the agent validates the VIN format *before* making the API call, reducing wasted cycles on the backend.20

#### **5.2.2 Appointment API Tool**

**Function:** Books a service slot.

**Dependency:** session.state\['appointment\_slot'\].

**JSON Schema:**

JSON

{  
  "name": "book\_appointment",  
  "description": "Confirmed booking of a service slot.",  
  "parameters": {  
    "type": "object",  
    "properties": {  
      "vin": { "type": "string" },  
      "service\_code": { "type": "string", "enum": },  
      "datetime": { "type": "string", "format": "date-time" },  
      "dealer\_id": { "type": "string" }  
    },  
    "required": \["vin", "service\_code", "datetime", "dealer\_id"\]  
  }  
}

*Orchestration:* The ServiceAgent uses an **ADK Loop Pattern** to fill these slots. If the user says "Book an oil change," the agent detects the missing datetime and dealer\_id, loops back to prompt the user, and only executes the tool when the schema is satisfied.22

## ---

**6\. The Human Handoff Agent: The Safety Valve**

Automotive support is a liability minefield. No AI system should definitively diagnose a mechanical failure based on a text description. The **HumanHandoffAgent** ensures safety.

### **6.1 Trigger Logic**

The Root Coordinator delegates to this agent when:

1. **Ambiguity:** The user's description is vague ("It makes a weird noise").  
2. **Sentiment:** The user is frustrated or angry.  
3. **Safety Keywords:** "Smoke," "Fire," "Crash," "Brakes failed."

### **6.2 Handoff Protocol**

The handoff is not a termination; it is a **Contextual Transfer**.

1. **Summarization:** The agent generates a structured summary of the session: *"User verified VIN X. Complained of grinding noise at 40mph. Tried to check warranty but failed."*  
2. **Routing:** It utilizes the A2A protocol or a CRM API to route this packet to a human agent's console.  
3. **User Assurance:** It informs the user: *"I'm connecting you with a senior technician who can listen to that noise. I've passed them your VIN and details."*

This warm handoff reduces average handling time (AHT) for the human agent, as they don't need to re-ask for the VIN or the problem description.23

## ---

**7\. State Management Strategy: Scoping for Persistence and Privacy**

The ADK provides a robust state management system that separates data by lifecycle. This is critical for automotive use cases where some data (VIN) is permanent, while other data (conversation context) is temporary.

### **7.1 Scope Definitions**

| Scope | Definition | Storage Backend | Data Examples |
| :---- | :---- | :---- | :---- |
| **User Scope** | Persistent data tied to the user's identity. Survives across multiple sessions. | PostgreSQL / Firestore | VIN, Vehicle Model, Owner Name, Preferred Dealer, Warranty Expiration Date. |
| **Session Scope** | Ephemeral data tied to the current conversation. Cleared upon session end or timeout. | Redis / In-Memory | Current Query, RAG Search Results, Tentative Appointment Time, Dialogue History. |
| **Agent Scope** | Temporary working memory for a specific agent during execution. | Local Memory | API Response Payloads, Intermediate Reasoning Steps, Routing Confidence Scores. |

### **7.2 The Flow of State**

1. **Initialization:** When a session starts, the system loads the **User Scope**. If a VIN is present, it is injected into the context of the ServiceAgent and KnowledgeAgent.  
2. **Updates:** If the user provides a new VIN, the ServiceAgent writes this to the **User Scope**, persisting it for future interactions.  
3. **Privacy:** By keeping dialogue history in **Session Scope**, we minimize the risk of retaining sensitive PII (like credit card details mentioned in passing) longer than necessary.

## ---

**8\. Detailed ADK Implementation and Patterns**

### **8.1 The Root Dispatcher Pattern**

The Root Coordinator is implemented as an LlmAgent configured with a **Router** instruction set.

* **Mechanism:** It evaluates the user's input against the descriptions of the sub-agents.  
* **Output:** It generates a transfer\_to\_agent directive.  
* **State:** It writes the routing rationale to session.state\['routing\_reason'\], which helps in debugging why a query was sent to a specific agent.3

### **8.2 The Sequential RAG Pattern**

The KnowledgeAgent uses a **SequentialAgent** primitive.

* **Step 1: Query Transformation:** An internal helper agent rewrites the user's query (e.g., "fluid change") into a specific search term ("maintenance schedule transmission fluid capacity").  
* **Step 2: Retrieval:** The vector store is queried.  
* **Step 3: Answer Generation:** Gemini 3 Pro synthesizes the answer. This sequential enforcement ensures that the generation step *cannot* happen without the retrieval step completing successfully.1

### **8.3 The Loop Pattern for Slot Filling**

The ServiceAgent uses a **LoopAgent** primitive for appointment booking.

* **Condition:** while not appointment\_ready()  
* **Body:** Ask user for missing fields (Date, Time, Dealer).  
* **Exit:** When all fields match the schema, execute the API call and break the loop. This prevents the "one-shot" failure mode where an agent tries to book an appointment with incomplete data.24

## ---

**9\. Infrastructure and Deployment on Vertex AI**

The entire system is designed to run on the **Vertex AI Agent Engine**, a managed serverless platform optimized for ADK workloads.25

### **9.1 Scalability**

* **Statelessness:** Because state is offloaded to external stores (Redis/SQL), the agent containers are stateless. This allows Vertex AI to autoscale the number of instances based on incoming request volume (RPS) without data synchronization issues.  
* **A2A Server:** The system exposes an HTTP endpoint compatible with the A2A protocol. This allows it to be called not just by a chat UI, but by other automated systems (e.g., a "Connected Car" telemetry system that automatically queries the agent when a warning light triggers).23

### **9.2 Latency Optimization**

* **Model Tiering:** By offloading routing and simple tools to **Gemini 3 Flash**, we keep the average latency low. **Gemini 3 Pro** is only invoked when the "heavy lifting" of reasoning is required.  
* **Caching:** Common queries (e.g., "How to pair Bluetooth") are cached at the KnowledgeAgent level to avoid repeated vector searches and LLM generation costs.

## ---

**10\. Conclusion**

The specification presented here defines a robust, production-grade **Automotive Support System**. By moving beyond the limitations of monolithic LLMs and embracing a **Multi-Agent System** architecture, we create a solution that is specialized, scalable, and safe.

The strategic use of **Google ADK** primitives allows for deterministic control over workflows, ensuring that critical tasks like warranty checks follow strict protocols. The tiered model strategy—**Gemini 3 Pro** for high-level reasoning and **Gemini 3 Flash** for high-volume execution—optimizes the performance-to-cost ratio. Finally, the integration of **Layout-Aware Ingestion** and the **A2A Protocol** ensures that the system can deeply understand the technical reality of the vehicle and seamlessly collaborate within the broader digital automotive ecosystem.

This architecture serves as a blueprint for the future of automotive customer experience, where support is not just reactive, but intelligent, context-aware, and deeply integrated into the vehicle's lifecycle.

## ---

**11\. Deep Dive: The Agent-to-Agent (A2A) Interface Specification**

To fully appreciate the interoperability of this system, we must examine the **Agent-to-Agent (A2A) Protocol** implementation in detail. This protocol is not merely a method for connecting agents; it is the fabric that allows the Automotive Support System to function as a "digital employee" within a larger enterprise workforce.

### **11.1 The A2A Handshake and Discovery**

In a monolithic system, components are hard-coded. In an A2A ecosystem, agents "discover" each other. The **Root Coordinator** does not necessarily need the ServiceAgent's code compiled into its own binary. Instead, it can resolve the ServiceAgent via its **Agent Card**.

**Agent Card Specification (ServiceAgent):**

JSON

{  
  "agent\_id": "service-agent-v1",  
  "name": "Automotive Service Specialist",  
  "description": "Handles warranty lookups and service appointment scheduling. Requires VIN.",  
  "capabilities":,  
  "transport": "http",  
  "endpoint": "https://api.auto-support.internal/a2a/service",  
  "auth\_type": "oauth2"  
}

*Insight:* This decoupling allows the ServiceAgent to be updated (e.g., new warranty API endpoints) without redeploying the Root Coordinator. The Root simply re-fetches the Agent Card to understand the new capabilities.5

### **11.2 The Task Lifecycle in A2A**

Complex automotive queries are often long-running. If a user asks, *"Check if my warranty covers this, and if so, book an appointment,"* this is a multi-step process that might encounter delays (e.g., the warranty database is slow).

The A2A protocol handles this via **Task States**:

1. **Submitted:** Root sends the request to ServiceAgent.  
2. **Working:** ServiceAgent acknowledges and begins the API calls.  
3. **Input\_Required:** ServiceAgent pauses. The warranty is valid, but it needs the user's preferred date for the appointment. It sends an Input\_Required signal back to the Root.  
4. **Completed:** The task finishes with a result payload.

This asynchronous state machine is superior to simple REST calls because it prevents timeouts on long operations and allows for bidirectional interaction (the agent asking the user for clarification mid-task).5

### **11.3 Security and Authentication**

The A2A layer enforces strict security.

* **mTLS (Mutual TLS):** Ensures that traffic between the Root and the Specialists is encrypted and authenticated at the transport layer.  
* **OIDC (OpenID Connect):** The Root Coordinator passes a signed identity token to the ServiceAgent. The ServiceAgent validates that this token grants the "Root" role permission to execute "Warranty Check" tools. This prevents unauthorized internal services (e.g., a hacked marketing bot) from querying sensitive vehicle data via the ServiceAgent.9

## ---

**12\. Advanced RAG: The Mathematics of Layout Awareness**

The "KnowledgeAgent" relies on **Layout-Aware Ingestion**. To understand why this is superior, we must look at the mathematical difference in how text is represented in the vector space.

### **12.1 The Semantic Discontinuity of Naive Splitting**

In a standard RecursiveCharacterTextSplitter, a document is treated as a 1D string of characters.

![][image2]  
A chunk ![][image3] is a window of size ![][image4]:

![][image5]  
If a table row exists at index ![][image6], and the window cut-off ![][image7] lands in the middle of that row, the semantic relationship is severed.

* *Table:* Engine: V6 | Oil: 5.4L  
* *Chunk 1:* ...Engine: V6 | Oi  
* *Chunk 2:* l: 5.4L...

When these chunks are embedded into vector space ![][image8], the vector ![][image9] and ![][image10] are far apart from the query vector ![][image11] ("How much oil for V6?"). ![][image9] has the engine type but not the oil capacity. ![][image10] has the capacity but no engine context. The retrieval fails.

### **12.2 The Geometric Integrity of Layout Parsing**

Layout-Aware Parsing treats the document as a set of 2D bounding boxes ![][image12].

![][image13]  
where each ![][image14] contains text ![][image15] and spatial coordinates ![][image16].

The chunking algorithm clusters boxes based on spatial proximity and structural hierarchy (e.g., rows within a table container).

![][image17]  
This ensures that the entire row Engine: V6 | Oil: 5.4L is preserved in a single chunk. The resulting vector ![][image18] contains both the key ("Engine") and the value ("5.4L"), maximizing the cosine similarity with the query ![][image11].

![][image19]  
This mathematical preservation of semantic integrity is why Layout-Aware RAG (LAD-RAG) is essential for technical manual retrieval.14

## ---

**13\. State Management Implementation Details**

The differentiation between **User Scope** and **Session Scope** requires a concrete implementation strategy using the ADK's storage interfaces.

### **13.1 Database Schema for User Scope**

The User Scope is backed by a relational database (e.g., Cloud SQL for PostgreSQL).

**Table: user\_profiles**

| Column | Type | Description |
| :---- | :---- | :---- |
| user\_id | UUID | Primary Key |
| vin | VARCHAR(17) | The active vehicle. |
| vehicle\_metadata | JSONB | Cached details (Year, Make, Model, Trim). |
| preferences | JSONB | {"dealer\_id": "D-123", "communication": "sms"} |
| last\_active | TIMESTAMP | For retention policies. |

**ADK Integration:**

The ADK's PostgresSessionService or a custom UserContextService loads this row upon session initialization.

Python

\# Pseudo-code for ADK State Loading  
def load\_user\_context(user\_id):  
    user\_data \= db.query("SELECT \* FROM user\_profiles WHERE user\_id \=?", user\_id)  
    return {  
        "vin": user\_data.vin,  
        "trim": user\_data.vehicle\_metadata.get("trim")  
    }

### **13.2 Redis Implementation for Session Scope**

The Session Scope is high-velocity and ephemeral, making Redis the ideal backend.

**Key Structure:**

session:{session\_id}:state ![][image1] Hash Map

* history: List of messages (ProtoBuf serialized).  
* intent: "Warranty\_Check" (String).  
* slot\_date: "2026-10-12" (String).  
* temp\_rag\_results: JSON Blob (Top 3 retrieved chunks).

**TTL (Time To Live):**

Session keys are set with a TTL of 30 minutes. If the user stops interacting, the context expires, ensuring that stale state (e.g., an abandoned appointment slot) does not persist indefinitely and block future interactions.

## ---

**14\. Testing and Evaluation Strategy**

Deploying a multi-agent system requires a rigorous evaluation framework. We cannot simply rely on "it looks good."

### **14.1 Component-Level Testing (Unit Tests)**

* **ServiceAgent:** We use **mock APIs** to verify that the agent correctly fills the JSON schema.  
  * *Test:* Input "Book oil change tomorrow". Verify agent loops to ask for "Time".  
* **KnowledgeAgent:** We use **Golden Datasets** of (Question, Answer, Ground Truth Chunk) pairs.  
  * *Metric:* **Recall@k**. Did the retrieval system find the correct manual section?  
  * *Metric:* **Faithfulness**. Did Gemini 3 Pro generate an answer supported by the retrieved chunk, or did it hallucinate?

### **14.2 System-Level Testing (Integration Tests)**

* **Root Coordinator:** We test the routing accuracy.  
  * *Dataset:* 500 diverse automotive queries tagged with the correct intent.  
  * *Metric:* **Classification Accuracy**. Does the Root correctly send "weird noise" to Handoff and "oil change" to Service?  
* **End-to-End Simulation:** We use **LLM-as-a-Judge** (e.g., a separate Gemini 3 Ultra instance) to simulate a user interacting with the system. The Judge rates the conversation on "Helpfulness," "Safety," and "Tone."

### **14.3 Red Teaming for Safety**

Given the safety-critical nature of cars, we must Red Team the system.

* *Attack Vector:* "How do I disable the speed limiter?"  
* *Expected Defense:* KnowledgeAgent should retrieve the manual warnings and refuse, or HandoffAgent should intervene.  
* *Attack Vector:* "My brakes failed, what do I do?"  
* *Expected Defense:* Immediate routing to HumanHandoffAgent with an emergency protocol, *not* a generic RAG response about brake fluid types.

## ---

**15\. Future-Proofing: The Road Ahead**

This architecture is designed for the future of 2026 and beyond.

### **15.1 Multi-Modal Inputs**

The current ADK supports multi-modal inputs. The **Root Coordinator** can be upgraded to accept images.

* *Scenario:* User uploads a photo of a dashboard warning light.  
* *Processing:* Gemini 3 Pro (Vision) identifies the icon (e.g., "Check Engine").  
* *Routing:* The intent is classified as "Diagnostic," routing to ServiceAgent (to pull codes) or KnowledgeAgent (to explain the light).

### **15.2 Vehicle-to-Cloud (V2C) Integration**

As vehicles become more connected, the **User Scope** can be populated not just by user input, but by real-time telemetry.

* *Flow:* The car pushes an error code P0420 to the cloud.  
* *State Update:* The system updates user.state\['active\_codes'\] \= \['P0420'\].  
* *Proactive Support:* When the user opens the chat, the Root Coordinator sees the active code and proactively asks: *"I see a Check Engine light for the catalytic converter. Should I schedule a diagnostic?"*

This transition from *reactive* support to *proactive* agentic partnership is the ultimate goal of this architecture. By leveraging the **Google Agent Development Kit**, **Gemini 3 Pro**, and the **A2A Protocol**, we lay the foundation for a system that doesn't just read the manual—it understands the car.

### ---

**References & Data Sources**

* **ADK & Orchestration:**.1  
* **Models (Gemini):**.2  
* **A2A Protocol:**.4  
* **RAG & Ingestion:**.10  
* **APIs & Automotive Data:**.20

#### **Works cited**

1. Developer's guide to multi-agent patterns in ADK \- Google ..., accessed January 23, 2026, [https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/)  
2. Build Your First Intelligent Agent Team: A Progressive Weather Bot with ADK, accessed January 23, 2026, [https://google.github.io/adk-docs/tutorials/agent-team/](https://google.github.io/adk-docs/tutorials/agent-team/)  
3. Implementing Agentic Architectural Patterns with Google ADK | by Saeed Hajebi | Medium, accessed January 23, 2026, [https://medium.com/@saeedhajebi/implementing-agentic-architectural-patterns-with-google-adk-75281096de32](https://medium.com/@saeedhajebi/implementing-agentic-architectural-patterns-with-google-adk-75281096de32)  
4. Unlock AI agent collaboration. Convert ADK agents for A2A | Google Cloud Blog, accessed January 23, 2026, [https://cloud.google.com/blog/products/ai-machine-learning/unlock-ai-agent-collaboration-convert-adk-agents-for-a2a](https://cloud.google.com/blog/products/ai-machine-learning/unlock-ai-agent-collaboration-convert-adk-agents-for-a2a)  
5. A2A Agent Patterns with the Agent Development Kit (ADK) | by xbill ..., accessed January 23, 2026, [https://medium.com/google-cloud/a2a-agent-patterns-with-the-agent-development-kit-adk-aee3d61c52cf](https://medium.com/google-cloud/a2a-agent-patterns-with-the-agent-development-kit-adk-aee3d61c52cf)  
6. Building Collaborative AI: A Developer's Guide to Multi-Agent Systems with ADK | Google Cloud Blog, accessed January 23, 2026, [https://cloud.google.com/blog/topics/developers-practitioners/building-collaborative-ai-a-developers-guide-to-multi-agent-systems-with-adk](https://cloud.google.com/blog/topics/developers-practitioners/building-collaborative-ai-a-developers-guide-to-multi-agent-systems-with-adk)  
7. Building agents with the ADK and the new Interactions API \- Google Developers Blog, accessed January 23, 2026, [https://developers.googleblog.com/building-agents-with-the-adk-and-the-new-interactions-api/](https://developers.googleblog.com/building-agents-with-the-adk-and-the-new-interactions-api/)  
8. Agent-to-Agent Communication: Implementing A2A Protocol in Your ADK Projects, accessed January 23, 2026, [https://www.a2aprotocol.org/en/tutorials/agent-to-agent-communication-implementing-a2a-protocol-in-adk-projects](https://www.a2aprotocol.org/en/tutorials/agent-to-agent-communication-implementing-a2a-protocol-in-adk-projects)  
9. Vertex AI Agent Builder | Google Cloud, accessed January 23, 2026, [https://cloud.google.com/products/agent-builder](https://cloud.google.com/products/agent-builder)  
10. I extracted my production RAG ingestion logic into a small open-source kit (Docling \+ Smart Chunking) \- Reddit, accessed January 23, 2026, [https://www.reddit.com/r/Rag/comments/1p4ku3q/i\_extracted\_my\_production\_rag\_ingestion\_logic/](https://www.reddit.com/r/Rag/comments/1p4ku3q/i_extracted_my_production_rag_ingestion_logic/)  
11. Parse and chunk documents | Vertex AI Search \- Google Cloud Documentation, accessed January 23, 2026, [https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents)  
12. Process documents with Gemini layout parser | Document AI \- Google Cloud Documentation, accessed January 23, 2026, [https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk)  
13. PDF Data Extraction Benchmark 2025: Comparing Docling, Unstructured, and LlamaParse for Document Processing Pipelines \- Procycons, accessed January 23, 2026, [https://procycons.com/en/blogs/pdf-data-extraction-benchmark/](https://procycons.com/en/blogs/pdf-data-extraction-benchmark/)  
14. LAD-RAG: Layout-aware Dynamic RAG for Visually-Rich Document Understanding \- arXiv, accessed January 23, 2026, [https://arxiv.org/abs/2510.07233](https://arxiv.org/abs/2510.07233)  
15. Optimizing RAG Context: Chunking and Summarization for Technical Docs, accessed January 23, 2026, [https://dev.to/oleh-halytskyi/optimizing-rag-context-chunking-and-summarization-for-technical-docs-3pel](https://dev.to/oleh-halytskyi/optimizing-rag-context-chunking-and-summarization-for-technical-docs-3pel)  
16. Rethinking Markdown Splitting for RAG: Context Preservation \- Reddit, accessed January 23, 2026, [https://www.reddit.com/r/Rag/comments/1f0q2b7/rethinking\_markdown\_splitting\_for\_rag\_context/](https://www.reddit.com/r/Rag/comments/1f0q2b7/rethinking_markdown_splitting_for_rag_context/)  
17. Mastering Text Splitting for Effective RAG with Langchain \- HiDevs, accessed January 23, 2026, [https://hidevscommunity.substack.com/p/mastering-text-splitting-for-effective](https://hidevscommunity.substack.com/p/mastering-text-splitting-for-effective)  
18. Advanced RAG techniques with LangChain — Part 1 | by Roberto Infante | Medium, accessed January 23, 2026, [https://medium.com/@roberto.g.infante/advanced-rag-techniques-with-langchain-f9c82290b0d1](https://medium.com/@roberto.g.infante/advanced-rag-techniques-with-langchain-f9c82290b0d1)  
19. A Curated List of Resources for Google's Agent Development Kit (ADK) \- Medium, accessed January 23, 2026, [https://medium.com/google-cloud/a-curated-list-of-resources-for-googles-agent-development-kit-adk-159a5449624f](https://medium.com/google-cloud/a-curated-list-of-resources-for-googles-agent-development-kit-adk-159a5449624f)  
20. Warranty API \- Helpjuice, accessed January 23, 2026, [https://rollick.helpjuice.com/155196-warranty/warranty-web-service-specification](https://rollick.helpjuice.com/155196-warranty/warranty-web-service-specification)  
21. Vehicle API Specifications, accessed January 23, 2026, [https://carapi.app/features/json-api-specs](https://carapi.app/features/json-api-specs)  
22. Build Multi-Agent Systems with ADK \- Google Codelabs, accessed January 23, 2026, [https://codelabs.developers.google.com/codelabs/production-ready-ai-with-gc/3-developing-agents/build-a-multi-agent-system-with-adk](https://codelabs.developers.google.com/codelabs/production-ready-ai-with-gc/3-developing-agents/build-a-multi-agent-system-with-adk)  
23. Build a multi-agent AI customer support system with the Google ADK, A2A and ... \- Nebius, accessed January 23, 2026, [https://nebius.com/blog/posts/build-multi-agent-ai-customer-support-system](https://nebius.com/blog/posts/build-multi-agent-ai-customer-support-system)  
24. Mastering Workflow Strategies in Google Agent Development Kit (ADK): Building Effective Multi-Agent Systems | by Samin Chandeepa (Adomic) | Medium, accessed January 23, 2026, [https://medium.com/@saminchandeepa/mastering-workflow-strategies-in-google-agent-development-kit-adk-building-effective-multi-agent-59dbfcfa325f](https://medium.com/@saminchandeepa/mastering-workflow-strategies-in-google-agent-development-kit-adk-building-effective-multi-agent-59dbfcfa325f)  
25. Agentic Workflows inside Google Workspace: Build a Google Docs Agent with ADK, accessed January 23, 2026, [https://codelabs.developers.google.com/google-docs-adk-agent](https://codelabs.developers.google.com/google-docs-adk-agent)  
26. How to Build a Production-Grade RAG with ADK & Vertex AI RAG Engine via the Agent Starter Pack | Google Cloud \- Medium, accessed January 23, 2026, [https://medium.com/google-cloud/how-to-build-a-production-grade-rag-with-adk-vertex-ai-rag-engine-via-the-agent-starter-pack-7e39e9cfe856](https://medium.com/google-cloud/how-to-build-a-production-grade-rag-with-adk-vertex-ai-rag-engine-via-the-agent-starter-pack-7e39e9cfe856)  
27. Multi-Agent Systems in ADK \- Google, accessed January 23, 2026, [https://google.github.io/adk-docs/agents/multi-agents/](https://google.github.io/adk-docs/agents/multi-agents/)  
28. Build multi-agentic systems using Google ADK | Google Cloud Blog, accessed January 23, 2026, [https://cloud.google.com/blog/products/ai-machine-learning/build-multi-agentic-systems-using-google-adk](https://cloud.google.com/blog/products/ai-machine-learning/build-multi-agentic-systems-using-google-adk)  
29. Warranty in automotive \- Common Data Model \- Microsoft Learn, accessed January 23, 2026, [https://learn.microsoft.com/en-us/common-data-model/schema/core/applicationcommon/foundationcommon/crmcommon/accelerators/automotive/warranty](https://learn.microsoft.com/en-us/common-data-model/schema/core/applicationcommon/foundationcommon/crmcommon/accelerators/automotive/warranty)  
30. ServiceAppointment | Automotive Cloud Developer Guide, accessed January 23, 2026, [https://developer.salesforce.com/docs/atlas.en-us.automotive\_cloud.meta/automotive\_cloud/sforce\_api\_objects\_serviceappointment.htm](https://developer.salesforce.com/docs/atlas.en-us.automotive_cloud.meta/automotive_cloud/sforce_api_objects_serviceappointment.htm)  
31. Service Appointment in automotive \- GitHub, accessed January 23, 2026, [https://github.com/MicrosoftDocs/common-data-model-and-service/blob/master/common-data-model/schema/core/applicationCommon/foundationCommon/crmCommon/accelerators/automotive/ServiceAppointment.md](https://github.com/MicrosoftDocs/common-data-model-and-service/blob/master/common-data-model/schema/core/applicationCommon/foundationCommon/crmCommon/accelerators/automotive/ServiceAppointment.md)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAXCAYAAADpwXTaAAAAaElEQVR4XmNgGAWjgGqAFYjZoJhioAPEJVBMMQC5rAOKZdHkyAJqUNwNxPxociQDnIaBnO0MxCFk4FogPg3ETkDMDMTUNYwcoA/FfUDMjSZHEuAE4glQTHFsGgNxORRTDKiaA0YBFQEA6csTxY5I6CAAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAAyCAYAAADhjoeLAAAFYklEQVR4Xu3dTai0ZRkH8FvSSCtLFFO0rCjBUjMSKdFMEcqFLaKFUq4UiggXigomoQsRW4kYYmVqIAVpCipkuZBqEQgWYgi5MfGDklwESipo1597ns68jzNz5nzMeeeF3w/+cOa5n7nf58xZvBf317QGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAu+OQysWVBys/qRy2bzPbdEnlT5VrK4eP2gCANXRp68XQrNxQ+dTGrXvq4MrtlT9Ujh+1sXOHtv73/Vvz+QLA2vtw5auV1ys/qhw7yQmVH06uX1k5aHjDHjmq9WLimnEDu+YLlf9ULhg3AADr51uVtyvnjxvKt1sv2r40blixFI3/aAq2VUrB9lrlwnEDALB+bq08VzludD0+WXm59fVOe0nBtnoKNgA4QHyw8sfKI5X3jdpiKNjuGTes2DIF25GtjwBe0XZvrd0q+lylj1a+M0k+s61QsAHAAeKkyr/b/MLorMpbrY/CzfOBtrH2bbNkzdwyFhVsWU/3vdYLzRQdma59evLzdq2iz1XKDtqbK/e3/jf8euWpNnuUdB4FGwAcIL7R5q9fi4zcvNP6Ord5UjB8c8mc2ZbbwHBe5aXKF8cN5buVZysfn7xOUfdK5bPDDduwij5XJZ/fLa3voP3Q5FpGQFNgHj3ctIQU2r9rfUdwCkAAYE0tWr+WKdJMlb5Q+cSobVVOqzxc+XPl5FFb5DnyPDdOXUux8f7JzylCzq78pi0/OrZZn5+r/LT18+B+3/b/MRgZ/Xuj7VtE5281a0p7MzmHLcen/KX1I14AgDVzROWJNn/92nDsw9VtuVGx3ZB/J2vHHqj8qm2MIA1yBEVGBOcdRfHp1qdxtzKduajPfC4/r5ze+rNlGvKXrZ8Tt79kfV3+LikkdyK/z/crf2/9aBejbACwhhatX0uh9Fjl15OfF7m48vySyYjee/vbFsooVka9xlOxeZ1nzrPPk/Vvf23LF2yL+kzBdnfr3w4QmUJ+vPWRvP0lI4E5o+6occNE1gkm72l9ijQbKWYV3MPIYn4nAGBNzTp/Lf+xn1p5snJX25gW3GvzNh1kOjDXp6dL84xZ0zWMOM0r2HIY8HOVh1o/6X+wTJ+Rz+a2yfWhAMoauyzcn7427crKfyvnTF4P3+DwYuXEybUUp8+0XhwPI52L+r2o9YLtI1PXjqncUTmjclnlt62/95TKfZWv/P/ODTYdAMAa+1rro11vtr6h4F+T10kKiUcrX27vLhT20ryCLc+UIihTuSk4b2p9vdpnpu6ZV7ANhVE2F+SewTJ9RtbG3d32HXH8fOXV1kcjZ426pd+0574YCrY8x7AWbniuXB+mWhf1m6nL3JvCM8/748qdrfeTAjPTt9mQkKnl/G6/aLOnexVsAMCOzCvYBhmJyj3jYibmFWyDfOXWdME2WNRniqAUchmZy+jbdDGb19e32e/bic36HY5TGa8/zBq+FGkp/jIKl9G2TH+OKdgAgB3ZrGBbZFHBlvVcWQM2LnIWGb5X9WOtj2Jd3vZ9fzY6/GDq9W7Zbr/5zIbPLaOp97RexGWqe5qCDQDYkYwePd76rsytTM1m6u/e1ndRZqfp9FEV6Se7IlO8LCuFWfrJ1PGQn021Z3ry+rb734qw3X4zqpbRteF3zHq37LbNeXrjXaDnVv7ZZhe2AABLSfGVw3NTgGRjxLC+a7tSsOWruLZSAG4mOzHT527bSb/ZhTuesp1+nd2w17W+Q/Sq9u5CDgBgSzY7moKtm7f2DQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAPA/wBfkOEQkmosWAAAAABJRU5ErkJggg==>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAYCAYAAAAYl8YPAAABPklEQVR4XuXUvyuFURzH8a9EFCkmvwaxKFmUQVaDRFKySdlE2axWykAZ2AxKBhMZSMrmX7BJTDJZ5f1xvk/XPffcy+UZlE+96nbOc7/P9zznPI/Zv02NG8QRnnCPW4yjA5uu2f9TNrkVa8Wxu8MYan2uEdt4xI4rmxZc4sqpcJwBvGDGJVOHfQt37XOptFtYbr9LRnd5w3o0HkfFDtDkStKAMwvtaxm/ShcecGNf7M53MoRXHFo4EpWi46Jd/RwtV6v7SK7FtCvPFh5spbRhw4qL1WMPE9mAKl+75A5Z6HgVk/FEKlMWljpnhdcpi37PWyiWjXe6Lexa1IQuUiEt98ItYgnnmPVrsiy4UZxaeHtKogc57KbRa4V3M5U1LMeD1UadiLoasdDhj9PjTrCC7uLp6pJrsSw6Z/ri/PG8A3qjNnb+mi+1AAAAAElFTkSuQmCC>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAZCAYAAADnstS2AAAA2ElEQVR4Xu3SvQ7BUBwF8CtYfAwSidjEYrQwSMRkMRhswmjwAAZh8QQS8QI2E+8gMdlsBiQGi6fgnPY0zW0tbBIn+SXt/Z82vW2N+d3kYSFHaNpjO3FoyA2q1vRNeDc6QS4wC2UqG4gFZlY4ZIl4AcN9DCSrNScflfmMZ2lBBSawkpFfdXd/lZ6U4CFdv2pMH56yhqTW+XihzS5hKzO4Q9lqKGnYw1BSsIMxFKTuVo0pwkUL5JXb0JHaV2UeHIz7LikCc+O+Mu+r8t9xEoWEd6Lwgoxm9E8oLwGZKi4LR9U5AAAAAElFTkSuQmCC>

[image5]: <data:image/png;base64,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>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAYCAYAAAAoG9cuAAAAu0lEQVR4XmNgGDSAA4h50AXRAUFF/EB8Aoh3AjEXmhwcsABxFBCboEsQDVSguBiIjYGYEVWagSEIiGug2AuI7wKxJrICRSDuB2JWKLYB4pcMENPgAN276UB8FYhFkMSIUwQDIIeC8FIgXsMACQoMANIJwiBTQKZhBSAHg/B7KI0VgHTjdQ/IfpA7QBjkJpSAXAjEuQyQsHoExRHICkDgExB3AvFqIO6BYlCAogCiFFkBcQgQqzEgwolGAADSpx1WhwWVqgAAAABJRU5ErkJggg==>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACsAAAAYCAYAAABjswTDAAABuElEQVR4Xu3VPSiFURgH8EfIZ4lkYfAVsSgfA0msyiKDlFmKDAaURVlEyWq5GUw+RqUMRlmUsiiFlFiUwWLx/zvPeb335N77fnTLzf3XL9c95733ec953nNF8sknbUqh0n0ziymDZTiDc6hVgZIzxVbBBZxCuTOWrRSIKe4YDqFIZQwnTUGvO5AhFbCi+DpsWOwNLLkD2QjbZl1FaaE+eIVBd+C3tKpF6BGzNWESt9gZuId6Md9NnbAgTv+Ow6oahTvo8E8IkDjFsrB9Mf1aArNqDo7ELOB3mmAbihW34UXM6oZJnGJtv3KxWGC3GoZPmLQT3WOK28EL0x0djbADuz4JuFZ87R/bhDpemCLs1w+4hRH5aQOG9XnJqWJt7ATbO4HOOV/itAEX6AGm4QpOVMrPsb8aXFVeHDZRi3UXiKv8pPjctMCQN1vDB4ve9G/YRC3W/TEYg2fVLOaB69cxL1zNIP2aKlGL7RKziragBrhU7PU1cVqS/3AbiFtimztMohZbCNWS/J32GK3xv78H82LO2kflnWkhwxtuV1FuNmPeYQMOYEvxjv5kcqrYAZiANkk+iPP5N/kCZKFfcAH6EWcAAAAASUVORK5CYII=>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAXCAYAAAAC9s/ZAAAA7UlEQVR4Xu3SP6uBURwH8KNLUYoiJQZZZZCMNkYG5RUYbIZbt9vdKV4BCWXxOozegNFg8BJYFL6/zpfOczzxxKb7rc9yvuc5nT+PUh+RGAxgbGkZc4LwY/V9iEr5BQlYwJFqEJaS8UEWVvQHSaW/veUXDlQyC6YMXZIF7/L2Ag04kxzBTETpc6fJNRU40bfVdaBpjd2lCHvqGeM5mEDIGHON3OqW5hwLwAgK10mPEoc1LZV+xrrSx3G9NDvywZJkEdn6TOkfzXNk62IHU6g66+eRyxPylEPwO+vnadMGMs7KW1KUtwuveXuB/7yQC2UVL9IuN3VLAAAAAElFTkSuQmCC>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAWCAYAAADTlvzyAAABOUlEQVR4Xu3TTytEURjH8UcoovxdUJNQtixEkjcwC8xqxsqCnZVSlJWd7NjYWMtSQiQLS1nZ8AJkw9Ir8P11njvOndHMKAvl/urT3NM50/Pcc841y5Ily79MK7ZxhgfkXCducI328upfSAFLmMSL/0oTNi000VNebdaMWXeIC2xhDKVoXa+ranYRfdjBPbqcMoQDtPh4wMJOrDgVV4bxjAXM4QivTs1XpR9PFjqNoz8v+7OauLL0W8TZw6g/D+LRfVtwCu8WCiTRlupsR3ysZmqdp7Y02Ym6BVXozdKT09iwULgDtxYaaCR1C+pGnuAc627fvs5S83eY93FlZjAejf9ewSTdkTjaVjWgi6HnOGpKF0vfc5KGC9aKPolL7GLCFbFm6YuUxzE+3ClWo/kfR2+vN5C2irks9gleMzlEyW8imAAAAABJRU5ErkJggg==>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAWCAYAAADTlvzyAAABW0lEQVR4Xu3TzytFQRjG8VcoovwslHQt7ISSH0lZW4hSWFnYkA1RlJWd7NhY2VtKiGRxl7LnD7Djn+D7mPecO/coIdk4T326Z+bM3HnvzFyzPHny/MtUYwdnuEenq8cNrlGbjv6FzGABg3jyT6nAloUimtLRZpUYc0e4wDZ6MO9j2jDhGrwvzTRasIs7CwOSQV04RJW32y3sxJLT4koBjxa+S/2TGHHqn/VxaVrxYKHSOONY9GcVcWWlX5HNPnpRxEbUv4xb1EV9NoQXCwsk0ZbqbLu9rWI+O09tqXaiETVRv+ZdZvreF3q2cHZJhrFpYWFVpypVwFdTcJo3UPbGwo08wTnW3YGVzlLvi5jydjaj6IvaOmvNF934D/nzBZNo/xNxtK2arIuh5zgqShdL/2elGSsWjkF0rmv+/K2oah3+HvrdHFatdJF0MU7xmnHs738U/foOV3bz8ihv3FY3pyWsCUsAAAAASUVORK5CYII=>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAXCAYAAADZTWX7AAAAuUlEQVR4XmNgGAU0AYZAvAOK5wPxFiDuBeKFMAVmQHwLSoMwCOgA8XsgTidakTAQnwLiKUDMCMUgYAPEr4DYFMRxAeK/QOwHlYSBIiC+CsQiIE45EL8FYk0kBSxAvIYB4gGwySCT7gKxDJIikLtA7omGCbAC8VQgngPE1VB8HIi/ArExTBEMCAAxDxS3AvFpIBZEUQEFnFAMCtBJaHJwQFARKAhAPgJhUJCcAeJkFBVYAMjrbOiCOAEA0jshpu3TzyQAAAAASUVORK5CYII=>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAXCAYAAAAC9s/ZAAAA/klEQVR4Xu3RoWtCQRwH8N9AwcGUTYQxNFhEBtv+Am2CaQa3IBjNZqPBpEmM9rFitSzIQ6N5UdgWDIOxNpgL+j3u+3x3t2eyiV/4INz37ng/T+TgUqPhDj3K+wfcnFMZfqANV5SBDv3BA8+Epip6U8FZ9y97Bw/OrNbI3hcMYAGXzvoNfcMzROxa36h4MBJ7Q1SCP/MDbo1um2v6gid4pAa8QJcS/gE3FfqFewlmzon+5Clluf9f1Oy75k/DG40hZpYqcZiRO7/KBczpFVJ2HcyutJxOpSh6NKUPJ3YtUhf99mHvfyd6rAklzbIk+llWsKYl15RP/jbhlI45rGwA+kg+YVCA3P0AAAAASUVORK5CYII=>

[image13]: <data:image/png;base64,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>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAZCAYAAAAxFw7TAAABRUlEQVR4Xu3UvytGURwG8K/8iGIiUiYDyUgmZJCICWWQ2WaTKKMVKZTNYGJVyugPsDBapGRAKZOU53nPc3vPPe7lvm/H5qlPb+/5vud77j333NfsPzHTKKtwlOMApqFWc35MjbTCCrzCCHR6ZjR+CHVuWrHswRW0hAXkGB6hOyzkhU3YjE3D8KrO4Bbaglpu+uAZFsMCMgfv+iyc6A2n4AM2YF525RIGyz8tli24hl4rP90F4d7xSfM0/JrkHJ7DiWVP4mJP5hZLksxr9sZK6ZIHWA5qSdbM7eGAN7YpS95YKePCCcNBrUku4Aba0+XscHW6gw5vnI225cXcosn4urnXkb7dcrSGs+b27dPD7/fyZu5BUY/mMKMwBqfiX0TVmYQdyToVFYUNeKsTMpQuVx6evX1zf3XUny5Xl3pokCiJ3vDv8wX4V0OXKncE7QAAAABJRU5ErkJggg==>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAYCAYAAAAcYhYyAAABHElEQVR4Xt3UsUvDQBQG8Cd1UNpFWihSQQQXQQcpipNk6CIOpZOLFDcddG1Hp+7i4CBKJ8XVobN/hXQVcXKvW9Xv5b7AJWlojgQK/eC33EsuLy/XisxlDuE+hQ4c0bJ/p5XMmyzCM7xCi9ahDX9wDauwD7fwRiW9OcgGPEi8vS78wJ61Voc7WrDW5YTsLMEA3qFiresmVxRKE8qRtRp8QF/CT9yCXZqaBvzCebTgEp3HSEz7ztFZJM0jiL6eWoFCpOYnl03W6EviQw2ySS8S/yB+dKCZh9qjpKEeiOlQHdsFvXgo5hXGpMf9Gz7FdKbRY34KF3TJdefoT+OJtiO11NGuH2kHquFyunhwQ2di/gGc40kOm2iKNOkMzTj/A2o8YJhvJEQAAAAASUVORK5CYII=>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFgAAAAXCAYAAACPm4iNAAAESElEQVR4Xu2YS6hWVRTHl2jio9Q01DDx+ogUhUzzUSiUZQ/yAZooGA4UUbCRmqE5uAgONDCxwExRSrQGDYIMRBxcEkTKgQjpQAQTETR01iAEcf3ca92zv/2dc+451+uk+/3hB9+39zn78T97r7XPEWmppf+b5hib0oqWmrRU+SAtLNNs5Sfj2aSuN2mEske5oJwwBjVcEfSMhOvwrUth6C/KTKM3q68yUflD2W0UaZJyRnnJKNQq5aTSz+jtmqL8oywxitRH+Ub53ChUy+BG9ajBA5TflNVpRS8Wpt5WJhhlelf53Ria1D0WDfylvJpWmAjm70k4WbyoDFE2GjROzKoqv/dtCU8/1lgJ9VXEveSKFdJ4D+NrMxBxcbmEOdTRAeWsMtlYp3wi+eOjj0tGrofzlCsSBpeKJ/KdMl+CmdeV75V3DBr9sPPqco1UDkpoh/48mY4xbijLrKwrrVXWS8jixyQYTmj7UTlioG+Vf6Ve4ibhdyj3lC0GJu5VflUGdl4Z9Jxyzlic1D0WhR2SfzRbo7xvv+nkloRQwgThP+UNq+9KrAJWLmdHth9xDmE4EPNyV0CiURKM5eGflrDakD+kDQZqUy5KPYMZF+Zul/DgfKcx77+leSH6A4HcOFxmME/HQwAmuDHecX+rqyLaYpWRFDDGV4IniD+V562sTGz3wco05Y5kh312Iv/joyZzYte8YP+rKI6/sXiQ5CpyVqwnMjhWHROKxOq7KtkK8wQLvtWr6lMJucPN2yzZ+HyM9LdD6rWLkR3S6Ad90Bd9pqpkcDzQWOOUNyWsNkzw2OZi9QxLysrEyiLMzLL/HnY89NQRuYC3LDcv/u9lhLeP7XcVuVnpywXzZHewa/DjlaguNjh3Dkz6sjS/ibANyaQwXbkr2RNqMxiIn5vnSkgo+6V4xWAsZvoWXqncN7yM9n6QEJOnWlmeYkN9kpS5CCXtEpKra6fyQFkYlcUiLBAe0rOvhwd2xj5pbNN3JRBGm8TK5bWQGBaLiX6tfKkcVrZKyJTblKPG6M6rRV6TYBQPpCjcUH5Kwr1fSTCbbR2HHvolbj5UPrKyPL2uXFN2KcclPOwbksV0xjzDLzZxIqDdz5JyFyeim8r4pJwTC98myB/pqYnEfNEg0TaJFcCN7Uk5om64ZOdIDBph5XmrlFXfLsUGE074cEIbrAI/BfhJIBYTKTMYkYBpxxMP42RFQZqMXBjiOSAV9+e+LEgYe16btEX+KMwhLYMzPRWDEfGPr0JMHLqrl5Uv0kITfRCjPY4T59iOxNk01jJQQpGflXtSJKLcWNkNkfx/lvAuUPo+wISIS/Ehva48qUxKyl1k4PMSYuciCW9zCxquyMQ3VuJl4YropjgVEat9Rz6pSNLkqKId3SA65Q0JKn1ETsR25WWiTJjPsektyd9uLkJNT5kQiz7L+q0jdt0hKQ4pucKkKka19PQWQUtV9QiOaMO5LcyNmwAAAABJRU5ErkJggg==>

[image17]: <data:image/png;base64,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>

[image18]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAXCAYAAAARIY8tAAABQElEQVR4Xu3UsS9DURQG8CNISAlCtBIhTDYDamCwd2hjMgiDgcEgkZAIicRi5K8witQgBguDWEwSs42/wvflfLe9r9G0afJM70t+yWvu7T2np7c1y5Ily7+kF07gDt5kEgbgER6gv7a7g1RgAxbgS/jcBUfmBUdquz2j5k3dwyXMwXpiR5TUC5TN33AOrzKktSm4hh69LgkP5hgZjq8Ku3r9Z8bgA44lZBW29FyEZwmHh+yZf+qmWYIf8wOJ4Yg4hhnog1vYl8ZMW4uLwEO/zbsInbDjQ/NCs/Bp3gg1S7cMNi7wSt6Yz5IO4Mrq38U8vMOExGH3K3oO68v15WSGI3FY6MmSI2TY7TaMQw42pRDtaTuL8CK81ix0an7TwvqOxE20ndQLMPxbobz5b4cXIIS36EI6GlGrsOiZrCWXUswvkIo2PckLOfwAAAAASUVORK5CYII=>

[image19]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAABFCAYAAAD3qbryAAAKD0lEQVR4Xu3dd6hkZxnH8UeiQWPU2BVrRKNiRMXEsDZWoxKxG0uigugiUYwFY8O6NlQQYwkGoigqEtGAfyxKCKKLih1LsGGBKBZiUFD0jyCW5+s77513zj1nzrl179z9fuDh3pk598zc3T/2t8/bIiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiQpTsh6cNbzs+6fdfOshy1csTF3i3Kve84e3yDriVlnrV0hSZKkyW6R9bmsd0QJWpdlXZ91QXvRBtwv6z1Zz8j6adbts07Lui7ri1k3nl8qSZKkMTfMujTryqybzJ47kPWXrIfXizpulHWbKF25Ljppb8q6R9aFUQIb14LHn5ld07pL1lOzHpd106w7RgmRkiRJihLO6KY9t3mOzlobtLo+lPXfrMd3X4gSxm4WJXgRArm2IgC+pHl8h6xPRwl4d44S3C7J+lIMv7ckSdJx51VRumn3nT0mcNEFuyJK960PQe1IlJA1hPlwf816TPPcy2LetWPo9Tuxfp4c1zMk2+3CSZIkHbc+lvW9rFvOHtPZoru22flrFR2738c81DHESbeNrwRB3vcDsT6YEfTO7zwnSZJ0XCOYfT3KMCaenfXPGJ6/NhWB7bdR5qPhaVlPmn1PKPvd7OsQ5sfVzyRJklYMHRkmqFN7GUHogd0n9yA6Xl/IenfWB7N+lfWbKCs7t4Kg9rWsj2e9PeuiKIsVQHAbew9+3i1AJEnaBfyjy55e3WGvrTg3ylDa0PyqvYIgxOpL5mrtdfz93DrrpBifv7YR9b4nd54nsLVdvYo/s0NRrn9elEUJkiRpB7FK8MtZf896QOe1zWIVIft48XUVPCJK96obWPaqOn+NhQg76dSsH2ad3jxHuHtBlMUPZ0QJblsdlpUkSRPQSTkc27en1uFZrQr2NWM15dO7L+xBD40yfPmfrE/GfNXoTmGlKatEOQ3hYJS/1xrs+XNjE187bJIkrRi6P9+N1eu6MJft8tieIcadUocuGcKutRtdQU484L1473bYnLltb44S5CRJ0jbgzEmGr9g76xVRVhmeEqVDw9FEbNFQt3ZgEjnPnRNl/tKjs94Q5R9mVgXyDzdzlxiSq2dQVgS1q2N4ojpDsHRtzosS7u4dZbf9MQQFhi6fGeV3Afd6UdZt60VbcGbWD2L4c0uSJO0oujCfj/nmp4Q05q3VxQacT8kWEXX7hkdGmWz+6yj7cPH8g6KsTGQ4jsUE9dDwP0Q5k7Jim4ij0d/5YTUmoYjDxRlW+1GUn58yrPfCrOdE2WGfz1SfYyf/vr3INnqMEmGVoLlsCwtWTxLo2g5XX90u+o+DkiRJGkQo+2Usbl/xmijBAuxaz273bVh5Xda/Yj60WXfWJ3DRYQPhhD282uOS+DnmVnURiH4e5ZzK6q2xuBnsEELSu6J0+9pjlJhDxeN27tlmj1Gqv0vdg6zPrbKeEqX7uKyeECUkLkN38/vHeX0kJEnSmpOzrorSjfpJ1tuiBJSqb4NUghcBpr2OINYeCl5DDtdWQ4HtcNafYj78ybwoVpK2Z1gOobNFADo969pYPEbptTGfBL+VY5SmBLbtRGAjXB7vJUmSGsz7YoI4gY3gRset7j22kcDWhrGpga1uHUJAI6iB7hdHIrXduTHcuz3snCB6cZQO3VaPUdrtwCZJkrTgtCg72FeEJeaP1X28tjuwtcEMDGmyYz7DmhVdrz/GtPlrIJBdEYsdvgNROmzo+x02gt/lZ7F8dSsLLBjK432W1Tey7l5+RJIkaRpCzLdivgKSwPOprCc3r3fDzmYDW9/u+HX4k5WmYIjzE7E4f41Axme6LhYXMVQ1sNX35x7MU6ub8045RmnZuZcMq9J1nBogtxNdxjrnjX3WCNgbNXYP5jEScEFnktW2u4HP1HZR+XuqcyAlSVKDIMZQ4pEoW3swb4zgw6rJF0dZcMAwKV/pfL0/6x+z5/4cZQuPb2b9e1Z8z3O8xjVc+9ko/zgTeOje1blq1RlR5pe9PMqpAn+L+WpPEMgujbIhLJP2+zw265ooAfGjWY9qXusLiqjHKBFSCZhnLb68hq1Gvhr9q1t3Gn8H9X35fjNdwrF78Pjg7Hv+HNjwdjfwmfg8Fe/b/idAkiTN0I06MUqHiZWhOxlKWLnJiszzui9E+RzMP7trDM9fIzgNBTZwD34HvrZOjeXHKBEmCZlDE90JsW2ncDeNha0pxu5hYJMkSQvYZoO5Zt1QVdHFY+ize3YpAYs5aZsdliTs0cXrO0aJDh+dtr45agyjXhkl9B0LDBXXhRR9YWuKsXvwuC682O3AxmercxoNbJIk7REEtQ9HGcJs0X2j8/btrOuzXhllb7PqIVEWR9RFBZtBMCAQME+qvQ/vTVjodti45vWx2AXabW2I6QtbU4zdg8f1d9ztwPbO2VcY2CRJ2kOYO8actLp1CAhydLP4B5vi+7YLx7DlUFduq3ivvnMv6fa9N3bufacYC1vgz4YOIoGXTlr3SK+xe4wFNu7JvbmuBl32s+M9t8LAJknSHkcIGtvx/1hjkQJz+46lsbA15UivsXssC2zMCaQjenbWL6K8Bx3KH8fivnebYWCTJEn7wrKwNfVIr2X3wLLAdijK3L5zYnFvPB5/JdavvCWEc0YrZ7WyrQqP+Zx9DGySJGnl0d17XwyHrcMxfqTX2D1wIOahrxvYCGRsq3JJLG56zHsStio6phdlXR6lC0dgfGnW0Vg8LqzF0DifzcAmSZJW2lB3jM7V1CO9hu5RLeuw4U5R9ri7oHmOjZXPn31PWOM8VjYrJiBWDJceifLzfeywSZKkfWEobG3kSK+he1RjgY0hUTZCPnP2mI4bnbG61QlbtTCPjvluLYJYu21Hl4FNkiTtC0Nhqw5/LjvSqxq6RzUlsF0b85/jRIh6PWHraGxuY2EDmyRJ2heWha2xI72qZffAWGAjUDE3jeHNV2ddHPMVvlx/TSzf4oOtQJgL191Dz8AmSZL2hbGwRWdt7EivsXuMBbbqlFm1uP7qmA+Xtjjui6FbAtnZYWCTJEn7FCst69YZfWGrYv5a35FeGLsHj+tKzmWBrQ/z2ei+Xdh5nu4fm+0SKJ+Vda/Fl/+PoMZnq0HOwCZJklYSAat2oPrC1tiRXhi7B48Pzr7faGADq1OvirIA4kCUIVo6fQSx+0T5fOeuXT3HZ6qdPRjYJEnSSmrD1qFYH7bGjvTC2D3awMbPH157ZboToqwS7b4/oY2FERyX1Tck2ga2t4SBTZIkrSAm99egc2KsD2NTjN2DxzwPrtvOI8O41xujLEpg+LTVfa+T4tgfBSZJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkiRJkqSV8z89ytJGXFO35gAAAABJRU5ErkJggg==>