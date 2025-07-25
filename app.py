from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from dotenv import load_dotenv
import os

from routes.pedidos import pedidos_bp
from routes.pagamentos import pagamentos_bp
from websocket.socket_events import socketio_config

load_dotenv()

app = Flask(__name__)
CORS(app, origins=["*"])
socketio = SocketIO(app, cors_allowed_origins="*")

# Registra blueprints
app.register_blueprint(pedidos_bp)
app.register_blueprint(pagamentos_bp)

# Configura eventos socket.io
socketio_config(socketio)

# Apenas se você for usar import * em outros módulos:
__all__ = ['app', 'socketio']
