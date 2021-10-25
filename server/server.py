from flask import Flask, request
from response import Response
app = Flask(__name__)

rsp = Response()

@app.route('/recognize_image', methods=['POST'])
def recognise_image():
    return rsp.handlePOSTReq(request.json)

@app.route('/evaluate_equation', methods=['POST'])
def evaluate_equation():
    return rsp.handleEquation(request.json)


app.run(host = '0.0.0.0', port=5000 )


