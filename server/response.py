from flask import jsonify
import json
from machinelearning import Machinelearning
from status_codes import *
from imageObject import *
class Response():
    def handlePOSTReq(request :json):

        #PROVERA OBJEKTA
        try:
            image = ImageObject.parse_obj(request)
        except:
            return jsonify('Invalid format'), StatusCodes.BAD_REQUEST
        #SLANJE ML FUNKCIJI
        try:
            number = Machinelearning.MLTest(image)

            #response
            return jsonify(number), StatusCodes.OK
            pass
        except:
            return jsonify('Unexpected server error'), StatusCodes.UNEXPECTED_ERROR