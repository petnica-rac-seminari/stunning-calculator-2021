import requests
import numpy
import json

def SendParsedImage(arr : list) -> str:
    try:                    
        #value = requests.post('http://localhost:5000/recognise_image', json = { 
        #    'image' : arr
        #    })                        
        #return str(value.json()) 
        return "5"
    except:        
        raise Exception("lele2")               
