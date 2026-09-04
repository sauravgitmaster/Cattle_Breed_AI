import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image

from tnbc3 import predict_breed

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

allowed_origins = [
    origin.strip()
    for origin in os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
    if origin.strip()
]
CORS(app, resources={r"/predict": {"origins": allowed_origins}})


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "Cattle Breed AI API is running"
    })


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:
        return jsonify({
            "success": False,
            "error": "No image uploaded"
        }), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "error": "No image selected"
        }), 400

    try:
        image = Image.open(file.stream)
        image.verify()
        file.stream.seek(0)
        image = Image.open(file.stream).convert("RGB")
        predictions = predict_breed(image)

        return jsonify({
            "success": True,
            "predictions": predictions
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": "The image could not be processed. Please try another animal photo."
        }), 500


@app.errorhandler(413)
def file_too_large(_error):
    return jsonify({
        "success": False,
        "error": "Image is too large. The maximum upload size is 10 MB."
    }), 413


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
