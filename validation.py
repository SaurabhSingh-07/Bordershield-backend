import re
def validate(text):
    t=text.upper(); checks=[]; missing=[]
    for label,pat in [('Passport number',r'\b[A-Z][A-Z0-9]{7,8}\b'),('Date',r'\b\d{2}[/-]\d{2}[/-]\d{4}\b')]:
        ok=bool(re.search(pat,t)); checks.append({'check':label,'status':'PASS' if ok else 'REVIEW'}); 
        if not ok: missing.append(label)
    mrz='<' in t and len(re.findall(r'[A-Z0-9<]{20,}',t))>=1
    checks.append({'check':'MRZ indicator','status':'PASS' if mrz else 'REVIEW'})
    return {'status':'PASS' if not missing and mrz else 'REVIEW','checks':checks,'missing_fields':missing}
