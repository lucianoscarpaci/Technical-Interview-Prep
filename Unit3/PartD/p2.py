def evalRPN(tokens):
    stack = []
    operators = {"+", "-", "*", "/"}

    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # Use int() to truncate towards zero
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]


tokens = ["2", "1", "+", "3", "*"]
print(evalRPN(tokens))  # Output: 9
tokens = ["4", "13", "5", "/", "+"]
print(evalRPN(tokens))  # Output: 6
tokens = ["4", "2", "-", "3", "*"]
print(evalRPN(tokens))  # Output: 6
