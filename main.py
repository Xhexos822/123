from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load keys
with open('keys.json') as f:
    keys = json.load(f)


# Endpoint for checking key
@app.route('/check_key', methods=['POST', 'GET'])
def check_key():
    if request.method == 'POST':
        data = request.json
        key = data.get('key')

        if not key:
            return jsonify({'error': 'Key is required'}), 400

        if key in keys:
            # Return the validity of the key along with the associated username
            return jsonify({'valid': True, 'username': keys[key]['user']}), 200
        else:
            return jsonify({'valid': False}), 200
    else:
        return jsonify({'error': 'Method not allowed'}), 405


if __name__ == '__main__':
    app.run(debug=True)
