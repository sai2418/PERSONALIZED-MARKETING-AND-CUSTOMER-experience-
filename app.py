from flask import Flask, jsonify, request
from recommendation_engine import RecommendationEngine
import pandas as pd

app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to the Personalized Marketing API. Try /recommendations/<user_id>"

# Load mock data
user_data = pd.read_csv('C:\\Users\\Sai\\Desktop\\New folder//user_data.csv')
user_data.columns = user_data.columns.str.strip()

product_data = pd.read_csv('C:\\Users\\Sai\\Desktop\\New folder//product_data.csv')
product_data.columns = product_data.columns.str.strip()

engine = RecommendationEngine(user_data, product_data)

@app.route('/recommendations/<user_id>', methods=['GET'])
def get_recommendations(user_id):
    recs = engine.get_recommendations(user_id)
    return jsonify(recs)

@app.route('/privacy-policy', methods=['GET'])
def privacy_info():
    return jsonify({"policy": "Your data is securely stored and used only for improving recommendations."})

@app.route('/update-preferences/<user_id>', methods=['POST'])
def update_preferences(user_id):
    preferences = request.json
    # Logic to update user preference DB
    return jsonify({"status": "updated", "user_id": user_id})

if __name__ == '__main__':
    app.run(debug=True)
