#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

#index Route
@app.route('/')
def index ():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:word>')
def print_string(word):
    print(word)
    return word

@app.route('/count/<int:num>')
def count(num):
    numbers = ""
    # loop from 0 up to num-1
    for i in range(num):
        numbers += str(i) + "\n" 
    return numbers


 # Math operations
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    # check what operation to do
    if operation == "add" or operation == "+":
        result = num1 + num2
    elif operation == "sub" or operation == "-":
        result = num1 - num2
    elif operation == "mult" or operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: cannot divide by zero"
    elif operation == "mod" or operation == "%":
        result = num1 % num2
    else:
        return "Error: unknown operation"

    return str(result)

#run the app
if __name__ == '__main__':
    app.run(port=5555, debug=True)
