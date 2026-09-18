import cv2
try: import pytesseract
except Exception: pytesseract=None
def extract_text(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); gray=cv2.resize(gray,None,fx=1.5,fy=1.5); gray=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    if pytesseract:
        data=pytesseract.image_to_data(gray,config='--psm 6',output_type=pytesseract.Output.DICT)
        vals=[(t,float(c)) for t,c in zip(data['text'],data['conf']) if t.strip() and float(c)>=0]
        text=' '.join(t for t,_ in vals); conf=round(sum(c for _,c in vals)/len(vals),1) if vals else 0
    else: text=''; conf=0
    return {'text':text,'confidence':conf,'engine':'Tesseract (lightweight)'}
