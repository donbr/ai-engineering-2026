import datetime
import random
from typing import Dict, Any, Optional
from google.adk.tools import FunctionTool

# -------------------------------------------------------------------------
# Mock Database / API Layers
# -------------------------------------------------------------------------

WARRANTY_DB = {
    "VIN123456789": {"status": "Active", "expires": "2028-01-01", "coverage": "Powertrain Plus"},
    "VIN987654321": {"status": "Expired", "expires": "2024-12-31", "coverage": "Standard"},
}

SCHEDULE_DB = {}

# -------------------------------------------------------------------------
# Tool Implementations
# -------------------------------------------------------------------------

def check_warranty_status(vin: str) -> Dict[str, Any]:
    """
    Retrieves the current warranty coverage and status for a specific Vehicle Identification Number (VIN).

    Use this tool BEFORE attempting to schedule paid services to determine if the repair
    might be covered.

    Args:
        vin: The 17-character Vehicle Identification Number.

    Returns:
        A dictionary containing 'status', 'expiration_date', and 'coverage_level'.
    """
    # Simulate API latency or lookups here
    record = WARRANTY_DB.get(vin)
    if not record:
        return {"error": "VIN not found", "vin": vin}
    
    return {
        "vin": vin,
        "warranty_status": record["status"],
        "coverage_plan": record["coverage"],
        "expiration_date": record["expires"]
    }

def schedule_service_appointment(vin: str, service_type: str, preferred_date: str) -> Dict[str, Any]:
    """
    Schedules a service appointment for a vehicle.

    Args:
        vin: The 17-character Vehicle Identification Number.
        service_type: The type of service required (e.g., 'Oil Change', 'Diagnostic', 'Tire Rotation').
        preferred_date: The customer's preferred date in YYYY-MM-DD format.

    Returns:
        A confirmation object with the booking ID and confirmed slot.
    """
    # Basic validation logic mock
    try:
        datetime.date.fromisoformat(preferred_date)
    except ValueError:
        return {"error": "Invalid date format. Please use YYYY-MM-DD."}

    booking_id = f"BK-{vin[-4:]}-{datetime.datetime.now().strftime('%H%M%S')}"
    
    # Store in mock DB
    SCHEDULE_DB[booking_id] = {
        "vin": vin,
        "service": service_type,
        "date": preferred_date,
        "status": "Confirmed"
    }

    return {
        "booking_id": booking_id,
        "status": "Confirmed",
        "service_type": service_type,
        "scheduled_date": preferred_date,
        "message": f"Appointment confirmed for {service_type} on {preferred_date}."
    }

def search_technical_manual(query: str, car_model: str = "Generic Model") -> str:
    """
    Performs a semantic search (RAG) against the vehicle's technical owner's manual.
    
    Use this tool to answer 'how-to' questions or questions about specific vehicle features,
    warning lights, or specifications.

    Args:
        query: The user's technical question.
        car_model: The model of the car (optional context).

    Returns:
        A string containing relevant excerpts from the manual.
    """
    # Mock RAG response
    return (
        f"[Result from Manual for {car_model}]:\n"
        f"Regarding '{query}': The recommended tire pressure for this vehicle is 32 PSI cold. "
        "The 'Check Engine' light flashing indicates a potential misfire condition. "
        "Immediate service is recommended to prevent catalytic converter damage."
    )

def log_safety_escalation(vin: str, risk_assessment: str, customer_description: str) -> Dict[str, str]:
    """
    Logs a high-priority ticket for Human-in-the-Loop (HITL) review.
    
    This tool MUST be called when subjective safety issues (knocking sounds, burning smells)
    are detected.

    Args:
        vin: The Vehicle Identification Number.
        risk_assessment: A brief summary of why this was escalated (e.g., 'Engine Knock detected').
        customer_description: The verbatim description provided by the user.

    Returns:
        A ticket confirmation dictionary.
    """
    ticket_id = f"SAFE-{random.randint(1000, 9999)}"
    print(f"!!! SAFETY ESCALATION TRIGGERED: {ticket_id} !!!")
    return {
        "ticket_id": ticket_id,
        "status": "ESCALATED_TO_HUMAN",
        "priority": "P0_SAFETY",
        "message": "A safety specialist has been notified and will review the audio logs."
    }

# -------------------------------------------------------------------------
# ADK Tool Wrapping
# -------------------------------------------------------------------------

# The ADK uses these wrappers to generate the function schemas for the LLM.
warranty_tool = FunctionTool(check_warranty_status)
scheduling_tool = FunctionTool(schedule_service_appointment)
manual_retrieval_tool = FunctionTool(search_technical_manual)
escalation_tool_function = FunctionTool(log_safety_escalation)