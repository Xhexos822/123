from flask import Flask, request, jsonify
import json
import uuid

app = Flask(__name__)

# Load keys and values from JSON file
with open('keys.json', 'r') as file:
    keys = json.load(file)

@app.route('/generate_key', methods=['POST'])
def generate_key():
    key = str(uuid.uuid4())
    value = str(uuid.uuid4())  # Generate a random value for each key
    keys[key] = value
    # Save updated keys to JSON file
    with open('keys.json', 'w') as file:
        json.dump(keys, file)
    return jsonify({'key': key, 'value': value}), 201

@app.route('/check_key', methods=['POST'])
def check_key():
    data = request.get_json()
    key = data.get('key')
    value = data.get('value')
    if key and key in keys:
        if keys[key] == value:
            return jsonify({'valid': True}), 200
        else:
            return jsonify({'valid': False, 'message': 'Invalid key or value.'}), 400
    else:
        return jsonify({'valid': False, 'message': 'Invalid key.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
