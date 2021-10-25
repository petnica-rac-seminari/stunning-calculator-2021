from flask import jsonify
import json
from customError import CustomError

import numpy as npy
import prepoznavanje as ML
from status_codes import *
from imageObject import *
from equationObject import *
from evalEquation import evalEquation


class Response():
    def handlePOSTReq(self,request :json):

        #PROVERA OBJEKTA
        try:
            #provera da li je list
            pixels = ImageObject.parse_obj(request).image

            

            #provera da li je duzine 784
            if (len(pixels)!=784):
                raise Exception()
     
            #pretvaranje u npy.array
            pixel_ints = npy.array(pixels)

            #provera da li su svi izmedju 0 i 255 (ukljucuje)
            if not (npy.all(pixel_ints>=0) and npy.all(pixel_ints<=255)):
                raise Exception()


            #pretvaranje u npy.array sa unsigned byteovima
            pixel_ints = npy.array(pixels,dtype=npy.uint8)
        except:
            return jsonify('Invalid format'), StatusCodes.BAD_REQUEST
        #SLANJE ML FUNKCIJI
        try:
            number = ML.PrepoznavanjeCifre(pixel_ints)
            #provera da li je cifra
            if type(number) != int:
                raise Exception()
            if not (number>=0 and number<=9):
                raise Exception()
            #response
            return jsonify(number), StatusCodes.OK
        except:
            return jsonify('Unexpected server error'), StatusCodes.UNEXPECTED_ERROR

    def handleEquation(self,request :json):

        try:
            equation = EquationObject.parse_obj(request).equation
        except:
            return jsonify('Invalid format'), StatusCodes.BAD_REQUEST
        try:
            if len(equation)>100: 
                raise Exception("Equation too long")
        except:
            return jsonify('Equation too long'), StatusCodes.BAD_REQUEST
        try:
            evalResult = evalEquation(equation)

            try:
                #provera da li je float
                if type(evalResult) != float:
                    raise Exception("EvalResultNotFloat")
            except:
                return jsonify('Invalid format'), StatusCodes.BAD_REQUEST

            return jsonify(evalResult), StatusCodes.OK
        except ZeroDivisionError:
            return jsonify('Arithmetic error'), StatusCodes.NOT_ACCEPTABLE
        except CustomError as err:
            return jsonify('Arithmetic error'), StatusCodes.NOT_ACCEPTABLE
        except:
            return jsonify('Unexpected server error'), StatusCodes.UNEXPECTED_ERROR