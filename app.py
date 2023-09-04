from flask import Flask
from flask_restful import Api, Resource, reqparse
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
api = Api(app)

# MongoDB Configuration
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Users'
mongo = MongoClient(app.config['MONGO_URI'])
db = mongo.get_database()

# User Collection
users_collection = db.users

# Define User Schema
class UserSchema(object):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def validate(cls, data):
        errors = {}
        if not data['name']:
            errors['name'] = 'Name is required'
        if not data['email']:
            errors['email'] = 'Email is required'
        if not data['password']:
            errors['password'] = 'Password is required'
        return errors

# Helper function to convert ObjectId to string
def jsonify_user(user):
    user['_id'] = str(user['_id'])
    return user

# Create a parser for handling request data
user_parser = reqparse.RequestParser()
user_parser.add_argument('name', type=str, required=True)
user_parser.add_argument('email', type=str, required=True)
user_parser.add_argument('password', type=str, required=True)

# Define a User resource class
class UserResource(Resource):
    def get(self, id=None):
        if id:
            user = users_collection.find_one({'_id': ObjectId(id)})
            if user:
                return jsonify(jsonify_user(user)), 200
            return jsonify({'message': 'User not found'}), 404
        else:
            users = list(users_collection.find())
            # Convert ObjectId to string for each user
            users = [jsonify_user(user) for user in users]
            return jsonify(users), 200

    def post(self):
        args = user_parser.parse_args()
        errors = UserSchema.validate(args)
        if errors:
            return jsonify(errors), 400
        user = UserSchema(args['name'], args['email'], args['password'])
        result = users_collection.insert_one(user.__dict__)
        return jsonify({'message': 'User created', 'id': str(result.inserted_id)}), 201

    def put(self, id):
        args = user_parser.parse_args()
        errors = UserSchema.validate(args)
        if errors:
            return jsonify(errors), 400
        result = users_collection.update_one({'_id': ObjectId(id)}, {'$set': args})
        if result.modified_count > 0:
            return jsonify({'message': 'User updated'}), 200
        return jsonify({'message': 'User not found'}), 404

    def delete(self, id):
        result = users_collection.delete_one({'_id': ObjectId(id)})
        if result.deleted_count > 0:
            return jsonify({'message': 'User deleted'}), 200
        return jsonify({'message': 'User not found'}), 404

# Add the User resource to the API with the '/users' endpoint
api.add_resource(UserResource, '/users', '/users/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)