import os
import aiofiles
from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from fastapi.responses import FileResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from typing import List
import database

router = APIRouter()
security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Get storage directory from main or environment
STORAGE_DIR = "/mnt/picloud_storage"
if not os.path.exists(STORAGE_DIR):
    STORAGE_DIR = "./picloud_storage"

async def get_current_user(credentials: HTTPBasicCredentials = Depends(security), db=Depends(database.get_db)):
    cursor = await db.execute("SELECT username, password_hash FROM users WHERE username = ?", (credentials.username,))
    user = await cursor.fetchone()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    hashed_password = user[1]
    if not pwd_context.verify(credentials.password, hashed_password):
            raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username

def is_safe_path(basedir, path):
    return os.path.commonpath([os.path.abspath(basedir), os.path.abspath(path)]) == os.path.abspath(basedir)

@router.get("/")
async def list_files(username: str = Depends(get_current_user)):
    try:
        if not os.path.exists(STORAGE_DIR):
            os.makedirs(STORAGE_DIR, exist_ok=True)
        files = os.listdir(STORAGE_DIR)

        file_list = []
        for f in files:
            file_path = os.path.join(STORAGE_DIR, f)
            if os.path.isfile(file_path):
                stat = os.stat(file_path)
                file_list.append({
                    "name": f,
                    "size": stat.st_size,
                    "modified": stat.st_mtime
                })
        return {"files": file_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), username: str = Depends(get_current_user)):
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR, exist_ok=True)

    file_path = os.path.join(STORAGE_DIR, file.filename)
    try:
        # Prevent path traversal
        if not is_safe_path(STORAGE_DIR, file_path):
            raise HTTPException(status_code=400, detail="Invalid file path")

        async with aiofiles.open(file_path, 'wb') as out_file:
            while content := await file.read(1024 * 1024):  # Read in 1MB chunks
                await out_file.write(content)

        return {"filename": file.filename, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/download/{filename}")
async def download_file(filename: str, username: str = Depends(get_current_user)):
    file_path = os.path.join(STORAGE_DIR, filename)

    # Prevent path traversal
    if not is_safe_path(STORAGE_DIR, file_path):
        raise HTTPException(status_code=400, detail="Invalid file path")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(path=file_path, filename=filename)

@router.delete("/{filename}")
async def delete_file(filename: str, username: str = Depends(get_current_user)):
    file_path = os.path.join(STORAGE_DIR, filename)

    # Prevent path traversal
    if not is_safe_path(STORAGE_DIR, file_path):
        raise HTTPException(status_code=400, detail="Invalid file path")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    try:
        os.remove(file_path)
        return {"status": "success", "message": f"Deleted {filename}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
