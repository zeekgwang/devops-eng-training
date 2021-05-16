from flask import Flask, render_template, request
from functions import add_func, subtract_func, multiply_func, division_func, sqrt_func

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/healthz", methods=["GET"])
def healthCheck():
    return "", 200


# TODO(everyone): GET 메소드로 더하기, 빼기, 곱하기, 나누기 함수 라우트 완성하기
@app.route("/add", methods=["GET"])
def add():
    x = request.args.get('x')
    y = request.args.get('y')
    if x.isdigit() and y.isdigit():
        result = str(add_func(int(x), int(y)))
        response = app.response_class(
            response=result,
            status=200
        )
    else:
        response = app.response_class(
            response="Bad Request",
            status=400
        )

    return response


@app.route("/subtract", methods=["GET"])
def subtract():
    x = request.args.get('x')
    y = request.args.get('y')
    if x.isdigit() and y.isdigit():
        result = str(subtract_func(int(x), int(y)))
        response = app.response_class(
            response=result,
            status=200
        )
    else:
        response = app.response_class(
            response="Bad Request",
            status=400
        )

    return response


@app.route("/multiply", methods=["GET"])
def multiply():
    x = request.args.get('x')
    y = request.args.get('y')
    if x.isdigit() and y.isdigit():
        result = str(multiply_func(int(x), int(y)))
        response = app.response_class(
            response=result,
            status=200
        )
    else:
        response = app.response_class(
            response="Bad Request",
            status=400
        )

    return response


@app.route("/division", methods=["GET"])
def division():
    x = request.args.get('x')
    y = request.args.get('y')
    if x.isdigit() and y.isdigit() and int(y) != 0:
        result = str(division_func(int(x), int(y)))
        response = app.response_class(
            response=result,
            status=200
        )
    else:
        response = app.response_class(
            response="Bad Request",
            status=400
        )

    return response


@app.route("/sqrt", methods=["GET"])
def sqrt():
    x = request.args.get('x')
    if x.isdigit():
        result = str(sqrt_func(int(x)))
        response = app.response_class(
            response=result,
            status=200
        )
    else:
        response = app.response_class(
            response="Bad Request",
            status=400
        )

    return response


def create_app():
    return app


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
