
def evaluate(expression):
    try:
        result = float(eval(expression, {}, {}))
        return str(result)
    except:
        return "Error"
    
