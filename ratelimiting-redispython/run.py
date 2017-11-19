from flask import Flask
from flask_restful import Resource, Api
from rate import ratelimit
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):

    @ratelimit(limit=3000, per=60 * 15)
    def get(self):
        return '<h1>This is a rate limited response</h1>'

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
