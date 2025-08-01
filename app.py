from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hacker_h_ham'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Message: {msg}")
    emit('message', msg, broadcast=True)  # sabhi users ko bhejna

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
