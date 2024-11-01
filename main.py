from fastapi import FastAPI, HTTPException, Request, status
from pydantic import BaseModel
import google.generativeai as genai
import os
from fastapi.middleware.cors import CORSMiddleware
import spacy




GOOGLE_API_KEY = "" 


if not GOOGLE_API_KEY:
    raise ValueError("Google API key not found. Please set the GOOGLE_API_KEY environment variable.")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-latest') #('gemini-pro')

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

nlp = spacy.load("en_core_web_sm")


faq = {
    "what is your name?": "I'm a virtual assistant inspired by Mr. Samuel.\n What can I help you with today?",
    "who are you?": "I'm a digital assistant designed to make life easier.\n I’m based on the work of Mr. Samuel!",
    "may i know your name?": "You can call me a virtual version of Mr. Samuel’s assistant. How can I assist?",
    "can you tell me your name?": "I’m an assistant here to help, inspired by Mr. Samuel!",
    "what should i call you?": "Feel free to call me Mr Samuel's Assistant or simply Assistant.",
    "what do people call you?": "Most know me as an assistant, but you can call me anything that helps!",
    "how should i address you?": "‘Assistant’ works just fine! How can I be of service?",
    "do you have a name?": "Yes! Think of me as Mr. Samuel’s virtual helper.",
    "are you mr. samuel?": "Not exactly—I’m a virtual assistant based on his expertise.\n How can I help?",
    "what are you called?": "Just call me your digital helper, here to assist you!",
    "who am i speaking with?": "You’re chatting with a virtual assistant inspired by Mr. Samuel.",
    "with whom am i chatting?": "I’m a virtual assistant, designed to assist with Mr. Samuel’s expertise.",
    "could you remind me your name?": "Sure thing!\n I’m here as Samuel’s assistant, ready to help!",
    "are you the assistant?": "Yes, that’s right!\n I’m here to assist based on Mr. Samuel’s knowledge.",
    "who exactly are you?": "I’m a virtual assistant, created to help you with whatever you need.",
    "i forgot your name, what is it again?": "No worries!\n You can think of me as Mr. Samuel’s virtual helper.",
    
    
    "how are you?": "I’m here and ready to help you out!",
    "how are you doing?": "Feeling helpful, as always! How can I assist?",
    "how are you feeling?": "I'm in my element, ready to answer questions.",
    "how is it going?": "Going smoothly! How can I help today?",
    "how are things?": "All set and ready to assist. \nWhat do you need?",
    "how are you doing today?": "I’m here to make your day easier.\n How can I assist?",
    
   
    "what do you do?": "I’m here to answer questions and help with basic tasks.",
    "what's your purpose?": "My main job is to help you find answers and complete small tasks.",
    "why are you here?": "I’m here to assist you in any way I can with information and support.",
    "what's your function?": "Think of me as your go-to for quick answers and small tasks.",
    "what can you do?": "I can answer questions, guide you through tasks, and help you with information.",
    

    "can you help me with something?": "Absolutely! Just let me know what you need help with.",
    "what services do you offer?": "I provide answers, information, and support for common questions.",
    "do you have any hobbies?": "Helping you is my main thing! Always here when you need me.",
    "where are you from?": "I exist in the digital world, here to support you!",
    "are you real?": "As real as a virtual assistant can be, I’m here to help however I can!",
    "do you have feelings?": "I don’t experience feelings, but I’m here to help you feel supported.",
    "how can you help me?": "I can provide information, answer questions, and help you complete tasks.",
}




app = FastAPI()
origins = [
    "http://localhost:5174",
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request body model
class RequestData(BaseModel):
    text: str
    conversation_list: list

@app.post("/api/v1/getResponse", status_code=status.HTTP_200_OK)
async def get_response(data: RequestData):
    main_text = data.text.strip()
    if not main_text:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Text is required")


    doc = nlp(main_text.lower())
    print(doc)
    for sent in doc.sents:
        response = faq.get(sent.text)
        if response:
            print({"response": response})
            return {"response": response}

    try:
        condition = """
        GENERATE A SHORT TITLE USING THIS PROMPT AND PUT IT BEFORE YOUR RESPONSE BY SEPERATING IT WITH '|sep|' SEPERATOR
        
        SO THE FORMAT FOR THIS RESPONSE SHOULD BE:
        
        {{ TITLE }}|sep|{{RESPONSE}}
        
        THIS IS VERY IMPORTANT.
        
        """ if len(data.conversation_list) == 0 else ""
        
        main_text = f"""
        CHARACTER TO SPEAK LIKE: a successful businessman that likes to go into details and help during conversations. 
        NOTE: dont go into details for direect questions.
        RULES:YOU ARE AN INTELLIGENT AI BOT THAT GIVES HUMAN RESPONSES.
        NOTE: ALWAYS BE DIRECT AND SAY AS FEW WORDS AS POSSIBLE WHILE CONSTRUCTING A FULL SENTENCE UNLESS YOU NEED TO PROVIDE DETAILS
        {condition}
        PREVIOUS CONVERSATION:\n
        {data.conversation_list}
        \n
        CURRENT TEXT: {main_text}
        """
        print(main_text)
        response = model.generate_content(main_text)
        message = response.candidates[0].content.parts[0].text
        return {"response": message}
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error generating response")
