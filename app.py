from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB Configuration
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Users'
mongo = MongoClient(app.config['MONGO_URI'])
db = mongo.get_database()

# User Collection
users_collection = db.users

# Define User Schema (Optional: You can use Marshmallow for validation)
class UserSchema:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# CRUD Endpoints

@app.route('/users', methods=['GET'])
def get_all_users():
    users = list(users_collection.find())
    return jsonify(users), 200

@app.route('/users/<string:id>', methods=['GET'])
def get_user(id):
    user = users_collection.find_one({'_id': ObjectId(id)})
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = UserSchema(data['name'], data['email'], data['password'])
    result = users_collection.insert_one(user.__dict__)
    return jsonify({'message': 'User created', 'id': str(result.inserted_id)}), 201

@app.route('/users/<string:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    result = users_collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({'message': 'User updated'}), 200
    return jsonify({'message': 'User not found'}), 404

@app.route('/users/<string:id>', methods=['DELETE'])
def delete_user(id):
    result = users_collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'User deleted'}), 200
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
