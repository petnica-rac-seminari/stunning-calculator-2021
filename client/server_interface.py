import requests
import numpy
import json

def SendParsedImage(arr : list) -> str:
    try:
        return '42'                    
        #print(arr)
        #value = requests.post('http://localhost:5000/recognise_image', json = { 
        #    'image' : arr
        #    })                        
        return str(value.json())         
    except:        
        raise Exception("lele2")               
