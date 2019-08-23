from flask import Flask, request, jsonify
app = Flask(__name__)

import datetime
import uuid


#GET request

@app.route('/action')
def action():
    
    current_time = datetime.datetime.now()
    response = {'text': '', 'current_time': current_time, 'status code': 200}
    
    return jsonify(response)


#POST request

@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()

    return jsonify(str(content) + ' ' + str(uuid.uuid1()))



#Examples:

#1. С помощью GET запроса посчитаем квадрат числа, переданного в строку

@app.route('/square/<num>')
def square(num):
    num = float(num)
    squared_num = num * num

    current_time = datetime.datetime.now()
    response = {'text': squared_num, 'current_time': current_time, 'status code': 200}
    
    return jsonify(response)

#2. С помощью POST получим переданные данные в Json + uuid

@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()

    return jsonify(str(content) + ' ' + str(uuid.uuid1()))
