from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change to a strong secret
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Message: {msg}")
    # Broadcast to all clients except sender
    emit('message', msg, broadcast=True, include_self=False)

if __name__ == '__main__':
    socketio.run(app, debug=True)
