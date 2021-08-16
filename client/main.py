from flask import Flask, request, render_template, Response, jsonify
import json
import requests

app = Flask(__name__)

all_updates = []

def log_message(msg):
    print(msg, flush=True)

def log_and_update(msg):
    log_message(msg)
    all_updates.append(msg)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html', all_updates=all_updates)

@app.route("/ajax/operation/", methods=['POST'])
def operation():
    data = request.get_json()
    log_message(data)

    op_type = data['op_type']
    operands = data['operands']

    log_message(op_type)
    log_message(operands)

    log_and_update(f'Sending a {op_type} operation for {operands}')

    log_message(data)
    res = requests.post('http://35.202.6.100/operations/', json=data)

    message = res.json()['message']
    log_and_update(f"The math_server responded with: {message}")

    return jsonify({"status": message}), res.status_code


@app.route("/ajax/result/", methods=['POST'])
def result():
    data = request.get_json()

    log_and_update(f"Received a result from math_server: {data['op_type']} for {data['operands']} = {data['result']}")

    log_message(all_updates)

    return jsonify({}), 200


@app.route("/ajax/updates/", methods=['GET'])
def updates():
    return Response(json.dumps(all_updates), mimetype='application/json')



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)