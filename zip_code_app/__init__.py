import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from rq import Queue
import redis


db = SQLAlchemy()
migrate = Migrate()
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)
q = Queue(connection=redis)

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("zip_code_app.config.DevelopmentConfig")
    if os.environ.get('PRODUCTION'):
        app.config.from_object("zip_code_app.config.ProductionConfig")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    migrate.init_app(app, db)

    # apply the blueprints to the app
    from zip_code_app import client, city
    bootstrap = Bootstrap(app)

    app.register_blueprint(client.bp)
    app.register_blueprint(city.bp)

    @app.route('/')
    def index():
        return "This is the app for the test"

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app
