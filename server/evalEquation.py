from customError import CustomError
def checkStrNumberValidity(strNumber):
    strNumber.replace("-", "", 1)
    strNumber.replace(".", "", 1)
    return strNumber.isdigit()

def evalEquation(equation):
    ops = {
        "+": (lambda a, b: a + b),
        "-": (lambda a, b: a - b),
        "*": (lambda a, b: a * b),
        "/": (lambda a, b: a / b)
    }

    priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2
    }
    stack = []
    queue = []
    lastNumber = -1
    lastSign = -1
    

    for i in equation:
        if (i.isdigit() or i == "."):
            if lastNumber == -1:
                queue.append(i)
                lastNumber = len(queue) - 1
                
            else:
                queue[lastNumber] += i
            
            

        else:
            try:
                if (equation.index(i) - lastSign >2):
                    while (priority[stack[-1]] >= priority[i]):
                        queue.append(stack.pop())
                else:
                    raise CustomError("2Operands")
            except:
                pass
            stack.append(i)
            lastNumber = -1
            lastSign = equation.index(i)

    for i in range(len(stack)):
        queue.append(stack.pop())
    try:
        queue.append(stack.pop())
    except:
        pass

    stack = []
    new_queue = []
    for i in queue:
        new_queue.append(i)

    for i in new_queue:

        try:
            float(i)
            stack.append(i)
            queue.remove(i)
        except:
            if i == "+" or i == "-" or i == "*" or i == "/":
                right = stack.pop()
                if checkStrNumberValidity(right):
                    right = float(right)
                else:
                    raise CustomError("EvalSideNotDigit")
                try:
                    left = stack.pop()
                    if checkStrNumberValidity(left):
                        left = float(left)
                    else:
                        raise CustomError("EvalSideNotDigit")
                except:
                    left = float(0)

                result = float(ops[i](left, right))
                stack.append(str(result))

    if type(stack[0]):
        return float(stack[0])
    
    else:
        raise CustomError("EvalLastStackNotFloat")

print(evalEquation("5*/2"))

