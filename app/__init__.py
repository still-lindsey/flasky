from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

DATABASE = 'postgresql+psycopg2://postgres:postgres@localhost:5432/flasky_development'


def create_app():
    # __name__ store the name of the module we're in
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.dog_routes import dog_bp
    app.register_blueprint(dog_bp)

    from .routes.cat_routes import cat_bp
    app.register_blueprint(cat_bp)

    return app