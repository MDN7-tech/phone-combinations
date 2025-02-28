from flask import Flask, request, jsonify
from itertools import product

app = Flask(__name__)

# Phone number to letter mapping
phone_map = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

# Function to calculate combinations
def get_combinations(phone_number):
    groups = [phone_map[digit] for digit in phone_number if digit in phone_map]
    return [''.join(combo) for combo in product(*groups)]

@app.route('/combinations', methods=['POST'])
def combinations():
    data = request.get_json()
    phone_number = data.get('phoneNumber')
    
    if not phone_number:
        return jsonify({"error": "Phone number is required"}), 400

    if not all(digit in '23456789' for digit in phone_number):
        return jsonify({"error": "Invalid phone number"}), 400

    # Get combinations
    result = get_combinations(phone_number)
    return jsonify({"combinations": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
