from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import Hero, Power, HeroPower  # Import models so migrations detect them
    from .routes import bp as api_bp
    app.register_blueprint(api_bp)

    @app.route('/')
    def home():
        return 'Migration Test'

    return app
