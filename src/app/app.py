from flask import Flask, request, jsonify
import torch
import xgboost as xgb
from google.cloud import storage
import os

app = Flask(__name__)

# Google Cloud Storage credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp_credentials.json"

pytorchModel = None
xgbModel = None

# Function to download PyTorch model from GCS
def download_pytorch_model():
    client = storage.Client()
    bucket = client.get_bucket("razor-pay-first-bucket")
    blob = bucket.blob("models/pytorch-model.pt")
    blob.download_to_filename("pytorch_model.pt")

# Function to download XGBoost model from GCS
def download_xgboost_model():
    client = storage.Client()
    bucket = client.get_bucket("razor-pay-first-bucket")
    blob = bucket.blob("models/xgb_model.json")
    blob.download_to_filename("xgb_model.json")

# Load PyTorch model
def load_pytorch_model():
    model = torch.load("pytorch_model.pt", map_location=torch.device('cpu'))
    model.eval()
    pytorchModel = model

# Load XGBoost model
def load_xgboost_model():
    model = xgb.XGBClassifier(model_file="xgb_model.json")
    xgbModel = model

# Download models when Flask app starts
download_pytorch_model()
download_xgboost_model()

# Define endpoint for serving the models
@app.route('/getChurnScore', methods=['POST'])
def get_churn_score():
    # Get userId from request
    user_id = request.json.get('userId')

    # Perform inference
    pytorch_score = infer_pytorch(user_id)
    xgboost_score = infer_xgboost(user_id)

    # Return inference results
    return jsonify({'pytorchScore': pytorch_score, 'xgboostScore': xgboost_score})


def infer_pytorch(user_id):
    
    # Placeholder return for demonstration
    return user_id * 2


def infer_xgboost(user_id):
    
    # Placeholder return for demonstration
    return user_id * 2


if __name__== "__main__":
    # we are just demonstrating so not worrying about prod/debug env or any optimizations here.
    app.run(port=8080)