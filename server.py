from flask import Flask
from flask_cors import CORS
from routes.graphQL import graphqlRoutes

app: Flask = Flask(__name__)
CORS(app, resources={r"/graphql/*": {"origins": "*"}})
app.register_blueprint(graphqlRoutes)