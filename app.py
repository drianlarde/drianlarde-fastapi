import shutil
import uvicorn
from typing import List
from fastapi import FastAPI, UploadFile, File

from db import database, metadata, engine
from pdf_service.api import pdf

app = FastAPI()

metadata.create_all(engine)
app.state.database = database

@app.get("/")
async def root():
    return [{"message": "Hello World!"}]

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    with open(f'{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

@app.post("/img")
async def create_upload_file_image(files: List[UploadFile] = File(...)):
    for img in files:
        with open(f'{img.filename}', 'wb') as buffer:
            shutil.copyfileobj(img.file, buffer)

@app.post("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()

@app.post("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

