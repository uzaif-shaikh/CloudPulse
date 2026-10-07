from flask import Flask
from app.extensions import db


def create_app():

    app = Flask(__name__)

    # -----------------------------
    # Configuration
    # -----------------------------

    app.config["SECRET_KEY"] = "change-this-secret-key"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cloudpulse.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # -----------------------------
    # Initialize extensions
    # -----------------------------

    db.init_app(app)

    # -----------------------------
    # Import models
    # -----------------------------

    from app.models import User

    # -----------------------------
    # Register Blueprints
    # -----------------------------

    from app.routes.auth import auth_bp
    from app.routes.dashboard import dashboard_bp
    from app.routes.servers import servers_bp
    from app.routes.alerts import alerts_bp
    from app.routes.reports import reports_bp
    from app.routes.settings import settings_bp
    from app.routes.users import users_bp
   

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(servers_bp)
    app.register_blueprint(alerts_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(settings_bp)
    app.register_blueprint(users_bp)
   
    
    # -----------------------------
    # Create database tables
    # -----------------------------
   
   
    with app.app_context():
        db.create_all()

    return app