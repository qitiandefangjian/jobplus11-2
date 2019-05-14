from flask import Flask
from jobplus.models import db,User
from flask_migrate import Migrate
from flask_login import LoginManager
from jobplus.config import configs

def registerdatabase(app):
    db.init_app(app)
    Migrate(app,db)
    login_manager = LoginManager()
    login_manager.login_view = 'front.index'
    login_manager.init_app(app)

    @login_manager.user_loader  
    def load_user(id):    
        return User.query.get(int(id))     

def registeredversion(app):
    from .handlers import front
    from .handlers import admin
    from .handlers import job
    from .handlers import company
    app.register_blueprint(front)
    app.register_blueprint(admin)
    app.register_blueprint(job)
    app.register_blueprint(company)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])
    registeredversion(app)
    registerdatabase(app)
    return app
