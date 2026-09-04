# Cattle Breed AI

The app has two separate deployments:

- **Frontend:** React/Vite, deploy on Vercel.
- **Prediction API:** Flask + PyTorch, deploy on Render. Vercel cannot run this long-lived ML server.

## Why the deployed site showed “Load failed”

The Vercel site was attempting `POST /predict`, but no Flask server exists on that Vercel deployment. The browser therefore had no API to contact. This repository makes that dependency explicit and gives a clear setup error if the URL is missing.

## Run locally

Terminal 1:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r Backend_new/breedai_public_backend/requirements.txt
cd Backend_new/breedai_public_backend
python backend.py
```

Terminal 2:

```bash
npm ci
npm run dev
```

Vite proxies `/predict` to `http://localhost:5000` in development, so no frontend environment variable is required locally.

## Deploy

1. Push this repository to GitHub.
2. Create a Render **Web Service** from the repo. Render detects [`render.yaml`](render.yaml); wait until `https://YOUR-SERVICE.onrender.com/health` returns success.
3. In Render, set `ALLOWED_ORIGINS` to the exact Vercel frontend URL, for example `https://cattle-breed-ai-pi.vercel.app`.
4. Import the same GitHub repo into Vercel. Add the environment variable below for **Production**, then redeploy:

   ```text
   VITE_API_BASE_URL=https://YOUR-SERVICE.onrender.com
   ```

`VITE_API_BASE_URL` must be the Render service URL only—do not append `/predict`.

The classifier returns its closest supported bovine breed prediction; the upload flow does not block images just because they are another species.
