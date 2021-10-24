from flask import Flask, request, jsonify
#from imageObject import ImageObject
import status_codes as StatusCodes

app = Flask(__name__)

@app.route('/recognise_image', methods=['POST'])
def handlePOSTReq():

    #PROVERA OBJEKTA
    try:
        #image = ImageObject.parse_obj(request.json)
        pass
    except:
        return jsonify('Invalid format', StatusCodes.BAD_REQUEST)
        pass

    #SLANJE ML FUNKCIJI
    try:
        #number = MLTest(image)

        #response
        #return jsonify(number), StatusCodes.OK
        pass

    except:
        return jsonify('Unexpected server error', StatusCodes.BAD_REQUEST)
app.run(host = '0.0.0.0' )


def MLTest(image):
    return 3