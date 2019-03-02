from flask import Flask
from page_objects.keys import VirtualKeys

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/play', methods=['GET'])
def play():
    VirtualKeys.send_key('play_key')
    return "Play!"

@app.route('/prev', methods=['GET'])
def prev():
    VirtualKeys.send_key('prev_key')
    return "Prev!"

@app.route('/next', methods=['GET'])
def next():
    VirtualKeys.send_key('next_key')
    return "Next!"

@app.route('/audio_lower', methods=['GET'])
def audio_lower():
    VirtualKeys.send_key('audio_lower_key')
    return "Audio lower!"

@app.route('/audio_higher', methods=['GET'])
def audio_higher():
    VirtualKeys.send_key('audio_higher_key')
    return "Audio higher!"

app.run()
