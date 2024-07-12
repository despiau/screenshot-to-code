from dotenv import load_dotenv
import os

load_dotenv()

from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from routes import screenshot, generate_code, home, evals
import requests

# Obtener la clave de acceso de ScreenshotOne
SCREENSHOTONE_API_KEY = os.getenv("SCREENSHOTONE_API_KEY")

# FastAPI app
app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add routes
app.include_router(generate_code.router)
app.include_router(screenshot.router)
app.include_router(home.router)
app.include_router(evals.router)

# Función para tomar una captura de pantalla
def take_screenshot(url):
    api_url = f"https://api.screenshotone.com/take?url={url}&access_key={SCREENSHOTONE_API_KEY}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Error taking screenshot: {response.status_code} - {response.text}")

@app.post("/screenshot")
async def screenshot_endpoint(request: Request):
    data = await request.json()
    url = data.get("url")
    if not url:
        raise HTTPException(status_code=400, detail="URL is required")
    
    try:
        screenshot = take_screenshot(url)
        return Response(content=screenshot, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
