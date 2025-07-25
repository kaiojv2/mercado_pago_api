from app import app, socketio
import eventlet
import eventlet.wsgi

if __name__ == '__main__':
    print("Servidor iniciado em http://0.0.0.0:5000")
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
