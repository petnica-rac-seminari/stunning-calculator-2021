import requests
import numpy
import json

def SendParsedImage(arr : list) -> str:
    try:                    
        value= requests.post('http://10.51.0.78:5000/recognise_image', json = { 
            'image' : arr
            })       
        print("VALUE parse return: ",value)         
        return str(value.json()) 
    except:        
        raise Exception("lele2")

def evaluate(equation : str) -> float:
    try:                    
        value= requests.post('http://10.51.0.78:5000/evaluate_equation', json = { 
            'equation' : equation
            })
        print("EVAL return:", value)                
        return str(value.json()) 
    except:        
        raise Exception("kukulele")                  
