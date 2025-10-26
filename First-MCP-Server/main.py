"""
Leave Management System MCP example.

Run:
    uv run server leave_mcp stdio
"""

from datetime import date
from typing import List, Dict
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("LeaveManagement")

# In-memory leave store (replace with DB in real-world)
leave_requests: List[Dict] = []


# Tool: Submit leave request
@mcp.tool()
def request_leave(employee: str, start_date: str, end_date: str, reason: str) -> str:
    """Submit a leave request for an employee"""
    request = {
        "employee": employee,
        "start_date": start_date,
        "end_date": end_date,
        "reason": reason,
        "status": "Pending",
        "submitted_on": str(date.today())
    }
    leave_requests.append(request)
    return f"Leave request submitted for {employee} ({start_date} → {end_date})"


# Tool: Approve a leave request
@mcp.tool()
def approve_leave(index: int) -> str:
    """Approve a leave request by index"""
    try:
        leave_requests[index]["status"] = "Approved"
        return f"Leave request {index} approved ✅"
    except IndexError:
        return "Invalid leave request index ❌"


# Tool: Reject a leave request
@mcp.tool()
def reject_leave(index: int, reason: str) -> str:
    """Reject a leave request by index"""
    try:
        leave_requests[index]["status"] = f"Rejected: {reason}"
        return f"Leave request {index} rejected ❌ ({reason})"
    except IndexError:
        return "Invalid leave request index ❌"


# Resource: List leave requests
@mcp.resource("leave://requests")
def list_requests() -> List[Dict]:
    """View all leave requests"""
    return leave_requests


# Prompt: Generate leave policy explanation
@mcp.prompt()
def leave_policy(policy_type: str = "general") -> str:
    """Generate explanation for leave policies"""
    policies = {
        "general": "Employees may request annual, sick, or emergency leave. Requests must be approved by a manager.",
        "annual": "Annual leave must be requested at least 2 weeks in advance.",
        "sick": "Sick leave requests require a medical certificate if longer than 2 days.",
        "emergency": "Emergency leave should be reported immediately to HR and direct supervisor.",
    }
    return policies.get(policy_type, policies["general"])
