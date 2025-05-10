from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from google.adk.agents import Agent
from hsn_validator import (
    load_hsn_data,
    validate_hsn_code,
    validate_hsn_codes,
    validate_hsn_hierarchy
)

app = FastAPI(title="HSN Code Validation Chatbot")

# Load data once at startup
FILE_PATH = "HSN_SAC.xlsx"
hsn_data = load_hsn_data(FILE_PATH)

# Wrap the logic functions with partial to inject hsn_data
from functools import partial
validate_hsn_code_tool = partial(validate_hsn_code, hsn_data=hsn_data)
validate_hsn_codes_tool = partial(validate_hsn_codes, hsn_data=hsn_data)
validate_hsn_hierarchy_tool = partial(validate_hsn_hierarchy, hsn_data=hsn_data)

# Define the ADK agent
agent = Agent(
    name="hsn_validation_agent",
    model="gemini-2.0-flash",
    description="Agent to validate HSN codes and provide descriptions.",
    instruction="You validate HSN codes using master data and give informative responses.",
    tools=[validate_hsn_code_tool, validate_hsn_codes_tool, validate_hsn_hierarchy_tool]
)

# Request model for chat
class ChatRequest(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "HSN Code Validator Agent is running!"}

@app.post("/chat")
def chat(request: ChatRequest):
    message = request.query.strip().lower()
    
    # Intent: single HSN validation
    if "batch" in message or "multiple" in message:
        # Extract comma-separated codes
        codes = [code.strip() for code in message.split() if code.strip().isdigit()]
        return validate_hsn_codes(codes, hsn_data)

    elif any(char.isdigit() for char in message):
        # Assume user wants to validate one code
        code = ''.join(filter(str.isdigit, message))
        return validate_hsn_hierarchy(code, hsn_data)

    return {"error": "Could not understand your intent. Please enter a valid HSN code or say 'validate multiple codes: 0101, 0102'"}

