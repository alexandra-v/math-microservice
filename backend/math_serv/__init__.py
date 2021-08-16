from flask import Flask
from celery import Celery
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from .config import Config
from .controllers import api as ns

db = SQLAlchemy()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)
admin = Admin()
api = Api(title='Basic math operations API', version='1.0')
api.add_namespace(ns)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    celery.conf.update(app.config)
    celery.autodiscover_tasks()
    api.init_app(app)
    admin.init_app(app)

    from .models import Operations
    admin.add_view(ModelView(Operations, db.session))
    
    Swagger(app)

    return app
