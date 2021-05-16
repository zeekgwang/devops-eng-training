# TODO(everyone): 더하기, 빼기, 곱하기, 나누기 함수 정의하기

import math


def add_func(x: int, y: int) -> int:
    return x + y


def subtract_func(x: int, y: int) -> int:
    return x - y


def multiply_func(x: int, y: int) -> int:
    if type(x) != int or type(y) != int:
        raise TypeError
    return x * y


def division_func(x: float, y: float) -> float:
    return x / y


def sqrt_func(x: int) -> float:
    return math.sqrt(x)