from flask import jsonify
import json
from machinelearning import Machinelearning
from status_codes import *
from imageObject import *
class Response():
    def handlePOSTReq(self,request :json):

        #PROVERA OBJEKTA
        try:
            
            pixels = ImageObject.parse_obj(request).image
        except:
            return jsonify('Invalid format'), StatusCodes.BAD_REQUEST
        #SLANJE ML FUNKCIJI
        try:
            number = Machinelearning.MLTest(pixels)
            print(number)
            #response
            return jsonify(number), StatusCodes.OK
        except:
            return jsonify('Unexpected server error'), StatusCodes.UNEXPECTED_ERROR