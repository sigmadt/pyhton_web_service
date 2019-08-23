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