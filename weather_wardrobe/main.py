import os
from flask import Flask, request, jsonify
from .recommender import get_outfit_recommendation
from .metrics import record_request

app = Flask(__name__)
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

@app.route("/recommend")
def recommend():
    city = request.args.get('city')
    record_request("recommend_total")
    if not city:
        record_request("recommend_error")
        return jsonify({"error": "City parameter is required"}), 400
    if not WEATHER_API_KEY:
        record_request("recommend_error")
        return jsonify({"error": "Server error: Weather API key is not configured"}), 500
    try:
        recommendation = get_outfit_recommendation(city, WEATHER_API_KEY)
        record_request("recommend_success")
        return jsonify({"outfit": recommendation})
    except Exception as e:
        record_request("recommend_error")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

@app.route("/")
def home():
    return "Weather-Wardrobe backend is running! Use /recommend?city=CityName"

