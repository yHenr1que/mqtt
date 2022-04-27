import json
import flask
from flask import Flask, jsonify, request

app = Flask(__name__)

messageArray = []

app = Flask(__name__, template_folder='views')
CORS(app, support_credentials=True)
socketio = SocketIO(app, async_mode=async_mode)

@app.route('/')

def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@app.route('/inserir', methods=['POST'])
def inserir_mensagem():
  global messageArray
  messageArray.append(request.json)
    with app.app_context():
        socketio.emit("on_message", request.json, namespace='/messages')
    return request.json


@app.route('/get-messages', methods=["GET"])
@cross_origin(supports_credentials=True)

def getMessages():
    global messageArray
    time.sleep(10)
    return jsonify(messageArray)
    

@socketio.on('on_connect', namespace='/messages')
def on_connect(message):
    print('conectou')

@socketio.on('on_message', namespace='/messages')
def on_message(message):
    print('conectou')
    send(message)

app.run(debug=True)

#def historico():
#  global messageArray
#  return jsonify(messageArray)
#

#app.run()
#  #new_message = Message(conteudo)