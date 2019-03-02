from flask import Flask, request
from page_objects.keys import VirtualKeys
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    data = json.loads(request.data)
    print(data['gesture_id'])
    VirtualKeys.send_key(data['gesture_id'])
    return "Hello World!"

app.run(host= '0.0.0.0')
