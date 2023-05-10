from flask import Flask, request, render_template, jsonify
import base64, os, random
from uuid import uuid4
from model import predict

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict-digit", methods=["POST"])
def predict_digit():
    image = request.get_json(silent=True)['image'].split(",")[1]
    image_data = base64.urlsafe_b64decode(image)

    prediction, confidence = predict(image_data)

    response = {
        "prediction": str(prediction),

    }

    return jsonify(response)
