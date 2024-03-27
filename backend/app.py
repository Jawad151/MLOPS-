from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://database:27017/")
db = client["webapp"]
collection = db["users"]

@app.route('/store', methods=['POST'])
def store_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    if name and email:
        collection.insert_one({"name": name, "email": email})
        return jsonify({"message": "User stored successfully"}), 200
    else:
        return jsonify({"error": "Name and email are required"}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
