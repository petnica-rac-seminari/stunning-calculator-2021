import requests
import numpy
import json

def SendParsedImage(arr : list) -> str:
    try:                    
        value = requests.post('http://10.51.0.78:5000/recognise_image', json = { 
            'image' : arr
            })                
        return str(value.json()) 
    except:        
        raise Exception("lele2")               
