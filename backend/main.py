from dotenv import load_dotenv
import os
import logging
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from routes.screenshot import router as screenshot_router
from routes.generate_code import router as generate_code_router
from routes.home import router as home_router
from routes.evals import router as evals_router
import requests
from typing import Optional

# Load environment variables
load_dotenv()

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get ScreenshotOne API Key
SCREENSHOTONE_API_KEY: Optional[str] = os.getenv("SCREENSHOTONE_API_KEY")

# Create a custom temporary directory
TEMP_DIR = os.path.join(os.path.dirname(__file__), 'tmp')
os.makedirs(TEMP_DIR, exist_ok=True)
os.environ['TEMP'] = TEMP_DIR
os.environ['TMP'] = TEMP_DIR

# FastAPI app
app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this according to your security needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add routes
app.include_router(generate_code_router)
app.include_router(screenshot_router)
app.include_router(home_router)
app.include_router(evals_router)

# Function to take a screenshot
def take_screenshot(url: str) -> bytes:
    api_url = f"https://api.screenshotone.com/take?url={url}&access_key={SCREENSHOTONE_API_KEY}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Error taking screenshot: {response.status_code} - {response.text}")

@app.post("/api/screenshot")
async def screenshot(request: Request):
    data = await request.json()
    url: Optional[str] = data.get("url")
    if not url:
        raise HTTPException(status_code=400, detail="URL is required")
    
    try:
        screenshot = take_screenshot(url)
        return Response(content=screenshot, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Add other routes if necessary
# app.include_router(other_router)