from flask import Flask
from routes.graphQL import graphqlRoutes

app: Flask = Flask(__name__)
app.register_blueprint(graphqlRoutes)