import os
from flask import Flask, request, jsonify
from .recommender import get_outfit_recommendation
from .metrics import record_request

app = Flask(__name__)
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

@app.route("/recommend")
def recommend():
    city = request.args.get('city')
    if not city:
        record_request(success=False)
        return jsonify({"error": "City parameter is required"}), 400
    if not WEATHER_API_KEY:
        record_request(success=False)
        return jsonify({"error": "Server error: Weather API key is not configured"}), 500
    try:
        recommendation = get_outfit_recommendation(city, WEATHER_API_KEY)
        record_request(success=True)
        return jsonify({"outfit": recommendation})
    except Exception as e:
        record_request(success=False)
        return jsonify({"error": str(e)}), 500
