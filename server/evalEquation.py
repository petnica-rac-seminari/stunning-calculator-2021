
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
    

    for i in equation:
        if (i.isdigit() or i == "."):
            if lastNumber == -1:
                queue.append(i)
                lastNumber = len(queue) - 1
                
            else:
                queue[lastNumber] += i
            
            

        else:
            try:
                while (priority[stack[-1]] >= priority[i]):
                    queue.append(stack.pop())
            except:
                pass
            stack.append(i)
            lastNumber = -1

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
                right = float(stack.pop())
                left = float(stack.pop())
                result = float(ops[i](left, right))
                stack.append(str(result))

    return float(stack[0])

#print(evalEquation("9/3/3"))

