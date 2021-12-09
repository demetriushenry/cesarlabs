import logging
import time
from enum import Enum

from flask import render_template, request, jsonify
from flask_socketio import SocketIO

from create_app import create_celery_app, create_flask_app
from morse_code_decoder import MorseCodeDecoder


class StatusCode(Enum):
    """
    Status code for request results.
    """
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_ALLOWED = 405
    NOT_FOUND = 404


# create log object
logger = logging.getLogger(__name__)
# create Flask app
app = create_flask_app()
# create celery app
celery = create_celery_app(app)
socketio = SocketIO(app, cors_allowed_origins='*')
namespace = '/decode_morse_code'


@celery.task(name='app.decode')
def decode(code):
    """
    Call decode morse code method.
    :param code: str
    :return: str
    """
    morse_decoder = MorseCodeDecoder()
    return morse_decoder.decode_code(code)


@app.route('/')
def index():
    """
    Renders the result page.
    :return: str
    """
    return render_template('index.html')


@app.route('/api/v1/morse_decode', methods=['GET', 'POST'])
def morse_decoding():
    """
    Decodes the morse code from request.
    :return: Response
    """
    if request.method == 'POST':
        try:
            code = request.json['code'].strip()
            return jsonify({'result': decode(code)}), StatusCode.OK.value
        except Exception as ex:
            logger.error(f'Error while trying to parse the json: {ex}')
            return jsonify({'message': 'payload should contain the parameter code'})

    return jsonify({'message': 'Not allowed. Use POST request instead'}), StatusCode.NOT_ALLOWED.value


@socketio.on('connect', namespace='/decode_morse_code')
def handle_connection():
    """
    Handle the socket connection.
    """
    logger.debug('Client connection received.')
    try:
        socketio.emit('message', {'message': 'Connection established.'}, namespace=namespace)
    except Exception as ex:
        logger.error(f'Error while trying to answer the client: {ex}')


@socketio.on('decode', namespace='/decode_morse_code')
def handle_connection(data):
    """
    Handle the decoding code result.
    :param data: str
    """
    logger.debug('Decoding request received.')
    try:
        socketio.emit('result', {'result': 'decoding...'}, namespace=namespace)
    except Exception as ex:
        logger.error(f'Error while trying to answer the received connection: {ex}')

    result = decode.delay(data)

    while not result.ready():
        time.sleep(0.1)

    decoded_code = result.get(timeout=10)

    logger.debug(f'Decode code: {decoded_code}')

    try:
        socketio.emit('result', {'result': decoded_code}, namespace=namespace)
    except Exception as ex:
        logger.error(f'Error while trying to send the decoded code: {ex}')


if __name__ == '__main__':
    socketio.run(app, port=5000, host='0.0.0.0', debug=True)
