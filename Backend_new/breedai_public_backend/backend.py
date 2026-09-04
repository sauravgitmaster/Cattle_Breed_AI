from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import tempfile

from tnbc6_FINAL_FIXED import predict_breed, get_breed_profile

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

allowed_origins = [
    origin.strip()
    for origin in os.getenv("ALLOWED_ORIGINS", "*").split(",")
    if origin.strip()
]
CORS(app, resources={r"/*": {"origins": allowed_origins}})

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.get("/")
def home():
    return jsonify({
        "success": True,
        "service": "BreedAI API",
        "status": "online"
    })


@app.get("/health")
def health():
    return jsonify({"success": True, "status": "healthy"})


@app.post("/predict")
def predict():
    temp_path = None

    try:
        if "image" not in request.files:
            return jsonify(success=False, error="No image uploaded."), 400

        image = request.files["image"]

        if not image.filename:
            return jsonify(success=False, error="No image selected."), 400

        if not allowed_file(image.filename):
            return jsonify(
                success=False,
                error="Unsupported image type. Use JPG, JPEG, PNG or WEBP."
            ), 400

        filename = secure_filename(image.filename) or "upload.jpg"
        suffix = os.path.splitext(filename)[1].lower()
        temp_file = tempfile.NamedTemporaryFile(
            prefix="breedai_", suffix=suffix, delete=False
        )
        temp_path = temp_file.name
        temp_file.close()
        image.save(temp_path)

        predictions = predict_breed(temp_path)
        profile = get_breed_profile(predictions[0]["breed"])

        return jsonify({
            "success": True,
            "predictions": predictions,
            "profile": profile
        })

    except Exception as exc:
        print("Prediction API error:", repr(exc), flush=True)
        return jsonify({
            "success": False,
            "error": str(exc)
        }), 500

    finally:
        if temp_path and os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except OSError:
                pass


@app.errorhandler(413)
def file_too_large(_error):
    return jsonify({
        "success": False,
        "error": "Image is too large. The maximum upload size is 10 MB."
    }), 413


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"BreedAI backend starting on port {port}", flush=True)
    app.run(host="0.0.0.0", port=port, debug=False)
