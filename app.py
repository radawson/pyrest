from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

users = []
id = 0

class UserAPI(Resource):
    def get(self, name):
        for user in users:
            if user['name'] == name:
                return user
            
    def post(self, name):
        global id
        user = {'name' : name, 'id' : id}
        id += 1
        users.append(user)
        return user

api.add_resource(UserAPI, '/users/<string:name>', endpoint = 'user')

if __name__ == '__main__':

	app.run(debug=True)