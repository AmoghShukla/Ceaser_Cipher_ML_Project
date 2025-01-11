from flask import Flask, request, jsonify
import pickle
import numpy as np
from utils import extract_features

app = Flask(__name__)

# Load the trained model
MODEL_PATH = "model.pkl"
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Caesar Cipher Shift Prediction API!"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    if "encrypted_text" not in data:
        return jsonify({"error": "Missing 'encrypted_text' in request"}), 400

    encrypted_text = data["encrypted_text"]
    features = extract_features(encrypted_text)
    features = np.array(features).reshape(1, -1)
    shift = model.predict(features)[0]

    return jsonify({
        "encrypted_text": encrypted_text,
        "predicted_shift": int(shift)
    })

if __name__ == "__main__":
    app.run(debug=True)
