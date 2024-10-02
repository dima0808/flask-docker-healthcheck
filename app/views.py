from flask import jsonify
from datetime import datetime
import pytz
from app import app


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    stockholm_tz = pytz.timezone('Europe/Stockholm')
    current_time = datetime.now(stockholm_tz).isoformat()
    response = {
        'status': 'ok',
        'date': current_time
    }
    return jsonify(response), 200
