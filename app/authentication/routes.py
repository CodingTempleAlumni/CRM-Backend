from flask import Blueprint

# this module will likely require some new packages and/or database work.... :)

authentication = Blueprint('authentication', __name__, url_prefix='/auth')