#to execute this file enter this "flask --app main.py run"

from flask import Flask, request, json, Response
from flask_cors import CORS
from service import *

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8100"}})
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})


@app.route('/')
def base():
    return Response(response=json.dumps({"Application": "ARSII System Evaluation"}),
                    status=200,
                    mimetype='application/json')


@app.route('/subject', methods=['GET'])
def getSubject():
    subjectId = request.args.get('id')
    if subjectId is None:
        return Response(response=json.dumps({"Error": "Please provide the subject id!"}), status=400,
                        mimetype='application/json')
    response = getShuffeledQuestions(subjectId)
    return Response(response=json.dumps(response), status=200, mimetype='application/json')


@app.route('/subject', methods=['POST'])
def getResult():
    data = request.json
    if data is None or 'Document' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}), status=400, mimetype='application/json')
    response = calculateScore(data['Document'])
    return Response(response=json.dumps(response), status=200, mimetype='application/json')



if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
