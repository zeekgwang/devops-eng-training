# TODO(everyone): 더하기, 빼기, 곱하기, 나누기 함수 테스트 케이스 작성

# fail이 뜬 경우, 해당 테스트 케이스 부터 동작을 안함
# AttributeError: module 'unittest' has no attribute 'SkipTest'

from functions import add_func, subtract_func, multiply_func, division_func


def test_add_func():
    assert add_func('1', '2') == 3


def test_subtract_func():
    assert subtract_func('1', '2') == -1


def test_multiply_func():
    assert multiply_func('3', '4') == 12


def test_division_func():
    assert division_func('4', '2') == 2.0
