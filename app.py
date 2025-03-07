from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# Simulated ticketing system (replace with real API integration)
TICKETS_DB = {}

class UserMessage(BaseModel):
    user_id: str
    message: str

class TicketResponse(BaseModel):
    ticket_id: str
    message: str

def create_ticket(user_id: str, issue: str):
    """Simulate ticket creation"""
    ticket_id = f"TICKET-{random.randint(1000, 9999)}"
    TICKETS_DB[ticket_id] = {"user_id": user_id, "issue": issue, "status": "Open"}
    return ticket_id

@app.post("/chatbot", response_model=TicketResponse)
def chatbot_interact(user_message: UserMessage):
    """Chatbot receives message and creates a ticket"""
    issue_description = user_message.message  # Simple extraction (NLP can be added)
    ticket_id = create_ticket(user_message.user_id, issue_description)
    
    response_message = f"Your ticket has been created successfully! Ticket ID: {ticket_id}"
    return TicketResponse(ticket_id=ticket_id, message=response_message)

@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: str):
    """Retrieve ticket details"""
    if ticket_id in TICKETS_DB:
        return {"ticket_id": ticket_id, "details": TICKETS_DB[ticket_id]}
    return {"error": "Ticket not found"}
