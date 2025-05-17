from flask import Flask
from routes.api import apiRoutes

app: Flask = Flask(__name__)
app.register_blueprint(apiRoutes)