# BorderShield AI - Lightweight Vercel/FastAPI prototype

This build removes EasyOCR/PyTorch and uses Tesseract + OpenCV/Pillow for a much smaller deployment footprint. It is a prototype and does not provide guaranteed forgery detection or legally binding identity decisions.

Endpoint: POST /api/screen-document (multipart field: document; optional face is accepted but not used in this lightweight build).

For Vercel, use a Python runtime configuration appropriate to your account; for Docker-capable hosting, use the included Dockerfile. Note: OpenCV and Tesseract still make this unsuitable for strict serverless package limits if dependencies are bundled directly.
