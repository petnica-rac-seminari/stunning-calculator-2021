
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
    

    for i in equation:
        if i.isdigit():
            queue.append(i)

        else:
            try:
                while (priority[stack[-1]] >= priority[i]):
                    queue.append(stack.pop())
            except:
                pass
            stack.append(i)

    for i in stack:
        queue.append(stack.pop())
    queue.append(stack.pop())

    stack = []
    new_queue = []
    for i in queue:
        new_queue.append(i)

    print(queue)
    for i in new_queue:
        print(i)
        if i.isdigit():
            print(f"{i} numeric")
            stack.append(i)
            queue.remove(i)
        elif i == "+" or i == "-" or i == "*" or i == "/":
            right = int(stack.pop())
            left = int(stack.pop())
            result = int(ops[i](left, right))
            stack.append(str(result))

    return stack[0]

print(evalEquation("2*6+2-9/3"))

