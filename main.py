import StackClass

def T_A_C(exp):
    stack = []
    x = 1
    # an instance of the StackClass module
    obj = StackClass.Conversion(len(exp))
    # Convert the given infix notation to postfix
    postfix = obj.infixToPostfix(exp)
    intermediate_code = ["Postfix notation: " + postfix + "\nExpressions:"]  # Store postfix notation
    
    # Generate intermediate code based on postfix
    for i in postfix:
        if i in "abcdefghijklmnopqrstuvwxyz" or i in "0123456789":
            stack.append(i)
        elif i == '-':
            op1 = stack.pop()
            intermediate_code.append(f"t({x}) = {i} {op1}")
            stack.append(f"t({x})")
            x += 1
            if stack:
                op2 = stack.pop()
                op1 = stack.pop()
                intermediate_code.append(f"t({x}) = {op1} + {op2}")
                stack.append(f"t({x})")
                x += 1
        elif i == '=':
            op2 = stack.pop()
            op1 = stack.pop()
            intermediate_code.append(f"{op1} {i} {op2}")
        else:
            op1 = stack.pop()
            if stack:
                op2 = stack.pop()
                intermediate_code.append(f"t({x}) = {op2} {i} {op1}")
                stack.append(f"t({x})")
                x += 1
    
    return '\n'.join(intermediate_code)

def process_expression(exp, output_type):
    obj = StackClass.Conversion(len(exp))
    postfix = obj.infixToPostfix(exp)
    if output_type == 'T_A_C':
        return T_A_C(exp)
    elif output_type == 'triples':
        return generate_triples(postfix)
    elif output_type == 'quadruples':
        return generate_quadruples(postfix)
    elif output_type == 'indirect_triples':
        return generate_indirect_triples(postfix)
    else:
        return "Invalid output type"

def generate_triples(postfix):
    stack = []
    x = 0
    results = ["{0:^10} | {1:^10} | {2:^10}".format('op', 'arg1', 'arg2')]
    for i in postfix:
        if i.isalnum():
            stack.append(i)
        elif i == '-':
            if stack:
                op1 = stack.pop()
                stack.append(f"({x})")
                results.append("{0:^10} | {1:^10} | {2:^10}".format(i, op1, '(-)'))
                x += 1
                if stack:
                    op2 = stack.pop()
                    op1 = stack.pop()
                    results.append("{0:^10} | {1:^10} | {2:^10}".format('+', op1, op2))
                    stack.append(f"({x})")
                    x += 1
        elif i == '=':
            if len(stack) >= 2:
                op2 = stack.pop()
                op1 = stack.pop()
                results.append("{0:^10} | {1:^10} | {2:^10}".format(i, op1, op2))
        else:
            if len(stack) >= 2:
                op2 = stack.pop()
                op1 = stack.pop()
                results.append("{0:^10} | {1:^10} | {2:^10}".format(i, op2, op1))
                stack.append(f"({x})")
                x += 1
    return "\n".join(results)

def generate_quadruples(postfix):
    stack = []
    x = 1
    results = ["{0:^10} | {1:^10} | {2:^10} | {3:^10}".format('op', 'arg1', 'arg2', 'result')]
    for i in postfix:
        if i.isalnum():
            stack.append(i)
        elif i == '-':
            op1 = stack.pop()
            stack.append(f"t({x})")
            results.append("{0:^10} | {1:^10} | {2:^10} | {3:^10}".format(i, op1, '(-)', f"t({x})"))
            x += 1
            if stack:
                op2 = stack.pop()
                op1 = stack.pop()
                results.append("{0:^10} | {1:^10} | {2:^10} | {3:^10}".format('+', op1, op2, f"t({x})"))
                stack.append(f"t({x})")
                x += 1
        elif i == '=':
            if len(stack) >= 2:
                op2 = stack.pop()
                op1 = stack.pop()
                results.append("{0:^10} | {1:^10} | {2:^10} | {3:^10}".format(i, op1, op2, '(-)'))
        else:
            if len(stack) >= 2:
                op2 = stack.pop()
                op1 = stack.pop()
                results.append("{0:^10} | {1:^10} | {2:^10} | {3:^10}".format(i, op1, op2, f"t({x})"))
                stack.append(f"t({x})")
                x += 1
    return "\n".join(results)

def generate_indirect_triples(postfix):
    stack = []
    x = 0
    results = ["{0:^10} | {1:^10} | {2:^10} | {3:^10}".format('op', 'arg1', 'arg2', 'result')]
    for i in postfix:
        if i.isalnum():
            stack.append(i)
        elif i == '-':
            if stack:
                op1 = stack.pop()
                stack.append(f"({x})")
                results.append("{0:^10} | {1:^10} | {2:^10} | {3:^10}".format(i, op1, '(-)', f"({x})"))
                x += 1
                if stack:
                    op2 = stack.pop()
                    op1 = stack.pop()
                    results.append("{0:^10} | {1:^10} | {2:^10} | {3:^10}".format('+', op1, op2, f"({x})"))
                    stack.append(f"({x})")
                    x += 1
            else:
                results.append("Error: Insufficient operands for operator: " + i)
                return "\n".join(results)
        elif i == '=':
            if len(stack) >= 2:
                op2 = stack.pop()
                op1 = stack.pop()
                results.append("{0:^10} | {1:^10} | {2:^10} | {3:^10}".format(i, op2, '(-)', op1))
            else:
                results.append("Error: Insufficient operands for operator: " + i)
                return "\n".join(results)
        else:
            if len(stack) >= 2:
                op1 = stack.pop()
                op2 = stack.pop()
                results.append("{0:^10} | {1:^10} | {2:^10} | {3:^10}".format(i, op2, op1, f"({x})"))
                stack.append(f"({x})")
                x += 1
            else:
                results.append("Error: Insufficient operands for operator: " + i)
                return "\n".join(results)
    return "\n".join(results)
