from flask import Flask
from config import Config

# register a blueprint
from .calendar_api.routes import calendar
from .resources_api.routes import resources
from .job_board_api.routes import job_board
from .authentication.routes import authentication
from .announcements_api.routes import announcements
from .admin_dashboard.routes import admin_dash

# orm import
from .models import db
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(calendar)
app.register_blueprint(resources)
app.register_blueprint(job_board)
app.register_blueprint(authentication)
app.register_blueprint(announcements)
app.register_blueprint(admin_dash)

db.init_app(app)
migrate = Migrate(app, db)

from . import routes