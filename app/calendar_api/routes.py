from flask import Blueprint

calendar = Blueprint('calendar', __name__, url_prefix='/calendar')

@calendar.route('/test')
def testroute():
    return 'oh hey a route within the calendar blueprint'