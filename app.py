from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/generate-zip', methods=['GET'])
def generate_zip():
    input1 = request.args.get('input1', '')
    input2 = request.args.get('input2', '')

    # Your logic to generate the zip file goes here
    # For demonstration, just echoing the inputs
    response_data = {
        'input1': input1,
        'input2': input2,
        'message': 'Zip generated successfully'
    }

    # print(f"Received request: {request.method} {request.url} - Input1: {input1}, Input2: {input2}")

    return jsonify(response_data)
