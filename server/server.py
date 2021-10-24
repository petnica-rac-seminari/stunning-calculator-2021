from flask import Flask, request
from response import Response
app = Flask(__name__)

rsp = Response()

@app.route('/recognise_image', methods=['POST'])
def recognise_image():
    return rsp.handlePOSTReq(request.json)

app.run(host = '0.0.0.0', port=5000 )


