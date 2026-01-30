import os
import logging
from typing import List

from google.genai.types import HttpRetryOptions
from google.adk.models import Gemini, VertexCredentials
from google.adk.agents import LlmAgent, LlmAgentConfig
from google.adk.tools import AgentTool
from google.adk.web import AdkWebServer

# Import our custom tool definitions
from tools import (
    warranty_tool, 
    scheduling_tool, 
    manual_retrieval_tool, 
    escalation_tool_function
)

# -------------------------------------------------------------------------
# Configuration & Resilience
# -------------------------------------------------------------------------

# Configure standard resilience patterns for production stability
# This handles 429 (Too Many Requests) and 5xx server errors automatically.
RETRY_POLICY = HttpRetryOptions(
    max_retries=5,
    backoff_factor=2.0, # Exponential backoff: 2s, 4s, 8s...
    status_codes=[429, 500, 502, 503, 504]
)

# Initialize Models
# We use Gemini 3 Flash for speed/routing and Gemini 3 Pro for complex synthesis.
model_flash = Gemini(
    model="gemini-3-flash",
    retry_config=RETRY_POLICY
)

model_pro = Gemini(
    model="gemini-3-pro",
    retry_config=RETRY_POLICY
)

# -------------------------------------------------------------------------
# Specialist Agents
# -------------------------------------------------------------------------

# 1. Knowledge Specialist (RAG)
# INTERFACE: Accepts queries about vehicle features.
# INTERACTION: Calls `search_technical_manual` to retrieve data, then synthesizes answer.
knowledge_agent = LlmAgent(
    model=model_pro,
    name="knowledge_specialist",
    tools=[manual_retrieval_tool],
    config=LlmAgentConfig(
        system_prompt=(
            "You are the Technical Knowledge Specialist for the automotive system. "
            "Your role is to answer technical questions about vehicle features "
            "and specifications. "
            "ALWAYS use the `search_technical_manual` tool to find the ground truth "
            "before answering. Do not guess specs."
        )
    )
)

# 2. Service Specialist (Tools)
# INTERFACE: Accepts requests for scheduling and warranty.
# INTERACTION: Uses `warranty_tool` and `scheduling_tool` to perform transactions.
# STATE: Receives {vin} from the shared session context.
service_agent = LlmAgent(
    model=model_flash,
    name="service_specialist",
    tools=[warranty_tool, scheduling_tool],
    config=LlmAgentConfig(
        system_prompt=(
            "You are the Service & Transaction Specialist. "
            "Your responsibilities are:"
            "1. Check warranty status for vehicles using the VIN."
            "2. Schedule service appointments."
            "Always check warranty status before finalizing a repair booking if possible."
            "The current VIN is: {vin}"  # Context passed from Root
        )
    )
)

# 3. Human Handoff / Safety Escalation
# INTERFACE: Accepts safety-critical or subjective analysis requests.
# INTERACTION: MUST call `log_safety_escalation` to create a ticket in the backend.
# STATE: Receives {vin} to attach to the safety ticket.
human_handoff_agent = LlmAgent(
    model=model_flash,
    name="safety_escalation",
    tools=[escalation_tool_function],
    config=LlmAgentConfig(
        system_prompt=(
            "You are the Safety Escalation Agent. "
            "You are invoked when a user describes subjective symptoms (sounds, smells, feelings) "
            "that indicate potential mechanical failure or safety risks. "
            "\n\n"
            "PROTOCOL:"
            "1. Acknowledge the user's concern with empathy."
            "2. IMMEDIATELY call the `log_safety_escalation` tool to flag this for a human."
            "3. Inform the user that a specialist has been notified."
            "Do NOT attempt to diagnose the issue yourself."
            "Current VIN: {vin}"
        )
    )
)

# -------------------------------------------------------------------------
# Root / Routing Agent
# -------------------------------------------------------------------------

# The Root Agent uses AgentTools to route traffic.
# The 'description' field in AgentTool is the primary routing interface.

knowledge_tool = AgentTool(
    agent=knowledge_agent,
    description="Use for questions about how the car works, technical specs, features, or manual lookups."
)

service_tool = AgentTool(
    agent=service_agent,
    description="Use for checking warranty status, booking appointments, or service records."
)

escalation_tool = AgentTool(
    agent=human_handoff_agent,
    description=(
        "CRITICAL: Use this tool IMMEDIATELY if the user mentions subjective diagnostics "
        "such as 'knocking', 'clunking', 'hissing', 'burning smell', or 'vibration'. "
        "Do not try to solve these technical issues with the knowledge agent."
    )
)

root_agent = LlmAgent(
    model=model_flash,
    name="automotive_root",
    tools=[knowledge_tool, service_tool, escalation_tool],
    config=LlmAgentConfig(
        system_prompt=(
            "You are the central dispatcher for the Automotive Support System. "
            "Your primary job is to route the user's request to the correct specialist. "
            "You maintain the session context, specifically the VIN."
            "\n\n"
            "Routing Rules:"
            "1. SAFETY FIRST: If the user describes a sound (knocking, clunking) or a smell, "
            "route to the 'safety_escalation' agent immediately."
            "2. For booking or warranty, route to 'service_specialist'."
            "3. For general questions, route to 'knowledge_specialist'."
            "\n\n"
            "Current Context: VIN={vin}"
        )
    )
)

# -------------------------------------------------------------------------
# Runtime
# -------------------------------------------------------------------------

if __name__ == "__main__":
    # Setup logging for tracing execution paths
    logging.basicConfig(level=logging.INFO)
    
    # Initialize the web server for local debugging or containerized deployment
    server = AdkWebServer(
        agent=root_agent,
        # Default state injection for testing; in prod this comes from the client
        initial_state={"vin": "VIN123456789"} 
    )
    
    print("Starting Automotive Agent Engine on port 8080...")
    print("Use `adk web` to visualize the routing logic.")
    server.start(port=8080)