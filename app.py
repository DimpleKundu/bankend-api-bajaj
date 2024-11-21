from flask import Flask, render_template, request, jsonify
# to run both bankend and forntend api seperately
from flask_cors import CORS
import base64
import mimetypes

app = Flask(__name__)
CORS(app)
@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    
    if request.method == 'GET':
        return jsonify({"operation_code": 1})

    if request.method == 'POST':
        data = request.json.get('data', [])
        file_b64 = request.json.get('file_b64', None)

        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        highest_lowercase = max([x for x in data if x.islower()], default=None)
        is_prime_found = any(is_prime(int(x)) for x in numbers)

        file_valid, file_mime_type, file_size_kb = False, None, None
        if file_b64:
            try:
                file_data = base64.b64decode(file_b64)
                file_mime_type = mimetypes.guess_type("temp")[0]
                file_size_kb = len(file_data) / 1024
                file_valid = True
            except Exception:
                file_valid = False

        return jsonify({
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
            "is_prime_found": is_prime_found,
            "file_valid": file_valid,
            "file_mime_type": file_mime_type,
            "file_size_kb": file_size_kb
        })
        

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
