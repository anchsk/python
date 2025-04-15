from flask import Flask, render_template, request
from Maths.mathematics import sum, substract, multiply

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/sum")
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = sum(num1,num2)
    return str(result)

@app.route("/sub")
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = substract(num1,num2)
    return str(result)

@app.route("/mul")
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = multiply(num1,num2)
    return str(result)


if __name__ == '__main__':
    app.run(debug=True,host="127.0.0.1",port=5001)

