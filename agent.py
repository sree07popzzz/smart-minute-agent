import os
import json
import sys
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List

# 1. Load your .env file
load_dotenv()

# 2. Force resolve the Google GenAI SDK
try:
    import google.genai
    from google.genai import types
except ImportError:
    sys.path.append('/home/user/.local/lib/python3.10/site-packages')
    import google.genai
    from google.genai import types

# 3. Define Data Structures
class TaskAllocation(BaseModel):
    owner: str = Field(description="Name or role of the person responsible for the task.")
    task: str = Field(description="Detailed description of the actionable task.")
    deadline: str = Field(description="Extracted deadline, milestone, or timeframe.")

class MeetingAssetsSchema(BaseModel):
    summary: str = Field(description="Concise, high-impact executive summary.")
    tasks: List[TaskAllocation] = Field(description="List of action items.")
    email: str = Field(description="Professional broadcast-ready email draft.")

# 4. Core Backend Engine
def process_transcript(raw_transcript: str) -> dict:
    # Initialize client; ensures GOOGLE_API_KEY is read from .env
    client = google.genai.Client()
    
    # IMPORTANT: Use a currently supported model
    MODEL_ID = 'gemini-3.5-flash' 
    
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=f"Analyze and process the following text log into the structural layout schemas:\n\n{raw_transcript}",
            config=types.GenerateContentConfig(
                system_instruction="You are an expert Administrative Agent.",
                response_mime_type="application/json",
                response_schema=MeetingAssetsSchema,
                temperature=0.1
            ),
        )
        return json.loads(response.text)
        
    except Exception as error:
        # This will print the ACTUAL error to your terminal so you can fix it
        print(f"CRITICAL ERROR in agent.py: {type(error).__name__}: {error}", file=sys.stderr)
        return {
            "summary": "Error: Could not parse meeting transcript.",
            "tasks": [{"owner": "System", "task": f"Error: {str(error)}", "deadline": "Check logs"}],
            "email": "Pipeline failed. Check terminal for error details."
        }
