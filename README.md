# Cattle Breed AI

AI-powered web application for identifying **Indian cattle and buffalo breeds from images** using deep learning.

The project combines a **React + Vite frontend** with a **Flask + PyTorch backend** to provide breed predictions along with confidence scores and breed information.

## Features

* Cattle & buffalo breed identification
* Deep-learning based image classification
* Top-3 breed predictions with confidence scores
* Breed information and characteristics
* Image preview before prediction
* JPG, JPEG, PNG and WEBP support
* Upload limit of 10 MB
* GPU support with CPU fallback
* Separate frontend and backend deployment
* API health-check endpoint

## How It Works

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

## Tech Stack

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

## Project Structure

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

## Deployment

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

## Limitations

Prediction quality may vary depending on:

* Image quality
* Lighting
* Camera angle
* Background
* Animal visibility
* Similarity between breeds

The confidence score represents the model's prediction probability and should not be considered a guaranteed identification.

## Future Scope

* [ ] Support more breeds
* [ ] Improve difficult-image recognition
* [ ] Multi-animal detection
* [ ] Explainable AI
* [ ] Breed comparison
* [ ] Prediction history
* [ ] Mobile optimization
* [ ] Multilingual support

## Contributing

Contributions and suggestions are welcome.


---

### Cattle Breed AI

**Computer Vision • Deep Learning • Agriculture • Full-Stack Development**
