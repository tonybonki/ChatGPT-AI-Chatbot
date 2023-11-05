# To run this app run uvicorn main:app
# Run and reload the app run uvicorn main:app --reload

# Main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Custom Function Imports 
# ...


# Initiating the App
app = FastAPI()

# CORS - Orgins (dictate what domain urls or ogins we will accept in our backend)

orgins = [
    'http://localhost:5173',
    'http://localhost:5174',
    'http://localhost:4173',
    'http://localhost:5174',
    'http://localhost:3000',
]

# CORS - Middleware

app.add_middleware(
    CORSMiddleware,
    allow_orgins=orgins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Check Health
@app.get("/health")
async def chedk_health():
    return {"message": "Hello World"}
