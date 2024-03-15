from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory dictionary to store keys and their usage status
keys = {}

# Route to generate a new key
@app.route('/generate_key', methods=['POST'])
def generate_key():
    key = str(uuid.uuid4())
    keys[key] = False  # Set usage status to False initially
    return jsonify({'key': key}), 201

# Route to check if a key is valid and mark it as used
@app.route('/check_key', methods=['POST'])
def check_key():
    data = request.get_json()
    key = data.get('key')
    if key and key in keys:
        if not keys[key]:  # Check if the key has not been used
            keys[key] = True  # Mark the key as used
            return jsonify({'valid': True}), 200
        else:
            return jsonify({'valid': False, 'message': 'Key already used.'}), 400
    else:
        return jsonify({'valid': False, 'message': 'Invalid key.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
