from flask import Flask
from flask_cors import CORS
def create_app():
    app = Flask(__name__)
    CORS(app)
    # Import and register Blueprints
    from .routes.ipl_routes import ipl_routes
    from .routes.epl_routes import epl_routes
    app.register_blueprint(ipl_routes)
    app.register_blueprint(epl_routes)

    return app