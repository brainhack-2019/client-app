from flask import Flask
from keys import send_key

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/play', methods=['GET'])
def play():
    send_key('play_key')
    return "Play!"

@app.route('/prev', methods=['GET'])
def prev():
    send_key('prev_key')
    return "Prev!"

@app.route('/next', methods=['GET'])
def next():
    send_key('next_key')
    return "Next!"

@app.route('/audio_lower', methods=['GET'])
def audio_lower():
    send_key('audio_lower_key')
    return "Audio lower!"

app.run()
