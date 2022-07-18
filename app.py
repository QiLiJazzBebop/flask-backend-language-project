from flask_jwt_extended import JWTManager

from route.helloWorld import baseRoute
from route.nodesBilingualForwardGraph import convertRoute as convertRouteF
from route.nodesBilingualBackwardGraph import convertRoute as convertRouteB
from route.nodeSpecification import nodeTransRoute
from route.nodesLink import nodeLink
from flask_cors import CORS
from flask import Flask


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Init JWT for this application
    JWTManager(app)

    # Registering endpoints
    app.register_blueprint(baseRoute)
    app.register_blueprint(convertRouteF)
    app.register_blueprint(convertRouteB)
    app.register_blueprint(nodeTransRoute)
    app.register_blueprint(nodeLink)

    return app


app = create_app()
