import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load key-value pairs from the local .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("System Error: GEMINI_API_KEY is missing from the local environment (.env) file.")

# Bind API token to the Google GenAI SDK wrapper
genai.configure(api_key=api_key)

def process_transcript(transcript_text: str) -> dict:
    """
    Ingests raw transcript strings, passes them to gemini-1.5-flash with rigorous 
    structural framing, and splits the response into programmatic data segments.
    """
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Rigorous formatting instructions to ensure the model output is parseable by code
    prompt = f"""
    You are an autonomous administrative AI agent. Your task is to process raw conversation logs.
    
    Raw Log:
    \"\"\"{transcript_text}\"\"\"
    
    Execute compliance checks and map outputs into exactly three sections. 
    Separate each section using the literal delimiter sequence: ---SPLIT---
    Do not add text, intros, or markdown headers like '# Section 1' outside the split tags.

    [SECTION 1]: Structured bulleted points containing executive meeting minutes, key technical alignments, and strategic decisions.
    ---SPLIT---
    [SECTION 2]: A clear Markdown data table representing action items. Columns must be exactly: | Owner | Action Item | Deadline |
    ---SPLIT---
    [SECTION 3]: A professional corporate follow-up email ready for distribution to stakeholders based on the discussion above.
    """
    
    try:
        response = model.generate_content(prompt)
        raw_text = response.text
        
        # Split string by programmatic delimiter
        segments = raw_text.split('---SPLIT---')
        
        # Array protection padding loop
        while len(segments) < 3:
            segments.append("Processing anomaly: System failed to isolate this structural block.")
            
        return {
            "minutes": segments.strip(),
            "tasks": segments.strip(),
            "email": segments.strip()
        }
        
    except Exception as e:
        return {"error": f"Backend Runtime Exception: {str(e)}"}
