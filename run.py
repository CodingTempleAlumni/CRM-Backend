# optional file for the creation of shell context processors
from app import app
from app.models import db, User, Company, Job


@app.shell_context_processor
def db_context():
    return {'db': db, 'User': User, 'Company': Company, 'Job': Job}