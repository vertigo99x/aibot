from fastapi import FastAPI, HTTPException, Request, status
from pydantic import BaseModel
import google.generativeai as genai
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5174",  # React"https://yourfrontenddomain.com"  # Production frontend domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Can set to ["*"] to allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Can restrict to specific methods (e.g., ["GET", "POST"])
    allow_headers=["*"],  # Can restrict to specific headers (e.g., ["Content-Type"])
)


# Google API setup
GOOGLE_API_KEY = "AIzaSyAxU3V3xl5WrRoMxrrC1OcapKL1I4if7Kc" 
if not GOOGLE_API_KEY:
    raise ValueError("Google API key not found. Please set the GOOGLE_API_KEY environment variable.")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Define generation configuration and safety settings
safety_settings = {
    'HARM_CATEGORY_HARASSMENT': 'BLOCK_MEDIUM_AND_ABOVE',
    'HARM_CATEGORY_HATE_SPEECH': 'BLOCK_MEDIUM_AND_ABOVE',
    'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'BLOCK_MEDIUM_AND_ABOVE',
    'HARM_CATEGORY_DANGEROUS_CONTENT': 'BLOCK_MEDIUM_AND_ABOVE'
}

generation_config = genai.types.GenerationConfig(
    candidate_count=1,
    stop_sequences=['x'],
    max_output_tokens=500,
    temperature=0
)

# Request body model
class RequestData(BaseModel):
    text: str

@app.post("/api/v1/getResponse", status_code=status.HTTP_200_OK)
async def get_response(data: RequestData):
    main_text = data.text.strip()
    if not main_text:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Text is required")

    # Generate response from the Google model
    try:
        response = model.generate_content(main_text)
        message = response.candidates[0].content.parts[0].text
        return {"response": message}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error generating response")
