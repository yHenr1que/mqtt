import json
import flask
from flask import Flask, jsonify, request

app = Flask(__name__)

messageArray = []

@app.route('/inserir', methods=['POST'])

def inserir_mensagem():
  record = json.loads(request.data)
  global messageArray
  messageArray.append(request.json)
  return jsonify(record)

@app.route('/', methods=['GET'])

def historico():
  global messageArray
  return jsonify(messageArray)


app.run()
  #new_message = Message(conteudo)