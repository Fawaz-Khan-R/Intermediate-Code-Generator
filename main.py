import StackClass
import random

def T_A_C(exp):
    stack = []
    x = 1
    obj = StackClass.Conversion(len(exp))
    postfix = obj.infixToPostfix(exp)
    intermediate_code = ["Postfix notation: " + postfix + "\nExpressions:"]  # Store postfix notation
    
    i = 0
    while i < len(postfix):
        if postfix[i] in "abcdefghijklmnopqrstuvwxyz" or postfix[i] in "0123456789":
            stack.append(postfix[i])
        elif postfix[i] == '(' and postfix[i + 1] == '-':
            stack.append(postfix[i] + postfix[i + 1])
            i += 1  
        elif postfix[i] == '-':
            if len(stack) >= 2 and stack[-2] in "+-*/":
                op1 = stack.pop()
                intermediate_code.append(f"t({x}) = {postfix[i]} {op1}")
                stack.append(f"t({x})")
                x += 1
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                intermediate_code.append(f"t({x}) = {op2} {postfix[i]} {op1}")
                stack.append(f"t({x})")
                x += 1
        elif postfix[i] == '=':
            op2 = stack.pop()
            op1 = stack.pop()
            intermediate_code.append(f"{op1} {postfix[i]} {op2}")
            stack.append(op1)
        i += 1
    
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
    start_address = random.randint(1, 50)
    current_address = start_address
    triples_results = []
    pointers_results = []

    triples_results.append("{0:^10} | {1:^10} | {2:^10}".format('Op', 'Arg1', 'Arg2'))
    pointers_results.append("{0:^10} | {1:^10}".format('#', 'Statement'))

    i = 0
    while i < len(postfix):
        char = postfix[i]
        if char.isdigit() or (char.isalpha() and (i == 0 or postfix[i-1] not in ['-', '+', '*', '/', '('])):
            stack.append(char)
        elif char in ['+', '-', '*', '/']:
            if char == '-' and i + 1 < len(postfix) and postfix[i + 1] == '(':
                i += 2  
                if i < len(postfix) and postfix[i].isdigit():
                    stack.append(f"-{postfix[i]}")
                    i += 1  
                    if postfix[i] == ')':
                        i += 1  
                continue
            if len(stack) < 2:
                return "Error: Insufficient operands for operator: " + char
            op2 = stack.pop()
            op1 = stack.pop()
            triples_results.append("{0:^10} | {1:^10} | {2:^10}".format(char, op1, op2))
            pointers_results.append("{0:^10} | {1:^10}".format(current_address, x))
            current_address += 1
            stack.append(f"t({x})")
            x += 1
        elif char == '(':
            i += 1
            continue
        elif char == ')':
            i += 1
            continue
        i += 1

    return "\n".join(triples_results) + "\n\nPointers Table:\n" + "\n".join(pointers_results)

# views.py

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    expression = request.form['expression']
    output_type = request.form.get('output_type', 'T_A_C')  
    try:
        output = process_expression(expression, output_type)
        if output_type == "indirect_triples":
            results = output.split("\n\n")  
            return jsonify({'success': True, 'output': results[0], 'pointers': results[1]})
        else:
            return jsonify({'success': True, 'output': output})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})


if __name__ == "__main__":
    app.run(debug=True)
