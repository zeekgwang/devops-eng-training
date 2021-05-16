# TODO(everyone): 더하기, 빼기, 곱하기, 나누기 함수 테스트 케이스 작성

# fail이 뜬 경우, 해당 테스트 케이스 부터 동작을 안함
# AttributeError: module 'unittest' has no attribute 'SkipTest'

import pytest
from functions import add_func, subtract_func, multiply_func, division_func


def test_add_func():
    assert add_func(1, 2) == 3
    assert add_func(1, 0) == 1
    assert add_func(1, -1) == 0
    assert add_func(0, 3) == 3.0
    with pytest.raises(TypeError):
        add_func('a', -1)
    with pytest.raises(TypeError):
        add_func(1)


def test_subtract_func():
    assert subtract_func(1, 2) == -1
    assert subtract_func(100, -1) == 101
    assert subtract_func(0, -1) == 1
    with pytest.raises(TypeError):
        subtract_func('a', -1)
    with pytest.raises(TypeError):
        subtract_func(1)


def test_multiply_func():
    assert multiply_func(3, 4) == 12
    assert multiply_func(0, 1) == 0
    assert multiply_func(-1, 20) == -20
    with pytest.raises(TypeError):
        multiply_func('a', -1)
    with pytest.raises(TypeError):
        multiply_func(1)


def test_division_func():
    assert division_func(4, 2) == 2
    assert division_func(4, -2) == -2
    assert division_func(0, 1) == 0
    with pytest.raises(ZeroDivisionError):
        division_func(1, 0)
    with pytest.raises(TypeError):
        division_func('a', -1)
    with pytest.raises(TypeError):
        division_func(1)
