import cv2, numpy as np
def analyze_tampering(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY); edges=cv2.Canny(gray,100,200); density=float(np.mean(edges>0))
    score=min(100,int(density*300))
    return {'score':score,'status':'SUSPICIOUS' if score>=30 else 'NORMAL','findings':['Edge-density heuristic used','Prototype indicator; not proof of forgery']}
