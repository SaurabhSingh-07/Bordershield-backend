def score_risk(r):
    s=0; factors=[]
    if r['ocr']['confidence']<70: s+=10; factors.append('OCR uncertainty')
    if r['validation']['status']!='PASS': s+=10; factors.append('Validation requires review')
    if r['tampering']['score']>=30: s+=30; factors.append('Tampering indicators')
    return {'score':min(100,s),'decision':'GREEN' if s<30 else ('AMBER' if s<60 else 'RED'),'label':'Low Risk' if s<30 else ('Medium Risk' if s<60 else 'High Risk'),'factors':factors,'prototype':True}
