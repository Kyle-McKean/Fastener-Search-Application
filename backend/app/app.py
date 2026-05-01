# Flask Application That Serves As The Backend API For Fastener Search
from flask import Flask, jsonify
from flask_cors import CORS
from main import json_code_lookup

# Initialize Flask app and enable CORS for cross-origin requests
app = Flask(__name__)
CORS(app)

# Home Route - Provides a welcome message and instructions for using the API
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Fastener Search API! Use /api/fastener/<code> to look up fastener details."
    })

# Fastener Lookup Route - Returns the details of a fastener based on its 3-letter code
@app.route('/fastener/<code>')
def lookup_fastener(code):
    fastener = json_code_lookup(code)

    if fastener:
        return jsonify(fastener)

    return jsonify({"error": "Fastener not found"}), 404

# Run the Flask app in debug mode when this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)