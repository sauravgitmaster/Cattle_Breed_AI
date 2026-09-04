BREEDAI PUBLIC BACKEND
======================

Files:
- backend.py                 Flask API
- tnbc6_FINAL_FIXED.py       ConvNeXt model + breed profiles
- requirements.txt           deployment dependencies
- render.yaml                Render configuration

API:
GET  /health
POST /predict   multipart/form-data field name: image

IMPORTANT:
The frontend must call the deployed /predict URL instead of:
http://localhost:5000/predict

Example after Render deployment:
https://YOUR-SERVICE.onrender.com/predict

The API returns:
{
  "success": true,
  "predictions": [...],
  "profile": {
    "origin": "...",
    "type": "...",
    "use": "...",
    "features": "..."
  }
}
