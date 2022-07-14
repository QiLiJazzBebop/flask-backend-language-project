from flask_jwt_extended import JWTManager

from route.helloWorld import baseRoute
from route.bilingualConvert import convertRoute
from flask_cors import CORS
from flask import Flask


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Init JWT for this application
    JWTManager(app)

    # Registering endpoints
    app.register_blueprint(baseRoute)
    app.register_blueprint(convertRoute)

    return app


app = create_app()