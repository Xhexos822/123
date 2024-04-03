from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load keys from JSON file
with open('keys.json') as f:
    keys = json.load(f)


# Endpoint to check key
@app.route('/check_key', methods=['POST'])
def check_key():
    data = request.json
    key = data.get('key')

    if not key:
        return jsonify({'error': 'Key is required'}), 400

    if key in keys:
        return jsonify({'valid': True}), 200
    else:
        return jsonify({'valid': False}), 200


if __name__ == '__main__':
    app.run(debug=True)
