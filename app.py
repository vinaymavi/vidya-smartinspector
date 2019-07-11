from flask import Flask
from flask import request,jsonify,make_response
from RandomForest_Predict import functionpredict
app = Flask(__name__)

def resp_message(status,desc,data):
    return {
        'status':status,
        'description':desc,
        'data':data
    }


@app.route("/")
def hello():
    return "Smart Inspector is Under Development"

@app.route("/v1/cnn")
def v1cnn():
    return "CNN model is running"

@app.route("/v1/rf")
def v1rf():
    test_str = None
    if 'testdata' not in request.args:
        return make_response(jsonify(resp_message("ERROR","testdata is not defined",None)),500)
    else:
        test_str = request.args['testdata']
        test_data = [float(n) for n in test_str.split(',')]
        predict_result = functionpredict(test_data)
        return make_response(jsonify(resp_message(predict_result['result'],predict_result['desc'],predict_result)),200)


