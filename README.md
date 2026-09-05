# 🐄 Cattle Breed AI

AI-powered web application for identifying **Indian cattle and buffalo breeds from images** using deep learning.

The project combines a **React + Vite frontend** with a **Flask + PyTorch backend** to provide breed predictions along with confidence scores and breed information.

## ✨ Features

* 🐄 Cattle & buffalo breed identification
* 🤖 Deep-learning based image classification
* 📊 Top-3 breed predictions with confidence scores
* 🧬 Breed information and characteristics
* 🖼️ Image preview before prediction
* 📁 JPG, JPEG, PNG and WEBP support
* 📏 Upload limit of 10 MB
* ⚡ GPU support with CPU fallback
* 🌐 Separate frontend and backend deployment
* ❤️ API health-check endpoint

## 🧠 How It Works

```text
Animal Image
     ↓
React Frontend
     ↓
Flask API
     ↓
Image Preprocessing
     ↓
PyTorch Model
     ↓
Class Probabilities
     ↓
Top-3 Predictions
     ↓
Breed Information
```

## 🏗️ Tech Stack

| Technology       | Purpose             |
| ---------------- | ------------------- |
| React            | Frontend            |
| Vite             | Frontend tooling    |
| JavaScript / JSX | UI logic            |
| CSS              | Styling             |
| Flask            | Backend API         |
| PyTorch          | Deep learning       |
| Pillow           | Image processing    |
| Gunicorn         | Production server   |
| Vercel           | Frontend deployment |
| Render           | Backend deployment  |

## 📂 Project Structure

```text
cattle-breed-ai-fixed/
│
├── Backend_new/
│   └── breedai_public_backend/
│       ├── backend.py
│       ├── tnbc6_FINAL_FIXED.py
│       ├── requirements.txt
│       └── render.yaml
│
├── src/
│   ├── App.jsx
│   ├── App.css
│   ├── index.css
│   └── main.jsx
│
├── public/
├── app.py
├── tnbc3.py
├── tnbc6_FINAL_FIXED.py
├── package.json
├── vite.config.js
├── render.yaml
├── requirements.txt
└── README.md
```

## 🚀 Run Locally

### Clone the repository

```bash
git clone https://github.com/sauravgitmaster/cattle-breed-ai-fixed.git
cd cattle-breed-ai-fixed
```

### Backend

Create and activate a virtual environment:

```bash
python -m venv .venv
```

**Windows:**

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r Backend_new/breedai_public_backend/requirements.txt
```

Start the API:

```bash
cd Backend_new/breedai_public_backend
python backend.py
```

### Frontend

Open another terminal:

```bash
npm ci
npm run dev
```

## 🔌 API

### `POST /predict`

Accepts an animal image and returns the predicted breeds.

Request:

```text
multipart/form-data
image=<image>
```

Example response:

```json
{
  "success": true,
  "predictions": [],
  "profile": {}
}
```

### `GET /health`

Checks whether the backend is running.

```json
{
  "success": true,
  "status": "healthy"
}
```

## ⚙️ Environment Variables

The frontend uses:

```text
VITE_API_BASE_URL
```

Example:

```text
VITE_API_BASE_URL=https://your-backend.onrender.com
```

The backend supports:

```text
ALLOWED_ORIGINS
```

for controlling allowed frontend origins.

## 🌐 Deployment

The project uses a split deployment architecture:

```text
┌───────────────┐
│    Vercel     │
│ React + Vite  │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│    Render     │
│ Flask + PyTorch│
└───────────────┘
```

## ⚠️ Limitations

Prediction quality may vary depending on:

* Image quality
* Lighting
* Camera angle
* Background
* Animal visibility
* Similarity between breeds

The confidence score represents the model's prediction probability and should not be considered a guaranteed identification.

## 🔮 Future Scope

* [ ] Support more breeds
* [ ] Improve difficult-image recognition
* [ ] Multi-animal detection
* [ ] Explainable AI
* [ ] Breed comparison
* [ ] Prediction history
* [ ] Mobile optimization
* [ ] Multilingual support

## 🤝 Contributing

Contributions and suggestions are welcome.


---

### 🐄 Cattle Breed AI

**Computer Vision • Deep Learning • Agriculture • Full-Stack Development**
