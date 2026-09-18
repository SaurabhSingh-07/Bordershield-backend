from fastapi import FastAPI
from screening import screen_document
app=FastAPI(title="BorderShield AI Lightweight API",version="1.0.0")
app.post("/api/screen-document")(screen_document)
@app.get("/api/health")
def health(): return {"status":"ok","mode":"lightweight","ocr":"Tesseract wrapper (if binary available)","opencv":True}
