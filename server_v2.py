from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)
COINGECKO_API_URL = "https://api.coingecko.com/api/v3"

# Serve the documentation page
@app.route('/')
def home():
    return render_template("index.html")

#Ping request for check!
@app.route('/ping', methods=['GET'])
def ping():
    response = requests.get(f"{COINGECKO_API_URL}/ping")
    return jsonify(response.json()), response.status_code

#Get live price of one or more coins
@app.route('/simple/price', methods=['GET'])
def get_price():
    coins = request.args.get("ids", "bitcoin")
    vs_currency = request.args.get("vs_currencies", "usd")
    #print(f"Requesting: {COINGECKO_API_URL}/simple/price?ids={coins}&vs_currencies={vs_currency}")
    response = requests.get(f"{COINGECKO_API_URL}/simple/price", params={"ids": coins, "vs_currencies": vs_currency})
    return jsonify(response.json()), response.status_code

#Get a list of all supported coins
@app.route('/coins/list', methods=['GET'])
def get_coins_list():
    response = requests.get(f"{COINGECKO_API_URL}/coins/list")
    return jsonify(response.json()), response.status_code

#Get market data for top coins
@app.route('/coins/markets', methods=['GET'])
def get_market_data():
    vs_currency = request.args.get("vs_currency", "usd")
    response = requests.get(f"{COINGECKO_API_URL}/coins/markets", params={"vs_currency": vs_currency, "order": "market_cap_desc", "per_page": 10, "page": 1})
    return jsonify(response.json()), response.status_code

#Get full details of a specific coin
@app.route('/coins/<coin_id>', methods=['GET'])
def get_coin_details(coin_id):
    response = requests.get(f"{COINGECKO_API_URL}/coins/{coin_id}")
    return jsonify(response.json()), response.status_code

#Get historical chart data for a coin
@app.route('/coins/<coin_id>/market_chart', methods=['GET'])
def get_coin_chart(coin_id):
    vs_currency = request.args.get("vs_currency", "usd")
    days = request.args.get("days", "30")  # Default: Last 30 days
    response = requests.get(f"{COINGECKO_API_URL}/coins/{coin_id}/market_chart", params={"vs_currency": vs_currency, "days": days})
    return jsonify(response.json()), response.status_code

#Get historical price data for a specific date
@app.route('/coins/<coin_id>/history', methods=['GET'])
def get_coin_history(coin_id):
    date = request.args.get("date", "01-01-2025")  # Default to Jan 1, 2024
    response = requests.get(f"{COINGECKO_API_URL}/coins/{coin_id}/history", params={"date": date})
    return jsonify(response.json()), response.status_code

#Get all coin categories with market data
@app.route('/coins/categories', methods=['GET'])
def get_coin_categories():
    response = requests.get(f"{COINGECKO_API_URL}/coins/categories")
    return jsonify(response.json()), response.status_code

# Get coin tickers from different exchanges
@app.route('/coins/<coin_id>/tickers', methods=['GET'])
def get_coin_tickers(coin_id):
    response = requests.get(f"{COINGECKO_API_URL}/coins/{coin_id}/tickers")
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)