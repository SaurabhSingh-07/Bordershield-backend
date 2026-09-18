import uuid, cv2, numpy as np
from fastapi import UploadFile, File, HTTPException
from ocr import extract_text
from tampering import analyze_tampering
from validation import validate
from risk import score_risk
async def screen_document(document: UploadFile=File(...), face: UploadFile|None=File(None)):
    raw=await document.read()
    if not raw: raise HTTPException(400,"Empty document image")
    arr=np.frombuffer(raw,np.uint8); img=cv2.imdecode(arr,cv2.IMREAD_COLOR)
    if img is None: raise HTTPException(400,"Unsupported or invalid image")
    ocr=extract_text(img); validation=validate(ocr["text"]); tampering=analyze_tampering(img)
    result={"case_id":"CASE-"+uuid.uuid4().hex[:10].upper(),"document":{"type":"Passport/ID (prototype)","filename":document.filename},"ocr":ocr,"validation":validation,"tampering":tampering,"face":{"status":"NOT_PROVIDED","similarity":None}}
    result["risk"]=score_risk(result); return result
