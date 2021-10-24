from flask import jsonify
import json

import numpy as npy
import machine_learning.prepoznavanje as ML
from status_codes import *
from imageObject import *
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