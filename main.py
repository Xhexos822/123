from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

keys = {}

@app.route('/generate_key', methods=['POST'])
def generate_key():
    key = str(uuid.uuid4())
    keys[key] = False
    return jsonify({'key': key}), 201

@app.route('/check_key', methods=['POST'])
def check_key():
    data = request.get_json()
    key = data.get('key')
    if key and key in keys:
        if not keys[key]:
            keys[key] = True
            return jsonify({'valid': True}), 200
        else:
            return jsonify({'valid': False, 'message': 'Key already used.'}), 400
    else:
        return jsonify({'valid': False, 'message': 'Invalid key.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
