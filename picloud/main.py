import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import database
from routers import files

app = FastAPI(title="PiCloud")

# Create storage directory if it doesn't exist
STORAGE_DIR = "/mnt/picloud_storage"
if not os.path.exists(STORAGE_DIR):
    try:
        os.makedirs(STORAGE_DIR, exist_ok=True)
    except PermissionError:
        # Fallback for local development
        STORAGE_DIR = "./picloud_storage"
        os.makedirs(STORAGE_DIR, exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(files.router, prefix="/api/files", tags=["files"])

@app.on_event("startup")
async def startup_event():
    await database.init_db()

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html") as f:
        return f.read()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
