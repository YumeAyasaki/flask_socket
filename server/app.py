from flask import Flask, render_template
from flask_socketio import SocketIO
import logging

import config

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])
logger = logging.getLogger()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


def create_app():
    logger.info(f'Starting app in {config.APP_ENV} environment')
    app = Flask(__name__)
    app.config.from_object('config')
    socketio = SocketIO(app)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    return socketio, app


if __name__ == "__main__":
    app, socketio = create_app()
    socketio.run(host='0.0.0.0', debug=True)