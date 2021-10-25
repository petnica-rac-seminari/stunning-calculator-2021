import requests
import numpy
from flask import Flask, request, jsonify

def evaluate_old(expression : str) -> float:
    try: 
        string = eval(expression)
        return str(string)
        #value = requests.post('http://10.51.0.78:5000/evaluate', json = {         
        #    'expression' : expression
        #    })
        #return value
    except:
        raise Exception("lele1")        
    
