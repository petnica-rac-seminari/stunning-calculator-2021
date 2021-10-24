from flask import Flask, request, jsonify
from imageObject import ImageObject

def MLTest(image):
    return 7

app = Flask(__name__)

@app.route('/recognise_image', methods=['POST'])
def handlePOSTReq():
    try:
        image = ImageObject.parse_obj(request.json).image
        if (len(image) != 784):
            raise Exception("nema dovoljno")
        try:
            number = MLTest(image)
            return jsonify(number), 200
        except:
            return jsonify("Server error!"), 500
    except:
        return jsonify("Invalid format!"), 400
    
    
app.run(host = '0.0.0.0', port=6969 )