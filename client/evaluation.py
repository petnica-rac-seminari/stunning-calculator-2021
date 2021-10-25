import requests
import numpy
from flask import Flask, request, jsonify

def evaluate(expression : str) -> float:
    try: 
        print(expression)
        string = eval(expression, {}, {})
        print(string)
        return string
        #value = requests.post('http://10.51.0.78:5000/evaluate', json = {         
        #    'expression' : expression
        #    })
        #return value
    except:
        raise Exception("lele1")        
    
